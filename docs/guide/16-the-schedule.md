# Chapter 16. The schedule: twelve evenings-only weeks, from "go" to a working system

## What it is (plain words and an analogy)

A schedule is a promise about order, not about speed. It says what you read, watch and touch each week, and what must be true before the next week starts. Think of a school term. Each week has classes, and a few weeks end in an exam you must pass before the next term. Here the "exams" are called checkpoints. A checkpoint is one sentence that is either true or false about the system, such as "the golden test is green".

The weeks are grouped into milestones. A milestone is a bundle of work with a named owner and a "done when" line. This project has five: M0 (documents, already delivered), M1 (your accounts and Cursor), M2 (the foundation, built for you), M3 (you take the wheel) and M4 (India, accuracy, ranges, the market panel). A sixth, M5, exists in the plan only if other people ever use the system, and is out of scope here. The milestone map board draws them as a road.

Source: docs/plan.md section 5 (2026-09-14); https://www.figma.com/board/LXcGUT7C2ArsRkwsUvRBWt

## Why this tool now (for this project)

The research report's original 12-week plan assumed you would build everything yourself, with pi as the daily tool. The approved plan changed both facts. The foundation is built for you in days 3 to 7, and Cursor is the daily tool, so the same learning has to be re-timed. A written week also protects the 8 hours, which are easy to lose.

Source: bkm2kob5x.txt, "12-week evening schedule" (2026-09-14); plan sections 2 and 4

## How it is used in this project

### The rule that comes first

Nothing after M0 starts until you say go. No account is opened, no repository is created, no code is written before then. Week 1 begins on the day you say it, not on a calendar date.

Source: plan, "Scope of this approval: M0 only" (2026-09-14)

### The weekly budget

About 8 hours a week: four weekday evenings of 1.5 hours plus one 2-hour weekend block. Roughly 4.5 hours go to guide chapters and 3.5 hours to Cursor work. The Damodaran track is separate: about 3.5 hours a week in the report, which chapter 15 schedules as five 45-minute evenings (3.75 hours, a little slack), and which can overlap with a commute, so the desk total stays near 8 hours. One evening a week is a no-AI evening (chapter 0, rule 4).

Source: bkm2kob5x.txt, "12-week evening schedule"; plan section 4; guide chapter 15

### The twelve weeks

"PR" means pull request, a proposed change that someone reviews before it joins the main code (chapter 1). "CI" means continuous integration, the robot that runs the tests on every PR (chapter 3). A vintage is a dated snapshot of an input, so every number knows which day's data it came from (chapter 5).

| Week | Milestone | Guide chapters | Damodaran (chapter 15) | Accounts to open | Do in Cursor | You can stop here if |
|---|---|---|---|---|---|---|
| 0 (now) | M0 | Preface, 0, 2 | Nothing yet | None | Nothing; read A and C | Always. This is the default until you say go. |
| 1 | M1 (you) and M2 (built for you) | 1, 3, 14 | Accounting sessions 1 to 5 | Evening 1: GitHub 2FA, OpenRouter ($20 credit, $75 limit, logging off). Evening 2: Neon, Pinecone, Voyage, Cloudflare. Evening 3: Langfuse, Mistral, Hex, then `.cursor/mcp.json` | Day-one exercise: ask why terminal cost of capital = risk-free + mature ERP, then find the `Mature Market ERP +` label yourself | every key is in place and Cursor's agent lists the valuation tools |
| 2 | M3 | 4, then read `docs/walkthrough.md` | Valuation online 1 to 4 | None | Create and resolve a merge conflict; break the golden test and watch CI go red, then fix it | you are content to read memos and never edit code |
| 3 | M3 | 5, 6 | Valuation online 5 to 8 | None | Add a company to the watchlist; try to store a number without a vintage and watch Neon refuse; re-index one blog year | the watchlist has the names you care about |
| 4 | M3 done | 7, 8 | Corporate Finance online 4 to 11 | None | Review and edit a memo; add a diagnostic warning in TypeScript | five PRs are merged, 20 names have approved memos, and you can explain every `AGENTS.md` rule aloud. A US-only system now works. |
| 5 | M4 | 9 | Data Update 5, then 4 | EODHD: test 20 NSE tickers free, then Fundamentals at $60 a month | `value_company TRENT IN` shows tier and vintage | you do not need India |
| 6 | M4 | 12 | Corporate Finance online 12, 13, 17, 18; Data Update 7 | None | Add a chart in Hex; the sector-exposure and value-vs-price views | the dashboard answers your weekly questions |
| 7 | M4 | 11 | Valuation online 9, 14 to 18; Document C chapter 6 | None | Hand-label 100 real memos and answers; check the nightly eval issue | the advice-word test and the citation test are green |
| 8 | M4 | 10, 13 | Corporate Life Cycle 1 to 7 | None | The market-regime panel; update the five boards to match what exists | the panel reproduces ERP 4.09% and expected return 8.84% |
| 9 to 10 | Buffer | Re-read 0 and 8 | Corporate Life Cycle 8 to 20 | None | Reverse DCF and Monte Carlo review; a first opposing memo | the ratio in chapter 0, rule 8, is trending to zero |
| 11 to 12 | Buffer | 17 as needed | Investment Philosophies; Document D chapter 5 | None | Prove one engine, three consumers: the same `value_company` answer from Cursor, Cline and Claude | you can teach this chapter to someone else |

Source: plan sections 0, 4 and 5 (2026-09-14); /Users/siddharth/Valuation/docs/read-this-first.md section 10; bkm2kob5x.txt "12-week evening schedule" and section 13; guide chapter 15 week table

The plan schedules work only through week 8. Weeks 9 to 12 exist because things slip and because the Damodaran track runs twelve weeks. The first accuracy score needs 90 days of price history after the first stored valuation, so it lands just after this schedule ends.

Source: plan section 5, M4 item 4 (2026-09-14)

### The five checkpoints

The report placed these at the end of weeks 4, 6, 8, 10 and 12 for a self-build. Because M2 delivers the code in week 1, your job is to prove each one yourself, earlier.

| # | Must be true | Report week | Your week |
|---|---|---|---|
| 1 | The Almarai golden test is green in CI at 1e-6, and you have seen it go red | 4 | 2 |
| 2 | No number can be stored without a `vintage_id`; the database rejects the attempt | 6 | 3 |
| 3 | Every displayed number traces to source, license class and vintage | 8 | 4 |
| 4 | The chat refuses "buy", "sell" and "target price", and always cites | 10 | 7 |
| 5 | One engine, three consumers, no duplicated formulas | 12 | 12 |

If a checkpoint is false, stop and fix it before the next week.

Source: bkm2kob5x.txt, "Checkpoints that must be true"; bkdrkpfng.txt (golden value 7.187840270062114 versus price 72.28)

## Learn it

- Damodaran's self-paced class index, https://pages.stern.nyu.edu/~adamodar/New_Home_Page/onlineclass.htm. Web page, 15 minutes to bookmark. Free. It is the master list behind chapter 15's session numbers.
- The milestone map board, https://www.figma.com/board/LXcGUT7C2ArsRkwsUvRBWt. FigJam board, 20 minutes. Free. It is this chapter as a picture; the PNG is at /Users/siddharth/Valuation/docs/diagrams/png/milestone-map.png.
- The plan, `docs/plan.md`, sections 0, 4 and 5. Markdown, 30 minutes. It is the contract this chapter is derived from.
- Document A, /Users/siddharth/Valuation/docs/read-this-first.md, sections 10 and 14. Markdown, 20 minutes. Section 10 is the click-by-click order for week 1's accounts.
- GitHub's two-factor authentication page, https://docs.github.com/en/authentication/securing-your-account-with-two-factor-authentication-2fa/about-two-factor-authentication. Web page, 20 minutes. Free. The first task of week 1, evening 1.

Source: bkm2kob5x.txt sections 13 and 15 (2026-09-14)

## 10-minute exercise

1. Open the milestone map board and the calendar side by side.
2. Write a go date, or write "not yet" in your decisions log (chapter 0, rule 6). Both are valid.
3. Counting from that date, put three 1.5-hour blocks in week 1 and label them "evening 1, 2, 3" with the accounts from the table.
4. Add the five checkpoints as all-day events in weeks 2, 3, 4, 7 and 12.
5. Copy the three real stopping points into the log: end of week 1, end of week 4, end of week 8.

## Done when

- A go date exists, or "not yet" is written down on purpose.
- Week 1's three evenings are on your calendar with their account lists.
- You can name the checkpoint that gates each week without looking.
- You can say in one sentence why the report's week 4 became your week 2.
