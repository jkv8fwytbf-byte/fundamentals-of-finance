# Plan v5, the withdrawn "public" draft

| | |
|---|---|
| Version | v5 (draft) |
| Written | 15 September 2026, about 15:08 IST, on the old dev branch |
| Verdict | Never submitted; removed in the next commit, 86 seconds later (15:08:37 to 15:10:03 IST) |
| Where it survives | Commit 7e778aa on the branch archive/first-attempt-plan-v5 |
| What changed next | Nothing. Plan v4 stayed the plan, and the folder stayed local and private until 26 September 2026, when Siddharth chose a public repository for everything. |

This draft flipped the v4 decision "Private, always" to a public repository. It was committed as `docs/plan.md` at 15:08 IST on 15 September (`7e778aa`, a checkpoint commit on the old dev branch) and removed in the next commit, `d2b2279`, at 15:10.
It is kept here because it shows the question was asked before, and because the 26 September
decision (docs/decisions/001) answers it the other way for a different reason.

## The draft, word for word as it was committed

# Plan v5: a public, outsourced Damodaran valuation system, built fast, explained slowly

Dated 2026-09-15. Replaces v4. The v4 decision **Private, always** and the Cursor Privacy Mode secrecy layer are withdrawn. The repo is public. Keys and licensed data stay out of git. Numbers below were checked against live vendor pages on 2026-09-13/14. Plain English first; the technical appendix (§10) is for later.

## Scope of this approval: M0 only

Siddharth wants to read and think before anything else is built. So this approval covers **M0
only**: the four documents, the FigJam diagrams, and the accounts checklist. Everything from M1
onward stays in this file as the agreed direction and is **parked until he says go**. Nothing is
installed, no repo is created, no account is opened, no code is written in this pass.

**M0 deliverables, in the order I will produce them:**
1. `docs/damodaran-essentials.md` + PDF (document C, the revision brain-dump), written from the
   corpus in `~/Downloads/financeMD/` with a pointer to the lecture or packet behind each idea.
2. `docs/read-this-first.md` + PDF (document A): the system in plain words with the diagrams,
   the vendor scorecard, the accounts checklist, the correctness rules, the model table explained.
3. FigJam boards through the Figma connector: architecture, nightly data flow, the valuation
   chain, the memo pipeline, the milestone map. Links go into document A. If the starter-plan
   view seat blocks creation, the boards ship as images inside A and I note the upgrade.
4. `docs/guide/` + PDF (document B, the teaching guide), including the Figma/FigJam chapter and
   a two-hour starter path (Figma's own free tutorials, then editing the architecture board).
5. `docs/other-side/` + PDF (document D, the critics reader).
Delivered where he can read them: a `docs/` folder on this Mac (in `~/Valuation/`) and, if
wanted, pages in this app. Done when the four PDFs open, every link resolves, and the
boards open in his Figma account or their images are in A.

**Figma, concretely.** The Figma connector in this app is signed in as Siddharth (team
"Siddharth's team", starter plan, seat "View"). It lets me create FigJam diagrams in his account
and read designs back into code. Learning it is a chapter in document B and the first exercise is
on the architecture board.

### M0 status and resume plan (2026-09-14, afternoon session)

**Context.** The first M0 pass delivered document A (`~/Valuation/docs/read-this-first.md` and
the 18-page PDF), the five FigJam boards (links in A, PNGs in `docs/diagrams/png/`) and the
pandoc + tectonic build script (`docs/_build/build.sh`). The background workflow that was writing
documents B, C and D chapter by chapter was killed when that session ended. Its journal marks
every writer as failed, so "resume from cache" would rerun all of them and overwrite good files.
Ten chapter files were fully written before the kill; 22 are missing. This section is the plan to
finish M0 without redoing what exists. Still nothing outside `~/Valuation/docs` is touched.

**What exists (complete files, keep as is):**
- C (`docs/damodaran-essentials/`): c1, c3, c6.
- B (`docs/guide/`): 00, 01, 03, 04.
- D (`docs/other-side/`): 00, 04, 05.

**What is missing (22 files):**
- C: c2 accounting minimum, c4 discount rates and country risk, c5 growth, terminal value and the
  dark side, c7 India and rules of thumb.
- B: 02 Cursor and Cline, 05 Postgres and Neon, 06 Pinecone/Voyage/RAG, 07 OpenRouter and
  benchmark literacy, 08 fine-tuning at three levels, 09 data sources, 10 OCR/crawling/sub-agents,
  11 evals and Langfuse, 12 Hex, 13 Figma and FigJam, 14 security hygiene, 15 Damodaran watch
  order, 16 the schedule, 17 glossary.
- D: 01 his own dark side, 02 his misses with numbers, 03 academic and practitioner critiques,
  06 what this means for the app.

**How I finish it (one continuation workflow, then assembly by hand):**
1. A new workflow script `m0-documents-resume` (not a cache resume): **one writer per missing
   file** (22 writers, finer than the old 3-files-per-writer batches so a kill loses less), same
   style rules and the same source list as before (the nine local research reports, the corpus in
   `~/Downloads/financeMD/`, this plan). Each writer also gets the list of sibling chapters that
   already exist and a block of canonical numbers (India CRP/ERP Jan and Jul 2026, Almarai golden
   case, September 2026 implied ERP, the three 2026 US risk-free snapshots, model prices and AA
   index values) so chapters agree with each other. The Figma chapter gets the five board URLs;
   the Cursor chapter gets the Cursor/Cline facts from the harness report.
2. Every written file (the 22 new ones and the 10 existing ones) is then checked by **one
   verifier** with a combined lens: style and forbidden language (advice words, em-dashes, arrows
   in prose, missing Source lines, jargon defined on first use) and facts against the named
   sources (every number traceable; URLs well formed; no invented resources). Only files with
   confirmed problems go to a fixer agent that edits in place. Then one cross-document consistency
   check over all 32 chapters (same numbers everywhere; reading order). Siddharth is short on
   tokens today, so this is the lean version of the loop (one verifier per file, no second pass).
3. I apply whatever the consistency check reports that the fixers did not, write a short
   preface file for each document (how to read it, chapter order), and build three PDFs with the
   existing script: `damodaran-essentials.pdf` (c1..c7), `guide.pdf` (00..17),
   `other-side.pdf` (00..06).
4. URL check: extract every http(s) link from all four documents and confirm each resolves
   (HEAD/GET, read-only); fix or mark "verify" any that do not.
5. Send the three PDFs. Update the memory file `valuation-project-direction.md` with "M0
   complete" and the file list.

**Scale note.** This is 22 writers, 32 verifiers, a handful of fixers and a final checker
(about 60 agents), above the medium-workflow guideline because the user asked for the whole of
M0; trimmed from the fuller two-verifier loop because tokens are tight today. Writers run one
file at a time so a kill loses at most one chapter and a resume picks up the rest from cache.
Concurrency is capped by the runtime; expected wall clock 20 to 40 minutes.

**Done when:** all 32 chapter files exist, the three PDFs open, no forbidden language remains,
numbers agree across documents, every link resolves or is marked "verify", and the PDFs have
been sent. Nothing from M1 onward starts until Siddharth says go.

### M0 addendum: "The Plan, Explained" (requested 2026-09-14, evening)

**Context.** M0 is delivered (PDFs 1 to 4 in `~/Valuation/docs/`, numbered in reading order, plus
`0-START-HERE.txt`). Siddharth asked for this plan file "broken down, with comments", all sections
including the technical appendix. He wants each part shortened to plain lines followed by a comment
that says what it means for him, whether a decision is needed, and the money involved. Still M0:
no repo, accounts, installs or code.

**Deliverable.** `~/Valuation/docs/5-the-plan-explained.pdf`, built from markdown chapters in
`~/Valuation/docs/plan-explained/` (one file per plan section: `00-preface.md`, `01-scope.md`,
`02-s0-five-steps.md` ... `12-s10-technical-appendix.md`), with the existing
`docs/_build/build.sh` (pandoc + tectonic, the wrapping filter already in place).

**Format of every section chapter (fixed, so it reads the same all the way through):**
1. `## Section N: <plan title>` (the scope section is "Section S").
2. `### In short`: 3 to 8 plain sentences or bullets; every term defined on first use.
3. `### Comment` (a blockquote) with four fixed lines: **What it means for you**, **Decision
   needed** (none, or exactly what and when), **Money** (from plan section 6 or "none"), **When**
   (milestone number and the calendar estimate from section 5).
4. `### Read more`: which PDF and chapter goes deeper (PDF 1 to 4 names as they are on disk).
The preface states the three decisions he actually has to take (go or wait; which US companies;
eight free accounts yes or no) and says the full plan text lives in the repo at `docs/plan.md`.

**Rules (same as the other documents):** plain English, about 20 words a sentence, no em-dashes,
no arrows in prose, no buy/sell/hold/target-price language, no number that is not in the plan or
the four documents (cite the plan section), American spelling, "will" for anything after M0.

**How (ultracode is on, so a small workflow):** 12 writers in parallel, one per plan section plus
the preface, each given only its slice of the plan text, the format above and the canonical
numbers block; then one checker that greps every number in the chapters against the plan file and
the M0 markdown and lists mismatches or invented figures; I apply fixes by hand, build the PDF,
run the same read-only URL check, and send it. Roughly 13 agents, 10 to 15 minutes.

**Done when:** the PDF opens, all 11 plan sections plus preface are present in order, the checker
reports no unmatched numbers, and the file is sent. `0-START-HERE.txt` gets one extra line for it.

## 0. What happens next, in five steps (after M0, when he says go)

1. **I write the four documents**, starting with **C, "Damodaran, the important parts"** (your
   revision brain-dump) and **A, "Read This First"**, then the teaching guide and the critics
   reader, plus the FigJam diagrams. Days 1–3.
2. **You read C and A** and create the accounts from A's checklist. Three evenings. No code yet.
3. **I build the foundation as code** in the public repo (calculator with the golden test,
   database, librarian, memo writer, MCP tools, nightly robots, first dashboard) and write a
   walkthrough that explains every file. Days 3–7.
4. **You work in Cursor**, one guide chapter and one small change at a time, with the walkthrough
   open. Weeks 2–4. I am on call.
5. **India, the accuracy scoreboard, ranges and the market panel** follow in weeks 4–8, you
   driving, me on request.

The "other md files" you asked about: A–D are reading; the walkthrough and the guide are reading;
everything else M2 produces is code and configuration in the repo, which you change through Cursor.

## 1. What we are building, in one page

You want a machine that does what you used to do by hand in Damodaran's spreadsheet, for many
companies at once, in India and the US, with his own lecture corpus on tap, as a public repo, and
with nothing running on your Mac except an editor. Seven parts:

1. **A calculator.** A program that takes a company's numbers (revenue, operating income, debt,
   cash, shares) plus Damodaran's reference tables (industry betas, country risk premiums, the
   risk-free rate) and computes value per share exactly the way his spreadsheet does. We know it
   is exact because his spreadsheet ships with a worked example (Almarai, a Saudi food company,
   value 7.187840270062114 per share) and our program must reproduce that number to six decimals
   before it is allowed to value anything else. That is the "golden test". Exactness here is about
   the *arithmetic* (including how an unlevered industry beta is re-levered for the company's
   debt); it says nothing about whether the inputs are right. Uncertainty in the inputs (which
   beta, what growth, what margin) is handled separately: every valuation also produces a range
   from Monte Carlo draws and a sensitivity table, and the scoreboard later measures the bias and
   variance of those estimates against realised prices. Exact engine, uncertain inputs, measured
   error: all three.
2. **A database in the cloud (Neon).** Every number the calculator uses is stored with three
   labels: where it came from (source), whether you may show it to others (licence class), and
   which snapshot of Damodaran's data it belongs to (vintage; he updates his tables every
   January, with quarterly and monthly refreshes of two of them, so one year has several
   versions of the risk-free rate and the risk premium that must never be mixed). The database
   refuses to save a number that is missing any label.
3. **A librarian in the cloud (Pinecone + Voyage).** His 609 blog posts, lecture packets, book,
   datasets and transcripts are cut into ~60,000 passages, each turned into a vector so a
   question can find the right passages. Answers cite them.
4. **A memo writer (the model, before the calculator).** For each company the model reads the
   whole latest filing in one go (long context, up to ~1.3 M tokens) *and* retrieves the relevant
   Damodaran passages, then writes a "story to numbers" memo in his own template (the "Stories to
   Numbers" sheet of the workbook): what the business is; the possible → plausible → probable
   test on every claim; what the current price already requires (reverse DCF); and a proposed
   value for each calculator input (growth years 1 and 2–5, target margin and years to converge,
   sales-to-capital, cost-of-capital path, failure probability, terminal assumptions), each with a
   citation to a filing page or a Damodaran passage. Only "probable" claims may set a base-case
   input; "plausible" ones set a scenario; "possible" ones are recorded at zero. The memo must
   also name the company's **uncertainty type** from his "Dark Side of Valuation" (young or
   growth company, distressed, cyclical or commodity, financial-service, complex holding
   structure, emerging-market), pull the matching Dark Side passages, and state the failure
   probability, the truncation assumption and the expected range explicitly, so uncertainty is
   written down rather than hidden in a point estimate. You review, edit, approve; then the
   calculator runs. A second, opposing memo per company is mandatory (the "Gurley field", after
   the Uber episode where he re-ran his model on Bill Gurley's story).
5. **Robots that run at night (GitHub Actions).** Scheduled jobs pull new filings from SEC EDGAR
   (US, free, public domain) and later from EODHD (India, paid), re-value your watchlist, check
   whether Damodaran posted a new risk-premium file, pull licensed news headlines, and write it
   all to the database. Nightly is the right cadence; nothing here is intraday.
6. **A personal Hex dashboard (you look, you do not print).** A hosted notebook over the same
   database (Hex) shows watchlist diversification by sector and country, value-versus-price
   distributions, Monte Carlo ranges, the accuracy scoreboard (bias and variance of past
   valuations against realised prices), and a descriptive "is the market on the rails" panel
   built from Damodaran's own implied-ERP series. As your data-science degree adds ideas, you add
   notebooks against the same tables.
7. **Your daily tool: Cursor** (already paid), with the system's tools plugged in as an MCP
   server: "value Trent", "write the memo for Apple", "ask Damodaran why he strips the default
   spread out of the Indian risk-free rate". Cline (free) sits in the same window as a bench for
   testing open-weight models. PDFs only when you want to read offline.

## 2. Your decisions, and the two that changed after your review

| Decision | What it means here |
|---|---|
| **Daily tool: Cursor, not pi (changed at your request).** | You already pay for Cursor Pro; it shows every change as a reviewable diff, has Plan mode (read the plan in English, then approve), MCP support, cloud agents on GitHub, PR review (BugBot) and scheduled Automations. Privacy Mode is not a secrecy guarantee and is not required. pi is terminal-only with no permission gates and everything is an extension you would write yourself; not a first tool. Cline (free, open source) is the second tool for trying open-weight models through OpenRouter with a different model for planning and for doing. Kilo is a fine substitute for Cline (acquired by Anaconda in July 2026). Do not buy a second paid harness. |
| **Open-weight models: in the runtime, not the editor.** | Inside Cursor, bringing your own OpenRouter key is unofficial, disables Tab/Auto/Composer, and puts the key in a place that leaks into logs. So Cursor stays on its included models for writing code. Open-weight models (GLM-5.3, GLM-5.3-Flash, Kimi K3, DeepSeek) run inside *your system*: the memo writer, the librarian, the bulk jobs, called from GitHub Actions through OpenRouter with prompt logging off and a $75 spend cap. That is where the 17–40× price gap pays. |
| **Outsource everything; you are the contractor's client.** | Neon (database), Pinecone (vectors), Voyage (embeddings), OpenRouter (models), GitHub (code + robots), Langfuse (logs of model calls), Cloudflare R2 (raw files), Hex (dashboard), Mistral (OCR, one-off), EODHD (India data). No Docker, no servers, no CSV/SQLite as the source of truth. Best-in-class per role, with evidence, in §7. |
| **Public repo; keys stay out of git.** | Public GitHub repo `valuation` on account `jkv8fwytbf-byte`. Anyone can read the code and the docs. API keys, `.env`, and licensed data never go in git. No public web app in v1. Cursor Privacy Mode is not required and is not treated as a promise that prompts stay secret: they leave the machine. Neon, Pinecone, Hex and Langfuse stay as your accounts because they hold keys and your watchlist, not because the project is hidden. A GitHub organisation is optional later for Blacksmith runners. |
| **Money is not the object; time is** ($200/month ceiling). | I build the foundation myself in the first week (repo, calculator + golden test, database + loaders, the librarian, the memo writer, the MCP tools, the nightly robots, the first dashboard). You spend that week creating accounts and reading the four documents. From week two you drive Cursor; I stay available for anything that blocks you. |
| **Explain everything.** | Four documents plus FigJam diagrams come first (M0). Every milestone has "what you will see". |
| **"Worth it if someone else ever uses it."** | The code is already public. Licence labels keep licensed facts out of the librarian. A web front end and commercial data licences (EODHD commercial) are still v3, not a rewrite of the engine. |
| Earlier decisions kept | US first, then India. Watchlist of 20–50 names, research only, no buy/sell language, no holdings tracking (your own holdings can be *read* from INDmoney's official API later, see §8). GitHub account `jkv8fwytbf-byte`. A descriptive market-regime panel is allowed ("what is the market pricing in"); advice is not. |

### 2a. What "the point of open-weight" is, honestly

Open-weight models (GLM, Kimi, Qwen, DeepSeek) are 7–40× cheaper per token than the frontier,
can be pinned to an exact checkpoint forever (so a valuation you ran in 2026 is reproducible in
2029, which closed models cannot promise), and carry permissive licences (GLM-5.3-Flash is plain
MIT; full GLM-5.3 and Kimi K3 have revenue-tiered clauses; read each model card because the repo is public).
The cost is capability: on Artificial Analysis Intelligence Index v4.3 (2026-09-07) the frontier
(Claude Fable 5.1, GPT-6 Astra) scores 53 and the best open weight (GLM-5.3) 45; the gap sits in
long agentic tasks, not in the summarise-and-extract work that dominates a valuation pipeline.
(Correction to something I wrote earlier: Meta's Muse Spark 1.3 is *not* open-weight.) Rule:
route per job by cost per task and hallucination rate, pinned in one file, changeable in one line.

### 2b. Plain answers to the questions from your review

- **Two different places where an AI model is used.** Place 1 is *while you write code*: that is
  Cursor, on the models Cursor includes in its subscription. Place 2 is *inside the product when
  it runs at night*: our own code calls a model to write memos, answer questions from the
  librarian, punctuate transcripts. Open-weight models go in place 2, because that is where the
  volume and the cost are, and because a model pinned to an exact checkpoint keeps last year's
  valuation reproducible. The tool you type into stays simple. That is all "runtime, not editor"
  means.
- **What is the point of pi.dev, then?** pi is a bare-bones terminal agent for people who want to
  build their own coding tool from four primitives and pay the least per task; it is genuinely
  good at that, and it is what I would use to run a scripted agent inside a nightly job one day.
  You do not need to build a coding tool; you need to build a valuation system, and you already
  pay for a tool with a screen, diffs and safety rails. pi is deferred, not judged.
- **Tavily and Firecrawl vs GitHub Actions vs Blacksmith.** Three different things. Tavily and
  Firecrawl are *search and crawl services* you pay per query: data sources, and on the
  Artificial Analysis Search Index (2026-08-18) Parallel and Exa beat them on quality per dollar.
  GitHub Actions is the *scheduler*: the thing that wakes up at night and runs our jobs.
  Blacksmith is a faster, cheaper *machine* for GitHub Actions to run on; optional, and only on
  a GitHub organisation. Cursor's own "Automations" can also run scheduled agents, but
  they bill through Cursor and tie the pipeline to your editor, so the nightly pipeline stays on
  GitHub Actions; Cursor Automations are fine for repo chores (summarise what changed, triage a PR).
- **Estimates yes, advice no.** The system prints: value per share, price as a percentage of
  value, the probability that value is below price from the Monte Carlo draws, what the price
  already requires, the market's implied risk premium against its history, and a scoreboard of
  how past valuations fared after 90, 180 and 365 days. It never prints "buy" or "sell". On "is
  it working for the next month": his own data says no valuation approach forecasts next year's
  return well, and one month is noise; the honest monthly question is "is the method working so
  far", which the scoreboard answers as valuations age.
- **"First I should visit the librarian and relearn."** Yes: document C comes first for exactly
  that reason, and the librarian's first job in M2 is to answer your questions with citations
  while you read.

### 2c. What "v1, v2, v3" mean

Labels for scope, not a fixed count. **v1** (weeks 1–8): public repo, working, correct: the
calculator with its golden test, the database with vintages and licences, the librarian, the memo
writer for US names, nightly robots, the first Hex dashboard. **v2** (months 3–6): India, the
accuracy scoreboard as valuations age, Monte Carlo and reverse DCF everywhere, the market-regime
panel, opposing memos, and whatever your coursework suggests (backtests over the 1998–2024
archives, bias studies, factor comparisons). **v3** (only if others use it): a web app, commercial
data licences, multi-user, a public method page. Nothing in v1 is rewritten for v2 or v3.

## 3. The four documents and the diagrams (M0, delivered by me first)

| Document | What it is for | Where |
|---|---|---|
| **A. Read This First** (~25 pages) | The system in plain words with pictures: every box, every vendor (what it does, why it is best, what the alternative was), the accounts you will create (click-by-click, with plan, price, what to copy where, 2FA), the correctness rules explained with examples (golden test, vintage, licence class, India fallback), the model table explained line by line, "what scales" in one page, how to set up Cursor for this repo (MCP, Plan mode, rules file; no Privacy Mode requirement), and a glossary. | `docs/read-this-first.md` + PDF |
| **B. Teaching Guide** (~70 pages) | Where and how to learn each thing, in order, with hours and links: git and PRs; Cursor (Plan/Agent, diff review, cloud agents, BugBot, Automations) and Cline; "fine-tuning" at three levels (the harness: rules, skills, MCP tools, prompts; prompt and context engineering; a model as an outsourced service and why not yet); OpenRouter and Artificial Analysis benchmark literacy (what every column means); TypeScript for a Python brain; Postgres and Neon for a beginner; Pinecone and RAG in plain words; GitHub Actions; evals with Langfuse; data sources (EDGAR, EODHD, NSE, INDstocks API); OCR; web crawling vs search APIs vs scraping (and the law); sub-agents; Figma and FigJam through the connector; Hex; security hygiene. Ends with a 12-week schedule and the rules for learning with an AI tool without becoming dependent on it. | `docs/guide/` + PDF |
| **C. Damodaran, the important parts** (~30 pages) | Your revision brain-dump, abstracted from the corpus you already have: the story-to-numbers frame and the 3P test, the three ways to value anything (intrinsic, relative, contingent), the DCF chain (revenue growth → margins → reinvestment → cash flows → cost of capital → terminal value → equity bridge), where every input comes from, the country-risk method and the India numbers, the implied ERP and "what the market is pricing in", relative valuation, the life-cycle lens, and his rules of thumb, each with the lecture or packet it comes from. | `docs/damodaran-essentials.md` + PDF |
| **D. The Other Side** (~25 pages) | His own "Dark Side of Valuation", his misses with the numbers (Tesla, Nvidia, Amazon, Uber, Facebook, Zomato, Paytm), the academic critiques (country risk premium, CAPM/beta, risk-premium surveys, terminal-value sensitivity, unfalsifiability, fat tails), twelve episodes where someone bet against him and won, what he got right (the 2020 series), a reading order, and what it means for this product. | `docs/other-side/` + PDF |
| **FigJam diagrams** | Architecture, nightly data flow, the valuation chain, the memo pipeline, the milestone map. Created through the Figma connector (signed in as you: `Siddharth's team`, starter plan, view seat) so you can open, edit and learn FigJam on them; if the view seat blocks creation, the same diagrams ship as images in doc A with the one-click seat upgrade noted. | Figma links in doc A |

## 4. Who does what, and when

**Week 1 (me):** M0 documents and diagrams; then the foundation build (M2) in the public repo
you own, with a walkthrough document explaining every file.

**Week 1 (you, 3 evenings, with doc A open):** create the accounts (OpenRouter with a $75 spend
limit, Neon, Pinecone, Voyage, Cloudflare, Langfuse, Mistral, Hex; GitHub 2FA + push protection),
set up Cursor for the repo (the MCP file, Plan mode), read doc C and the first
three chapters of doc B.

**Weeks 2–4 (you, in Cursor):** learn by changing what exists: the 10-minute exercises, your
first PRs, add companies to the watchlist, review memos, look at the dashboard. One no-AI evening
a week. I am on call for anything that blocks you.

**Weeks 4–8 (you in Cursor, me on request):** India (EODHD), the sector-exposure and accuracy
views, evals in Langfuse, Monte Carlo and reverse DCF, opposing memos, the market-regime panel.

**Later, only if others use it:** a web app, commercial data licences, sub-agents.

## 5. Milestones

### M0 — Documents and diagrams (me; days 1–3)
Deliverables in §3. Done when: the four PDFs open, every link in them resolves, the FigJam boards
open in your Figma account (or the images are in doc A), and the accounts checklist is complete.

### M1 — Accounts and Cursor (you; 3 evenings; doc A §accounts, doc B ch. 1–3)
1. GitHub: enable 2FA (save recovery codes offline). The public repo `valuation` on
   `jkv8fwytbf-byte` is the home of the code. Repo settings: secret scanning + push protection on.
2. OpenRouter: buy $20 of credits, set a **$75/month limit**, prompt logging **off**, create a
   key. Put it in `~/.zshrc`; you should see
   `echo $OPENROUTER_API_KEY | cut -c1-6` print `sk-or-`. Zero-data-retention routing is optional
   hygiene for runtime prompts that may include licensed filings, not a secrecy architecture.
3. Neon (free), Pinecone (Starter), Voyage (free 200 M tokens), Cloudflare (one R2 bucket),
   Langfuse (Hobby), Mistral (pay-as-you-go), Hex (Community): one project each named
   `valuation`; paste each key into the repo's `.env` (never committed) and into GitHub Actions
   secrets, using the names in §7.
4. Cursor: open the public repo. Do not treat Privacy Mode as a secrecy guarantee; prompts
   leave the machine. Never paste API keys into Cursor. `.cursor/mcp.json` (I ship it) makes
   the system's tools appear in the agent; `.cursor/rules/` holds the hard rules. Try Plan mode
   (Shift+Tab): ask "explain how value_company works", read the plan, do not execute.
5. Cline (optional, free): install the VS Code extension inside Cursor, add the OpenRouter key,
   set "different models for Plan and Act" (GLM-5.3 for plan, GLM-5.3-Flash for act). This is
   your bench for feeling what open-weight models do before a model id goes into a robot.
6. Day-one exercise: ask Cursor to explain why terminal WACC = risk-free + mature ERP, then find
   the cell label `Mature Market ERP +` in the workbook yourself. Compare.
**Done when:** every key is in place; Cursor's agent lists the valuation tools; you have read doc C.

### M2 — Foundation build (me; days 3–7; you read the walkthrough)
1. Public repo `valuation` (TypeScript, pnpm workspace): `AGENTS.md`
   (read by Cursor, Cline and Claude alike) with the eight hard rules; `.cursor/mcp.json` and
   `.cursor/rules/`; CI on GitHub's own Linux runners (public repos get standard minutes free;
   a $25 Actions spending cap anyway; `timeout-minutes` on every job; schedules off the hour
   because top-of-hour cron runs get dropped; a 60-day schedule-sleep if there are no new commits;
   a `last_run_at` row in Neon with a staleness alarm).
   A GitHub organisation and Blacksmith are optional later, only if usage is high.
2. The calculator (`packages/engine`): a formula-by-formula port of the spreadsheet; the golden
   fixture extracted from the workbook by script (never typed); the golden test required in CI;
   the sheet's diagnostics turned into real errors and warnings; reverse DCF (price-implied
   growth or margin); Monte Carlo from the workbook's industry quartiles.
3. The database (`packages/db`, Neon): the tables in §10.3; the constraints proven ("insert a
   number without a vintage → refused"); the Damodaran datasets loaded once by an Actions job with
   their vintage taken from each file's own "Updated" cell; the three 2026 market vintages seeded;
   the monthly implied-ERP history (`ERPbymonth`) and the annual history (`histimpl`) loaded for
   the regime panel.
4. US ingest: SEC EDGAR for Apple, Costco and three more US names of your choice; the LTM rule;
   Apple's missing interest-expense line shown as a visible flag, not a silent zero.
5. The librarian (`packages/rag`): tier 1 (blog posts) and tier 3 (dataset sentences) indexed in
   Pinecone with Voyage; the grounded prompt; both smoke questions passing; the exam-based eval set.
6. The memo writer (`packages/memo`): filing → long-context read; Damodaran passages → retrieval;
   output = the "Stories to Numbers" table as rows (`valuation_inputs` with `p3_class` and a
   `claim_id` per number) plus a claims table (`claim_text, p3_class, source_type, source_locator,
   quote, confidence`); an uncited claim rejects the memo; a reverse-DCF section is mandatory;
   plausibility guard rails from his own posts (a cost of capital outside the 80% band of 5.3–9.9%
   US / 6.3–11.7% global is flagged); you approve in Cursor before a run.
7. MCP server (`packages/mcp-server`, works from Cursor, Cline, Claude, pi alike): `value_company`,
   `write_memo`, `review_memo`, `get_industry_stats`, `search_corpus`, `report` (markdown + PDF).
8. Nightly robots: EDGAR refresh on new filings, watchlist revaluation, monthly ERP / quarterly
   CRP watch that opens a GitHub issue when Damodaran posts a new file, licensed headline pull.
9. The first Hex dashboard (Community tier) over Neon: watchlist with vintage, sector and country
   exposure, value-vs-price distribution, the Almarai and Apple runs with their ranges.
10. `docs/walkthrough.md`: every folder and file explained; how to run each command; what to try first.
**Done when:** in Cursor, `value_company AAPL US` prints value/share, WACC, rating basis, vintage
and licence; `write_memo AAPL` produces a cited memo you can approve; `search_corpus` answers the
smoke questions with citations; the golden test is green in CI and a deliberate lag change turns it
red; the nightly job has run once; the Hex dashboard shows the watchlist.

### M3 — You take the wheel (you in Cursor; weeks 2–4)
Follow doc B in order. Each chapter ends with a 10-minute exercise on this repo (create and resolve
a merge conflict; break the golden test and watch CI go red; add a company to the watchlist;
review and edit a memo; add a diagnostic warning; re-index one blog year; add a chart in Hex).
Track your ratio of lines written vs accepted (doc B ch. 0). **Done when:** five PRs merged by
you, the watchlist has 20 names with approved memos, and you can explain every rule in
`AGENTS.md` out loud.

### M4 — India, accuracy, ranges, the market panel (you in Cursor; me on request; weeks 4–8)
1. EODHD: check `TRENT.NSE` depth on the free tier, then subscribe (Fundamentals, $59.99/mo), or
   indianapi.in if it proves as deep for less. Ingest with `license_class = licensed_personal`;
   cross-check once against Trent's own annual report. INR risk-free = RBI 10-year G-sec yield
   (entered monthly as a vintage row) minus India's default spread; ERP = mature + CRP; industry
   fallback India → emerg → Global at 10 firms, recorded on every run. Optional: your own
   holdings and NSE prices read through INDmoney's official INDstocks API (read-only endpoints,
   no static IP needed).
2. Sector-exposure and value-vs-price views for 20–50 India + US names (research only; a test
   forbids advice words in reports and chat).
3. Langfuse tracing of every model call; error analysis on 100 real memos and answers; nightly
   eval issue.
4. The accuracy scoreboard, filled in as valuations age: `realised_price` at 90/180/365 days;
   bias = average signed error of value vs later price, variance = its spread, by sector, region,
   vintage and memo version. Banner: "The engine is tested (Almarai 1e-6). The forecast is not."
5. The market-regime panel (descriptive only; spec in §10.7): his monthly implied ERP and its
   variants against 1960–2025 and 10-year history, expected return on stocks, earnings yield vs
   bond yield (context only), high-yield spreads from FRED, concentration (top-7 weight), and a
   fair-value grid of the index at ERP 2–6%, each rendered as a plain-language state with his own
   market-timing caveats printed on the panel. Headline sentiment from licensed sources is an
   annotation on the chart, never an input.
**Done when:** `value_company TRENT IN` shows tier + vintage; the exposure view renders; the
first scored horizon appears after 90 days; the regime panel reproduces his published September
2026 numbers (ERP 4.09%, expected return 8.84%).

### M5 — Only if others use it (later)
A browser front end, app-level login, commercial data licences, sub-agents, a public method page.

## 6. Budget at $200/month

| Line | Now | Notes |
|---|---|---|
| Cursor Pro | $20 (already paying) | Included model pool for coding; stays on Cursor's models (no BYOK). |
| OpenRouter (runtime) | $30–70 | GLM-5.3 for memos and answers, Flash batch for bulk, Kimi K3 as judge; a frontier model only for a final synthesis if you want it. Spend limit $75. |
| EODHD Fundamentals (from M4) | $60 | Personal-use licence. Test indianapi.in first; may save ~$50. |
| Hex | $0 → $36 | Community is free; Professional when you want a published app and a daily refresh. |
| GitHub Actions CI | $0 | Public repo: standard runners are free. Keep a $25 spending cap anyway. |
| Neon | $0 → ~$10–20 | Free until 0.5 GB; Launch is pay-as-you-go with scale-to-zero. |
| Pinecone | $0 → $20 | Starter holds the corpus; Builder if you re-index often. |
| Voyage, Langfuse Hobby, Cloudflare R2 | $0 | Free at this scale. |
| Mistral OCR (one-off) | ~$10 | The three image-only decks and any scanned packet. |
| Optional: Kite Connect or INDstocks API (India prices), Parallel search (news) | ₹500 / free / ~$18 | INDstocks API is free with an INDmoney account. |
| **Total** | **~$120–200** | Bloomberg Digital is your personal subscription outside this. |

## 7. Vendor scorecard: are they the best at what they do?

| Role | Pick | Runner-ups | Why the pick wins here |
|---|---|---|---|
| Coding tool | **Cursor Pro** | Cline (free bench, per-mode models, Apache-2.0); Kilo (Cline lineage, 500+ models, acquired by Anaconda); pi (terminal, DIY); Claude Code, Codex (extra $20–200/mo) | Already paid; diff review + Plan mode are what let a beginner learn instead of cargo-cult; MCP, cloud agents on GitHub, BugBot, Automations. Privacy Mode is not a secrecy guarantee. |
| Database | **Neon** (Postgres) | Supabase Pro; PlanetScale Postgres | Scale-to-zero (idle costs nothing) + copy-on-write branches. Weakest uptime record in the stack (outages 2026-05-08, 07-11, 08-10); acceptable for retryable batch work. |
| Vectors | **Pinecone** Starter (your choice; free 2 GB) | pgvector inside Neon (one vendor fewer, also free at 60k vectors); Qdrant Cloud; Turbopuffer | Purpose-built, free at this scale, hybrid sparse+dense. If two systems ever feel like a burden, pgvector on Neon is the fallback behind the same retriever interface. |
| Embeddings + rerank | **Voyage** (`voyage-context-4`, `rerank-3`) | Gemini Embedding; OpenAI; Cohere Rerank 3.5 ($0.001/search) | 200 M free tokens; 32k input; neighbour-aware chunks fix unpunctuated transcripts. |
| Model router | **OpenRouter** | Vercel AI Gateway (cannot restrict providers); Fireworks (direct fallback) | One key, one bill, pin a model by name. Logging off (vendor rights). No built-in web-search plugin. |
| Models | **GLM-5.3** (memos, answers), **GLM-5.3-Flash batch** (bulk), **Kimi K3** (judge) | DeepSeek V4.1 Flash; Qwen3.8; a frontier model for final synthesis | AA Intelligence Index v4.3 and Coding Agent Index v1.5; GLM has the lowest hallucination rate among strong open weights; DeepSeek V4 Pro excluded (94% hallucination rate). |
| Dashboard / notebooks | **Hex** (Community → Professional $36) | Deepnote (Jupyter-shaped, $39); Grafana Cloud free (SQL only); Evidence OSS (SQL only, self-built) | Only tool with SQL against Neon, real Python for Monte Carlo and bias/variance, product-grade charts with input widgets, a personal workspace (not a public website) and a built-in AI agent within budget. Build a custom web app only when you need write-back, other viewers, or embedding. |
| Observability + evals | **Langfuse** Hobby | Braintrust free (biggest eval allowance); Arize Phoenix; Helicone (maintenance mode: avoid) | Open source, evals on the free tier, acquired by ClickHouse Jan 2026 with no pricing change. |
| Job runner | **GitHub Actions** | Cursor Automations (repo hygiene only); Inngest; Trigger.dev; QStash | Already where the code lives; keeps the pipeline independent of the editor vendor. |
| Raw file storage | **Cloudflare R2** | Backblaze B2; S3; Vercel Blob | 10 GB free, zero egress. |
| OCR | **Mistral Document AI 4.1** (batch $2/1,000 pages) | Reducto; Azure DI; Marker/Docling | Best on the only independent 2026 OCR benchmark (74.9%, tables 94.3%); bounding boxes for slide-level citations. |
| Web search (optional) | **Parallel** | Exa; Firecrawl; Tavily (reject) | AA Search Index 2026-08-18: top of quality and bottom of cost. |
| India fundamentals | **EODHD** ($59.99) | indianapi.in; FMP; Alpha Vantage (25 req/day) | Only vendor with documented long-history India statements in a normalised schema. |
| India prices / your holdings | **INDstocks API** (INDmoney, free) or Kite Connect (₹500) | NSE bhavcopy files | Official, free with your account; read-only endpoints usable from Actions; scraping the app is forbidden. |

**Accounts to create (in this order; doc A has the click-by-click version):**

| # | Vendor | Plan | $/mo | Goes into `.env` and GitHub Actions secrets as | Security note |
|---|---|---|---|---|---|
| 1 | GitHub (public repo `valuation`) | Free | 0 | `GITHUB_TOKEN` (fine-grained, repo-scoped, 90-day expiry) | 2FA required; recovery codes offline; root of trust. Organisation optional later. |
| 2 | Cursor (existing) | Pro | 20 | none | Never paste API keys into Cursor's BYOK settings. Privacy Mode is optional and not a secrecy guarantee. |
| 3 | OpenRouter | pay-as-you-go | 30–70 | `OPENROUTER_API_KEY` | Spend limit $75; logging OFF; 2FA. ZDR routing optional. |
| 4 | Neon | Free → Launch | 0–20 | `DATABASE_URL` (pooled), `DATABASE_URL_UNPOOLED` | Email + password sign-up (not only "continue with GitHub"); 2FA. |
| 5 | Pinecone | Starter | 0 | `PINECONE_API_KEY` | 2FA. |
| 6 | Voyage | Free | 0 | `VOYAGE_API_KEY` | Billing alert before the free grant runs out. |
| 7 | Cloudflare | Free (R2) | 0 | `R2_ACCOUNT_ID`, `R2_ACCESS_KEY_ID`, `R2_SECRET_ACCESS_KEY`, `R2_BUCKET` | Hardware key or TOTP; token scoped to one bucket. |
| 8 | Langfuse | Hobby | 0 | `LANGFUSE_PUBLIC_KEY`, `LANGFUSE_SECRET_KEY`, `LANGFUSE_BASEURL` | 2FA. |
| 9 | Mistral | pay-as-you-go | ~2 one-off | `MISTRAL_API_KEY` | Use the batch endpoint. |
| 10 | Hex | Community | 0 → 36 | Neon connection configured inside Hex (pooled host, SSL) | Personal workspace for your watchlist, not a public site. |
| 11 | EODHD (M4) | Fundamentals | 60 | `EODHD_API_TOKEN` | Read the redistribution clause; test 20 NSE tickers on the free tier first. |
| 12 | Optional: INDstocks API, Kite Connect, Parallel, Braintrust | | 0 / 6 / 18 / 0 | `INDSTOCKS_*`, `KITE_*`, `PARALLEL_API_KEY`, `BRAINTRUST_API_KEY` | Broker tokens expire daily; budget a re-auth step. |

Hygiene: never commit `.env`; a committed `.env.example` with empty values; a distinct email alias
per vendor; hard spend caps at OpenRouter, Mistral and Parallel; rotate the GitHub token and the
OpenRouter key every 90 days; create a Neon branch before any migration the agent proposes.

## 8. Bloomberg, INDmoney, OCR, crawling, sub-agents, benchmarks, Figma, fine-tuning

- **Bloomberg API library: verdict.** The page you found is the download index for Bloomberg's
  BLPAPI SDK. It is free to download and connects to nothing without an entitlement; the page
  itself says the Linux/macOS builds "are only compatible with the Bloomberg Server API and
  B-Pipe", and Windows builds ride a logged-in Terminal (~$32k/year, 2-year minimum). A
  bloomberg.com subscription is a reading product with no data entitlement and no consumer API in
  2026. What exists for free: undocumented headline-only RSS feeds (`feeds.bloomberg.com/markets/
  news.rss`, `technology`, `economics`, `industries`, `bview`; verified live 2026-09-14) and
  email newsletters. The feeds are a grey area under Bloomberg's terms (no scrapers, no
  databases): poll a few times a day with caching, store title + link + time only, never
  commit article text, never make it load-bearing. Your Bloomberg reading goes into `narrative_note` rows
  (URL, date, your paraphrase, the input it moves), never article text, never the index.
- **INDmoney.** Scraping the app is forbidden by its terms (bots, copying and republishing all
  named). But INDmoney's broking arm publishes a free official API (INDstocks API Suite:
  holdings, positions, live quotes, 10+ years of daily prices, option chains; no fee beyond
  brokerage; KYC account required; order endpoints need a static IP, read-only market-data
  endpoints do not). So: your own holdings and NSE prices can be read legitimately through it
  from a nightly job; fundamentals still come from EDGAR, Damodaran's tables and EODHD.
- **Crawling nightly with Firecrawl?** Not Bloomberg or INDmoney (terms). A nightly robot may
  read Bloomberg's headline feeds, the newsletters in your Gmail, SEC EDGAR's own RSS and
  full-text search, and licensed search APIs (Parallel, Exa) for "what changed this quarter for
  Trent". Results feed the memo writer's evidence list and annotate the regime panel.
- **OCR.** Turning a picture of a page into text. Three of Damodaran's "Dark Side" decks are
  image-only; check with `pdffonts` first, then Mistral Document AI through the batch endpoint;
  verify with an arithmetic round-trip (columns must sum to the stated total).
- **Web crawling vs search APIs vs scraping.** Search = ask, get ranked pages; crawl = walk a
  site; scrape = pull fields off one page. Terms of service, not the law, are the real risk
  (hiQ v. LinkedIn); honour `robots.txt`; stamp a licence class on every row.
- **Sub-agents.** Helper sessions with their own context that return a summary; good for
  parallel reading, bad for anything whose numbers you must audit (helpers write rows, not prose).
  Cursor's cloud agents and "Projects" provide this when needed; deferred to v2.
- **Benchmark literacy.** Intelligence Index = a weighted exam across 10 tests; Coding Agent Index
  = harness + model pairs on real tasks; AA-Omniscience = does it make things up; tokens per
  second = typing speed; time to first token = the wait before it starts (for reasoning models,
  the first *thinking* token); cost per task = the dollars to finish one question, the number
  that maps to your bill. Traps: reasoning tokens bill as output; the same model has many hosts at
  different prices; pick per job, not by headline.
- **Figma / FigJam.** Figma exposes a connector; this app is signed in as you. Through it I create
  FigJam boards (diagrams) in your account and can read designs back into code later. You open
  them like any Figma file, drag boxes, add notes. Doc B has a chapter; you only draw a screen
  when you build one (v3).
- **Fine-tuning, three levels.** (1) The harness: rules file, MCP tools, prompts, model routing;
  $0 and 95% of the quality; this is what you will do. (2) Prompt and context engineering.
  (3) A model, as an outsourced service (Together, Fireworks, Vertex, Unsloth on Colab): about $2
  per training run for 800 examples on a ≤16B model, but it changes form, not facts, needs
  500–1,000 hand-corrected examples, and a GPU endpoint left running can eat $200 in a weekend.
  Not in v1; revisit with 500+ logged corrections and a repeated formatting failure.

## 9. Non-goals, risks, cut lines, deferred

**Non-goals for v1:** holdings valuation or P&L, real-time prices, multi-user, commercial use,
any buy/sell output, scraping Bloomberg/INDmoney/screener.in/Tickertape, Docker or self-hosting,
Python in the production path, the option-value and lease/R&D converter sheets, fine-tuning any
model, BYOK inside Cursor.

**Risks → mitigations.** Operation-order drift breaks 1e-6 → per-module sub-assertions, a 1e-9
warning, a second golden case later. Neon Free 0.5 GB → plan Launch at M4. Pinecone write units on
re-embeds → content-hash manifest. Actions 6-hour cap and dropped top-of-hour schedules → chunked
jobs, off-hour cron, staleness alarm. Licence leakage → NOT NULL + database CHECK + retrieval
allow-list + `data_collection: deny`. Corpus gaps (blog 2012, 2025; image-only decks) → backfill
and OCR before tier 1 is declared complete. Dependence on the AI tool → attempt-then-ask, own
the tests, one no-AI evening a week, a decisions log. Cursor included pool exhausted → coding
falls back to Composer/Grok; the pipeline is unaffected because it never used Cursor's models.

**Cut lines:** if month 3 arrives with M4 unfinished, ship US-only and postpone EODHD rather than
ship India without the fallback tests. Never cut: the golden test in CI, three vintage ids, source
+ licence NOT NULL, the India fallback log, the no-advice test, memo claims cited.

**Deferred:** pi (optional terminal tool later); sub-agents; Blacksmith; the four remaining
regional tables and `indname.xls`; option value and converters; second golden case (Apple TTM);
Parallel/Exa news discovery; Pinecone Assistant spike; a web app; commercial licences.

## 10. Technical appendix (skip on first read)

### 10.1 Correctness rules in plain words
- **Golden test.** The spreadsheet's own example must reproduce to 1e-6 before any code merges.
  The expected values are extracted from the workbook by a script; the fixture file is protected
  in CI so an agent can never "fix" the test instead of the code.
- **Vintage.** Every run stores three ids: which market file (risk-free rate, mature ERP), which
  country-risk file, which industry file. The 2026 data alone carries risk-free rates of 3.95%,
  4.58% and 4.75% and ERPs of 4.20%, 4.23% and 4.46%; mixing them silently is the most common way
  to get a confidently wrong value.
- **Source and licence class.** Every stored fact says where it came from and one of
  `public_domain` (SEC), `damodaran_public`, `open_access` (RBI, arXiv, SSRN author copies),
  `asr_youtube`, `licensed_personal` (EODHD, INDstocks), `proprietary_personal` (Bloomberg notes),
  `link_only` (books, paid newsletters). The librarian's index has a database rule that refuses the
  last three. The code is already public; this rule keeps licensed facts out of the librarian
  and off any page a stranger can see.
- **India rules.** Risk-free = RBI 10-year G-sec yield minus India's default spread (otherwise
  sovereign risk is counted twice, because the cost of debt already adds it). ERP = mature ERP +
  India CRP (Jan-2026: 4.23% + 2.85% = 7.08%). If an India industry has fewer than 10 firms (27 of
  94 do), use the emerging-markets table, then Global, and print which one was used.
- **No advice.** A test scans every report, memo and chat answer for buy/sell/hold/target price.

### 10.2 Engine (TypeScript, pure functions, float64)
Modules mirror the sheets: `rating.ts` (synthetic rating from interest coverage, three firm-type
tables, country default spread), `costOfCapital.ts` (four approaches; industry-average and
distribution approaches add `rf − table.embedded_rf`, stored per table), `fcff.ts`/`terminal.ts`
(growth path, margin convergence, tax fade, reinvestment = ΔRevenue ÷ sales-to-capital with the
lag switch, NOL, running-product discount factors, terminal WACC = rf + mature ERP, terminal
reinvestment g/ROIC), `failure.ts`, `options.ts` (disabled for Almarai), `india.ts`,
`reverseDcf.ts`, `monteCarlo.ts`, `impliedErp.ts` (his goal-seek as a root finder; anchors:
index 7398.084728 at ERP 4.25%, expected return 8.8437%). Output carries the full audit (rating
basis, interest missing, tier used, three vintage ids, sources, engine version, input hash).
Excel and JavaScript share IEEE-754 float64, so an order-faithful port agrees to ~1e-12.

### 10.3 Database (Neon) tables
`vintage`, `country_risk`, `industry_stat` (long format with `n_firms`), `industry_dist`
(quartiles), `erp_monthly` (ERPbymonth columns verbatim), `erp_annual` (histimpl), `company`,
`fact` (source_url, license_class, filed, accession, vintage_id all NOT NULL), `ltm_financials`
(interest_missing flag), `memo` (versioned; story text, `story_kind` base/opposing, status),
`claim` (`claim_text, p3_class, source_type, source_locator, quote, confidence`),
`valuation_inputs` (`run_id, field, value, unit, p3_class, claim_id`), `valuation_run` (inputs
hash, outputs, three vintage ids NOT NULL, tier used, rating basis, seed, memo id),
`watchlist`, `narrative_note`, `market_context_event` (headline, source, time; annotation only),
`chunk_manifest` (with the licence CHECK), `rag_eval_case`, `rag_eval_run`, `realised_price`,
`job_heartbeat`. Raw bytes in a private R2 bucket keyed by sha256.

### 10.4 Librarian (Pinecone + Voyage) and models
Pinecone serverless index, 1024-dim vectors from `voyage-context-4`, `rerank-3` from 50 to 8;
metadata `{source_url, title, date, doc_type, license_class, vintage, asr, region, company}`.
Tiers: 1 blog → 2 book, packets with speaker notes, exams → 3 dataset rows as sentences → 4
transcripts after a ~$11 punctuation pass. Never indexed: third-party press, filings, the Tykoh
guide, Bloomberg, EODHD. Hybrid router: single-document questions stuff the document; corpus-wide
questions retrieve. Models pinned with the AA index version: `z-ai/glm-5.3` (memos, answers),
`z-ai/glm-5.3-flash:batch` (bulk, reasoning off), `moonshotai/kimi-k3` (judge),
`deepseek/deepseek-v4.1-flash` (fallback); prices re-checked monthly (GLM-5.3 was listed at
$0.92–1.40 in / $3.14–4.40 out per M in September 2026).

### 10.5 Memo writer
Implements his five steps (develop the narrative; test it against history and common sense;
convert it into value drivers; connect to a valuation; keep the feedback loop open) with the 3P
gate on every claim. Template = the workbook's "Stories to Numbers" sheet, one row per driver with a
mandatory "link to story". Reverse DCF section computed first (hold margin and cost of capital,
solve for the year-10 revenue the price implies, convert to implied market share, run *that*
through 3P). Guard rails: uncited claim rejects the memo; numbers go to `valuation_inputs`, never
parsed from prose; the engine is untouched; you approve a diff of proposed vs prior inputs in
Cursor; an opposing memo is mandatory; on re-run the memo classifies the change as tweak, shift or
break. Sources: his 2014 narrative posts, the Uber/Gurley exchange, Corporate Life Cycle sessions
10–13, Data Update 5 for 2026 (cost-of-capital plausibility bands).

### 10.6 Jobs (GitHub Actions)
`load-damodaran` (dispatch, per vintage), `ingest-edgar` (nightly, only on a new accession),
`value-watchlist` (nightly), `watch-erp-crp` (monthly/quarterly HEAD on his file names; new sha256
→ new vintage row + GitHub issue), `rag-index` (dispatch per tier), `rag-eval` (nightly,
report-only), `news-headlines` (nightly, licensed sources), `realised-prices` (weekly), `report`
(on demand). Every job writes `job_heartbeat`; a staleness alarm fires after 36 h.

### 10.7 Market-regime panel (descriptive)
Indicators and sources: headline implied ERP and its variants (`ERPbymonth`: T12m, adjusted
risk-free, smoothed, normalised, net cash yield); ERP vs history (`histimpl` 1960–2025; his
benchmark averages 4.25% long-run, 5.16% for 2006–2025, 5.00% for 2016–2025); expected return on
stocks (he calls 8–9% healthy); earnings yield vs bond yield (context only: he calls PE "noisy and
unreliable"); high-yield and BBB spreads from FRED (`BAMLH0A0HYM2`, `BAMLC0A4CBBB`, `DGS10`);
concentration (top-7 weight, 30.9% in his 2026 update); the fair-value grid of the index at ERP
2–6%. States: percentile bands with plain sentences ("the market is pricing in less risk than its
10-year median"). Printed on the panel, in his words: "I am not a market timer, but I do value the
market at regular intervals, more to get a measure of what the market is pricing in, than to
forecast future movements." Headline sentiment lives in `market_context_event` and is drawn as an
overlay only; it never enters any computation.

### Critical files
- `/Users/siddharth/Downloads/fcffsimpleginzu.xlsx` — the model and its golden case
- `/Users/siddharth/Downloads/damodaran-data-01.zip`, `-02.zip` — 2026 datasets loaded once into Neon
- `/Users/siddharth/Downloads/financeMD/` — the corpus (blog, packets, exams, book, `pc/implprem/ERPbymonth.md`, `pc/datasets/histimpl.md`) for the librarian, the regime panel and doc C
- `~/code/valuation/packages/{engine,db,rag,memo,mcp-server,models}/`, `.cursor/`, `AGENTS.md` — what M2 creates
