# Chapter 9. Data sources: where every number comes from, and what you may do with it

## What it is (plain words and an analogy)

A data source is any place the system fetches a number or a sentence from. Think of the system as a restaurant kitchen. The engine (Chapter "The DCF chain" in Document C) is the recipe. The data sources are the suppliers who deliver ingredients to the back door.

Every supplier differs in three ways: a delivery schedule (daily, monthly, yearly), a container (a JSON file, an old Excel file, a CSV), and a contract saying what you may do with the goods. In this project that contract is written onto every stored row as a licence class (section 3.3 of read-this-first.md).

Source: /Users/siddharth/Valuation/docs/read-this-first.md, section 3.3 (2026-09-14)

Two terms you will meet on every page below:

- An API (application programming interface) is a web address that returns data for a program instead of a web page for a human.
- A rate limit is the maximum number of requests a supplier allows per second or per day. Exceeding it gets you blocked.

## Why this tool now (for this project)

Damodaran himself tells you where the numbers should come from. His data page says that for a live valuation you should "get real time data from the company's filings or annual report." His own tables are industry averages, refreshed mostly once a year. So the project needs two kinds of suppliers: company filings for the base year, and his tables for the averages that fill in the rest.

Source: /Users/siddharth/Downloads/financeMD/damodaran/New_Home_Page/datahistory.md, rule 3 (corpus copy, 2026)

The second reason is money and law. The system must run under $200 a month, and everything stored must be legal to keep. So: free public sources first (SEC, Damodaran, FRED, NSE files), one paid licence for India statements (EODHD), and nothing scraped from apps or newspapers.

Source: /Users/siddharth/Valuation/docs/read-this-first.md, section 12 (2026-09-14)

## How it is used in this project

The nightly robot (Chapter 3, GitHub Actions) wakes at about 6:17 UTC, checks each watchlist company for a new filing, downloads the numbers, builds trailing-twelve-month figures, and writes them to Neon with source, licence class and vintage. A monthly and quarterly job watches Damodaran's files for a changed fingerprint. A third job pulls licensed headlines and stores them as annotations only.

Source: /Users/siddharth/Valuation/docs/read-this-first.md, section 7 (2026-09-14)

### The source table

| Source | What it supplies | Cadence | Format | Cost | Licence class |
|---|---|---|---|---|---|
| SEC EDGAR | US company statements, filing lists | nightly | JSON | free | `public_domain` |
| Damodaran datasets | industry averages, country risk, implied ERP | yearly, quarterly, monthly | `.xls` and `.xlsx` | free | `damodaran_public` |
| EODHD | India (and global) statements | on request | JSON | $60 a month, from M4 | `licensed_personal` |
| NSE bhavcopy | daily NSE closing prices | daily file | CSV in a zip | free | read NSE terms before use |
| INDstocks API | your own holdings, quotes, price history | on request | JSON | free with account | `licensed_personal` |
| FRED | US Treasury yields, credit spreads | daily | CSV or JSON | free | `open_access` |
| Bloomberg | reading only | n/a | web, email | your own subscription | `proprietary_personal` |

Source: /Users/siddharth/Valuation/docs/read-this-first.md, sections 3.3, 10 and 12; /Users/siddharth/.claude/plans/help-me-out-here-abstract-wilkinson.md, section 7 (2026-09-14)

### SEC EDGAR

EDGAR is the US regulator's public filing system. Every listed US company files its statements there in XBRL, a tagging standard that gives every number a name such as `OperatingIncomeLoss`. There is no API key and the data is public domain.

Three endpoints matter. Each takes the company's CIK, a ten-digit identifier padded with zeros.

| Endpoint | Address pattern | What you get |
|---|---|---|
| submissions | `https://data.sec.gov/submissions/CIK##########.json` | the list of filings, each with an accession number |
| companyfacts | `https://data.sec.gov/api/xbrl/companyfacts/CIK##########.json` | every tagged number the company ever filed |
| frames | `https://data.sec.gov/api/xbrl/frames/us-gaap/<Tag>/USD/CY2019Q1I.json` | one tag, one period, across all filers |

The nightly job reads `submissions` first. A new accession number means a new filing, and only then does it fetch `companyfacts`. The `frames` endpoint is your free peer-group builder: one number for every filer in one period, which is how you check a US industry median for free. Bulk zip files of both are published nightly at about 03:00 US Eastern time.

Source: /Users/siddharth/.claude/projects/-Users-siddharth-Downloads/edcdeb19-7793-4e1b-9e73-4cf6186716bf/tool-results/bkm2kob5x.txt, section 12 (2026-09-14)

The User-Agent rule. The SEC requires every request to carry a descriptive User-Agent header with your name and email. A request without it is refused. Read the SEC's fair-access policy before you write any loop, because it sets a request-rate limit and the SEC blocks addresses that exceed it.

Source: same report, section 12

The LTM construction. LTM means "last twelve months." Company filings do not give it to you directly. A 10-K (the annual report) covers a fiscal year, and a 10-Q (the quarterly report) covers a year-to-date period. The rule is: LTM = last 10-K, minus the prior year's year-to-date interim, plus the current year-to-date interim. Damodaran's own workbook has a "Trailing 12 month" worksheet that computes exactly `E = B - C + D`, but it is a standalone helper that you paste into by hand. Our ingest code does the subtraction and records which three filings it used.

Source: /Users/siddharth/.claude/projects/-Users-siddharth-Downloads/edcdeb19-7793-4e1b-9e73-4cf6186716bf/tool-results/bkdrkpfng.txt, sections 1.2 and 3.8 (2026-09-14)

Missing interest expense. The workbook turns interest expense into a synthetic credit rating through the coverage ratio, operating income divided by interest expense. If interest expense is zero the sheet sets coverage to 1,000,000, which reads as a perfect rating. Apple's `InterestExpense` tag exists in `companyfacts`, but its last value covers the year ending 2023-09-30 (3,933 million dollars) and nothing after. So a naive loader sees "missing" and writes zero, and the model rewards Apple with a top rating by accident. The plan's fix is a visible `interest_missing` flag on the `ltm_financials` row, never a silent zero.

Source: https://data.sec.gov/api/xbrl/companyfacts/CIK0000320193.json (fetched 2026-09-14); bkdrkpfng.txt, section 3.4; /Users/siddharth/.claude/plans/help-me-out-here-abstract-wilkinson.md, sections M2 and 10.3 (2026-09-14)

### Damodaran's datasets

Cadence. His data page says: "I update most of the data only once a year, in the first two weeks of January." The current full update is dated January 9, 2026. Three things move faster: country risk premiums (January, April, July), the implied equity risk premium (monthly), and a daily market tape during crises.

Source: /Users/siddharth/Downloads/financeMD/damodaran/New_Home_Page/datahistory.md; /Users/siddharth/.claude/projects/-Users-siddharth-Downloads/edcdeb19-7793-4e1b-9e73-4cf6186716bf/tool-results/bafb6h9rb.txt, section 5 (2026-09-14)

File names. Files live under `https://pages.stern.nyu.edu/~adamodar/pc/datasets/`. The name is a family plus a region suffix: `wacc.xls` for the US, `waccIndia.xls`, `waccemerg.xls`, `waccGlobal.xls`, and so on across eight regions. Five names break the pattern and must be hard-coded: `betas.xls` (not `beta`), `pedata`, `pbvdata`, `psdata`, and `DollarUS.xls`. The `R&D` files contain an ampersand that must be URL-encoded. Dated files such as `ctrypremJuly26.xlsx` and `ERPSept26.xlsx` cannot be guessed; the job must read the link list and discover them.

Source: bafb6h9rb.txt, sections 1 and 5 (2026-09-14)

The 244-URL manifest. His `datacurrent` page contains 244 distinct dataset addresses. That page is a ready-made download list, and the corpus copy at `financeMD/damodaran/New_Home_Page/datacurrent.md` yields the same 244 with one grep. The `load-damodaran` job will use it once per vintage. Two more gotchas: the site misbehaves for Chrome, so use a plain HTTP client with a User-Agent, and `indname` (the company-to-industry map) is not linked from that page at all.

Source: bafb6h9rb.txt, section 5; verified by grep on /Users/siddharth/Downloads/financeMD/damodaran/New_Home_Page/datacurrent.md (2026-09-14)

The `.xls` gotcha. Most files are `.xls`, the pre-2007 Excel binary format called BIFF8. ExcelJS cannot read it at all. The only mainstream JavaScript reader is SheetJS Community Edition, version 0.20.3, which is installed from `cdn.sheetjs.com` by tarball address, not from npm. The `xlsx` package on npm is stuck at 0.18.5 with two unpatched high-severity security advisories. Never run `npm i xlsx`. The Python fallback is `pandas.read_excel(..., engine="xlrd")`.

Source: /Users/siddharth/.claude/projects/-Users-siddharth-Downloads/edcdeb19-7793-4e1b-9e73-4cf6186716bf/tool-results/bo0hrclp7.txt, section 7 (2026-09-14)

Inside each file the data sheet is named "Industry Averages" and the real header row is not row 1. Eight to twelve rows of notes come first, so the loader reads the sheet headerless and finds the row whose first cell is "Industry Name". Row 1 carries a "Date updated:" cell, which becomes the vintage stamp. His usage rules: acknowledgment is optional, per-company raw data is not to be redistributed, and he asks that the data stay out of court cases.

Source: bafb6h9rb.txt, section 5, points 5, 6 and 8 (2026-09-14)

### EODHD

EODHD is a paid data vendor covering more than 70 exchanges, including NSE and BSE. It is the project's only paid data licence, chosen because it is the one vendor with documented, long-history India statements in a normalized schema. It arrives at milestone M4, not before.

Source: /Users/siddharth/.claude/projects/-Users-siddharth-Downloads/edcdeb19-7793-4e1b-9e73-4cf6186716bf/tool-results/bj0fbejiq.txt, Role 10 (2026-09-14)

- Price: the Fundamentals Data Feed is $59.99 a month (read-this-first.md rounds it to $60). The free plan allows 20 calls a day.
- Call units: one fundamentals request costs 10 API call units, not one. A 50-name daily refresh is 500 units a day. So the project caches every response in Neon and re-pulls only on a new filing.
- Licence: the standard plans are for personal use. Every row is stored as `licensed_personal`, which the database rule keeps out of the librarian's index. Read the redistribution clause before paying, and test 20 NSE tickers first. The ticker form is `TRENT.NSE`.

Source: bkm2kob5x.txt, section 12; read-this-first.md, sections 10 and 12; plan, section M4 (2026-09-14)

### NSE bhavcopy

A bhavcopy is the free end-of-day price file that the National Stock Exchange publishes for every trading day, under "All reports" on its website. It is the licit free India price source. Screener.in and Tickertape forbid scraping, so they are not sources.

The format changed twice. In July 2024 the old layout was retired in favor of "CM-UDiFF Common Bhavcopy Final" (NSE circular 62424, dated 2024-06-12). In October 2025 the file names moved to four-digit years, `bhddmmyyyy.csv`, and gained session indicators (I1, I2, F1, F2). Any GitHub parser written before late 2025 will break silently. History is available from 2016-01-01.

Source: bkm2kob5x.txt, section 12 (2026-09-14)

### INDmoney's INDstocks API

INDmoney's broking arm, INDstocks, publishes a real, free, official API at `api-docs.indstocks.com`. It offers REST and WebSocket endpoints for orders, holdings and positions, live quotes, more than 10 years of daily price history, and option chains. There is no subscription fee; you need an INDstocks account with SEBI KYC. Endpoints have per-endpoint rate limits, roughly 10 requests a second on several, and return HTTP 429 when you exceed them.

Two rules shape its use here. First, order-placement endpoints require a whitelisted static IP address under NSE rules. GitHub Actions runners have no fixed address, and this project never places orders, so that constraint never applies. Read-only market-data endpoints have no such restriction. Second, INDmoney's terms forbid bots on its app and forbid copying or republishing content. So the system reads your holdings and prices through the official API only, and never scrapes the app or the website.

Source: /Users/siddharth/.claude/projects/-Users-siddharth-Downloads/edcdeb19-7793-4e1b-9e73-4cf6186716bf/tool-results/btzaixzyh.txt, CHECK 2, INDmoney section (2026-09-14)

### FRED

FRED (Federal Reserve Economic Data) is the free database run by the Federal Reserve Bank of St. Louis. Every series has a short code. The market-regime panel in M4 uses three:

| Series | What it is | Value the report saw |
|---|---|---|
| `DGS10` | 10-year US Treasury yield, daily | 4.95% on 2026-09-10 |
| `BAMLH0A0HYM2` | ICE BofA US high-yield option-adjusted spread, daily | 2.70% on 2026-09-10 |
| `BAMLC0A4CBBB` | the BBB-rated version of the same spread | not stated in the report |

Damodaran's own September 2026 post cites "Federal Reserve Data (FRED)" for these spreads, and `DGS10` is the risk-free input for replicating his implied-ERP calculator. FRED offers a free API key and plain CSV downloads; that detail is web knowledge, so verify it on the site.

Source: btzaixzyh.txt, CHECK 3, indicator 7 and "How to compute it" (2026-09-14); plan, section 10.7

### Bloomberg

There is no consumer API. The "API Library" page is the download index for the BLPAPI software kit, which connects to nothing without a Terminal (about $31,980 per user per year) or an enterprise data contract. A bloomberg.com subscription is a reading product with no data entitlement.

Source: bj0fbejiq.txt, CHECK 1, parts 1.1 to 1.7 (2026-09-14)

Headline RSS is a grey area. RSS is a machine-readable list of headlines with links. On 2026-09-14 `feeds.bloomberg.com/markets/news.rss` redirected to `www.bloomberg.com/feeds/markets/news.rss` and returned same-day items with no licence text. Bloomberg does not document or support these feeds, and its terms forbid any "scraper, robot, bot, spider" and forbid building a database from the service. If the project polls them at all it will do so a few times a day with caching, store title, link and time only, keep the output private, and never make them load-bearing.

Source: btzaixzyh.txt, CHECK 2, Bloomberg RSS section; bo0hrclp7.txt, RESEARCH 6, part 1 (2026-09-14)

Newsletters are the cleanest path. Bloomberg sends them to your Gmail, so reading your own mailbox does not touch its website. For India the two that matter are "India Edition" and "Markets Daily India". Your reading becomes a `narrative_note` row: link, date, your own one-sentence paraphrase, and the valuation input it moves. Never article text, and never a row in the index.

Source: bo0hrclp7.txt, RESEARCH 6, part 2 (2026-09-14)

### Licence classes, applied

The seven classes in read-this-first.md section 3.3 are the contract label on every box. A database rule refuses `licensed_personal`, `proprietary_personal` and `link_only` rows from the librarian's index. For any new source, write down its class first, then its cadence, then its format. Legal, then fresh, then correct.

Source: /Users/siddharth/Valuation/docs/read-this-first.md, section 3.3 (2026-09-14)

## Learn it

About four hours of documentation reading in total, all free.

| Resource | URL | Format | Hours | Why |
|---|---|---|---|---|
| SEC EDGAR APIs page, then the fair-access policy linked from it | https://www.sec.gov/search-filings/edgar-application-programming-interfaces | web docs | 1 | The three endpoints, the User-Agent rule and the rate limit, from the source itself |
| Damodaran's data pages, current and history | https://pages.stern.nyu.edu/~adamodar/New_Home_Page/datacurrent.html and `datahistory.html` (local copies in `financeMD/damodaran/New_Home_Page/`) | web, markdown | 1 | The 244 links, the cadence, the usage rules, in his words |
| EODHD fundamentals docs and quick start | https://eodhd.com/financial-apis/stock-etfs-fundamental-data-feeds and https://eodhd.com/financial-apis/quick-start-with-our-financial-data-apis | web docs | 0.5 | Call units, ticker format and the personal-use licence, before M4 |
| NSE "All reports" | https://www.nseindia.com/all-reports | web | 0.25 | See the bhavcopy file names and session codes with your own eyes |
| INDstocks API FAQ | https://api-docs.indstocks.com/faq/ | web docs | 0.5 | Rate limits, the static-IP rule for orders, and what read-only endpoints exist |
| FRED series pages and API docs | https://fred.stlouisfed.org/series/DGS10, https://fred.stlouisfed.org/series/BAMLH0A0HYM2, API docs at fred.stlouisfed.org (verify) | web | 0.5 | Learn to read a series page, then fetch the same series by code |

Source: bkm2kob5x.txt, section 12; btzaixzyh.txt, CHECK 2 and CHECK 3 (2026-09-14)

## 10-minute exercise

Pull Apple's `companyfacts` file and find its revenue tag. Apple's CIK is 320193, padded to `CIK0000320193`. Replace the name and email in the User-Agent with your own.

```bash
curl -s -H "User-Agent: Your Name your.email@example.com" \
  "https://data.sec.gov/api/xbrl/companyfacts/CIK0000320193.json" -o apple.json

python3 -c "
import json
d = json.load(open('apple.json'))
tags = d['facts']['us-gaap']
print(d['entityName'], 'tags:', len(tags))
for t in sorted(tags):
    if 'Revenue' in t:
        vals = tags[t]['units']['USD']
        print(t, 'last period ends', max(v['end'] for v in vals))
"
```

What you should notice:

1. The file is about 3.8 MB and holds 503 `us-gaap` tags for Apple.
2. The tag literally named `Revenues` stops at a period ending 2018-09-29. Searching for "Revenues" alone would give you stale numbers.
3. The live tag is `RevenueFromContractWithCustomerExcludingAssessedTax`. Its FY2025 value, for the year ending 2025-09-27, is 416,161,000,000 dollars, filed 2025-10-31 with frame `CY2025`.
4. Now repeat the loop with `'Interest' in t` and check the last `end` date for `InterestExpense`. You should see 2023-09-30. That is the missing-interest-expense problem, seen with your own eyes.

Source: https://data.sec.gov/api/xbrl/companyfacts/CIK0000320193.json (fetched 2026-09-14)

## Done when

- You can say, without looking, which three EDGAR endpoints exist and what each returns.
- You can write the LTM formula in one line and name the three filings it needs.
- You can explain why a zero interest expense produces a perfect synthetic rating, and what flag replaces the zero.
- You can list the Damodaran cadence (yearly, quarterly, monthly) and the five file-name exceptions.
- You know why `npm i xlsx` is banned and what to install instead.
- You can state EODHD's price, its call-unit rule, and its licence class.
- You can say which INDstocks endpoints need a static IP and why this project never touches them.
- You can name the two FRED series the regime panel uses.
- You can explain, in two sentences, why Bloomberg is reading only and where your reading notes go.
- The exercise printed Apple's FY2025 revenue and the 2023-09-30 interest-expense cutoff.
