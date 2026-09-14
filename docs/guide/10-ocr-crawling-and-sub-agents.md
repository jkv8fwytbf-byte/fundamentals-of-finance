# Chapter 10. OCR, web crawling and sub-agents: three helpers, and when to leave them in the drawer

This chapter covers three tools that sound advanced and are mostly optional. Each solves a narrow problem here. Knowing the problem matters more than knowing the tool. Read it after Chapter 3 and before you touch the corpus ingest code in milestone M2.

## What it is (plain words and an analogy)

### OCR

OCR stands for optical character recognition. It is software that looks at a picture of a page and writes out the letters it sees. A PDF can contain real text, or it can contain a photograph of text. On screen the two look the same. In the first you can select and copy words. In the second you cannot, because there are no words, only pixels.

Analogy: a typed letter and a photograph of it look identical on your desk. Only the typed one can be searched by a computer. OCR is the typist who reads the photograph and types it back in. Modern OCR services are vision language models, AI models that read images. They also rebuild headings, reading order and, most important for us, tables.

Source: bj0fbejiq.txt, CHECK 3 section 2 (2026-09-14). The photograph analogy is mine.

### Search APIs, crawling and scraping

These are three different jobs, and beginners mix them up.

| Job | What you send | What you get back | Library analogy |
|---|---|---|---|
| Search API | A question | Ranked web pages, often with their text | Asking the librarian |
| Crawling | One starting web address | Every page linked from it, then every page linked from those | Walking every aisle and noting every book |
| Scraping | One known page | Specific fields pulled out of that page | Opening a known book to page 42 and copying the table |

An API, an application programming interface, is a door a service opens so a program can ask it questions. A search API is a search engine with such a door. Search first. Crawl only when you must list a whole site. Scrape only when the numbers are not available through an API.

Source: bj0fbejiq.txt, CHECK 3 section 3 (2026-09-14); the plan, section 8.

### Sub-agents

A sub-agent is a second AI session that your main AI session starts. It has its own memory window, its own instructions and a limited set of tools. It does one job and hands back a short summary. The parent never sees the thousands of words the helper read.

Analogy: a research assistant who reads a whole annual report in another room and returns a one-page note. Three things make this worth doing: helpers work at once, each starts with a fresh memory, and a cheap model can read while an expensive model thinks.

Source: bj0fbejiq.txt, CHECK 3 section 4 (2026-09-14); read-this-first.md, glossary.

## Why this tool now (for this project)

### OCR: three decks that our converter could not read

The local corpus, the folder `financeMD`, was made by converting Damodaran's site to text. Three free PDF decks did not convert cleanly: the "Dark Side of Valuation" core deck, the 2012 full-day seminar deck and the 2013 extended "Jedi Guide" deck. They are image-heavy. A plain PDF-to-text pass returns headings and loses the numbers in the tables.

Source: bkm2kob5x.txt, learning path, Dark Side table and ingestion note (2026-09-14); the plan, section 8; other-side/00-read-me-first.md, "The gaps in the local corpus".

The plan says the librarian's tier 1 is not complete until these decks are backfilled. Document D, "The Other Side", leans on them for the uncertainty types the memo writer names. So OCR is a one-time chore, not a feature.

Source: the plan, sections 1 and 9 ("Corpus gaps"); read-this-first.md, section 2.

### Search APIs: only for news, and not yet

Our numbers come from structured sources: SEC EDGAR, Damodaran's tables and later EODHD. None needs a search engine. A search API earns its place only for the qualitative layer, "what changed this quarter for Trent", which feeds the memo writer's evidence list. That is deferred beyond v1.

Source: b31x0pyot.txt, section 5 ("Not relevant" and "Relevant" notes) and section 8; the plan, section 9 ("Deferred").

### Sub-agents: deferred to v2

The plan defers sub-agents, for auditability. A prose summary is lossy, and every number in a memo must trace to a row with a source. When the time comes, Cursor's cloud agents and Cursor Projects supply the mechanism, so there is nothing to build.

Source: the plan, sections 8 and 9.

## How it is used in this project

### OCR, step by step

1. Check before you pay. Run `pdffonts file.pdf`. If no fonts are listed, the file is image-only. Then run `pdftotext -layout file.pdf -` on a few pages. If the text is there, skip OCR.
2. Send the image-only decks to Mistral Document AI through its batch endpoint. Batch means you queue all the pages at once and collect results later, for a lower price. The account is number 9 in Document A's list, key `MISTRAL_API_KEY`.
3. Store the output in the R2 bucket (our cloud file store), named by its hash (a fingerprint computed from the file's bytes), next to the other raw files. It is Markdown, so it enters the librarian's index like any other page.
4. Check quality with three cheap tests. Hand-type three to five representative pages and compare. Add up the columns of each table; if they miss the printed total, a digit was misread. Confirm the page count so no page was silently dropped.

`pdffonts` and `pdftotext` come from a free tool set called Poppler. That is general knowledge, not from the project reports, so verify it.

Source: bj0fbejiq.txt, CHECK 3 section 2 and CHECK 2 Role 8 (2026-09-14); the plan, section 8; read-this-first.md, sections 2 and 10.

Why Mistral. On the only independent 2026 OCR comparison the project found, an olmOCR-Bench run dated 2026-06-28, Mistral scored 74.9% overall and 94.3% on tables. Open-source tools scored far lower: Marker 55.2%, Docling 37.7%. Mistral also returns bounding boxes, the pixel coordinates of each block, which will let a memo cite a slide number.

Source: bj0fbejiq.txt, CHECK 2 Role 8 (2026-09-14).

What it costs. Mistral OCR is $4 per 1,000 pages, about $2 per 1,000 through the batch API. A 100-page deck is therefore about $0.40 at list price, or about $0.20 through the batch endpoint we use. Document A budgets about $10 once for all OCR and expects the three decks to cost about $2. Table quality, not price, decides.

Source: bj0fbejiq.txt, CHECK 3 section 2 and CHECK 2 Role 8; read-this-first.md, sections 10 and 12 (2026-09-14).

### Crawling, search and the law, in plain words

Robots.txt is a small text file at a website's root, for example `example.com/robots.txt`. It tells automated visitors which paths they may fetch. The format is a published standard, RFC 9309. Obeying it is voluntary, and no law makes ignoring it a crime. Courts have treated ignoring it as bad faith. We honor it, always.

Source: bj0fbejiq.txt, CHECK 3 section 3 (2026-09-14).

The legal picture, as the report summarizes it, not as legal advice: in the United States, fetching a public page is generally not a computer-crime offense. The hiQ v. LinkedIn case held that an open page has no gate to break. But hiQ still lost on LinkedIn's terms of service, and Meta v. Bright Data confirmed that contract claims survive. The real risks are a site's terms, copyright and privacy law. That is why every database row carries a `license_class`, and why the index refuses the classes that may not be shown.

Source: bj0fbejiq.txt, CHECK 3 section 3 (2026-09-14); read-this-first.md, section 3.3; the plan, section 10.3.

The good news is that we rarely scrape. SEC EDGAR publishes free official JSON APIs (structured data a program can read directly) with no key. You send a descriptive `User-Agent` header (a short self-identification line sent with each request) with a contact email and stay under 10 requests per second. Damodaran's pages are static files we fetch directly. Bloomberg and INDmoney forbid scraping in their terms, so we never crawl them; Chapter 9 covers the allowed feeds.

Source: b31x0pyot.txt, section 8B (2026-09-14); the plan, section 8.

Which search API, if we add one. Artificial Analysis published a Search Index on 2026-08-18. It ran the same AI agent over three question sets and changed only the search provider. Higher score is better.

| Provider | Index score | Cost per 1,000 tasks | Seconds per task |
|---|---|---|---|
| Parallel (advanced) | 75 | $83.51 | 35.9 |
| Exa (auto) | 74 | $127.15 | 26.2 |
| Firecrawl | 73 | $75.42 | 55.0 |
| Parallel (turbo) | 67 | $60.21 | 18.8 |
| Tavily (basic) | 66 | $192.58 | 36.3 |

Parallel turbo is about six cents per task, my division of the table's figures. The project's pick is Parallel: turbo for routine lookups, advanced for the few that matter. Tavily is the worst value on the board, lowest quality of the five shown here (second-lowest on the full board) at the highest price. Two cautions. This is one benchmark from one publisher, so treat three points as noise. And two project reports quote different dollar figures for the same index; the ranking agrees, the dollars do not, so re-check the live page before spending.

Source: bj0fbejiq.txt, CHECK 2 Role 9 and caveat 2 (2026-09-14); b31x0pyot.txt, section 5; read-this-first.md, section 13.

Outside the benchmark, all three leaders have free tiers: Exa $20 of credit plus $10 a month, Parallel $5 of credit monthly, Firecrawl 1,000 credits a month at one credit per page. Document A lists Parallel as an optional later account at about $18 a month.

Source: bj0fbejiq.txt, CHECK 3 section 3 (2026-09-14); read-this-first.md, section 10, row 12.

### Sub-agents: what Cursor already gives you

Cursor cloud agents run in isolated cloud machines. You start one by writing `@cursor` on a GitHub pull request or issue, or from cursor.com/agents. Any number can run at once, under a spend limit you set. They bill at the standard price of the chosen model, from your Cursor usage pool. The MCP tools (the project's own tool server that Cursor plugs into, see Chapter 2) in `.cursor/mcp.json` work inside them, so a cloud agent can call `search_corpus` or `value_company`.

Cursor Projects, released 2026-09-10, adds a coordinator agent that plans and hands pieces to parallel sub-agents without writing code itself. That is the sub-agent pattern, packaged.

Source: btzaixzyh.txt, CHECK 1, "Cloud / Background Agents" (2026-09-14); read-this-first.md, section 11.

The cost, plainly. Each helper pays for its own instructions and tool list. Five helpers cost roughly five times one call, plus the parent's cost to split and merge. Anthropic's account of its multi-agent research system puts the token bill near fifteen times a single chat. On a $200 a month ceiling, remember that number.

Source: bj0fbejiq.txt, CHECK 3 section 4 (2026-09-14).

When not to use them:

- Step two needs the full output of step one, and a summary would lose it.
- Two helpers would write the same database row and silently conflict.
- The task is small, and the handoff costs more than the work.
- The numbers must be audited. Make helpers write structured rows with citations and return only row ids. The parent reads facts from the database, never from a paraphrase.
- You are debugging. One straight transcript is easier to read than ten interleaved ones.

Source: bj0fbejiq.txt, CHECK 3 section 4 (2026-09-14); the plan, section 8.

### Speed and cost per task, side by side

| Task | Tool | Rough cost | Rough speed |
|---|---|---|---|
| OCR one 100-page deck | Mistral batch | about $0.20 to $0.40 | Queued; results come back later, not in seconds |
| One search query | Parallel turbo | about $0.06 | About 19 seconds inside an agent loop |
| One EDGAR fact lookup | SEC API | $0 | Under a second; stay under 10 per second |
| Five parallel helpers | Cursor cloud agents | about 5 times one call | All five run at once |

Source: bj0fbejiq.txt, CHECK 2 Roles 8 and 9, CHECK 3 sections 2 to 4; b31x0pyot.txt, section 8B (2026-09-14).

## Learn it

All free. Total about 4 hours. Stop after row 3 if you are not adding news search.

| # | Resource | Format | Hours | Why |
|---|---|---|---|---|
| 1 | https://mistral.ai/pricing/api/ and https://mistral.ai/news/mistral-ocr | Official pricing and announcement | 0.5 | The exact price per 1,000 pages and what the Markdown output looks like. |
| 2 | https://www.sec.gov/search-filings/edgar-application-programming-interfaces | Official docs | 1 | Free, legal, structured US data; removes most of the reason to scrape. |
| 3 | https://www.rfc-editor.org/rfc/rfc9309.html | Standard, about 30 pages | 0.5 | The actual robots exclusion protocol, so you know what you are honoring. |
| 4 | https://artificialanalysis.ai/methodology/search-api | Benchmark write-up (2026-08-18) | 0.5 | How the Search Index was built, and the cost table you would budget from. |
| 5 | https://www.anthropic.com/engineering/building-effective-agents | Article | 0.75 | The decision tree between one chain of steps and an orchestrator with workers. |
| 6 | https://cursor.com/docs/cloud-agent | Official docs | 0.5 | How to start, watch and cap a cloud agent from a pull request. |

Source: bj0fbejiq.txt, CHECK 3 sections 2 to 4 resource tables; b31x0pyot.txt, section 5; btzaixzyh.txt, CHECK 1 links (all as listed 2026-09-14).

## 10-minute exercise

The goal is to tell a text PDF from an image PDF with your own hands.

1. Download the short core deck, `darkside.pdf`, from https://pages.stern.nyu.edu/~adamodar/pdfiles/country/darkside.pdf (the link Document D also lists). Save it in your Downloads folder.
2. In a terminal, run `pdffonts ~/Downloads/darkside.pdf`. If no fonts are listed under the header, the file is image-only.
3. Run `pdftotext -layout ~/Downloads/darkside.pdf - | head -40`. Read what comes out. Are the words there, or only a few headings and blank lines?
4. Note which class the deck falls in, in your decisions log.
5. In a browser, open `https://www.sec.gov/robots.txt`. Read the first twenty lines. Write one sentence on what it allows and what it delays.

If `pdffonts` is missing, install Poppler first; on a Mac that is a Homebrew command, which you should verify on the Homebrew site.

Source: bkm2kob5x.txt, learning path, Dark Side table (2026-09-14); bj0fbejiq.txt, CHECK 3 sections 2 and 3.

## Done when

- You can say in one sentence why a PDF can look normal yet contain no text.
- You have run `pdffonts` and `pdftotext` on one deck and written down which class it is.
- You can name the three quality checks for OCR output without looking: hand-typed pages, column sums, page count.
- You can explain the difference between search, crawl and scrape with the library analogy.
- You can state why terms of service, not computer-crime law, are the real scraping risk, and why every row carries a `license_class`.
- You can name two cases where a sub-agent is the wrong tool, and say where the sub-agent machinery already lives in Cursor.
