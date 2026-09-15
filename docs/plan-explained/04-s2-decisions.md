# Section 2: Your decisions, and the two that changed after your review

## The decisions table

**In short.** This part of the plan records eight decisions, and two of them changed after your review of the earlier draft (plan section 2). Here is each row in plain words.

- **Cursor, not pi, as the daily tool.** Cursor is a code editor with an AI helper built in, and you already pay for it. It shows every change as a diff, a before-and-after view of a file, and its Plan mode shows an English plan before any change. pi is a bare terminal tool, a text-only command window, with no safety gates, so it is not a first tool. Cline, a free add-on inside Cursor, will be the bench for trying other models. You will not buy a second paid tool (plan section 2).
- **Open-weight models in the runtime, not the editor.** An open-weight model is one whose trained parameters are published, so anyone can run it. The runtime is the part of the system that runs by itself at night; the editor is the tool you type code into. Putting your own model key into Cursor is unofficial and breaks its privacy promise, so Cursor will keep its own models. Open-weight models will run inside your system, through OpenRouter, one account that reaches many models (plan section 2).
- **Outsource everything.** Every part will be a hosted service, like hiring specialists instead of building a workshop: Neon for the database, Pinecone for search, Voyage for turning text into searchable numbers, OpenRouter for models, GitHub for code and night jobs, Langfuse for model logs, Cloudflare R2 for raw files, Hex for dashboards, Mistral for scanned pages, EODHD for India data. You will manage no servers (plan section 2).
- **Private, always.** The code will live in a private repository, the folder GitHub keeps code in, inside a GitHub organization you own; an organization is a shared workspace that keeps faster job machines available later. No public web app, and Cursor Privacy Mode stays on (plan section 2).
- **Money is not the object, time is.** The ceiling is $200 per month. I will build the foundation in the first week while you create accounts and read the four documents; from week two you will drive Cursor (plan section 2).
- **Explain everything.** Four documents and diagrams come first, and every milestone says what you will see (plan section 2).
- **Worth it if someone else ever uses it.** Every stored number will carry a license label, a tag saying where it came from and what you may do with it, so going public later would be a data license purchase plus web screens, not a rewrite (plan section 2).
- **Earlier decisions kept.** US first, then India; a watchlist of 20 to 50 names, where a watchlist is the list of companies the system follows; research only; no tracking of holdings; a descriptive market panel allowed, advice not (plan section 2).

> **Comment**
> **What it means for you:** The tool you type into stays the one you already know, and the clever model routing happens out of sight, inside the system.
> **Decision needed:** Decision 1, go or wait, after you read 1-read-this-first.pdf and 2-damodaran-essentials.pdf; the eight rows themselves are already decided in the plan.
> **Money:** Cursor Pro $20 per month, already paid; the overall ceiling is $200 per month (plan section 6).
> **When:** M0, documents and diagrams, me, done today 2026-09-14; the Cursor and Cline setup comes in M1, you, 3 evenings, starting only when you say go (plan section 5).

**Read more.** In 4-the-guide.pdf, read "Chapter 2. Cursor and Cline: the tool you type into, and the free bench beside it". In 1-read-this-first.pdf, read "2. Where the pieces live and who runs them".

## 2a. What the point of open-weight models is

**In short.** Open-weight models such as GLM, Kimi, Qwen and DeepSeek cost 7 to 40 times less per token than frontier models (plan section 2a). A token is a piece of a word, and models charge by the token; a frontier model is one of the most capable closed models of the moment. An open-weight model can be pinned to an exact checkpoint, one frozen version, so a valuation run in 2026 could be re-run in 2029 with the same model, which closed models cannot promise (plan section 2a). The licenses, the legal terms of use, are permissive: GLM-5.3-Flash uses the plain MIT license, and GLM-5.3 and Kimi K3 have revenue clauses that do not touch a private project (plan section 2a). The price is capability. On the Artificial Analysis Intelligence Index v4.3, a public scoreboard dated 2026-09-07, the frontier scores 53 and the best open-weight model, GLM-5.3, scores 45 (plan section 2a). That gap appears in long tasks where a model takes many steps alone, not in the summarizing and extracting that fills a valuation pipeline, the chain of steps from raw data to memo. One correction: I earlier wrote that Meta's Muse Spark 1.3 was open-weight, and it is not (plan section 2a). The rule will be to pick a model per job by cost per task and hallucination rate, where a hallucination is a confident false statement, with every choice in one file that changes in one line (plan section 2a).

> **Comment**
> **What it means for you:** Think of hiring a reliable clerk for routine paperwork rather than a senior partner; the clerk is cheaper, and paperwork is most of the job.
> **Decision needed:** none, already decided in the plan.
> **Money:** OpenRouter $30 to 70 per month, with a first purchase of $20 of credits and a $75 spend limit (plan section 6).
> **When:** M1, you, 3 evenings after go, sets up the Cline bench; M2, foundation build, me, days 3 to 7 after go, wires the models into the runtime (plan section 5).

**Read more.** In 4-the-guide.pdf, read "Chapter 7. OpenRouter and benchmark literacy: one door to every model, and how to read the scoreboard". In 1-read-this-first.pdf, read "4.1 The model table, explained line by line".

## 2b. Plain answers to the questions from your review

**In short.** You asked five questions in your review, and the plan answers each one (plan section 2b).

- **Two places a model is used.** Place 1 is while you write code, in Cursor, on the models it includes. Place 2 is inside the product at night, when our own code asks a model to write memos, answer questions or tidy call transcripts. Open-weight models go in place 2, because that is where the volume and cost are, and a pinned model keeps old valuations reproducible (plan section 2b).
- **The point of pi.** pi is for people who want to build their own coding tool from a few basic parts and pay the least per task. I would use it one day to run a scripted agent, a model that acts on its own, inside a nightly job. You need a valuation system, not a coding tool, so pi is deferred, not judged (plan section 2b).
- **Tavily and Firecrawl, GitHub Actions, Blacksmith.** These are three different things. Tavily and Firecrawl are search and crawl services paid per query, and on the Artificial Analysis Search Index of 2026-08-18 Parallel and Exa beat them on quality per dollar. GitHub Actions is the scheduler, the alarm clock that wakes at night and runs the jobs. Blacksmith is a faster machine for those jobs, irrelevant until you pass the 2,000 free minutes. Cursor Automations can also schedule agents, but they bill through Cursor and tie the pipeline to your editor, so they will only do small chores (plan section 2b).
- **Estimates yes, advice no.** The system will print value per share, price as a percentage of value, the chance that value is below price from Monte Carlo draws (many re-runs with random inputs), what the price already requires, the market's implied risk premium against its history, and a scoreboard of how past valuations fared after 90, 180 and 365 days (plan section 2b). The implied risk premium is the extra return the market demands for stocks over safe bonds, read from today's prices. It will never print advice words. "Is it working for the next month" cannot be answered: Damodaran's own data says no valuation method forecasts next year's return well, and one month is noise. The honest question is "is the method working so far", and the scoreboard will answer it as valuations age (plan section 2b).
- **Visit the librarian first.** Yes. The librarian is the part that answers your questions with citations from Damodaran's writing. 2-damodaran-essentials.pdf, which the plan calls document C, comes right after 1-read-this-first.pdf for that reason, and the librarian's first job in M2 will be answering your questions while you read (plan section 2b).

> **Comment**
> **What it means for you:** None of these answers adds to your workload; they settle where each tool sits, and the scoreboard, not a monthly feeling, will say whether the method is working.
> **Decision needed:** none, already decided in the plan.
> **Money:** GitHub CI, the robot that tests code on every change, $0 to 25 per month; optional Parallel search about $18 (plan section 6).
> **When:** M2, foundation build, me, days 3 to 7 after go, for the librarian and the nightly scheduler; M4, you in Cursor, weeks 4 to 8, for the scoreboard (plan section 5).

**Read more.** In 1-read-this-first.pdf, read "4. The two places an AI model is used" and "6. Estimates, not advice: what the scoreboard shows". In 4-the-guide.pdf, read "Chapter 3. GitHub Actions: the robot that tests your code and runs it at night". In 3-the-other-side.pdf, "The Other Side, Chapter 2: His Misses with the Numbers" shows why one month tells you nothing.

## 2c. What v1, v2 and v3 mean

**In short.** v1, v2 and v3 are labels for scope, not a promise of exactly three versions (plan section 2c). v1 covers weeks 1 to 8 and means private, working and correct: the calculator with its golden test, the check that the engine reproduces the Almarai workbook answer; the database with vintages and licenses, where a vintage is the dated version of an input; the librarian; the memo writer for US names; the nightly robots; the first Hex dashboard (plan section 2c). v2 covers months 3 to 6 and adds India, the accuracy scoreboard, Monte Carlo and reverse DCF everywhere, the market-regime panel, opposing memos, and whatever your coursework suggests, such as backtests over the 1998 to 2024 archives (plan section 2c). DCF is discounted cash flow, the method that values a company from its future cash; reverse DCF works backward from the price to the growth it assumes; a backtest runs the method on old data; the market-regime panel shows what the market as a whole is pricing in. v3 happens only if others use it, adding a web app, commercial data licenses, multiple users and a public method page (plan section 2c). Nothing built in v1 will be rewritten for v2 or v3 (plan section 2c).

> **Comment**
> **What it means for you:** You get a private, correct system first, and every later stage adds rooms to a house whose foundation is already finished.
> **Decision needed:** Decision 2, which 10 to 20 US companies go on the first watchlist, because v1 memos are for US names; I will ask for the list after go, since M3 ends with a 20-name watchlist (plan section 5).
> **Money:** EODHD $60 per month, only from M4, when v2 starts India (plan section 6); v3 costs are not priced in the plan.
> **When:** v1 runs from M1 (you, 3 evenings, after go) through M4 (you in Cursor, weeks 4 to 8); v2 follows in months 3 to 6 (plan section 2c); v3 is M5, only if others ever use it, later (plan section 5).

**Read more.** In 4-the-guide.pdf, read "Chapter 16. The schedule: twelve evenings-only weeks, from "go" to a working system". In 1-read-this-first.pdf, read "14. What happens next".
