# Section 10: Technical appendix, in plain words

## 10.1 Correctness rules

**In short.** Five rules keep every number honest. Each will be enforced by a test or a database rule, not by memory.

- Golden test. The engine must reproduce the workbook's own example, Almarai, to within 1e-6, one millionth (plan section 10.1). That example gives 7.187840270062114 per share against a price of 72.28 (plan section 10.1, the verified golden case). A script will pull the expected numbers from the workbook, and CI, the robot that runs tests on every change, will lock that file so no AI agent can edit the test instead of the code (plan section 10.1).
- Vintage. A vintage is the dated version of one data file. Every run will store three vintage ids: market, country risk, industry (plan section 10.1). The 2026 data alone holds risk-free rates of 3.95%, 4.58% and 4.75%, and ERPs of 4.20%, 4.23% and 4.46% (plan section 10.1). ERP is the equity risk premium, the extra return people demand for holding stocks instead of safe bonds.
- Source and license class. Every stored fact will name its source and one of seven license classes, and the librarian's index will refuse the last three: personal licensed data, proprietary notes, link-only sources (plan section 10.1).
- India rules. The rupee risk-free rate is the 10-year government bond yield published by the RBI, India's central bank, minus India's default spread, so country risk is not counted twice (plan section 10.1). India's ERP is the mature ERP plus the country risk premium: 4.23% plus 2.85% equals 7.08% for January 2026 (plan section 10.1). An industry with fewer than 10 Indian firms falls back to emerging markets, then Global; 27 of 94 Indian industries are that thin (plan section 10.1).
- No advice. A test will scan every report, memo and chat answer for words that recommend a trade or name a future price (plan section 10.1).

> **Comment**
> **What it means for you:** You cannot break these rules by accident; the code and the database will refuse the wrong input.
> **Decision needed:** none, already decided in the plan.
> **Money:** none.
> **When:** M2, foundation build, me, days 3 to 7 after go, for the first three rules and the advice test; M4, weeks 4 to 8, for the India rules (plan section 5).

**Read more.** 1-read-this-first.pdf, section "3. The six rules that make the numbers trustworthy". 4-the-guide.pdf, "Chapter 9. Data sources: where every number comes from, and what you may do with it".

## 10.2 The engine

**In short.** The engine is the calculator that turns inputs into a value per share. It will be written in TypeScript as pure functions. A pure function always returns the same output for the same input and changes nothing else, like a calculator with no memory. It will use float64, the standard 64-bit format computers use for decimal numbers. A module is one code file with one job, and each module mirrors one workbook sheet (plan section 10.2):

| File | What it computes (plan section 10.2) |
|---|---|
| `rating.ts` | a credit rating estimated from interest coverage, with three firm-type tables and the country default spread |
| `costOfCapital.ts` | the cost of capital by four approaches; two of them add the current risk-free rate minus the rate embedded in the table |
| `fcff.ts` and `terminal.ts` | the cash flow path: growth, margin convergence, tax fade, reinvestment with the lag switch, past losses, discount factors, terminal cost of capital as risk-free plus mature ERP, terminal reinvestment as growth divided by return on capital |
| `failure.ts` | the failure adjustment |
| `options.ts` | the option adjustment, switched off for Almarai |
| `india.ts` | the India rules from 10.1 |
| `reverseDcf.ts` | the growth or margin the current price implies (plan section 5) |
| `monteCarlo.ts` | ranges from random draws over the industry quartiles (plan section 5) |
| `impliedErp.ts` | his goal-seek as a root finder, a routine that adjusts one input until an output hits a target; anchors: index 7398.084728 at ERP 4.25%, expected return 8.8437% |

Every output carries an audit: rating basis, missing interest flag, tier used, three vintage ids, sources, engine version and a hash, a short fingerprint, of the inputs (plan section 10.2). Excel and JavaScript both use float64, so an order-faithful port agrees to about 1e-12 (plan section 10.2).

> **Comment**
> **What it means for you:** You will be able to open one file, hold the matching sheet beside it, and check the formulas line by line.
> **Decision needed:** none, already decided in the plan.
> **Money:** none.
> **When:** M2, foundation build, me, days 3 to 7 after go (plan section 5).

**Read more.** 2-damodaran-essentials.pdf, "Chapter 3: The DCF Chain, Exactly As the Workbook Does It". 4-the-guide.pdf, "Chapter 4. TypeScript for a Python brain".

## 10.3 The database tables

**In short.** The database will live on Neon, a hosted version of Postgres. A table is a grid with named columns, one row per record. NOT NULL means a column may never be empty. CHECK means a value must pass a test before it is stored. The plan names twenty-one tables, grouped here by purpose (plan section 10.3).

| Purpose | Tables | Rules worth knowing |
|---|---|---|
| Reference data from his files | `vintage`, `country_risk`, `industry_stat`, `industry_dist`, `erp_monthly`, `erp_annual` | firm counts and quartiles kept; his ERP columns copied verbatim |
| Companies and facts | `company`, `fact`, `ltm_financials`, `watchlist` | in `fact`, source, license class, filing date, accession and vintage id are all NOT NULL; missing interest is a flag |
| Memos and claims | `memo`, `claim`, `valuation_inputs`, `narrative_note` | memos are versioned, base or opposing; every input row points to a claim |
| Runs and results | `valuation_run`, `realised_price`, `market_context_event` | a run stores input hash, outputs, three vintage ids NOT NULL, tier, rating basis, seed; headlines are annotation only |
| Jobs and evals | `job_heartbeat`, `rag_eval_case`, `rag_eval_run`, `chunk_manifest` | `chunk_manifest` carries the license CHECK that refuses the three forbidden classes |

Raw files sit in a private R2 bucket, a file store on Cloudflare, keyed by sha256, a fingerprint of the file's bytes (plan section 10.3).

> **Comment**
> **What it means for you:** The database will refuse a number without a vintage, so the honesty rules live in the storage.
> **Decision needed:** none, already decided in the plan.
> **Money:** Neon $0 now, later about $10 to 20 per month; Cloudflare R2 $0 (plan section 6).
> **When:** M2, foundation build, me, days 3 to 7 after go (plan section 5).

**Read more.** 4-the-guide.pdf, "Chapter 5. Postgres and Neon: the one place the numbers live".

## 10.4 The librarian and the models

**In short.** The librarian is the search part of the system. It will find Damodaran passages that answer a question and hand them to the model with citations.

- Vectors and embeddings. An embedding turns text into a vector, a list of numbers that captures its meaning. Voyage's `voyage-context-4` makes vectors of 1024 numbers, stored in a Pinecone serverless index (plan section 10.4).
- Reranker. A second model that re-sorts the first results; `rerank-3` cuts 50 candidates to 8 (plan section 10.4).
- Metadata. The label on each stored chunk: source, title, date, document type, license class, vintage, speech flag, region, company (plan section 10.4).
- Tiers. Batches indexed in order: tier 1 the blog; tier 2 the book, packets with speaker notes, exams; tier 3 dataset rows as sentences; tier 4 transcripts after a punctuation pass of about $11 (plan section 10.4). Third-party press, filings, the Tykoh guide, Bloomberg and EODHD are never indexed (plan section 10.4).
- Router. The rule that picks a method: a question about one document pastes that document in; a question across the corpus searches (plan section 10.4).
- Pinned model ids. An exact model name fixed in code, recorded with the benchmark version it was chosen under. The four: `z-ai/glm-5.3` for memos and answers, `z-ai/glm-5.3-flash:batch` for bulk work, `moonshotai/kimi-k3` as judge, `deepseek/deepseek-v4.1-flash` as fallback (plan section 10.4). Prices are re-checked monthly; GLM-5.3 was listed at $0.92 to 1.40 per million tokens in and $3.14 to 4.40 out in September 2026 (plan section 10.4).

> **Comment**
> **What it means for you:** Every answer will cite its passage, and nothing paid or proprietary can leak into the index.
> **Decision needed:** none, already decided in the plan.
> **Money:** OpenRouter $30 to 70 per month, first purchase $20 of credits, spend limit $75; Pinecone $0 now, later $20; Voyage $0 (plan section 6).
> **When:** M2, foundation build, me, days 3 to 7 after go, for tiers 1 and 3 (plan section 5); the plan sets no date for tiers 2 and 4.

**Read more.** 4-the-guide.pdf, "Chapter 6. Pinecone, Voyage and RAG in plain words" and "Chapter 7. OpenRouter and benchmark literacy: one door to every model, and how to read the scoreboard".

## 10.5 The memo writer

**In short.** The memo writer will turn a filing and his writing into a story with numbers attached. It follows his five steps: develop the narrative; test it against history and common sense; convert it into value drivers; connect it to a valuation; keep the feedback loop open (plan section 10.5). Every claim passes the 3P gate, his test of whether a story is possible, plausible and probable.

- Template. The workbook's "Stories to Numbers" sheet, one row per driver, each with a required link to the story (plan section 10.5).
- Reverse DCF first. A DCF, discounted cash flow, is the valuation itself; running it in reverse means starting from today's price and asking what it assumes. Hold margin and cost of capital, solve for the year-10 revenue the price implies, turn it into market share, test that with 3P (plan section 10.5).
- Guard rails. An uncited claim rejects the memo. Numbers go into `valuation_inputs`, never read out of prose. The engine is never edited. You approve a diff, proposed against prior inputs, in Cursor. An opposing memo is mandatory. A re-run labels the change tweak, shift or break (plan section 10.5).
- Plausibility bands. A cost of capital outside 5.3 to 9.9% for the US, or 6.3 to 11.7% globally, is flagged (plan section 5).
- Sources. His 2014 narrative posts, the Uber exchange with Gurley, Corporate Life Cycle sessions 10 to 13, Data Update 5 for 2026 (plan section 10.5).

> **Comment**
> **What it means for you:** The model proposes, you approve, and the calculator never sees a number you have not seen.
> **Decision needed:** none, already decided in the plan.
> **Money:** OpenRouter $30 to 70 per month, spend limit $75 (plan section 6).
> **When:** M2, foundation build, me, days 3 to 7 after go (plan section 5).

**Read more.** 2-damodaran-essentials.pdf, "Chapter 1: Why value, the story, and the 3P test". 3-the-other-side.pdf, "The Other Side, Chapter 6: What This Means for the App".

## 10.6 The jobs

**In short.** A job is a script that GitHub Actions, GitHub's robot, runs on a schedule or on request. Cron is the schedule format. Dispatch means a run you start by hand. A heartbeat is a row a job writes when it finishes, so silence can be noticed. An accession is the id of one SEC filing. The nine jobs (plan section 10.6):

- `load-damodaran`: dispatch; loads one vintage of his datasets.
- `ingest-edgar`: nightly; pulls a filing only when a new accession appears.
- `value-watchlist`: nightly; revalues every watchlist name.
- `watch-erp-crp`: monthly and quarterly; checks his file names, and a new sha256 creates a vintage row and a GitHub issue.
- `rag-index`: dispatch; indexes one tier.
- `rag-eval`: nightly; scores the librarian, report only.
- `news-headlines`: nightly; pulls headlines from licensed sources.
- `realised-prices`: weekly; records later prices for the scoreboard.
- `report`: on demand; produces the markdown and PDF report.

Every job writes a heartbeat, and a staleness alarm fires after 36 hours (plan section 10.6). Schedules sit off the hour, because top-of-hour cron runs get dropped (plan section 5).

> **Comment**
> **What it means for you:** The robots work at night, and a missed night shows up as an alarm rather than a stale number.
> **Decision needed:** none, already decided in the plan.
> **Money:** GitHub CI $0 to 25 per month (plan section 6).
> **When:** M2, foundation build, me, days 3 to 7 after go, for the nightly robots; M4, weeks 4 to 8, for the first scored horizon (plan section 5).

**Read more.** 4-the-guide.pdf, "Chapter 3. GitHub Actions: the robot that tests your code and runs it at night".

## 10.7 The market-regime panel

**In short.** A regime is the mood of the whole market. This panel will describe that mood and will never feed a number into a valuation.

- Implied ERP. His monthly headline figure and its variants from `ERPbymonth`: trailing 12 months, adjusted risk-free, smoothed, normalized, net cash yield (plan section 10.7).
- ERP against history. His `histimpl` series, 1960 to 2025, with his benchmark averages of 4.25% long run, 5.16% for 2006 to 2025 and 5.00% for 2016 to 2025 (plan section 10.7).
- Expected return on stocks. He calls 8 to 9% healthy (plan section 10.7).
- Earnings yield against bond yield. Context only, because he calls PE noisy and unreliable (plan section 10.7).
- Credit spreads. High-yield and BBB spreads from FRED, the US Federal Reserve's public data service, series `BAMLH0A0HYM2`, `BAMLC0A4CBBB`, `DGS10`; a spread is the extra yield on riskier bonds (plan section 10.7).
- Concentration. The weight of the top 7 stocks in the index, 30.9% in his 2026 update (plan section 10.7).
- Fair-value grid. What the index would be worth at each ERP from 2 to 6% (plan section 10.7).

Each indicator becomes a percentile band, the share of past readings below today's, with a plain sentence, for example that the market is pricing in less risk than its 10-year median (plan section 10.7). His caveat is printed on the panel in his own words: "I am not a market timer", he says, and he values the market at regular intervals to measure what it is pricing in, not to forecast where it goes (plan section 10.7). Headline sentiment stays in `market_context_event` as an overlay only and never enters a computation (plan section 10.7).

> **Comment**
> **What it means for you:** You will see what the market is pricing in, in plain sentences, with his own warning against timing beside it.
> **Decision needed:** none, already decided in the plan.
> **Money:** none.
> **When:** M4, weeks 4 to 8; done when the panel reproduces his September 2026 numbers, ERP 4.09% and expected return 8.84% (plan section 5).

**Read more.** 2-damodaran-essentials.pdf, "Chapter 6: Relative Valuation and What the Market Prices In". 3-the-other-side.pdf, "The Other Side, Chapter 2: His Misses with the Numbers".

## Critical files

**In short.** Four locations hold everything the build depends on (plan section 10, Critical files):

- `/Users/siddharth/Downloads/fcffsimpleginzu.xlsx`: the workbook and its golden case.
- `/Users/siddharth/Downloads/damodaran-data-01.zip` and `-02.zip`: the 2026 datasets, loaded once into Neon.
- `/Users/siddharth/Downloads/financeMD/`: the corpus of blog, packets, exams and book, including `pc/implprem/ERPbymonth.md` and `pc/datasets/histimpl.md`, for the librarian, the regime panel and the document the plan calls doc C.
- `~/code/valuation/packages/{engine,db,rag,memo,mcp-server,models}/`, `.cursor/` and `AGENTS.md`: what M2 will create.

> **Comment**
> **What it means for you:** Keep the three Downloads items where they are until M2 has loaded them; the fourth path will not exist until I build it.
> **Decision needed:** none, already decided in the plan.
> **Money:** none.
> **When:** M2, foundation build, me, days 3 to 7 after go (plan section 5).

**Read more.** 4-the-guide.pdf, "Chapter 15. The Damodaran watch and read order for this project". 1-read-this-first.pdf, section "2. Where the pieces live and who runs them".
