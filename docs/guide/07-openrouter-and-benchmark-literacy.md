# Chapter 7. OpenRouter and benchmark literacy: one door to every model, and how to read the scoreboard

## What it is (plain words and an analogy)

### OpenRouter

An **API** (application programming interface) is a door that one program uses to talk to another. Every AI company has its own door, its own key, and its own bill. **OpenRouter** is a single door in front of hundreds of those doors. You hold one key, you keep one credit balance, and you pick a model by changing one name in your code. If the company serving that model goes down, OpenRouter can quietly route the same request to another company serving the same model.

Source: /Users/siddharth/.claude/projects/-Users-siddharth-Downloads/edcdeb19-7793-4e1b-9e73-4cf6186716bf/tool-results/b31x0pyot.txt, section 3 (2026-09)

The analogy is a food-delivery app. You do not open an account with every restaurant. You open one account with the app, and the app takes your order to whichever kitchen you choose. The app adds a service fee on top-ups, but the menu prices are the kitchen's own prices. OpenRouter works the same way: it charges a fee when you buy credit, and charges nothing extra per token.

Source: /Users/siddharth/.claude/projects/-Users-siddharth-Downloads/edcdeb19-7793-4e1b-9e73-4cf6186716bf/tool-results/bcy86uopa.txt, section 4 (2026-09-14)

### Artificial Analysis

A **benchmark** is a standardized exam for a model. **Artificial Analysis** (AA) is an independent site that runs many such exams on many models and publishes the marks, together with speed and price. Think of it as the consumer-testing magazine for AI models. The headline mark is the **Intelligence Index**, a weighted average of ten exams. Underneath it sit narrower scoreboards for coding agents, for making things up, and for web-search services.

Source: /Users/siddharth/.claude/projects/-Users-siddharth-Downloads/edcdeb19-7793-4e1b-9e73-4cf6186716bf/tool-results/b31x0pyot.txt, section 5

## Why this tool now (for this project)

### The two places a model is used

This confused you before, so slowly. **Place 1 is while you write code.** That is Cursor, on the models Cursor includes in the $20 subscription you already pay. You never paste an API key into Cursor. Doing so is unofficial, switches off features like Tab, and puts the key in logs. Cursor Privacy Mode is not a secrecy guarantee. This repo is public.

Source: /Users/siddharth/Valuation/docs/read-this-first.md, sections 4 and 11 (2026-09-14); /Users/siddharth/.claude/projects/-Users-siddharth-Downloads/edcdeb19-7793-4e1b-9e73-4cf6186716bf/tool-results/btzaixzyh.txt, CHECK 1

**Place 2 is inside the product when it runs at night.** Our own code, started by GitHub Actions (Chapter 3), calls a model to write memos, answer librarian questions, and clean transcripts. Those calls go through OpenRouter. That is where the volume and the cost live, so that is where the cheap open-weight models go. **Open-weight** means the model's weights are downloadable and hosted by many companies, so no single vendor can switch you off, and a pinned checkpoint keeps a 2026 valuation reproducible in 2029.

Source: docs/plan.md, sections 2a and 2b (2026-09-14)

The price of that choice is capability. On the AA Intelligence Index v4.3 (released 2026-09-07) the frontier models score 53 and the best open-weight model, GLM-5.3, scores 45. The gap sits in long autonomous coding tasks, not in the "read a filing and extract" work that fills a valuation pipeline. Open-weight models cost 7 to 40 times less per token, so for Place 2 the trade is worth it.

Source: /Users/siddharth/Valuation/docs/read-this-first.md, section 4; bcy86uopa.txt, section 1b

Cline, the free extension inside Cursor, is the one exception that touches both places. It takes your OpenRouter key and lets you feel what an open-weight model does before its name goes into a robot. It is a bench, not the daily driver.

Source: /Users/siddharth/Valuation/docs/read-this-first.md, section 11

## How it is used in this project

### Three settings on the OpenRouter account

You will create the account in milestone 1 (Document A, section 10). Buy $20 of credit. Then set three things before any code runs.

| Setting | Value | Why |
|---|---|---|
| Monthly spend limit | $75 | The budget line for OpenRouter is $30 to $70 a month, inside the $200 ceiling |
| Prompt logging | Off | Logging is opt-in, and turning it on hands OpenRouter broad rights over your prompts |
| Zero-data-retention routing | Optional | Hygiene for runtime prompts that may include licensed filings. Not a claim that the project is secret |

Source: /Users/siddharth/Valuation/docs/read-this-first.md, sections 10 and 12

**Zero data retention** (ZDR) means the company that ran your request deletes the prompt and the answer once the answer is sent. OpenRouter can enforce ZDR per request. That is optional hygiene. It does not make "everything private". The research also notes that enabling prompt logging "grants OpenRouter an irrevocable right to commercial use" of the logged text. That is why logging stays off.

Source: /Users/siddharth/.claude/projects/-Users-siddharth-Downloads/edcdeb19-7793-4e1b-9e73-4cf6186716bf/tool-results/bj0fbejiq.txt, Role 4

### Fees, and the credit arithmetic

OpenRouter adds no markup on tokens. It charges 5.5% when you buy credit by card, with a minimum of $0.80 per purchase, or 5% by USDC (a dollar-pegged cryptocurrency; ignore this option). On small top-ups the minimum bites, so buy in $20 chunks rather than $5 chunks. Models with a `:free` suffix exist, but none of our four picks has one, and free models are capped at 20 requests a minute and at most 1,000 a day. Models with a `:batch` suffix cost half price for work that can wait, which is exactly our bulk job. One more fact that shaped the design: OpenRouter serves no embedding or reranking models at all, so the librarian's embeddings come from Voyage.

Source: bcy86uopa.txt, section 4

### Why not OpenRouter's web-search plugin

OpenRouter offers a plugin that lets a model search the web mid-answer. We do not use it. The plugin runs under a third party's retention rules. If the project ever needs web search for the news layer, it will use a separate vendor, chosen from the AA Search Index, described below.

Source: bj0fbejiq.txt, Role 4 and the accounts checklist

### The model picks, and why each

The runtime will pin four model ids in one file, with the AA index version next to them. Prices will be re-checked monthly. A swap will be one line. All four are open-weight and all go through OpenRouter.

| Job | OpenRouter id | Price per million tokens, in / out | Why this one |
|---|---|---|---|
| Write memos, answer questions | `z-ai/glm-5.3` | about $0.92 to 1.40 / $3.14 to 4.40 | Best open-weight score on the index (45); lowest hallucination rate among strong open weights (30%) |
| Bulk cleaning: punctuate transcripts, tag passages | `z-ai/glm-5.3-flash:batch` | $0.075 / $0.25 | Half price for work that can wait; the whole transcript job costs about $11 once; reasoning must be switched off |
| Judge: grade the librarian's answers in evaluations | `moonshotai/kimi-k3` | $2.65 / $13.28 | Best-calibrated open weight on AA-Omniscience (+18 to 20); it abstains rather than invents; the judge must never be the model being judged |
| Fallback | `deepseek/deepseek-v4.1-flash` | $0.15 / $0.60 | Fastest in class at 214 tokens a second; plain MIT license |
| Never | DeepSeek V4 Pro | | 94% hallucination rate on AA-Omniscience, fatal for a chat that must cite |

Source: /Users/siddharth/Valuation/docs/read-this-first.md, section 4.1; bcy86uopa.txt, sections 1a, 3 and 9

To make the prices concrete: a typical librarian answer sends about 8,000 tokens and receives about 700. That costs about $0.0143 on GLM-5.3 and about $0.00155 on GLM-5.3-Flash. One judge call on Kimi K3 costs about $0.0298, so a 200-case evaluation run costs about $5.96. A **token** is a word piece, roughly four characters.

Source: /Users/siddharth/Valuation/docs/read-this-first.md, section 4.1; bcy86uopa.txt, section 9

One caution on licenses. The model-selection report lists GLM-5.3 under a bespoke permissive license that is explicitly not MIT, and DeepSeek V4.1 Flash under plain MIT. The plan describes GLM-5.3-Flash as plain MIT, while the report lists it as bespoke permissive. The repo is public, so read each model card yourself before deciding.

Source: bcy86uopa.txt, section 1a; docs/plan.md, section 2a

### Reading the Artificial Analysis pages

**Intelligence Index v4.3.** Ten exams in four groups, released 2026-09-07. The weights matter because they tell you what the headline rewards.

| Group | Weight | Exams inside it |
|---|---|---|
| Agents | 30% | AA-Briefcase 15%, GDPval-AA v2 10%, AutomationBench-AA 5% |
| Coding | 20% | Terminal-Bench v4.0 10%, SciCode 10% |
| General | 30% | AA-Omniscience accuracy 10%, AA-Omniscience non-hallucination 5%, GDP.pdf 10%, AA-LCR v1.1 (long context) 5% |
| Scientific reasoning | 20% | Humanity's Last Exam 10%, CritPt 10% |

Half the headline is agent and coding work, which our pipeline barely does. Only 15% is "does it make things up", which is the part we care about most. That is why the picks were made from the sub-scores, not the headline. Current marks: frontier 53, GLM-5.3 45, Kimi K3 44, GLM-5.3-Flash 42, DeepSeek V4.1 Flash 40, DeepSeek V4 Pro 36.

Source: bcy86uopa.txt, section 1

**Coding Agent Index v1.5** (snapshot 2026-09-11) is different in kind. It scores a **harness plus model pair**, not a model alone. A harness is the tool wrapped around the model: the prompts, the file access, the permission gates. Claude Code with Fable 5.1 scores 62.2%. The best open-weight pair, Opencode with GLM-5.3, scores 53.6%. This index describes Place 1 work, so it matters for Cursor and Cline, not for the nightly robots.

Source: bcy86uopa.txt, section 2

**AA-Omniscience** is the hallucination exam. Six thousand closed-book questions across 42 topics. The index runs from minus 100 to plus 100. A right answer earns points, a confident wrong answer loses points, and "I do not know" costs nothing. **Calibration** is the habit of knowing when you do not know. As of 2026-08-27 only 46 of 167 models scored above zero. Kimi K3 scores +18 to 20 with a 51% hallucination rate on the questions it attempts. GLM-5.3 scores 14 with a 30% hallucination rate. DeepSeek V4 Pro hallucinates 94% of the time, which is why it is banned from the answer path despite a decent headline score. In our system the facts arrive from retrieved passages, so raw recall matters less. Willingness to abstain transfers directly.

Source: bcy86uopa.txt, section 3

**Search Index** (launched 2026-08-18) grades web-search services, not models. AA holds the model and the agent scaffold fixed and swaps only the search provider. Three exams are averaged: DeepSearchQA, BrowseComp, and an AA-Omniscience subset. Parallel scores 75, Exa 74, Firecrawl 73; the no-search baseline is 33. Search cost alone ranges from $13.64 per 1,000 tasks (Parallel turbo) to $126 (Tavily basic), which is why Tavily is the worst value on the board; a second report (bj0fbejiq.txt) quotes higher figures for the same index, $60.21 and $192.58, so re-check the AA page before choosing a vendor.

Source: b31x0pyot.txt, section 5; bj0fbejiq.txt, section 5

**Speed and money columns.** Time to first token (TTFT) is the seconds until the first token arrives; for reasoning models that is the first thinking token, so a fast TTFT can still mean a long wait for a useful word. Output tokens per second is the speed after that: GLM-5.3 runs at 72, GLM-5.3-Flash at 107, Kimi K3 at 37, DeepSeek V4.1 Flash at 214. Cost per task is the average dollars to finish one index task, computed from real token counts and cache-hit rates; this is the column that maps to a bill. Blended price is a single dollars-per-million figure that assumes a fixed mix of cached, input and output tokens. AA's blended price for GLM-5.3 shows $0.90; OpenRouter lists $1.40 in and $4.40 out. Always budget from OpenRouter's numbers.

Source: bj0fbejiq.txt, section 5; bcy86uopa.txt, sections 0 and 1a

### The five traps

1. **Index inflation.** Labs tune for the composite. Read the sub-exam that matches your job: AA-Omniscience and AA-LCR for valuation, not Humanity's Last Exam.
2. **Provider versus model pricing.** The same open-weight model is served by many companies at different prices, speeds, and **quantizations** (compressed copies that are cheaper and slightly dumber). The leaderboard row may not be the endpoint you get routed to. Pin the provider.
3. **Reasoning tokens bill as output.** A $0.30 model that thinks for 8,000 tokens costs more than a $3 model that answers in 300. Compare cost per task, never dollars per million. This is why reasoning is off for the bulk job.
4. **Blended price assumes a cache-hit rate you may not reach.** A **cache** is the provider re-using an unchanged prompt prefix at a discount; GLM-5.3 cache reads cost $0.26 instead of $1.40. If every prompt changes, your real bill can be several times the blended figure. Keep a stable prefix.
5. **Harness dependence.** A model at the top of the Coding Agent Index under one scaffold may do worse under another.

Source: bj0fbejiq.txt, section 5; bcy86uopa.txt, sections 7 and 9

## Learn it

All free. About five hours in total.

| # | Resource | Format | Hours | Why |
|---|---|---|---|---|
| 1 | https://artificialanalysis.ai/methodology/intelligence-benchmarking | Official methodology page | 1 | The exact v4.3 weights and how token counts and cache rates feed cost per task |
| 2 | https://artificialanalysis.ai/evaluations/omniscience and the paper at https://arxiv.org/pdf/2511.13029 | Leaderboard plus paper | 1.5 | Hallucination and abstention, the axis that matters most for a system that must cite |
| 3 | https://artificialanalysis.ai/methodology/coding-agents-benchmarking | Official methodology page | 0.5 | Why that index scores harness plus model pairs, and why it belongs to Place 1 |
| 4 | https://openrouter.ai/docs/features/provider-routing | Official docs | 1 | Pin providers, exclude quantizations, set price and latency ceilings |
| 5 | https://artificialanalysis.ai/methodology/search-api | Official methodology page | 0.5 | How to choose a search vendor on evidence if the news layer ever needs one |
| 6 | OpenRouter docs, the page on zero data retention and data policies (search the docs site for "zero data retention"; verify the exact URL) | Official docs | 0.5 | What ZDR routing does and does not cover |

Source: bj0fbejiq.txt, section 5 resource table; bcy86uopa.txt, section 0

## 10-minute exercise

Pick a model for one job and defend the pick in writing.

1. The job: tag 60,000 corpus passages with a topic label each. Not urgent. Finance jargon such as "sales-to-capital" and "Baa3" must survive. Every passage sends about 600 tokens and gets 150 back.
2. Open https://artificialanalysis.ai/models/open-source. Sort by price. Write down the three cheapest models with an Intelligence Index of 40 or more.
3. For each of the three, open its AA-Omniscience row and note the hallucination rate.
4. Open https://openrouter.ai/models, search each id, and copy the real in and out price and whether a `:batch` variant exists.
5. Work out cost per task for each: 600 times the input price plus 150 times the output price, divided by one million. Multiply by 60,000.
6. Choose. Write five lines in your decisions log (Chapter 0, rule 6): the job, the pick, the cost per task, the trap you checked, the number you would recheck next month.

Then compare with the project's answer: `z-ai/glm-5.3-flash:batch`, about $4.95 for the tagging half of the bulk job, reasoning off. If you chose differently with a written reason, that is a good outcome, not a wrong one.

Source: bcy86uopa.txt, section 7

## Done when

- You can say, in one sentence each, what OpenRouter is and what Artificial Analysis is.
- You can explain why Cursor never sees an OpenRouter key, and where the open-weight models actually run.
- Your OpenRouter account has a $75 monthly limit and logging off, and you can say why each.
- You can name the four pinned model ids and give one number that justifies each.
- You can list the five traps without looking, and say which one the bulk job guards against.
- Your decisions log holds the five-line note from the exercise, with a cost per task in it.
