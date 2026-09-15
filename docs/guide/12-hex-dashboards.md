# Chapter 12. Hex: a private dashboard over Neon {#r4-dashboard}

::: {.reading-only .optional}
**For the dashboard stage.** Understand the connection between stored data and the chart, then return to the notebook exercises.
:::

## What it is (plain words and an analogy)

Hex is a website where you write small blocks of code, called cells, and see the result under each block. A page of cells is a notebook. One click turns the notebook into a dashboard, which is the same page with the code hidden and only the charts and tables showing. Hex runs in the cloud, so nothing is installed on your Mac.

Think of a kitchen with a serving hatch. The notebook is the kitchen, where you chop, mix and taste. The dashboard is the hatch, where the finished plate appears. Hex is the one tool on the shortlist where the kitchen and the hatch are the same room.

Three kinds of cell matter here. A SQL cell asks the database a question in SQL, the standard language for talking to databases. Its answer arrives as a dataframe, which is a table held in Python memory, like one tab of a spreadsheet. A Python cell can then do arithmetic on that table. A chart cell draws a table as a bar, line, scatter or histogram without any code. An input widget is a dropdown or slider on the page that feeds a value into the cells below it.

Source: /Users/siddharth/.claude/projects/-Users-siddharth-Downloads/edcdeb19-7793-4e1b-9e73-4cf6186716bf/tool-results/btzaixzyh.txt, CHECK 2 comparison table and "Why Hex" list (September 2026).

## Why this tool now (for this project)

The plan lists seven parts of the system. Part 6 is "a private dashboard (you look, you do not print)", a hosted notebook over the same database that shows diversification, value-versus-price distributions, Monte Carlo ranges, the accuracy scoreboard and the market panel. Hex was picked because it is the only tool within budget that combines five things in one surface: SQL straight against Neon, real Python for Monte Carlo and bias and variance, product-grade chart cells with input widgets, private single-user sharing, and a built-in AI agent.

Source: /Users/siddharth/.claude/plans/help-me-out-here-abstract-wilkinson.md, sections 1 and 7 (2026-09-14).

Hex has two plans that concern you. The comparison below copies the report.

| Plan | Price | What you get | What you do not get |
|---|---|---|---|
| Community | Free | Unlimited users, 5 projects, small compute, 7-day history, project-level database connections, AI agent trial | No published apps, so the dashboard is only visible inside the notebook editor |
| Professional | $36 per editor per month | Published, code-hidden apps; one scheduled refresh per project, daily at most; workspace-level connections | Custom timed schedules (cron) and hourly runs, which need Team at $75 |

The plan and Document A budget the same line: Hex costs $0 now and $36 later, when you want a published dashboard with a daily refresh. The honest costs of Hex are lock-in (the notebook lives in Hex, not in git), small compute on Community, and embedding into a web app being an Enterprise feature.

Source: btzaixzyh.txt CHECK 2 comparison table and "honest costs" paragraph; /Users/siddharth/Valuation/docs/read-this-first.md section 12 (2026-09-14).

## How it is used in this project

### Connecting to Neon

Neon is the cloud Postgres database that holds every number the calculator uses. Hex talks to it through a native Postgres connector with SSL, which encrypts the link. The accounts table in the plan says exactly one thing about the Hex setup: configure the Neon connection inside Hex with the pooled host and SSL on. The pooled host is the address that ends in `-pooler` and goes through a connection pooler called PgBouncer, which shares a few real connections among many short queries. Use `sslmode=require`, not `verify-full`, on the pooled host. Keep the direct host for migrations only. Neon also recommends pointing dashboard tools at a read replica, because dashboards fire long queries at the main database. At this size a read-only database role is the cheaper first step; the replica can wait.

Source: btzaixzyh.txt CHECK 2, "Neon connection gotchas"; plan section 7, accounts row 10 (2026-09-14).

### The pattern: robots compute, Neon stores, Hex draws

The nightly GitHub Actions jobs (chapter 3) do all the heavy work and write finished tables into Neon. Hex only runs `SELECT`. The report says this removes in-tool scheduling as a buying criterion, and it is why Community is enough for a long time. Treat the dashboard as a disposable read layer. If you ever swap Hex for something else, it is a weekend, not a rewrite.

Source: btzaixzyh.txt CHECK 2, last bullet of "Neon connection gotchas" and closing paragraph of "When you'd need a custom Next.js app" (September 2026).

### The four dashboards

| Dashboard | Tables it reads | Cells it uses | Milestone |
|---|---|---|---|
| Diversification and sector exposure | `watchlist`, `company`, `valuation_run` | SQL cell into a dataframe, treemap or stacked bar chart cell, a dropdown widget for country or date; a scatter of value against price with a 45-degree line; Monte Carlo range per run | M2 first version, M4 for 20 to 50 India and US names |
| Accuracy scoreboard | `valuation_run`, `realised_price` | Python cell with pandas for rolling error, table plus trend chart, grouped by sector, region, vintage and memo version | M4, first scored horizon after 90 days |
| Market regime panel | `erp_monthly`, `erp_annual`, credit spread series from FRED (the St. Louis Fed's free economic data service) | Line charts against Damodaran's 1960 to 2025 history, percentile bands, plain-sentence states, Damodaran's market-timing caveat printed on the panel | M4 |
| Run health | `job_heartbeat` | One table: job name, last success time, hours since; a red flag when any nightly row is older than 36 hours | M2 onward |

Source: plan sections 5 (M2 item 9, M4 items 2, 4 and 5), 10.3 and 10.7; btzaixzyh.txt CHECK 2 "Why Hex, concretely" (2026-09-14).

### Python cells: Monte Carlo, bias, variance

Monte Carlo means drawing each uncertain input many times from a range, running the calculator each time, and looking at the spread of results. The ranges come from Damodaran's own industry quartiles. In Hex this is numpy code (numpy and pandas are the standard Python libraries for arrays and tables; scikit-learn adds statistics helpers) in a Python cell over the rows a SQL cell pulled above it. Bias is the average signed error of value against the later price. Variance is the spread of that error. Both are pandas or scikit-learn arithmetic in the same cell, then a table and a trend chart. The banner on that page must read: "The engine is tested (Almarai 1e-6). The forecast is not."

Source: read-this-first.md sections 3.5 and 6; btzaixzyh.txt CHECK 2 items 3 and 4 (2026-09-14).

### When a custom web app would be needed instead

Not now. Build one only when any of these becomes true: you want write-back (edit a growth assumption on the page and re-run); you need more than one class of viewer with per-user access; embedding is the product; you need bespoke visuals such as a DCF waterfall or a football-field range; you are stitching three or more tools together or the dashboard bill passes about $75 per month; or you want a portfolio piece for an employer. Until then, Hex.

Source: btzaixzyh.txt CHECK 2, "When you'd need a custom Next.js app instead" (September 2026).

### Deepnote, the runner-up

Deepnote is the close second. Its free tier gives 3 editors, 5 projects and 2 vCPU with 5 GB machines, with no scheduling. Team costs $39 per editor per month on an annual plan, or $49 monthly, and adds scheduled notebooks. Pick Deepnote if you value "it is just a notebook", which will feel like coursework. Pick Hex if you value "it turns into a dashboard".

Source: btzaixzyh.txt CHECK 2 comparison table and "Close second" paragraph (September 2026).

## Learn it

All free. Total about 4 hours.

| # | Resource | Format | Hours | Why |
|---|---|---|---|---|
| 1 | https://learn.hex.tech/docs | Official docs, start with the getting-started pages | 1 | Cells, projects, the app builder and the publish button, in Hex's own words. |
| 2 | Hex Learn docs, data connections page for PostgreSQL (verify exact URL) | Official docs | 0.5 | The form you fill to connect Neon: host, database, user, SSL. |
| 3 | https://neon.com/docs/connect/connection-pooling | Official docs | 0.5 | Why the `-pooler` host exists and what it does not allow. |
| 4 | https://neon.com/docs/connect/connection-errors | Official docs | 0.5 | The SNI rule (SNI is a field in the encrypted handshake that tells Neon which database you want; old drivers do not send it) and the fix if a connector refuses to talk to Neon. |
| 5 | https://pandas.pydata.org/docs/user_guide/10min.html | Official tutorial | 1 | Dataframes, grouping and rolling windows, which is all the scoreboard needs. |
| 6 | https://learn.hex.tech/docs/share-insights/scheduled-runs | Official docs | 0.5 | Read this before paying for Professional, so the daily cap is not a surprise. |

Source: URLs 4 and 6 are from btzaixzyh.txt CHECK 2 (September 2026); URLs 1, 3 and 5 are official documentation homes that the local reports do not cover, so they come from general knowledge; the hours are my estimates.

## 10-minute exercise

::: {.reading-only .optional}
**For the practical stage.** Use this exercise when working on this chapter's tool. The following "Done when" checklist tells you how to judge completion.
:::

This assumes the M2 dashboard project exists in your Hex workspace. The plan lists "add a chart in Hex" as one of the M3 exercises.

1. Open the project and add a SQL cell. Write a query that counts rows in `valuation_run` by the sector of the company, joined through `company`.
2. Name the result dataframe `by_sector`.
3. Add a chart cell on `by_sector`. Choose a bar chart, sector on one axis, count on the other.
4. Add an input widget above the SQL cell, a dropdown of countries. Reference its value in the query's `WHERE` clause.
5. Change the dropdown and watch the bar chart change.

If the repo does not exist yet, do the smaller version. Create a free Community workspace, make one project, add a Postgres connection with the pooled Neon host and SSL on, and run `select 1` in a SQL cell. Confirm the cell returns a one-row dataframe.

Source: plan section 5, M3 exercises; plan section 7, accounts row 10 (2026-09-14).

## Done when

::: {.reading-emphasis .key-idea}
- You can say the difference between a notebook and a published app, and which Hex plan gives you each.
- Your Hex project connects to Neon through the pooled host with SSL on, and a `select 1` returns.
- You have made one SQL cell, one chart cell and one input widget that change together.
- You can name the four dashboards and the Neon table each one reads.
- You can list three of the six reasons to build a custom web app, and say why none applies yet.
:::
