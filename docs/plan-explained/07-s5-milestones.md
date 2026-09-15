# Section 5: Milestones

## M0. Documents and diagrams

**In short.** A milestone is a checkpoint with a clear finish line. Plan section 5 has six, M0 to M5. M0 is my job, done today, 2026-09-14 (plan section 5). It delivers the four PDFs, the diagrams, and the accounts checklist. The diagrams live in FigJam, the whiteboard tool inside Figma. The checklist lists the services you will sign up for in M1. M0 is done when the four PDFs open, every link works, the FigJam boards open in your Figma account or their pictures sit in document 1, and the checklist is complete (plan section 5).

> **Comment**
> **What it means for you:** Nothing to build. Read PDF 1 and PDF 2, then tell me "go" or "wait".
> **Decision needed:** Decision 1, go or wait, after PDF 1 and PDF 2.
> **Money:** none.
> **When:** M0, documents and diagrams, me, done today 2026-09-14.

**Read more.** 1-read-this-first.pdf, "1. What we are building, in one page" and "14. What happens next".

## M1. Accounts and Cursor

**In short.** M1 is yours: about 3 evenings, starting only when you say "go" (plan section 5). The steps, in plan order:

- GitHub stores code and its history. Turn on 2FA, two-factor authentication, a second code beside your password, and save the recovery codes offline. I will create the organization and the private repo, one project's folder of code and history, and hand you ownership. Turn on secret scanning and push protection, which stop keys landing in the repo by mistake (plan section 5).
- OpenRouter is one door to many AI models with one key. Buy $20 of credits, set a $75 per month spend limit, turn prompt logging off, and turn zero-data-retention routing on, so providers keep no copy of what you send (plan section 5). Put the key in `~/.zshrc`, the file your terminal reads at start; `echo $OPENROUTER_API_KEY | cut -c1-6` should print `sk-or-` (plan section 5).
- Free accounts, one project each named `valuation`: Neon, a hosted Postgres database; Pinecone Starter, a search index; Voyage, free for 200 M tokens; Cloudflare, one R2 storage bucket; Langfuse Hobby; Mistral pay-as-you-go; Hex Community (plan section 5). Each key goes into the repo's `.env` file, never committed, and into GitHub Actions secrets, using the names in plan section 7.
- Cursor: turn Privacy Mode on in Settings, so Cursor stores none of your code. Open the repo. I will ship `.cursor/mcp.json`, which shows the system's tools to Cursor's agent, and `.cursor/rules/`, the hard rules. Try Plan mode (Shift+Tab): ask "explain how value_company works", read the plan, do not run it (plan section 5).
- Cline, optional and free, is a VS Code extension inside Cursor. Add the OpenRouter key and set GLM-5.3 for Plan and GLM-5.3-Flash for Act (plan section 5). It is your free bench for trying open-weight models before one goes into a robot.
- Day-one exercise: ask Cursor why terminal WACC equals the risk-free rate plus the mature ERP. WACC, the weighted average cost of capital, is the blended rate a company pays lenders and shareholders. ERP, the equity risk premium, is the extra return people ask for holding stocks instead of safe bonds. Then find the cell label `Mature Market ERP +` in the workbook yourself and compare (plan section 5).

M1 will be done when every key is in place, Cursor's agent lists the valuation tools, and you have read document C, which is 2-damodaran-essentials.pdf (plan section 5).

> **Comment**
> **What it means for you:** The only hands-on steps before you touch code. Two settings matter most: OpenRouter with spend limit $75, logging off, zero-data-retention on; and Cursor Privacy Mode on.
> **Decision needed:** Decision 3, yes or no to opening the free accounts listed in plan section 7, during M1 after go.
> **Money:** OpenRouter first purchase $20 of credits, spend limit $75; Cursor Pro $20 per month, already paid; other accounts $0 (plan section 6).
> **When:** M1, accounts and Cursor, you, 3 evenings, starts only when you say "go".

**Read more.** 1-read-this-first.pdf, "10. The accounts you will create, in order"; 4-the-guide.pdf, "Chapter 2. Cursor and Cline: the tool you type into, and the free bench beside it".

## M2. Foundation build

**In short.** M2 is my build, days 3 to 7 after go, while you read the walkthrough, a file that explains every folder, every command, and what to try first (plan section 5). The pieces:

- The repo: a private repository named `valuation` in TypeScript, holding `AGENTS.md`, the eight hard rules that Cursor, Cline and Claude all read (plan section 5). CI, continuous integration, is a robot that runs the tests every time code changes; it will use GitHub's Linux machines, 2,000 free minutes a month, then $0.006 per minute, capped at $25 (plan section 5).
- The calculator, `packages/engine`: a formula-by-formula port of Damodaran's spreadsheet. The golden test is one worked example with a known answer, Almarai at 7.187840270062114 per share against a price of 72.28, which the engine must match within 1e-6, that is to six decimal places (plan section 5; 1-read-this-first.pdf section 3.1). Its inputs will be pulled from the workbook by script, never typed, and CI will refuse code that fails it. Reverse DCF asks what growth or margin today's price assumes, and Monte Carlo draws many random inputs to give a range.
- The database, `packages/db`, on Neon: the tables from plan section 10.3, with constraints proven, for example a number without a vintage is refused. A vintage is the date stamp of the data file a number came from (plan section 5).
- US ingest: filings from SEC EDGAR, the US regulator's free filing site, for Apple, Costco and three more US names you choose (plan section 5). Apple's missing interest-expense line will show as a visible flag, never a silent zero.
- The librarian, `packages/rag`: RAG, retrieval-augmented generation, means the model looks up passages before answering. Blog posts and dataset sentences will sit in Pinecone, and both smoke questions, two check questions with known answers that prove the librarian works end to end, must pass (plan section 5).
- The memo writer, `packages/memo`: it will read the filing, retrieve Damodaran passages, and write the "Stories to Numbers" table plus a claims table; an uncited claim will reject the memo. A cost of capital outside 5.3% to 9.9% for the US, or 6.3% to 11.7% globally, will be flagged, and you approve in Cursor before a run (plan section 5).
- The MCP server, `packages/mcp-server`: MCP, Model Context Protocol, is a standard way to hand tools to an AI assistant. It will expose `value_company`, `write_memo`, `review_memo`, `get_industry_stats`, `search_corpus` and `report` from Cursor, Cline, Claude and pi alike (plan section 5).
- Nightly robots are scheduled jobs that run while you sleep: an EDGAR refresh, a watchlist revaluation, a watch that opens a GitHub issue when Damodaran posts a new file, and a licensed headline pull (plan section 5).
- The first Hex dashboard over Neon: watchlist, exposure, value-versus-price distribution, and the Almarai and Apple runs with ranges (plan section 5).

M2 will be done when `value_company AAPL US` prints value per share, WACC, rating basis, vintage and license; `write_memo AAPL` produces a cited memo; `search_corpus` answers the smoke questions with citations; the golden test is green in CI and a deliberate change turns it red; the nightly job has run once; and the Hex dashboard shows the watchlist (plan section 5).

> **Comment**
> **What it means for you:** You read and try commands; you do not write code yet. If I break the calculator, the golden test will turn CI red before it reaches you.
> **Decision needed:** Decision 2 starts here: I will need three US names beyond Apple and Costco, the seed of your 10 to 20 company watchlist.
> **Money:** OpenRouter $30 to 70 per month; GitHub CI $0 to 25; Neon, Pinecone, Voyage, Langfuse and Cloudflare R2 $0 (plan section 6).
> **When:** M2, foundation build, me, days 3 to 7 after go.

**Read more.** 1-read-this-first.pdf, "3.1 The golden test" and "7. The nightly robots"; 4-the-guide.pdf, "Chapter 3. GitHub Actions: the robot that tests your code and runs it at night".

## M3. You take the wheel

**In short.** In M3 you drive, in Cursor, weeks 2 to 4 (plan section 5). You will follow 4-the-guide.pdf in order. Each chapter ends with a 10-minute exercise on the real repo (plan section 5): resolve a merge conflict, two edits to the same line that Git cannot combine alone; break the golden test and watch CI go red; add a company to the watchlist; edit a memo; add a diagnostic warning; re-index one blog year; add a chart in Hex. You will track lines you wrote against lines you accepted from the tool (guide chapter 0). M3 will be done when you have merged five PRs, pull requests, which are proposed changes reviewed before merging, the watchlist holds 20 names with approved memos, and you can explain every rule in `AGENTS.md` out loud (plan section 5).

> **Comment**
> **What it means for you:** The learning phase. Every exercise is small, but each touches the real system, so the skills stick.
> **Decision needed:** Decision 2, which 10 to 20 US companies go on the first watchlist; the finish line is 20 names with approved memos (plan section 5).
> **Money:** Cursor Pro $20 per month, already paid; OpenRouter $30 to 70 per month (plan section 6).
> **When:** M3, you take the wheel in Cursor, weeks 2 to 4.

**Read more.** 4-the-guide.pdf, "Chapter 0. How to learn with an AI coding tool without becoming dependent on it" and Chapter 16, The schedule: twelve evenings-only weeks, from "go" to a working system.

## M4. India, accuracy, ranges, the market panel

**In short.** M4 runs weeks 4 to 8, you in Cursor, me on request (plan section 5). The pieces:

- EODHD is a paid vendor of company financials through an API, a machine-readable feed. Check its free tier on `TRENT.NSE`, the retailer Trent on India's National Stock Exchange, then subscribe to Fundamentals at $59.99 per month, or use indianapi.in if it is as deep for less (plan section 5). Cross-check once against Trent's own annual report.
- The INR risk-free rule: the rupee risk-free rate is the RBI 10-year G-sec yield, a 10-year Indian government bond, entered monthly as a vintage row, minus India's default spread, the extra yield India pays over a top-rated borrower (plan section 5). In the January 2026 vintage the spread is 1.87% and total ERP is 7.08%, the mature ERP 4.23% plus a country risk premium of 2.85% (2-damodaran-essentials.pdf chapter 7). Industry averages will fall back from India to emerging markets to Global below 10 firms, recorded on every run (plan section 5).
- Sector-exposure and value-versus-price views for 20 to 50 India plus US names, research only; a test will forbid advice words (plan section 5).
- Langfuse will trace every model call; you will do error analysis on 100 real memos and answers (plan section 5).
- The accuracy scoreboard: `realised_price` at 90, 180 and 365 days (plan section 5). Bias is the average signed error of value against later price: does the engine run high or low. Variance is the spread of those errors: how scattered they are. Both by sector, region, vintage and memo version. The banner will read "The engine is tested (Almarai 1e-6). The forecast is not." (plan section 5).
- The market-regime panel, descriptive only, spec in plan section 10.7. Implied ERP is the equity premium backed out of today's index price. The panel will show his monthly implied ERP against the 1960 to 2025 and 10-year history, expected return on stocks, earnings yield, company profits as a percentage of share price, against bond yield as context, high-yield spreads, the extra yield risky company bonds pay over government bonds, from FRED, the St Louis Fed's free data site, top-7 concentration, how much of the index sits in its seven largest companies, and a fair-value grid at ERP 2% to 6%, each as a plain-language state with his own market-timing caveats printed (plan section 5). Headline sentiment is an annotation, never an input.

M4 will be done when `value_company TRENT IN` shows tier, the licence class of the data source, plus vintage, the exposure view renders, the first scored horizon appears after 90 days, and the panel reproduces his September 2026 numbers, implied ERP 4.09% and expected return 8.84% (plan section 5).

> **Comment**
> **What it means for you:** Indian names arrive, and the system starts grading its own past estimates; the first grade comes only after 90 days (plan section 5).
> **Decision needed:** none, already decided in the plan.
> **Money:** EODHD $60 per month from M4; optional INDstocks API free, Kite Connect 500 rupees, Parallel about $18; total about $120 to 200 per month, ceiling $200 (plan section 6).
> **When:** M4, India, accuracy, ranges, market panel, weeks 4 to 8.

**Read more.** 2-damodaran-essentials.pdf, "Chapter 4: Discount Rates and Country Risk" and "Chapter 7: India and the Rules of Thumb"; 1-read-this-first.pdf, "6. Estimates, not advice: what the scoreboard shows".

## M5. Only if others use it

**In short.** M5 has no date; it starts only if other people ever use the system (plan section 5). It would add a browser front end, a website instead of Cursor; app-level login; commercial data licenses, paid rights to show vendor data to others; sub-agents, helper AI programs that run tasks on their own; and a public method page. The plan sets no finish line, because the trigger, other users, may never arrive (plan section 5).

> **Comment**
> **What it means for you:** Nothing now. The private version is the whole plan until someone else asks to use it.
> **Decision needed:** none, already decided in the plan.
> **Money:** none now; the line that would move later is Hex, $0 now and $36 if Professional (plan section 6).
> **When:** M5, only if others ever use it, later.

**Read more.** 1-read-this-first.pdf, section 5, What "scales", in plain words; 4-the-guide.pdf, "Chapter 10. OCR, web crawling and sub-agents: three helpers, and when to leave them in the drawer".
