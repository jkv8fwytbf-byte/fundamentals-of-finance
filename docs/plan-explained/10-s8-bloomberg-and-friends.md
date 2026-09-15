# Section 8: Bloomberg, INDmoney, OCR, crawling, sub-agents, benchmarks, Figma, fine-tuning

## Bloomberg

**In short.** An API (application programming interface) is a door one program uses to ask another for data. Bloomberg has no consumer API in 2026; the download page you found connects to nothing without a paid Terminal contract (plan section 8). Its free headline RSS feeds, plain headline lists for reader programs, are a gray area under Bloomberg's terms (plan section 8).

> **Comment**
> **What it means for you:** The robot will store only title, link and time, never commit article text, and never let a headline move a number (plan section 8).
> **Decision needed:** none, already decided in the plan.
> **Money:** none; Bloomberg Digital is your personal subscription outside the budget (plan section 6).
> **When:** M2, foundation build, me, days 3 to 7 after go, in the nightly headline pull (plan section 5).

**Read more.** 1-read-this-first.pdf, section "13. Bloomberg, INDmoney and news, honestly".

## INDmoney

**In short.** Scraping means a program copying data off a page or app screen, and INDmoney's terms forbid it (plan section 8). Its broking arm publishes a free official API, the INDstocks API Suite, and the plan uses only its read-only endpoints for your own holdings and NSE prices, quotes from India's National Stock Exchange (plan section 8). It needs a KYC account, an identity-verified brokerage account, but no static IP, a fixed internet address (plan section 8).

> **Comment**
> **What it means for you:** Fundamentals, the accounting numbers, still come from EDGAR, the SEC's free filings database, Damodaran's tables and EODHD, a paid market-data provider (plan section 8).
> **Decision needed:** none now; plan section 6 marks it optional.
> **Money:** INDstocks API free with an INDmoney account; Kite Connect at 500 rupees is the alternative (plan section 6).
> **When:** M4, India, accuracy, ranges, market panel, you in Cursor, me on request, weeks 4 to 8 (plan section 5).

**Read more.** 1-read-this-first.pdf, section "13. Bloomberg, INDmoney and news, honestly".

## Crawling Bloomberg or INDmoney at night?

**In short.** A crawler is a robot that visits pages on a schedule and brings text home; Firecrawl is one such service. It will not touch Bloomberg or INDmoney, because their terms forbid it (plan section 8). It may read Bloomberg's headline feeds, newsletters in your Gmail, SEC EDGAR's own feeds and search, and licensed search APIs such as Parallel and Exa (plan section 8).

> **Comment**
> **What it means for you:** Results become evidence lines for the memo writer and notes on the market regime panel, the market conditions dashboard, never inputs (plan section 8).
> **Decision needed:** none, already decided in the plan.
> **Money:** Parallel search is optional at about $18; the rest is $0 (plan section 6).
> **When:** M2, foundation build, me, days 3 to 7 after go; regime panel notes in M4, weeks 4 to 8 (plan section 5).

**Read more.** 1-read-this-first.pdf, section "7. The nightly robots".

## OCR

**In short.** OCR (optical character recognition) turns a picture of a page into searchable text. Three of Damodaran's "Dark Side" decks are image-only, and only those three will go through OCR (plan section 8). pdffonts, a command that reports whether a PDF holds real text, checks first; Mistral Document AI's batch endpoint, the slower cheaper queue, does the work; every table must add up to its stated total (plan section 8).

> **Comment**
> **What it means for you:** Three decks, one job, and you will not run it yourself.
> **Decision needed:** none, already decided in the plan.
> **Money:** Mistral OCR about $10, one-off (plan section 6).
> **When:** not before M2, foundation build, me, days 3 to 7 after go; the Mistral account comes after the free M1 accounts (plan section 7).

**Read more.** 4-the-guide.pdf, "Chapter 10. OCR, web crawling and sub-agents: three helpers, and when to leave them in the drawer".

## Web crawling, search APIs and scraping

**In short.** Search means asking a question and getting ranked pages; crawl means walking a whole site; scrape means pulling fields off one page (plan section 8). The real risk is a site's terms of service, the contract you accept by using it, not the law (plan section 8). Every robot will honor robots.txt, a site's public list of pages robots may visit, and every row will carry a license class, a label saying what you may do with it (plan section 8).

> **Comment**
> **What it means for you:** Any row in the database will show where it came from and what you may do with it.
> **Decision needed:** none, already decided in the plan.
> **Money:** none.
> **When:** M2, foundation build, me, days 3 to 7 after go, when the database is built (plan section 5).

**Read more.** 4-the-guide.pdf, "Chapter 9. Data sources: where every number comes from, and what you may do with it".

## Sub-agents

**In short.** A sub-agent is a helper AI session with its own working memory, called context, that returns a summary (plan section 8). Helpers suit parallel reading, not numbers you must audit, so helpers write rows, not prose (plan section 8). Cursor's cloud agents provide this when needed; the plan defers it to v2 (plan section 8).

> **Comment**
> **What it means for you:** No sub-agents in the first build; every number will come from one traceable step.
> **Decision needed:** none, already decided in the plan.
> **Money:** none.
> **When:** not before M4. Plan section 8 says v2, months 3 to 6; plan sections 4 and 5 say M5, only if others ever use it (plan sections 2c, 4, 5, 8).

**Read more.** 4-the-guide.pdf, "Chapter 10. OCR, web crawling and sub-agents: three helpers, and when to leave them in the drawer".

## Benchmark literacy

**In short.** A benchmark is a public exam for AI models. The Intelligence Index is a weighted score across 10 tests; the Coding Agent Index scores a model plus its harness, the tool around it; AA-Omniscience measures whether a model makes things up (plan section 8). Tokens per second is typing speed; time to first token is the wait before it starts; cost per task is the dollars per question, the number that maps to your bill (plan section 8).

> **Comment**
> **What it means for you:** Two traps: reasoning tokens bill as output, and one model has many hosts at different prices; pick per job, not by headline (plan section 8).
> **Decision needed:** none, already decided in the plan.
> **Money:** OpenRouter $30 to 70 per month, spend limit $75 (plan section 6).
> **When:** M1, accounts and Cursor, you, 3 evenings, when you set up OpenRouter and Cline, a free coding extension you use as a test bench (plan section 5).

**Read more.** 4-the-guide.pdf, "Chapter 7. OpenRouter and benchmark literacy: one door to every model, and how to read the scoreboard".

## Figma and FigJam

**In short.** Figma is a design tool and FigJam is its whiteboard. Figma exposes a connector, a link this app uses while signed in as you, so I create FigJam boards, the system diagrams, in your account (plan section 8). You open them like any Figma file and drag boxes; you only draw a screen when you build one, which the plan calls v3 (plan section 8).

> **Comment**
> **What it means for you:** The diagrams are yours to edit, and moving a box changes no code or number.
> **Decision needed:** none, already decided in the plan.
> **Money:** none.
> **When:** M0, documents and diagrams, me, done today 2026-09-14; your own screens wait for a front end, which plan section 5 places in M5, only if others ever use it, later.

**Read more.** 4-the-guide.pdf, "Chapter 13. Figma and FigJam: the whiteboard where the system is drawn".

## Fine-tuning at three levels

**In short.** Fine-tuning usually means retraining a model on your own examples; the plan uses the word at three levels (plan section 8). Level 1 is the harness, meaning the rules file, the MCP tools (a standard way to hand a model tools), the prompts and the model routing; it costs $0, gives 95% of the quality, and is what you will do (plan section 8). Level 2 is better prompts and context. Level 3 trains a model as an outsourced service, about $2 per run for 800 examples, but it changes form, not facts, and needs 500 to 1,000 hand-corrected examples (plan section 8).

> **Comment**
> **What it means for you:** Your fine-tuning is editing rules and prompts in Cursor; level 3 is not in v1 and returns only with 500+ logged corrections and a repeated formatting failure (plan section 8).
> **Decision needed:** none, already decided in the plan.
> **Money:** level 1 $0 (plan section 8); a level 3 GPU endpoint, a rented graphics computer, left running can eat $200 in a weekend (plan section 8), which is the whole monthly ceiling (plan section 6).
> **When:** M2, foundation build, me, days 3 to 7 after go, for the first harness; M3, you take the wheel in Cursor, weeks 2 to 4, when you edit it (plan section 5).

**Read more.** 4-the-guide.pdf, "Chapter 8. "Fine-tuning" at three levels: the harness, the context, and the model".
