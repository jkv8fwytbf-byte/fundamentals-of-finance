# Section 9: Non-goals, risks, cut lines, deferred

## Non-goals for v1

**In short.** A non-goal is something the plan leaves out on purpose. "v1" is the first working version, which M2 through M4 will build. Plan section 9 lists these non-goals:

- Valuing your own holdings or tracking your P&L, meaning your personal profit and loss.
- Real-time prices, meaning prices that refresh every second.
- Multi-user use, meaning more than one person logging in, and any commercial use.
- Any buy or sell output of any kind.
- Scraping Bloomberg, INDmoney, screener.in or Tickertape. Scraping means a program copying data off a website.
- Docker or self-hosting, meaning running the system on your own packaged server.
- Python in the production path, the code that actually runs the nightly jobs. That code stays in TypeScript.
- The option-value sheet and the lease and R&D converter sheets, extra workbook tabs for special cases.
- Fine-tuning any model, meaning retraining a model on your own data.
- BYOK inside Cursor. BYOK means "bring your own key", pasting your own model key into Cursor.

> **Comment**  
> **What it means for you:** if you catch yourself wanting one of these, the answer is "not in v1". Leaving them out keeps the build small enough to finish.  
> **Decision needed:** none, already decided in the plan.  
> **Money:** none. Cursor Pro stays at $20 per month, already paid, with no extra keys inside it (plan section 6).  
> **When:** M0 to M4. Some come back only in M5, only if others ever use it, later.

**Read more.** 1-read-this-first.pdf, *1. What we are building, in one page*. 4-the-guide.pdf, *Chapter 9. Data sources: where every number comes from, and what you may do with it*.

## Risks and what catches them

**In short.** A risk is a thing that could go wrong. A mitigation is the catch that stops it from hurting. Plan section 9 pairs each risk with its catch, one sentence each below.

- If the code does the same math in a different order and breaks the 1e-6 golden test, checks inside each module, a 1e-9 warning and a later second golden case catch it (plan section 9). The golden test checks that the engine reproduces the Almarai example to within one millionth.
- If the free Neon database, the service that holds the numbers, fills its 0.5 GB limit, moving to the paid Launch tier at M4 catches it (plan section 9).
- If Pinecone, the search index for Damodaran's writing, bills for re-sending unchanged text, a content-hash manifest catches it (plan section 9). That manifest is a list of fingerprints, one per text, so unchanged text is never re-sent.
- If a GitHub Actions job, the robot that runs jobs, hits the 6-hour cap or a top-of-hour schedule is dropped, chunked jobs, off-hour timers and a staleness alarm catch it (plan section 9). A staleness alarm fires when the last run is too old.
- If a licensed number leaks to a place it may not go, four locks catch it: NOT NULL, a database CHECK, a retrieval allow-list and `data_collection: deny` (plan section 9). NOT NULL means the database refuses a blank source or license, CHECK means it refuses a wrong value, and an allow-list means the search reads only approved sources, and `data_collection: deny` is a setting that tells crawlers and tools not to collect that text.
- If the corpus, the collection of his writing, has gaps in blog years 2012 and 2025 or in image-only decks, backfill and OCR before tier 1 is declared complete catch it (plan section 9). OCR turns images of text into text, and tier 1 is the blog posts.
- If you become dependent on the AI tool, attempt-then-ask, owning the tests, one no-AI evening a week and a decisions log catch it (plan section 9).
- If Cursor's included model pool runs out, coding falls back to Composer or Grok, and the pipeline is unaffected because it never used Cursor's models (plan section 9).

> **Comment**  
> **What it means for you:** every risk has its catch written down before the build starts. You do not have to remember them, and I will build most of the catches.  
> **Decision needed:** none, already decided in the plan.  
> **Money:** Neon $0, later about $10 to 20 for the Launch tier; Mistral OCR about $10 one-off for the image-only decks (plan section 6).  
> **When:** most catches land in M2, foundation build, me, days 3 to 7 after go. The Neon move waits for M4, weeks 4 to 8. The no-AI evening starts in M3, weeks 2 to 4.

**Read more.** 4-the-guide.pdf, *Chapter 0. How to learn with an AI coding tool without becoming dependent on it* and *Chapter 3. GitHub Actions: the robot that tests your code and runs it at night*.

## Cut lines

**In short.** A cut line is a rule for what to drop if time runs short. Plan section 9 sets one rule and one "never cut" list. The rule: if month 3 arrives and M4 is unfinished, ship US-only and postpone EODHD, the paid feed for Indian company numbers (plan section 9). India without its fallback tests would be worse than no India. The "never cut" list has six items (plan section 9): the golden test in CI, three vintage ids on every run, source and license NOT NULL, the India fallback log, the no-advice test, and cited claims in every memo. CI means continuous integration, the automatic test run on every change. A vintage id names which dated version of a Damodaran table a run used. The India fallback log records when an industry number came from emerging markets or Global instead of India.

> **Comment**  
> **What it means for you:** if the schedule slips, the India feature waits, not the safety checks. You will still have a working US system.  
> **Decision needed:** none, already decided in the plan.  
> **Money:** postponing EODHD saves $60 per month, a line that only starts from M4 anyway (plan section 6).  
> **When:** checked when month 3 arrives after go (plan section 9), which is after the planned end of M4, weeks 4 to 8.

**Read more.** 1-read-this-first.pdf, *3. The six rules that make the numbers trustworthy*. 4-the-guide.pdf, *Chapter 16. The schedule: twelve evenings-only weeks, from "go" to a working system*.

## Deferred

**In short.** Deferred means "not now, maybe later". Plan section 9 lists these:

- pi, an optional terminal tool, where a terminal is the text window for typing commands. pi may come later, or never.
- Sub-agents, helper AI programs that run tasks for the main one.
- Blacksmith, a faster paid runner for CI jobs.
- The four remaining regional tables and `indname.xls`, the file that maps company names to industries (plan section 9).
- Option value and the converter sheets.
- A second golden case, Apple TTM. TTM means trailing twelve months, the last four quarters added up.
- Parallel or Exa news discovery, two services that find news stories.
- A Pinecone Assistant spike, a short trial of Pinecone's built-in question tool.
- A web app, and commercial licenses, the paid data rights needed if others ever use the system.

> **Comment**  
> **What it means for you:** none of these block the first working system. You will not need to learn them in M1 to M4.  
> **Decision needed:** none, already decided in the plan.  
> **Money:** none now. Parallel about $18 is optional and only if it is ever used (plan section 6).  
> **When:** after M4, weeks 4 to 8, at the earliest. Several belong to M5, only if others ever use it, later.

**Read more.** 4-the-guide.pdf, *Chapter 10. OCR, web crawling and sub-agents: three helpers, and when to leave them in the drawer*. 3-the-other-side.pdf, *The Other Side, Chapter 6: What This Means for the App*.
