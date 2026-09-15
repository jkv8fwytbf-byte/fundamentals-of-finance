# Chapter 8. "Fine-tuning" at three levels: the harness, the context, and the model

## What it is (plain words and an analogy)

You asked how to "fine-tune this thing". The word has three meanings in practice, and people mix them up. Only the third one changes the model itself. The first two change what the model sees and what it is allowed to do. In this project you will spend nearly all your time on the first two.

Think of the model as a brilliant new employee who has amnesia every morning. You cannot retrain their brain each day. You can leave them a desk. On the desk sits a job description, a filing cabinet of procedures, a set of tools, and some pre-written memos. That desk is level 1, the harness. A harness is the program that wraps the model, feeds it files, and runs its commands. In this project the harness is Cursor while you code, and our own TypeScript while the product runs.

Level 2 is what you put on the desk for today's task. The model reads a fixed amount of text per request, called the context window. Choosing what goes into that window is called context engineering. Writing the instruction itself is called prompt engineering.

Level 3 is sending the employee back to school. Training changes the model's weights, the millions of numbers inside it that decide how it answers. This is what most people mean by fine-tuning. It is real, it is cheap to run, and it is not what this project needs yet.

Source: /Users/siddharth/.claude/projects/-Users-siddharth-Downloads/edcdeb19-7793-4e1b-9e73-4cf6186716bf/tool-results/bj0fbejiq.txt, CHECK 3, section 1 (2026-09)

| Level | What changes | Cost | Reversible? | Who does it here |
|---|---|---|---|---|
| 1. Harness | Rules file, tools, prompt templates, model routing | $0 and your time | In seconds, by a pull request | You, from M3 |
| 2. Context | Which facts and examples enter the window per request | $0 and your time | In seconds | You and the code |
| 3. Model weights | How the model behaves by default | About $2 per training run, but see the serving trap | Only by retraining | Nobody, until stated conditions are met |

Source: docs/plan.md, section 8, "Fine-tuning, three levels" (2026-09-14)

## Why this tool now (for this project)

The plan's own summary is blunt: the harness is "$0 and 95% of the quality; this is what you will do." The tool landscape report reaches the same conclusion from a different angle. Damodaran's method is facts, arithmetic, and a book of rules. Cost-of-capital tables, equity risk premiums, and industry betas change every year. Facts that change yearly belong in a database, where they can be updated and cited. They do not belong baked into a model's weights, where they go stale and cannot be cited.

Source: docs/plan.md, section 8 (2026-09-14); /Users/siddharth/.claude/projects/-Users-siddharth-Downloads/edcdeb19-7793-4e1b-9e73-4cf6186716bf/tool-results/b31x0pyot.txt, section 4 (2026-09)

The same report gives the accepted 2026 order of work: prompt first, then retrieval, then fine-tuning, then distillation (training a small model to copy a big one's answers). Its rule of thumb is that fine-tuning is for form, not facts. Form means output shape, tone, and refusal habits. This project's form problems, such as always emitting a valid table of assumptions, are solved for $0 by a prompt plus a schema plus a validator function. So the chapter teaches level 3 so you understand it, and tells you honestly why it stays on the shelf.

Source: /Users/siddharth/.claude/projects/-Users-siddharth-Downloads/edcdeb19-7793-4e1b-9e73-4cf6186716bf/tool-results/b31x0pyot.txt, section 4 (2026-09)

## How it is used in this project

### Level 1. The harness: the files that will exist

Milestone M2 will create these files in the public repo `valuation`. Nothing after M0 exists yet, so read "will" throughout. Tuning the harness means editing one of these files, opening a pull request, and reading the diff (chapter 1).

| File or folder | What it is | What "tuning" it means |
|---|---|---|
| `AGENTS.md` | The eight hard rules, read by Cursor, Cline, and Claude alike | Add or sharpen a rule when the model repeats a mistake |
| `.cursor/rules/` | The same rules on one page; Cursor reads them on every request | Keep them short so they always fit in the window |
| `.cursor/mcp.json` | Registers the system's tools inside Cursor | Add a tool, or take one away |
| `packages/mcp-server` | The tools themselves: `value_company`, `write_memo`, `review_memo`, `get_industry_stats`, `search_corpus`, `report` | Change what a tool returns, or what it refuses |
| `packages/models` | One file with the pinned model ids and prices | Model routing: swap a model in one line |
| `packages/memo` and `packages/rag` | The memo template and the grounded prompt | Rewrite a prompt, add an example, change the citation format |

Source: docs/plan.md, milestone M2 and section 10 (2026-09-14); /Users/siddharth/Valuation/docs/read-this-first.md, sections 4.1 and 11 (2026-09-14)

MCP stands for Model Context Protocol. It is a standard plug that lets an AI tool call other programs. It matters for tuning because a tool is a fence. When the model must call `get_industry_stats` to get a beta, it cannot invent one. The rules file says what to do; the tool set says what is even possible.

Source: /Users/siddharth/Valuation/docs/read-this-first.md, section 11 (2026-09-14)

Model routing is the choice of which model does which job. In the runtime that is `z-ai/glm-5.3` for memos and answers, `z-ai/glm-5.3-flash:batch` for bulk cleaning, `moonshotai/kimi-k3` as the judge, and `deepseek/deepseek-v4.1-flash` as the fallback. DeepSeek V4 Pro is never used, because it scored a 94% hallucination rate on the AA-Omniscience test. All of this lives in `packages/models`, pinned to the Artificial Analysis index version it was chosen under. Changing a model is a one-line edit and a pull request, not a retraining job.

Source: /Users/siddharth/Valuation/docs/read-this-first.md, section 4.1 (2026-09-14); docs/plan.md, section 10.4 (2026-09-14)

Sub-agents are helper sessions with their own context that return a summary. The plan defers them to v2. The rule for later is that helpers write database rows, never prose you must audit. The `.pi/` folder layout you may see in the model-selection report (skills, prompts, extensions, agents) belongs to pi, which is also deferred.

Source: docs/plan.md, section 8, "Sub-agents" (2026-09-14); /Users/siddharth/.claude/projects/-Users-siddharth-Downloads/edcdeb19-7793-4e1b-9e73-4cf6186716bf/tool-results/bcy86uopa.txt, "PI SETUP FOR THE VALUATION REPO", part B (2026-09)

### Level 2. Prompt and context engineering

A prompt is the question on the exam paper. Context is which textbooks, notes, and past papers are on the desk. Choosing the desk is the harder and more valuable skill. Anthropic's article of 29 September 2025 names the enemy: context rot. As the number of tokens in the window climbs, the model's recall of any single fact degrades. A token is a word piece, roughly four characters. The discipline is the smallest set of high-signal tokens, not everything you have.

Source: /Users/siddharth/.claude/projects/-Users-siddharth-Downloads/edcdeb19-7793-4e1b-9e73-4cf6186716bf/tool-results/bj0fbejiq.txt, CHECK 3, section 1b (2026-09)

For a valuation this has a concrete meaning. Never paste a 200-page annual filing into the window. Extract the eight line items you need into a database row, then put that row in the window with its citation. The plan's librarian follows a hybrid rule: a question about one document gets that document stuffed in whole; a question across the corpus retrieves 50 passages, then a second model scores them again (reranking) and keeps the best 8.

Source: /Users/siddharth/.claude/projects/-Users-siddharth-Downloads/edcdeb19-7793-4e1b-9e73-4cf6186716bf/tool-results/bj0fbejiq.txt, CHECK 3, section 1b (2026-09); docs/plan.md, section 10.4 (2026-09-14)

The money says the same thing. A retrieval question that sends 8,000 tokens and gets 700 back costs about $0.0143 on GLM-5.3. Stuffing 200,000 tokens into the same model costs about $0.283, which is about 20 times more. Prompt caching helps too: a cached read on GLM-5.3 costs $0.26 per million tokens against $1.40 uncached, a 5.4 times discount.

Source: /Users/siddharth/.claude/projects/-Users-siddharth-Downloads/edcdeb19-7793-4e1b-9e73-4cf6186716bf/tool-results/bcy86uopa.txt, RESEARCH 1, "Three operational rules" and KEY FACTS (2026-09-14)

Few-shot examples are worked answers you show the model before asking your question. They teach form better than instructions do. This project already has its example: the "Stories to Numbers" sheet in Damodaran's own workbook. Each assumption row ends with a "Link to story" cell, and the sheet's own instruction reads "Tie each assumption to the part of your story that relates to it." The memo writer will use that sheet as its template, one row per driver, with the link mandatory.

Source: /Users/siddharth/Downloads/financeMD/damodaran/pc/fcffsimpleginzu.md, "Stories to Numbers" sheet (2026-02-01); docs/plan.md, section 10.5 (2026-09-14)

Evals are the steering wheel. An eval is a fixed set of questions with known good answers, run again after every prompt change. Without one, prompt editing is guesswork. With one, it is measurement. The database will contain `rag_eval_case` and `rag_eval_run` tables. Langfuse Hobby is free at 50,000 units a month, and its datasets and evaluation runner are included on every tier. Every model call will carry `vintage`, `source_ids`, `license_class`, `model_id`, and `prompt_version` in its metadata, so a score can be sliced by which prompt produced it. Kimi K3 grades the answers, and the judge is never the model being judged. Chapter 11 covers the mechanics.

Source: docs/plan.md, section 10.3 (2026-09-14); /Users/siddharth/.claude/projects/-Users-siddharth-Downloads/edcdeb19-7793-4e1b-9e73-4cf6186716bf/tool-results/bo0hrclp7.txt, section 6, "LLM observability / evals" (2026-09); /Users/siddharth/Valuation/docs/read-this-first.md, section 4.1 (2026-09-14)

### Level 3. The model itself, as an outsourced service

Fine-tuning proper changes the weights so the model behaves differently by default. The analogy in the explainer report is exact: you are not teaching the analyst new facts, you are drilling your firm's memo template into them until they cannot write it wrong. LoRA, short for Low-Rank Adaptation, trains a small adapter on top of a frozen base model. That is why it is cheap. A form task needs roughly 500 to 1,000 high-quality examples, and every example must be exactly the output you want.

Source: /Users/siddharth/.claude/projects/-Users-siddharth-Downloads/edcdeb19-7793-4e1b-9e73-4cf6186716bf/tool-results/bj0fbejiq.txt, CHECK 3, section 1c (2026-09)

The best evidence for finance is the FinLoRA paper (arXiv 2505.19819, May 2025). It tested five LoRA methods on five base models across 19 financial datasets, including four new XBRL sets built from 150 SEC filings. XBRL is the tagged format companies use to file numbers with the SEC.

| FinLoRA result | Figure |
|---|---|
| Average lift of LoRA over the base models | +36% |
| Vanilla LoRA (8-bit, rank 8) on Llama 3.1 8B | 74.74 versus 37.05 for the base model |
| Training time | 14.1 to 15.9 hours on four A5000 cards, 56 to 64 GPU-hours |
| Compute cost at $0.26 per GPU-hour | $14.66 to $16.54 |

Source: /Users/siddharth/.claude/projects/-Users-siddharth-Downloads/edcdeb19-7793-4e1b-9e73-4cf6186716bf/tool-results/bj0fbejiq.txt, CHECK 3, section 1c; /Users/siddharth/.claude/projects/-Users-siddharth-Downloads/edcdeb19-7793-4e1b-9e73-4cf6186716bf/tool-results/b31x0pyot.txt, section 4, citing https://arxiv.org/abs/2505.19819 (2025-05-26)

The 2026 prices per training run are small. Prices are per million training tokens. SFT means supervised fine-tuning, the plain kind. An epoch is one pass over your examples.

| Vendor | Price for LoRA SFT | Note |
|---|---|---|
| Together AI | about $0.48 (16B parameters or less), about $1.50 (17 to 69B), about $2.90 (70 to 100B) | Weights can be downloaded |
| Fireworks | $0.50 (under 16B), $3.00 (16 to 80B), $6.00 (80 to 300B), $10.00 (over 300B) | DPO (direct preference optimisation, a second training style that learns from pairs of better and worse answers) costs about twice SFT |
| Google Vertex | Training tokens = dataset tokens times epochs | Tuned endpoint priced the same as the base model |
| Unsloth on Colab | Free on a T4 | A 7 to 8B model fits in 6 to 8 GB; 1,000 to 10,000 examples take 15 to 60 minutes |

Worked arithmetic: 800 examples times about 1,500 tokens times 3 epochs is about 3.6 million training tokens, or about $1.80 on a 16B-or-smaller LoRA. Ten experiments cost under $20.

Source: /Users/siddharth/.claude/projects/-Users-siddharth-Downloads/edcdeb19-7793-4e1b-9e73-4cf6186716bf/tool-results/bj0fbejiq.txt, CHECK 3, section 1c (2026-09)

The training run is never the expense. Two things are. First, data curation: 500 to 1,000 hand-corrected pairs is weeks of your evenings, and the tool landscape report budgets three to five times the training cost for a year of retraining and evaluation. Second, serving. A dedicated GPU endpoint left running at $2 to $10 an hour will eat the whole $200 monthly ceiling in a weekend. The rule, if you ever do this, is serverless LoRA inference billed at the base-model rate, or shut the endpoint down. OpenRouter can route a Together or Fireworks key for a 5% fee, waived for the first million requests a month, but routing a truly private endpoint is an Enterprise-plan feature. Two of the friendlier solo options are gone: Predibase was acquired by Rubrik in June 2025 and OpenPipe by CoreWeave in September 2025.

Source: /Users/siddharth/.claude/projects/-Users-siddharth-Downloads/edcdeb19-7793-4e1b-9e73-4cf6186716bf/tool-results/bj0fbejiq.txt, CHECK 3, section 1c (2026-09); /Users/siddharth/.claude/projects/-Users-siddharth-Downloads/edcdeb19-7793-4e1b-9e73-4cf6186716bf/tool-results/b31x0pyot.txt, section 4 (2026-09)

Why not yet for this project. Level 3 is revisited only when two conditions are both true: the running system has logged at least 500 hand-corrected outputs, and there is a measurable, repeated format failure that a prompt plus a schema plus a validator cannot fix. Examples would be a model that keeps mislabeling operating leases or will not emit the assumptions table in the required shape. Until then it is a $2 experiment with a $200 trap attached, solving a problem you do not have.

Source: docs/plan.md, section 8 (2026-09-14); /Users/siddharth/.claude/projects/-Users-siddharth-Downloads/edcdeb19-7793-4e1b-9e73-4cf6186716bf/tool-results/bj0fbejiq.txt, CHECK 3, section 1c (2026-09)

## Learn it

All free. Read them in this order; the last two are for understanding, not for doing.

| # | Resource | Format | Hours | Why |
|---|---|---|---|---|
| 1 | https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents | Article | 1 | The reference on context rot and just-in-time retrieval; explains why the librarian retrieves instead of stuffing |
| 2 | https://github.com/anthropics/prompt-eng-interactive-tutorial | Notebooks, 9 chapters | 4 to 6 | Hands-on few-shot and structured-output practice you can port to open-weight models |
| 3 | https://www.anthropic.com/engineering/building-effective-agents | Article | 0.75 | When not to use an agent; most of this pipeline is a plain workflow |
| 4 | https://www.promptingguide.ai/ | Site | 3 | Model-agnostic; good on chain-of-thought and self-consistency |
| 5 | https://arxiv.org/abs/2505.19819 and https://github.com/Open-Finance-Lab/FinLoRA | Paper and code | 1 (abstract and results table only) | The only rigorous LoRA benchmark on SEC and XBRL tasks |
| 6 | Unsloth docs, fine-tuning guide (unsloth.ai, verify) | Docs and free Colab | 3 to 4 | Only when the two revisit conditions are met; cheapest end-to-end run |

Source: /Users/siddharth/.claude/projects/-Users-siddharth-Downloads/edcdeb19-7793-4e1b-9e73-4cf6186716bf/tool-results/bj0fbejiq.txt, CHECK 3, sections 1b and 1c resource tables (2026-09)

## 10-minute exercise

Rewrite one prompt and compare two answers. Use Cursor's chat, or any chat model you already pay for. The material is public Damodaran text. This repo is public.

1. Prompt A, no context: "Why is the terminal cost of capital equal to the risk-free rate plus the mature-market ERP?" Save the answer.
2. Open `/Users/siddharth/Downloads/financeMD/damodaran/pc/fcffsimpleginzu.md` and copy the lines around the label `Mature Market ERP +`.
3. Prompt B, with context: paste those lines, then ask the same question, and add "Answer in three sentences. Quote the label you relied on. Say if the label and the formula disagree."
4. Compare. Does answer A mention the misleading "+4.5%" label at all? Does answer B notice that the label says one thing and the formula another? Which answer could you cite in a memo?
5. Write two lines in your decisions log (chapter 0, rule 6): what you added to the window, and what changed in the answer.

Source: /Users/siddharth/.claude/projects/-Users-siddharth-Downloads/edcdeb19-7793-4e1b-9e73-4cf6186716bf/tool-results/bkdrkpfng.txt, terminal cost of capital note (2026-09); docs/plan.md, milestone M1, day-one exercise (2026-09-14)

## Done when

- You can state the three levels, each in one sentence, with its cost.
- You can name the six harness files from the table above and say what tuning each one means.
- Your decisions log holds the A and B answers from the exercise, and you can say which one you would cite.
- You can recite the two conditions under which level 3 gets revisited, and the serving trap that goes with it.
