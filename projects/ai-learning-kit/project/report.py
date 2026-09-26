"""Generate a portable, escaped HTML report without a web framework."""
import html
import json
import statistics
from pathlib import Path
from lab import usage_total


def esc(value):
    return html.escape(str(value), quote=True)


def fmt(value, digits=2):
    return "Unavailable" if value is None else f"{value:,.{digits}f}"


def score_label(row):
    n = row["grade"]["score"]
    if n is None: return "Awaiting review"
    if row["status"] == "error": return "Request failed"
    return f"{n * 100:.0f}% credit"


def summary_rows(bundle):
    output = []
    for m in bundle["models"]:
        rows = [r for r in bundle["results"] if r["model"] == m["id"] and r["mode"] == "baseline"]
        auto = [r for r in rows if r["category"] != "summary"]
        summaries = [r for r in rows if r["category"] == "summary"]
        graded_summaries = [r for r in summaries if r["status"] == "ok" and r["grade"]["score"] is not None]
        good = [r for r in rows if r["status"] == "ok"]
        costs = [usage_total(r, "cost") for r in rows]
        cost_total = sum(costs) if costs and all(v is not None for v in costs) else None
        latency = statistics.median([r["seconds"] for r in good]) if good else None
        output.append({"model": m["id"], "attempts": len(rows), "auto_count": len(auto),
                       "auto_pass": sum(r["grade"]["score"] == 1 for r in auto),
                       "summary_reviewed": len(graded_summaries), "summary_count": len(summaries),
                       "summary_mean": statistics.mean(r["grade"]["score"] for r in graded_summaries) if graded_summaries else None,
                       "errors": sum(r["status"] == "error" for r in rows), "seconds": latency, "cost": cost_total})
    return output


def write_report(bundle, output):
    rows = bundle["results"]
    tasks = {t["id"]: t for t in bundle["tasks"]}
    demo = bundle.get("demo", False)
    summaries = summary_rows(bundle)
    warning = ("OFFLINE DEMONSTRATION · All model identities, answers, timings and token counts are fictional fixtures. No API calls or charges occurred."
               if demo else "LIVE EXPERIMENT · Custom learning tasks, one attempt per condition. These results describe this run, not a general model ranking.")
    table = "".join(f"<tr><th scope='row'>{esc(s['model'])}</th><td>{s['auto_pass']}/{s['auto_count']}</td>"
                    f"<td>{s['summary_reviewed']}/{s['summary_count']} reviewed · {fmt(None if s['summary_mean'] is None else s['summary_mean']*100, 0)}{'%' if s['summary_mean'] is not None else ''}</td>"
                    f"<td>{fmt(s['seconds'])} s</td><td>{('$'+fmt(s['cost'],6)) if s['cost'] is not None else 'Unavailable / incomplete'}</td><td>{s['errors']}</td></tr>" for s in summaries)
    pairs = []
    for m in bundle["models"]:
        baseline = {r["task_id"]: r for r in rows if r["model"] == m["id"] and r["category"] == "arithmetic" and r["mode"] == "baseline"}
        tool = {r["task_id"]: r for r in rows if r["model"] == m["id"] and r["mode"] == "calculator"}
        ids = sorted(set(baseline) & set(tool))
        if ids:
            b = sum(baseline[i]["grade"]["score"] == 1 for i in ids)
            c = sum(tool[i]["grade"]["score"] == 1 for i in ids)
            used = sum(bool(tool[i]["trace"]) for i in ids)
            pairs.append(f"<tr><th scope='row'>{esc(m['id'])}</th><td>{b}/{len(ids)}</td><td>{c}/{len(ids)}</td><td>{c-b:+d} tasks</td><td>{used}/{len(ids)}</td></tr>")
    blocks = []
    for index, r in enumerate(rows):
        t = tasks[r["task_id"]]
        score = r["grade"]["score"]
        status = "pending" if score is None else ("passed" if score == 1 and r["status"] == "ok" else "failed")
        trace = ""
        if r["trace"]:
            trace = "<h4>Calculator actions</h4><pre>" + esc(json.dumps(r["trace"], indent=2, ensure_ascii=False)) + "</pre>"
        providers = ", ".join(sorted({c.get("provider") or "Not returned" for c in r["calls"]})) or "No completed response"
        actual_models = ", ".join(sorted({c.get("actual_model") or "Not returned" for c in r["calls"]})) or "Not returned"
        review = ""
        if r["category"] == "summary" and r["status"] == "ok":
            old = r["grade"].get("rubric", {})
            selects = ""
            for field, maximum in (("faithfulness", 2), ("coverage", 2), ("brevity", 1)):
                options = "<option value=''>Unscored</option>" + "".join(f"<option value='{n}' {'selected' if old.get(field)==n else ''}>{n}</option>" for n in range(maximum+1))
                selects += f"<label>{field.title()} (0–{maximum})<select data-score='{field}'>{options}</select></label>"
            review = f"<div class='review' data-review='{esc(r['row_id'])}'><h4>Your review</h4><p>{esc(t['rubric'])}</p><div class='review-grid'>{selects}</div><label>Reason for your scores<textarea data-notes placeholder='Cite a factual omission, unsupported claim, or a strength.'>{esc(old.get('notes',''))}</textarea></label></div>"
        reference = t.get("accepted", t.get("expected", t.get("key_points", "")))
        blocks.append(f"""<details class="result" data-model="{esc(r['model'])}" data-category="{esc(r['category'])}" data-mode="{esc(r['mode'])}" data-status="{status}">
<summary><span class="taskid">{esc(r['task_id'])}</span><strong>{esc(r['model'])}</strong><span>{esc(r['mode'])}</span><span class="badge {status}">{score_label(r)}</span></summary>
<div class="detail"><h4>Task</h4><p class="preserve">{esc(t['prompt'])}</p><h4>Answer</h4><pre>{esc(r['answer'] or '(No answer)')}</pre>
{'<p class="failure">'+esc(r['error'])+'</p>' if r.get('error') else ''}
<p><b>Grade:</b> {esc(r['grade']['reason'])}</p><details><summary>Reference answer / required points</summary><pre>{esc(json.dumps(reference, ensure_ascii=False, indent=2))}</pre></details>
<p class="metadata">End-to-end: {fmt(r['seconds'])} s · Input tokens: {fmt(usage_total(r, 'prompt_tokens'),0)} · Output tokens: {fmt(usage_total(r,'completion_tokens'),0)} · Cost: {('$'+fmt(usage_total(r,'cost'),6)) if usage_total(r,'cost') is not None else 'Unavailable'}</p>
<p class="metadata">Provider: {esc(providers)} · Returned model: {esc(actual_models)}</p>{trace}{review}</div></details>""")
    pending = sum(r["grade"]["score"] is None for r in rows)
    if demo:
        conclusion = "This sample teaches you how to inspect a report. Its fictional model differences provide no evidence about any real AI model. Review the summaries and inspect the deliberate JSON-format mistake and simulated timeout."
    else:
        fully_attempted = len([t for t in bundle["tasks"] if t["category"] != "summary"])
        candidates = [s for s in summaries if s["auto_count"] == fully_attempted and fully_attempted > 0]
        if candidates:
            top = max(s["auto_pass"] for s in candidates)
            names = ", ".join(s["model"] for s in candidates if s["auto_pass"] == top)
            conclusion = f"On the {fully_attempted} automatically checked baseline tasks in this run, the highest pass count was {top}, achieved by {names}. Treat this as a shortlist for further testing on your own use case."
        else:
            conclusion = "There is not a complete set of automatically checked tasks to compare. Inspect the partial results and failures before drawing conclusions."
        if pending: conclusion += f" {pending} summaries still need human review, so a complete quality recommendation is premature."
    model_options = "".join(f"<option>{esc(m['id'])}</option>" for m in bundle["models"])
    css = """
:root{--ink:#172e2a;--muted:#5f706b;--line:#d9e0d8;--paper:#f7f8f3;--accent:#086b54}*{box-sizing:border-box}body{margin:0;background:var(--paper);color:var(--ink);font:16px/1.65 system-ui,sans-serif}main{max-width:1200px;margin:auto;padding:50px 32px 90px}h1{font-size:clamp(32px,5vw,54px);line-height:1.08;letter-spacing:-2px;margin:12px 0 20px}h2{font-size:26px;margin-top:48px}h4{margin:22px 0 7px}.eyebrow{letter-spacing:.16em;font-size:12px;font-weight:800;color:var(--accent)}.banner{padding:16px 20px;background:#fff2cd;border:1px solid #e3c56b;border-radius:10px;margin:25px 0}.muted,.metadata{color:var(--muted);font-size:14px}.stats{display:flex;gap:15px;flex-wrap:wrap}.stat{padding:20px;border:1px solid var(--line);border-radius:12px;min-width:175px;background:white}.stat b{display:block;font-size:28px}.table-wrap{overflow-x:auto;background:white;border:1px solid var(--line);border-radius:12px}table{width:100%;border-collapse:collapse;text-align:left;font-size:14px}th,td{padding:16px;border-bottom:1px solid var(--line)}thead{background:#e9eee6}tbody th{font-weight:600}.filters,.review-grid{display:flex;gap:12px;flex-wrap:wrap;margin:18px 0}label{display:grid;gap:6px;font-size:13px;font-weight:650}select,button,textarea{font:inherit;border:1px solid #b4c4ba;border-radius:7px;padding:10px;background:white;color:var(--ink)}button{background:var(--accent);color:white;cursor:pointer;font-weight:650}button:hover{background:#064c3c}button:focus-visible,select:focus-visible,textarea:focus-visible,summary:focus-visible{outline:3px solid #df9500;outline-offset:3px}textarea{width:100%;min-height:90px}.result{background:white;border:1px solid var(--line);border-radius:10px;margin:10px 0}.result>summary{display:flex;align-items:center;gap:16px;padding:16px;cursor:pointer;flex-wrap:wrap}.result>summary strong{flex:1}.taskid{font:12px ui-monospace,monospace;color:var(--muted)}.badge{font-size:12px;padding:4px 9px;border-radius:5px}.passed{background:#dcf1e6}.failed{background:#fde4d8}.pending{background:#eaf0f5}.detail{padding:0 22px 24px}.preserve{white-space:pre-wrap}pre{white-space:pre-wrap;overflow-wrap:anywhere;background:#f0f3ef;padding:18px;border-radius:8px;font:13px/1.65 ui-monospace,monospace}.review{background:#f0f5f2;padding:20px;border-radius:8px;margin-top:20px}.failure{color:#982e13}#visible-count{font-size:14px;color:var(--muted)}[hidden]{display:none!important}@media(max-width:600px){main{padding:24px 16px}th,td{padding:10px}.result>summary{gap:10px}.result>summary strong{flex-basis:60%}}@media print{button,.filters{display:none}main{padding:0}.result{break-inside:avoid}}
"""
    script = """
const filters=[...document.querySelectorAll('[data-filter]')];
function filterRows(){let count=0;document.querySelectorAll('.result').forEach(r=>{r.hidden=!filters.every(f=>!f.value||r.dataset[f.dataset.filter]===f.value);if(!r.hidden)count++;});document.getElementById('visible-count').textContent=count+' matching results';}
filters.forEach(f=>f.addEventListener('change',filterRows));filterRows();
document.getElementById('export').addEventListener('click',()=>{const scores={};let error='';document.querySelectorAll('[data-review]').forEach(r=>{const fields=[...r.querySelectorAll('[data-score]')];if(fields.every(f=>f.value===''))return;if(fields.some(f=>f.value==='')||!r.querySelector('textarea').value.trim()){error='Complete all three scores and a note for each review you started.';return;}const s={notes:r.querySelector('textarea').value};fields.forEach(f=>s[f.dataset.score]=Number(f.value));scores[r.dataset.review]=s;});const status=document.getElementById('review-status');if(error||!Object.keys(scores).length){status.textContent=error||'Score at least one summary first.';return;}const a=document.createElement('a');const url=URL.createObjectURL(new Blob([JSON.stringify(scores,null,2)],{type:'application/json'}));a.href=url;a.download='scores.json';a.click();setTimeout(()=>URL.revokeObjectURL(url),1000);status.textContent='Downloaded scores.json. Apply it with the review command in the project guide. Scores are not automatically saved in this page.';});
"""
    document = f"""<!doctype html><html lang="en"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{'Demo · ' if demo else ''}Model comparison report</title><style>{css}</style>
<main><div class="eyebrow">AI LEARNING LAB / EXPERIMENT REPORT</div><h1>Read the answers.<br>Then read the scores.</h1><p class="muted">Created {esc(bundle['created_at'])} · Run state: {esc(bundle['state'])}</p><div class="banner">{warning}</div>
<div class="stats"><div class="stat"><b>{len(bundle['models'])}</b>models / fixtures</div><div class="stat"><b>{len(bundle['tasks'])}</b>distinct tasks</div><div class="stat"><b>{len(rows)}</b>attempts across conditions</div><div class="stat"><b>{pending}</b>summaries awaiting review</div></div>
<h2>Baseline comparison</h2><p>Automatic passes cover passage questions, extraction and arithmetic. Summary scores use a separate human rubric. Failed requests count as unsuccessful; missing usage remains unavailable.</p>
<div class="table-wrap"><table><thead><tr><th>Model</th><th>Automatic passes</th><th>Summary review</th><th>Median successful time</th><th>Total reported cost</th><th>Errors</th></tr></thead><tbody>{table}</tbody></table></div>
<p class="muted">Time is end-to-end elapsed time, including all calls in a task. Cost totals cover baseline attempts only and require usage for every included attempt. Demo figures are synthetic. Token totals and per-call usage are in the saved JSON.</p>
<h2>Calculator experiment</h2><p>Compare only task IDs present in both conditions. “Calculator available” allows tool use; inspect whether the model actually used it.</p>
{'<div class="table-wrap"><table><thead><tr><th>Model</th><th>Baseline passes</th><th>Calculator available</th><th>Difference</th><th>Actually called tool</th></tr></thead><tbody>'+''.join(pairs)+'</tbody></table></div>' if pairs else '<p>No paired calculator results in this run.</p>'}
<h2>What this run supports</h2><p>{esc(conclusion)}</p><p>{esc(bundle['limitations'])}</p>
<h2>Inspect each result</h2><div class="filters"><label>Model<select data-filter="model"><option value="">All models</option>{model_options}</select></label><label>Task type<select data-filter="category"><option value="">All types</option><option value="qa">Passage questions</option><option value="extraction">Extraction</option><option value="arithmetic">Arithmetic</option><option value="summary">Summaries</option></select></label><label>Condition<select data-filter="mode"><option value="">Both conditions</option><option value="baseline">Baseline</option><option value="calculator">Calculator</option></select></label><label>Outcome<select data-filter="status"><option value="">All outcomes</option><option value="passed">Full credit</option><option value="failed">Errors / lost credit</option><option value="pending">Awaiting review</option></select></label></div><p id="visible-count" aria-live="polite"></p>
{''.join(blocks)}<h2>Save your summary reviews</h2><p>Use the rubric controls inside summary results. Export completed reviews before closing this page, then apply them to generate an updated report.</p><button id="export">Download review scores</button><p id="review-status" role="status"></p>
<pre>python3 compare.py review PATH_TO_RESULTS.json PATH_TO_SCORES.json --output runs/reviewed</pre>
<details><summary>Reproduction metadata</summary><pre>{esc(json.dumps({'settings':bundle['settings'],'models':bundle['models'],'task_sha256':bundle['task_sha256'],'order_seed':bundle.get('order_seed'),'budget_usd':bundle.get('budget_usd')},ensure_ascii=False,indent=2))}</pre></details>
</main><script>{script}</script></html>"""
    output = Path(output)
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(document, encoding="utf-8")
