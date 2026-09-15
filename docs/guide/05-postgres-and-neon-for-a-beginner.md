# Chapter 5. Postgres and Neon: the one place the numbers live

## What it is (plain words and an analogy)

A database is a program whose only job is to store facts and answer questions about them. Postgres (its full name is PostgreSQL) is a free, open-source database that has existed for decades. You talk to it in SQL, a small language of questions such as "give me every row where the country is India". Postgres is not a spreadsheet, but the mental picture of a spreadsheet is a good place to start.

Source: /Users/siddharth/.claude/projects/-Users-siddharth-Downloads/edcdeb19-7793-4e1b-9e73-4cf6186716bf/tool-results/bj0fbejiq.txt, CHECK 3 section 7 (2026-09)

Here are the five words you will meet on the first day.

- A **table** is one spreadsheet tab with a fixed shape. Every row has the same columns, and the database enforces that.
- A **row** is one record. In this project, a row is one fact: one number, for one company, from one source, on one date.
- A **column** is one named slot with one data type. A `numeric` column holds numbers and refuses the word "unknown".
- **NOT NULL** is a rule on a column that says "this slot can never be empty". The database refuses the write, not the program.
- A **CHECK constraint** is a rule the database tests on every insert. `CHECK (tax_rate >= 0 AND tax_rate <= 1)` refuses a 340% tax rate at the door.

Source: /Users/siddharth/.claude/projects/-Users-siddharth-Downloads/edcdeb19-7793-4e1b-9e73-4cf6186716bf/tool-results/bj0fbejiq.txt, CHECK 3 section 7 (2026-09)

The analogy the research report uses is worth keeping. Constraints are the guard rails on a mountain road. They are annoying while you drive, and they are the reason you are alive. A spreadsheet lets you type anything into any cell. A database with constraints is a spreadsheet that argues back.

Source: /Users/siddharth/.claude/projects/-Users-siddharth-Downloads/edcdeb19-7793-4e1b-9e73-4cf6186716bf/tool-results/bj0fbejiq.txt, CHECK 3 section 7 (2026-09)

Three more phrases matter for this project.

- **System of record** means that for any fact there is exactly one place that holds the truth. Everything else is a copy that can be thrown away and rebuilt. Here, the Postgres rows are the truth. The search index, the model's context window and every Markdown memo are copies.
- A **migration** is a versioned script that changes the shape of the database (the set of tables, columns and rules is called the schema): add a table, add a column, add a CHECK. Migrations are committed to git and applied in order, so every copy of the database has the same shape. Think of a migration as a commit for the database's structure, not its contents.
- A **Neon branch** is a full copy of your database created in seconds. Neon does not duplicate the storage; it only records what changed, which is called copy-on-write. It behaves like a git branch: try a migration on a branch, and drop the branch if it goes wrong.

Source: /Users/siddharth/.claude/projects/-Users-siddharth-Downloads/edcdeb19-7793-4e1b-9e73-4cf6186716bf/tool-results/bj0fbejiq.txt, CHECK 3 section 7 (2026-09)

Neon is a company that runs Postgres for you in the cloud. You install nothing. You get a connection string, a long URL with a host name, a user and a password inside it. Neon's trick is that the database switches itself off after about five minutes of silence and costs nothing while asleep.

Source: /Users/siddharth/.claude/projects/-Users-siddharth-Downloads/edcdeb19-7793-4e1b-9e73-4cf6186716bf/tool-results/bo0hrclp7.txt, section 2.1 (2026-09)

## Why this tool now (for this project)

The whole system rests on one rule from the research: retrieval finds the paragraph, the database holds the number. An AI model will eventually try to write a number that is wrong, badly scaled, or from the wrong year. If that number goes straight from a retrieved paragraph into a valuation, you find out weeks later. If it must first pass a NOT NULL and a CHECK, you find out at once, with an error message.

Source: /Users/siddharth/.claude/projects/-Users-siddharth-Downloads/edcdeb19-7793-4e1b-9e73-4cf6186716bf/tool-results/bj0fbejiq.txt, CHECK 3 sections 6 and 7 (2026-09)

Why Neon rather than another host? The vendor comparison scored six options. Neon won because a nightly batch job that runs for forty minutes and then sleeps costs cents, and because branches make experiments safe. The same report is honest about the weak spot: Neon acknowledged outages on 2026-05-08, 2026-07-11 and 2026-08-10. That was accepted because a failed nightly run simply retries; nothing here serves live users.

| Option | Why it lost |
|---|---|
| Supabase | Pro is $25 a month flat with no true scale-to-zero; its branching is heavier, a branch is a whole preview environment |
| PlanetScale Postgres | No free tier; branches need a restore from backup, so they are not instant |
| Turso | It is SQLite, not Postgres; the wrong family for numeric work |
| Railway Postgres | A container you look after yourself, with no branching |
| Xata | Free tier retired; a 27-person company is a thin longevity bet |

Source: /Users/siddharth/.claude/projects/-Users-siddharth-Downloads/edcdeb19-7793-4e1b-9e73-4cf6186716bf/tool-results/bj0fbejiq.txt, CHECK 2 Role 1 (2026-09)

Two earlier chapters already lean on this one. Chapter 3 (GitHub Actions) showed the nightly robots writing the `job_heartbeat` row to Neon. Chapter 4 (TypeScript) warned that `node-postgres` returns `NUMERIC` columns as strings. Both make more sense once you can picture the tables.

## How it is used in this project

### The tables, in one glance

The plan lists about twenty tables. Do not memorize them. Notice the pattern: some hold Damodaran's data by vintage, some hold company facts, and some record what the system did.

| Group | Tables | What a row is |
|---|---|---|
| Damodaran's data | `vintage`, `country_risk`, `industry_stat`, `industry_dist`, `erp_monthly`, `erp_annual` | One published number, stamped with the file it came from |
| Company facts | `company`, `fact`, `ltm_financials`, `realised_price` | One reported figure with its source URL, license class and vintage id |
| The system's own work | `valuation_run`, `valuation_inputs`, `memo`, `claim`, `narrative_note`, `market_context_event`, `job_heartbeat` | One run, one input, one memo, one claim, one note, one nightly success |
| The librarian's bookkeeping | `chunk_manifest`, `rag_eval_case`, `rag_eval_run` | One indexed chunk, one test question, one test result |

In `fact`, the columns `source_url`, `license_class`, `filed`, `accession` and `vintage_id` are all NOT NULL. In `valuation_run`, the three vintage ids are NOT NULL. Raw files are not stored in Postgres; they sit in a private bucket, named by their hash.

Source: docs/plan.md, section 10.3 (2026-09-14)

### Vintage: why every run stores three ids

Damodaran refreshes most tables every January, the country risk premiums quarterly, and the implied equity risk premium monthly. So one calendar year holds several versions of the same number. The 2026 files alone carry three risk-free rates and three mature-market risk premiums. A risk-free rate is the yield on a government bond with no default risk. A mature-market equity risk premium (ERP) is the extra return investors demand for owning stocks in a stable market.

| Where it sits | Risk-free rate | ERP |
|---|---|---|
| `wacc.xls` header block, January 2026 | 3.95% | 4.46% |
| `fcffsimpleginzu`, January 2026 vintage (the Almarai example) | 4.58% | 4.23% |
| `ERPSept26.xlsx` for the bond; `ctrypremJuly26` for the premium | 4.75% | 4.20% |

Source: /Users/siddharth/.claude/projects/-Users-siddharth-Downloads/edcdeb19-7793-4e1b-9e73-4cf6186716bf/tool-results/bafb6h9rb.txt, lines 34, 84 and 88; /Users/siddharth/.claude/projects/-Users-siddharth-Downloads/edcdeb19-7793-4e1b-9e73-4cf6186716bf/tool-results/bkdrkpfng.txt, line 23 (2026-09)

Mix a January industry table with a September risk premium and you get a confident answer with no warning. So every `valuation_run` row stores three ids: which market file, which country-risk file, which industry file. Each is NOT NULL, so the database refuses a run that is missing one. That is what "vintage" means in Document A, section 3.2. The workbook itself hard-codes 4.58% inside two formulas; the plan turns that literal into a stored vintage value.

Source: /Users/siddharth/Valuation/docs/read-this-first.md, section 3.2 (2026-09-14); /Users/siddharth/.claude/projects/-Users-siddharth-Downloads/edcdeb19-7793-4e1b-9e73-4cf6186716bf/tool-results/bkdrkpfng.txt, line 446 (2026-09)

### License class: why it sits on every row

Rights attach to facts, not to files. Document A, section 3.3, lists the seven classes. Note the spelling: Document A writes "licence", and the column is named `license_class`; they are the same thing. The classes are `public_domain`, `damodaran_public`, `open_access`, `asr_youtube`, `licensed_personal`, `proprietary_personal` and `link_only`. A CHECK on the column allows only those seven strings. A second rule, on `chunk_manifest`, refuses the last three from the search index.

Source: /Users/siddharth/Valuation/docs/read-this-first.md, section 3.3 (2026-09-14); docs/plan.md, sections 10.1 and 10.3 (2026-09-14)

The Bloomberg example shows why. Your bloomberg.com subscription is a reading product. Its terms say the service "may not be used to construct a database of any kind" (Bloomberg.com Terms of Service, section 3). So when you read an article, the system stores only the link, the headline, the date and your own one-sentence note, in `narrative_note`, with `license_class = 'proprietary_personal'`. Books and paid newsletters get `link_only`, meaning the row holds a link and nothing else. Both classes are refused by the index rule, so they never reach the librarian. The research report's analogy: allergen labels belong on every ingredient, not on the finished cake. One unlabeled Bloomberg number in `fact` would make the whole table unshareable, because you could no longer prove which rows were clean.

Source: /Users/siddharth/.claude/projects/-Users-siddharth-Downloads/edcdeb19-7793-4e1b-9e73-4cf6186716bf/tool-results/bo0hrclp7.txt, Bloomberg section (2026-09); /Users/siddharth/.claude/projects/-Users-siddharth-Downloads/edcdeb19-7793-4e1b-9e73-4cf6186716bf/tool-results/bj0fbejiq.txt, CHECK 3 section 7 (2026-09)

The payoff arrives later. When you ask "can I show this to someone?", the answer becomes a query: `WHERE license_class IN ('public_domain', 'damodaran_public', 'open_access')`. No audit, no guessing.

Source: /Users/siddharth/Valuation/docs/read-this-first.md, section 3.3 (2026-09-14)

### Migrations and branches in the daily loop

The schema will be written in Drizzle, a TypeScript library where the table definitions are TypeScript and the migrations are plain SQL you can read. The learning path picked it over Prisma for exactly that reason: when a `vintage_id` join duplicates rows and the ERP comes out wrong, you want to see the SQL.

Source: /Users/siddharth/.claude/projects/-Users-siddharth-Downloads/edcdeb19-7793-4e1b-9e73-4cf6186716bf/tool-results/bkm2kob5x.txt, learning path section 6 (2026-09)

The loop will work like this. You open a pull request. A GitHub Action creates a Neon branch, runs the migrations and tests against it, and posts the schema difference as a comment. When the pull request closes, the branch is deleted. Neon's GitHub App sets a `NEON_API_KEY` secret and a `NEON_PROJECT_ID` variable in the repo to make that possible. The free plan allows 10 branches per project; on the paid plan each extra branch costs $1.50 per branch-month, so branches are always deleted on close.

Source: /Users/siddharth/.claude/projects/-Users-siddharth-Downloads/edcdeb19-7793-4e1b-9e73-4cf6186716bf/tool-results/bo0hrclp7.txt, sections 2.1 to 2.3 (2026-09)

One habit from the research to adopt on day one: create a branch before any schema change an AI tool proposes. Neon branching is your undo button.

Source: /Users/siddharth/.claude/projects/-Users-siddharth-Downloads/edcdeb19-7793-4e1b-9e73-4cf6186716bf/tool-results/bj0fbejiq.txt, CHECK 2 accounts checklist (2026-09)

### The two connection URLs, and the SNI gotcha

Neon gives you two connection strings for the same database, and Document A asks you to save both.

| Name in `.env` | Host looks like | Who uses it | Why |
|---|---|---|---|
| `DATABASE_URL` (pooled) | `ep-xxx-pooler.<region>.aws.neon.tech` | Web functions, Hex, any dashboard | A pooler (PgBouncer) shares a few real connections among many short visits |
| `DATABASE_URL_UNPOOLED` (direct) | `ep-xxx.<region>.aws.neon.tech` | Migrations and long scripts | Migrations need features the pooler does not pass through |

A pooler is a doorman. A web function opens and closes a connection on every request, and bare Postgres would run out of doors. The pooler keeps a few doors open and lets visitors share them. The pooled host needs `sslmode=require`, not `verify-full`, and accepts only a short list of startup settings. Migrations use the direct endpoint.

Source: /Users/siddharth/Valuation/docs/read-this-first.md, section 10, rows 4 and 10 (2026-09-14); /Users/siddharth/.claude/projects/-Users-siddharth-Downloads/edcdeb19-7793-4e1b-9e73-4cf6186716bf/tool-results/bo0hrclp7.txt, section 2.4; btzaixzyh.txt, "Neon connection gotchas" (2026-09)

Now the gotcha. SNI stands for Server Name Indication. It is a field at the start of an encrypted connection where the client names the host it wants. The Postgres protocol carries no host name, so Neon relies on SNI to route your connection to the right database. Modern drivers send it; the reference library `libpq` has since version 14, released in September 2021. An old or unusual tool may not, and the connection fails with a confusing error. The fix is to append `?options=endpoint%3D<endpoint-id>` to the URL, or to prefix the password with `endpoint=<endpoint-id>;`. If a dashboard tool refuses to connect, check this first.

Source: /Users/siddharth/.claude/projects/-Users-siddharth-Downloads/edcdeb19-7793-4e1b-9e73-4cf6186716bf/tool-results/btzaixzyh.txt, "Neon connection gotchas", citing https://neon.com/docs/connect/connection-errors (2026-09)

### What it costs

| Plan | Included | Price |
|---|---|---|
| Free | 0.5 GB storage per project, 100 compute-hours a month, 10 branches per project, sleeps after 5 minutes | $0 |
| Launch | Pay as you go, no monthly minimum since December 2025 | $0.106 per compute-hour, $0.35 per GB-month, $1.50 per extra branch-month |

A compute-hour (CU-hour) is one hour of Neon's smallest unit of processor and memory, so 100 CU-hours is roughly 400 hours at the quarter-unit size. The binding limit for this project is the 0.5 GB of storage, not compute. Document A budgets Neon at $0 now and $10 to $20 later, inside the $200 ceiling.

Source: /Users/siddharth/.claude/projects/-Users-siddharth-Downloads/edcdeb19-7793-4e1b-9e73-4cf6186716bf/tool-results/bo0hrclp7.txt, sections 2.1 and 2.2 (2026-09); /Users/siddharth/Valuation/docs/read-this-first.md, section 12 (2026-09-14)

## Learn it

All free. Hours are the estimates in the research reports.

| # | Resource | Format | Hours | Why |
|---|---|---|---|---|
| 1 | https://www.postgresql.org/docs/current/tutorial.html | Official tutorial | 3 | Tables, queries and joins from zero; short and authoritative |
| 2 | https://www.postgresql.org/docs/current/ddl-constraints.html | Official docs | 1 | NOT NULL, CHECK and foreign keys; the chapter that protects your valuations |
| 3 | https://neon.com/docs/introduction/branching | Official docs | 1 | What a branch is and how to make one per pull request |
| 4 | https://neon.com/docs/get-started/signing-up | Official guide | 0.5 | Account, first project, where the SQL editor lives (open in M1, not today) |
| 5 | https://orm.drizzle.team/docs/tutorials/drizzle-with-neon | Official tutorial | 2 | Define a table in TypeScript, generate SQL, run it against Neon |
| 6 | https://neon.com/docs/guides/drizzle-migrations | Official guide | 1.5 | The one that matters most: versioned schema changes on Neon |

Source: /Users/siddharth/.claude/projects/-Users-siddharth-Downloads/edcdeb19-7793-4e1b-9e73-4cf6186716bf/tool-results/bj0fbejiq.txt, CHECK 3 section 7 table; bkm2kob5x.txt, learning path section 6 (2026-09)

Read 1 and 2 before the exercise. Do 3 to 6 in the week Document A's schedule opens the Neon account.

## 10-minute exercise

This needs the Neon account from Document A, section 10, item 4, opened in M1. Until then, read the SQL and predict each result. With the account, open your project in the Neon Console, create a branch called `scratch` so nothing touches `main`, then open the SQL Editor (the SQL Editor is in the left sidebar of the Neon Console) and run the blocks one at a time.

Block 1 builds a tiny fact table with the two rules from this chapter.

```sql
CREATE TABLE practice_fact (
  id            serial PRIMARY KEY,
  company       text    NOT NULL,
  field         text    NOT NULL,
  value         numeric NOT NULL CHECK (value >= 0),
  vintage_id    text    NOT NULL,
  license_class text    NOT NULL
    CHECK (license_class IN ('public_domain', 'damodaran_public', 'open_access',
                             'asr_youtube', 'licensed_personal',
                             'proprietary_personal', 'link_only'))
);
```

Block 2 inserts a good row: the Almarai example's risk-free rate, stamped with its vintage.

```sql
INSERT INTO practice_fact (company, field, value, vintage_id, license_class)
VALUES ('Almarai', 'riskfree', 0.0458, 'ginzu-2026-01', 'damodaran_public');
```

Block 3 leaves out the vintage. Predict what happens, then run it.

```sql
INSERT INTO practice_fact (company, field, value, license_class)
VALUES ('Almarai', 'mature_erp', 0.0423, 'damodaran_public');
```

You should see an error like `null value in column "vintage_id" ... violates not-null constraint`. The wording may differ by version. Nothing was written. That refusal is the whole point of Document A, section 3.2.

Block 4 tries to smuggle in a number with a made-up license class.

```sql
INSERT INTO practice_fact (company, field, value, vintage_id, license_class)
VALUES ('Almarai', 'tax_rate', 0.2517, 'ginzu-2026-01', 'bloomberg');
```

You should see `violates check constraint "practice_fact_license_class_check"`. The database does not know or care that the string means Bloomberg; it only knows the string is not one of the seven.

Block 5 checks what survived, then cleans up.

```sql
SELECT * FROM practice_fact;
DROP TABLE practice_fact;
```

Exactly one row should come back. Delete the `scratch` branch afterward so it does not count toward the ten.

Source for the numbers: /Users/siddharth/.claude/projects/-Users-siddharth-Downloads/edcdeb19-7793-4e1b-9e73-4cf6186716bf/tool-results/bkdrkpfng.txt, lines 23 and 90, and section 6 for the 25.17% India new-regime tax rate (2026-09)

## Done when

- You can explain table, row, column, NOT NULL and CHECK to a friend in one minute, and say why the Postgres rows are the system of record and the search index is not.
- You ran the exercise and saw two refusals and one surviving row, or you predicted all three outcomes correctly while reading.
- You can name the three 2026 risk-free rates, say which file each comes from, and explain why a run must store three vintage ids.
- You can state which two connection strings go in `.env`, which one the migrations use, and what SNI has to do with a failed connection.
- You know that a Bloomberg reading note is `proprietary_personal`, that a book is `link_only`, and that neither ever reaches the index.
