import copy
import contextlib
import io
import json
import os
import subprocess
import sys
import tempfile
import unittest
import urllib.error
from pathlib import Path
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from lab import (LabError, OpenRouter, apply_reviews, calculate, eligible,
                 evaluate_task, grade, http_json, usage_total)
from compare import DEFAULTS, bundle_for, load_tasks, main
from report import summary_rows, write_report


MODEL = {"id": "test/model", "context_length": 1000,
         "pricing": {"prompt": "0", "completion": "0", "request": "0"},
         "supported_parameters": ["temperature", "max_tokens", "tools", "tool_choice"]}
TASKS = load_tasks(ROOT / "data/tasks.json")


def reply(content="4", tools=None, usage=True, finish="stop"):
    obj = {"id": "response-id", "model": "test/model", "provider": "test/provider",
           "choices": [{"message": {"role": "assistant", "content": content}, "finish_reason": finish}]}
    if tools is not None: obj["choices"][0]["message"]["tool_calls"] = tools
    if usage: obj["usage"] = {"prompt_tokens": 12, "completion_tokens": 3, "cost": 0.002}
    return obj


def tool(expression="2+2", name="calculate"):
    return {"id": "tool-1", "type": "function", "function": {"name": name, "arguments": json.dumps({"expression": expression})}}


class FakeClient:
    def __init__(self, responses):
        self.responses = iter(responses)
        self.requests = []
    def complete(self, model, payload):
        self.requests.append(copy.deepcopy(payload))
        r = next(self.responses)
        if isinstance(r, Exception): raise r
        return r


class TaskAndGraderTests(unittest.TestCase):
    def test_twenty_balanced_unique_tasks(self):
        self.assertEqual(len(TASKS), 20)
        self.assertEqual(len({t["id"] for t in TASKS}), 20)
        for category in ("qa", "extraction", "arithmetic", "summary"):
            self.assertEqual(sum(t["category"] == category for t in TASKS), 5)

    def test_reference_answers_and_calculations(self):
        for t in TASKS:
            if t["category"] == "qa": answer = t["accepted"][0]
            elif t["category"] == "extraction": answer = json.dumps(t["expected"])
            elif t["category"] == "arithmetic": answer = calculate(t["example_expression"])
            else:
                self.assertLessEqual(len(t["example_summary"].split()), 35)
                self.assertIsNone(grade(t, t["example_summary"])["score"])
                continue
            self.assertEqual(grade(t, answer)["score"], 1, t["id"])

    def test_qa_is_not_substring_matching(self):
        task = TASKS[1]
        self.assertEqual(grade(task, " Four. ")["score"], 1)
        self.assertEqual(grade(task, "four or five")["score"], 0)

    def test_extraction_requires_types_and_pure_json(self):
        t = next(t for t in TASKS if t["id"] == "extract-02")
        good = json.dumps(t["expected"])
        self.assertEqual(grade(t, good)["score"], 1)
        for bad in ["```json\n" + good + "\n```", good.replace("false", "0"), good.replace("9", "9.0"),
                    '{"name":"Starter","monthly_usd":9,"trial":false,"trial":true}',
                    '{"name":"Starter","monthly_usd":NaN,"trial":false}']:
            self.assertEqual(grade(t, bad)["score"], 0)

    def test_arithmetic_rejects_nonfinite_or_prose(self):
        t = next(t for t in TASKS if t["id"] == "math-02")
        for answer in ("NaN", "Infinity", "28%", "The answer is 28", "128"):
            self.assertEqual(grade(t, answer)["score"], 0)
        self.assertEqual(grade(t, "28.0000001")["score"], 1)


class CalculatorTests(unittest.TestCase):
    def test_decimal_precision_and_precedence(self):
        self.assertEqual(calculate("0.1 + 0.2"), "0.3")
        self.assertEqual(calculate("-(3+4) * 2"), "-14")
    def test_unsafe_and_unbounded_expressions(self):
        for text in ("__import__('os').system('id')", "1/0", "2**10", "9"*201,
                     "1000000000001", "(1).__class__", "[1,2]", "1//2", "True"):
            with self.assertRaises(LabError, msg=text): calculate(text)


class ToolLoopTests(unittest.TestCase):
    def setUp(self):
        self.task = {"id": "math-test", "category": "arithmetic", "prompt": "2+2? Return only a number.", "expected": "4"}
    def test_real_loop_sends_observation_and_preserves_reasoning_details(self):
        first = reply(None, [tool()])
        first["choices"][0]["message"]["reasoning_details"] = [{"type": "reasoning.text", "text": "fixture"}]
        client = FakeClient([first, reply()])
        row = evaluate_task(client, MODEL, self.task, "calculator", DEFAULTS)
        self.assertEqual(row["grade"]["score"], 1)
        self.assertEqual(len(row["trace"]), 1)
        second = client.requests[1]
        self.assertIn("tools", second)
        self.assertIn("reasoning_details", second["messages"][-2])
        self.assertEqual(json.loads(second["messages"][-1]["content"]), {"result": "4"})
        self.assertEqual(usage_total(row, "prompt_tokens"), 24)
        self.assertEqual(usage_total(row, "cost"), .004)
    def test_calculator_availability_does_not_force_use(self):
        row = evaluate_task(FakeClient([reply()]), MODEL, self.task, "calculator", DEFAULTS)
        self.assertEqual(row["trace"], [])
    def test_invalid_tool_is_returned_as_observation(self):
        client = FakeClient([reply(None, [tool(name="shell")]), reply()])
        row = evaluate_task(client, MODEL, self.task, "calculator", DEFAULTS)
        self.assertIn("error", row["trace"][0]["result"])
        self.assertEqual(len(client.requests), 2)
    def test_turn_limit_and_malformed_calls(self):
        row = evaluate_task(FakeClient([reply(None,[tool()])]*4), MODEL, self.task, "calculator", DEFAULTS)
        self.assertEqual(row["status"], "error")
        self.assertIn("turn limit", row["error"])
        row = evaluate_task(FakeClient([reply(None,[{}])]), MODEL, self.task, "calculator", DEFAULTS)
        self.assertEqual(row["status"], "error")
    def test_empty_truncated_and_missing_choices(self):
        for response in [reply(""), reply("4", finish="length"), {"choices": []}, {"choices": [None]}]:
            row = evaluate_task(FakeClient([response]), MODEL, self.task, "baseline", DEFAULTS)
            self.assertEqual(row["status"], "error")
            self.assertEqual(row["grade"]["score"], 0)
    def test_failure_and_missing_usage_are_not_zero_cost(self):
        for response in [LabError("timeout"), reply(usage=False)]:
            row = evaluate_task(FakeClient([response]), MODEL, self.task, "baseline", DEFAULTS)
            self.assertIsNone(usage_total(row, "cost"))
    def test_partial_tool_loop_has_incomplete_usage(self):
        row = evaluate_task(FakeClient([reply(None, [tool()]), LabError("timeout")]), MODEL, self.task, "calculator", DEFAULTS)
        self.assertEqual(len(row["calls"]), 1)
        self.assertIsNone(usage_total(row, "cost"))
        self.assertFalse(row["usage_complete"])


class TransportAndBudgetTests(unittest.TestCase):
    def test_missing_key(self):
        with self.assertRaisesRegex(LabError, "OPENROUTER_API_KEY"): OpenRouter(None)
    def test_http_errors_have_actionable_messages(self):
        for code, phrase in [(401,"API key"),(404,"unavailable"),(429,"Rate limit"),(503,"provider")]:
            error = urllib.error.HTTPError("https://test.invalid",code,"error",{},io.BytesIO(b"sensitive provider content"))
            with patch("urllib.request.urlopen",side_effect=error):
                with self.assertRaisesRegex(LabError,phrase): http_json("https://test.invalid")
    def test_timeout_and_malformed_json(self):
        with patch("urllib.request.urlopen",side_effect=TimeoutError):
            with self.assertRaisesRegex(LabError,"timed out"): http_json("https://test.invalid")
        with patch("urllib.request.urlopen") as opener:
            opener.return_value.__enter__.return_value.read.return_value=b"not json"
            with self.assertRaisesRegex(LabError,"malformed JSON"): http_json("https://test.invalid")
    def test_price_and_capability_filter(self):
        self.assertTrue(eligible(MODEL, tools=True))
        bad = copy.deepcopy(MODEL); bad["pricing"].pop("prompt")
        self.assertFalse(eligible(bad))
        bad = copy.deepcopy(MODEL); bad["supported_parameters"].remove("tools")
        self.assertFalse(eligible(bad, tools=True))
    def test_zero_price_caps_are_sent(self):
        seen=[]
        def transport(url, **kw): seen.append(kw); return reply()
        OpenRouter("test-key",transport=transport).complete(MODEL,{"max_tokens":10})
        self.assertEqual(seen[0]["payload"]["provider"]["max_price"], {"prompt":0,"completion":0,"request":0})
        self.assertTrue(seen[0]["payload"]["provider"]["require_parameters"])
    def test_paid_requires_explicit_budget_and_reservation(self):
        paid=copy.deepcopy(MODEL); paid["pricing"]["prompt"]="0.000001"
        with self.assertRaisesRegex(LabError,"paid"): OpenRouter("key").complete(paid,{"max_tokens":10})
        with self.assertRaisesRegex(LabError,"reservation"): OpenRouter("key",.00001).complete(paid,{"max_tokens":10})
    def test_missing_paid_usage_stops_next_request(self):
        paid=copy.deepcopy(MODEL); paid["pricing"]["prompt"]="0.000001"
        client=OpenRouter("key",1,transport=lambda *a,**kw: reply(usage=False))
        client.complete(paid,{"max_tokens":10})
        self.assertTrue(client.billing_unknown)
        with self.assertRaisesRegex(LabError,"prior charge"): client.complete(paid,{"max_tokens":10})


class EndToEndTests(unittest.TestCase):
    def test_live_command_with_controlled_catalogue_and_responses(self):
        models=[]
        for n in range(3):
            m=copy.deepcopy(MODEL);m["id"]=f"fixture/{n}";models.append(m)
        client=FakeClient([reply(TASKS[0]["accepted"][0]) for _ in range(3)])
        client.spent=0;client.billing_unknown=False
        with tempfile.TemporaryDirectory() as tmp:
            arguments=["compare.py","run","--free-auto","--limit","1","--output",tmp]
            with patch("sys.argv",arguments), patch("compare.catalog",return_value=models), patch("compare.OpenRouter",return_value=client), contextlib.redirect_stdout(io.StringIO()):
                self.assertEqual(main(),0)
            bundle=json.loads((Path(tmp)/"results.json").read_text())
            self.assertFalse(bundle["demo"])
            self.assertEqual(bundle["state"],"complete")
            self.assertEqual(len(bundle["results"]),3)
            self.assertEqual(len(bundle["task_sha256"]),64)
            self.assertTrue(all(r["grade"]["score"]==1 for r in bundle["results"]))
    def test_failed_summary_does_not_count_as_human_review(self):
        task=next(t for t in TASKS if t["category"]=="summary")
        row=evaluate_task(FakeClient([LabError("timeout")]),MODEL,task,"baseline",DEFAULTS)
        bundle=bundle_for([task],[MODEL],DEFAULTS);bundle["results"]=[row]
        self.assertEqual(summary_rows(bundle)[0]["summary_reviewed"],0)
        self.assertEqual(summary_rows(bundle)[0]["errors"],1)
    def test_demo_report_and_manual_review(self):
        with tempfile.TemporaryDirectory() as tmp:
            run=subprocess.run([sys.executable,str(ROOT/"compare.py"),"demo","--output",tmp],capture_output=True,text=True)
            self.assertEqual(run.returncode,0,run.stderr)
            bundle=json.loads((Path(tmp)/"results.json").read_text())
            self.assertEqual(len(bundle["results"]),75)
            self.assertEqual(sum(r["grade"]["score"] is None for r in bundle["results"]),15)
            text=(Path(tmp)/"report.html").read_text()
            self.assertIn("OFFLINE DEMONSTRATION",text)
            self.assertIn("Unavailable / incomplete",text)
            baseline=summary_rows(bundle)
            self.assertEqual(baseline[0]["auto_pass"],15)
            self.assertEqual(baseline[1]["auto_pass"],12)
            self.assertEqual(baseline[2]["auto_pass"],13)
            key=next(r["row_id"] for r in bundle["results"] if r["category"]=="summary")
            review={key:{"faithfulness":2,"coverage":1,"brevity":1,"notes":"One required point omitted."}}
            self.assertEqual(apply_reviews(bundle,review),1)
            self.assertEqual(next(r for r in bundle["results"] if r["row_id"]==key)["grade"]["score"],.8)
            with self.assertRaises(LabError): apply_reviews(bundle,{key:{"faithfulness":True}})
    def test_report_escapes_untrusted_answer(self):
        task=TASKS[0]
        row=evaluate_task(FakeClient([reply('<script>alert("x")</script>')]),MODEL,task,"baseline",DEFAULTS)
        row["row_id"]="test"
        bundle=bundle_for([task],[MODEL],DEFAULTS); bundle["results"]=[row]
        with tempfile.TemporaryDirectory() as tmp:
            path=Path(tmp)/"report.html";write_report(bundle,path)
            text=path.read_text()
            self.assertNotIn('<script>alert("x")</script>',text)
            self.assertIn('&lt;script&gt;',text)
    def test_live_without_key_is_clear_and_does_not_network(self):
        env=dict(os.environ);env.pop("OPENROUTER_API_KEY",None)
        run=subprocess.run([sys.executable,str(ROOT/"compare.py"),"run","--models","anything"],capture_output=True,text=True,env=env)
        self.assertEqual(run.returncode,2)
        self.assertIn("OPENROUTER_API_KEY",run.stderr)


if __name__ == "__main__":
    unittest.main()
