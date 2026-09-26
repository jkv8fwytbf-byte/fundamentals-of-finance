#!/usr/bin/env python3
"""Run `python3 compare.py demo` first. See README.md for live experiments."""
from __future__ import annotations
import argparse
import copy
import hashlib
import json
import math
import os
import random
import sys
from pathlib import Path

from lab import (LabError, OpenRouter, apply_reviews, calculate, catalog, eligible,
                 evaluate_task, grade, prices, read_json, save_json, timestamp)
from report import write_report

ROOT = Path(__file__).resolve().parent
DEFAULTS = {"temperature": 0.0, "max_tokens": 512, "max_tool_rounds": 3, "timeout": 45}


def load_tasks(path):
    tasks = read_json(path)
    if not isinstance(tasks, list) or not tasks: raise LabError("Tasks must be a nonempty JSON list.")
    ids = set()
    for task in tasks:
        if not isinstance(task, dict) or not all(isinstance(task.get(k), str) and task[k] for k in ("id", "prompt", "category")):
            raise LabError("Each task needs string id, prompt and category fields.")
        if task["id"] in ids: raise LabError("Task identifiers must be unique.")
        ids.add(task["id"])
        if task["category"] not in ("qa", "extraction", "arithmetic", "summary"): raise LabError("Unknown task category.")
        if task["category"] == "qa" and not (isinstance(task.get("accepted"), list) and task["accepted"] and all(isinstance(x, str) for x in task["accepted"])):
            raise LabError("QA tasks need a nonempty accepted-answer list.")
        if task["category"] in ("extraction", "arithmetic") and "expected" not in task: raise LabError("Missing expected answer.")
        if task["category"] == "summary" and not task.get("rubric"): raise LabError("Summary tasks need a rubric.")
    return tasks


def bundle_for(tasks, models, settings, demo=False):
    encoded = json.dumps(tasks, sort_keys=True, ensure_ascii=False).encode()
    return {"version": 1, "run_id": timestamp(), "demo": demo, "created_at": timestamp(),
            "settings": settings, "task_sha256": hashlib.sha256(encoded).hexdigest(),
            "tasks": tasks, "models": models, "results": [], "state": "running",
            "limitations": "Twenty custom learning tasks, one attempt per condition. Not a public benchmark or proof of general superiority. Summary quality requires human review. Provider and network differences affect elapsed time."}


def row_id(model, mode, task):
    return f"{model}|{mode}|{task}"


def run_demo(args):
    tasks = load_tasks(args.tasks)
    names = ["demo/cedar", "demo/maple", "demo/willow"]
    models = [{"id": n, "name": n.split("/")[1].title() + " (fictional fixture)"} for n in names]
    bundle = bundle_for(tasks, models, DEFAULTS, True)
    for index, model in enumerate(models):
        for task in tasks:
            modes = ["baseline", "calculator"] if task["category"] == "arithmetic" else ["baseline"]
            for mode in modes:
                answer = task.get("example_summary", "")
                if task["category"] == "qa": answer = task["accepted"][0]
                elif task["category"] == "extraction": answer = json.dumps(task["expected"])
                elif task["category"] == "arithmetic": answer = str(task["expected"])
                trace = []
                if mode == "calculator":
                    expression = task.get("example_expression", str(task["expected"]))
                    answer = calculate(expression)
                    trace = [{"tool": "calculate", "arguments": json.dumps({"expression": expression}), "result": {"result": answer}}]
                elif index == 1 and task["id"] in ("qa-03", "math-02", "math-04"):
                    answer = "42"
                elif index == 2 and task["id"] == "extract-02":
                    answer = "```json\n" + answer + "\n```"
                row = {"row_id": row_id(model["id"], mode, task["id"]), "task_id": task["id"],
                       "category": task["category"], "model": model["id"], "mode": mode,
                       "answer": answer, "status": "ok", "error": None,
                       "started_at": bundle["created_at"], "seconds": round(0.3 + index * 0.17 + len(trace) * 0.5, 2),
                       "trace": trace, "calls": [{"id": "fixture-only", "actual_model": model["id"],
                       "provider": "fictional offline provider", "usage": {"prompt_tokens": 100 + index * 10, "completion_tokens": 25 + index * 5, "cost": 0}}]}
                row["grade"] = grade(task, answer)
                if index == 2 and task["id"] == "qa-05":
                    row.update(status="error", error="Simulated timeout for learning.", answer="", calls=[])
                    row["grade"] = {"score": 0, "reason": "Simulated failure; counted as unsuccessful."}
                bundle["results"].append(row)
    bundle["state"] = "complete"
    finish(bundle, args.output)


def finish(bundle, output):
    output = Path(output)
    output.mkdir(parents=True, exist_ok=True)
    save_json(output / "results.json", bundle)
    write_report(bundle, output / "report.html")
    template = {r["row_id"]: {"faithfulness": None, "coverage": None, "brevity": None, "notes": ""}
                for r in bundle["results"] if r["category"] == "summary" and r["status"] == "ok"}
    save_json(output / "review-template.json", template)
    print(f"Report: {output.resolve() / 'report.html'}")
    print(f"Results: {output.resolve() / 'results.json'}")


def live(args):
    if args.budget_usd is not None and (not math.isfinite(args.budget_usd) or args.budget_usd <= 0):
        raise LabError("--budget-usd must be a positive finite number.")
    config = read_json(args.config)
    if not isinstance(config, dict): raise LabError("Configuration must be a JSON object.")
    settings = dict(DEFAULTS)
    settings.update({k: config[k] for k in DEFAULTS if k in config})
    if type(settings["max_tokens"]) is not int or not 1 <= settings["max_tokens"] <= 4096: raise LabError("max_tokens must be 1–4096.")
    if type(settings["max_tool_rounds"]) is not int or not 0 <= settings["max_tool_rounds"] <= 5: raise LabError("max_tool_rounds must be 0–5.")
    if type(settings["temperature"]) not in (int, float) or not math.isfinite(settings["temperature"]) or not 0 <= settings["temperature"] <= 2: raise LabError("temperature must be 0–2.")
    if type(settings["timeout"]) not in (int, float) or not 1 <= settings["timeout"] <= 180: raise LabError("timeout must be 1–180 seconds.")
    if args.limit is not None and args.limit < 1: raise LabError("--limit must be positive.")
    tasks = load_tasks(args.tasks)
    if args.category: tasks = [t for t in tasks if t["category"] == args.category]
    if args.limit: tasks = tasks[:args.limit]
    if not tasks: raise LabError("No tasks match the selection.")
    client = OpenRouter(os.environ.get("OPENROUTER_API_KEY"), args.budget_usd, settings["timeout"])
    available = catalog()
    needs_tools = args.calculator and any(t["category"] == "arithmetic" for t in tasks)
    ids = args.models or config.get("models", [])
    if args.free_auto:
        ids = sorted(m["id"] for m in available if eligible(m, tools=needs_tools))[:3]
        if len(ids) < 3: raise LabError("Fewer than three compatible free models. List models and explicitly choose one or two.")
    if not isinstance(ids, list) or not ids or not all(isinstance(x, str) for x in ids):
        raise LabError("Choose model IDs with --models, fill config.json, or use --free-auto.")
    if len(set(ids)) != len(ids): raise LabError("Choose distinct model identifiers.")
    mapping = {m["id"]: m for m in available}
    models = []
    for model_id in ids:
        if model_id not in mapping: raise LabError(f"Model unavailable in the current catalogue: {model_id}")
        model = mapping[model_id]
        if not eligible(model, free_only=args.budget_usd is None, tools=needs_tools):
            raise LabError(f"{model_id} does not meet the price or parameter requirements. List compatible models first.")
        models.append(model)
    # Save only the catalogue fields relevant to reproducing this run.
    model_snapshots = [{k: m.get(k) for k in ("id", "name", "context_length", "pricing", "supported_parameters")} for m in models]
    bundle = bundle_for(tasks, model_snapshots, settings)
    bundle["budget_usd"] = args.budget_usd
    bundle["order_seed"] = 17
    output = Path(args.output)
    jobs = []
    for task in tasks:
        for model in models:
            jobs.append((model, task, "baseline"))
            if needs_tools and task["category"] == "arithmetic": jobs.append((model, task, "calculator"))
    random.Random(17).shuffle(jobs)
    save_json(output / "results.json", bundle)
    try:
        for count, (model, task, mode) in enumerate(jobs, 1):
            print(f"{count}/{len(jobs)}  {model['id']}  {task['id']}  {mode}", flush=True)
            row = evaluate_task(client, model, task, mode, settings)
            row["row_id"] = row_id(model["id"], mode, task["id"])
            bundle["results"].append(row)
            bundle["reported_spend_usd"] = client.spent
            save_json(output / "results.json", bundle)
            if client.billing_unknown:
                bundle["state"] = "stopped: billing unknown"
                break
        else:
            bundle["state"] = "complete"
    except KeyboardInterrupt:
        bundle["state"] = "interrupted; an in-flight charge may be absent"
    finish(bundle, output)


def main():
    parser = argparse.ArgumentParser(description="A small, transparent model-comparison learning lab.")
    sub = parser.add_subparsers(dest="command", required=True)
    demo = sub.add_parser("demo", help="Offline fictional answers; never contacts a model")
    demo.add_argument("--tasks", default=ROOT / "data/tasks.json")
    demo.add_argument("--output", default=ROOT / "runs/demo")
    listing = sub.add_parser("models", help="Read the current OpenRouter model catalogue")
    listing.add_argument("--free", action="store_true")
    listing.add_argument("--tools", action="store_true")
    run = sub.add_parser("run", help="Run live calls with your own OPENROUTER_API_KEY")
    run.add_argument("--config", default=ROOT / "config.json")
    run.add_argument("--tasks", default=ROOT / "data/tasks.json")
    choose = run.add_mutually_exclusive_group()
    choose.add_argument("--models", nargs="+")
    choose.add_argument("--free-auto", action="store_true", help="Choose the first three compatible free IDs alphabetically; saves the selection")
    run.add_argument("--calculator", action="store_true", help="Add paired calculator conditions for arithmetic tasks")
    run.add_argument("--category", choices=["qa", "extraction", "arithmetic", "summary"])
    run.add_argument("--limit", type=int)
    run.add_argument("--budget-usd", type=float)
    run.add_argument("--output", default=ROOT / "runs/live")
    report = sub.add_parser("report", help="Regenerate an HTML report from saved results")
    report.add_argument("results")
    report.add_argument("--output", default=ROOT / "runs/report.html")
    review = sub.add_parser("review", help="Apply human summary rubrics to saved results")
    review.add_argument("results")
    review.add_argument("scores")
    review.add_argument("--output", default=ROOT / "runs/reviewed")
    args = parser.parse_args()
    try:
        if args.command == "demo": run_demo(args)
        elif args.command == "models":
            rows = [m for m in catalog() if eligible(m, free_only=args.free, tools=args.tools)]
            for m in sorted(rows, key=lambda x: x["id"]):
                p = prices(m)
                print(f"{m['id']}\tinput ${p['prompt'] * 1e6:g}/M\toutput ${p['completion'] * 1e6:g}/M")
            print(f"{len(rows)} compatible models; prices/availability can change.")
        elif args.command == "run": live(args)
        elif args.command == "report":
            write_report(read_json(args.results), args.output)
            print(Path(args.output).resolve())
        elif args.command == "review":
            bundle = copy.deepcopy(read_json(args.results))
            count = apply_reviews(bundle, read_json(args.scores))
            if not count: raise LabError("No completed reviews found. Fill all three scores and notes for at least one row.")
            finish(bundle, args.output)
            print(f"Applied {count} human reviews.")
        return 0
    except (LabError, OSError) as exc:
        print(f"Could not complete: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
