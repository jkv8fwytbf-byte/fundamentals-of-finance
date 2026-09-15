# Section 7: Vendor scorecard and the accounts to create {#r5-vendors}

::: {.reading-only .optional}
**For choosing and opening accounts.** Refer to the scorecard and setup checklist when you reach that stage.
:::

## The scorecard: are they the best at what they do?

**In short.** A vendor is a company whose service the system will rent, such as a database or an AI model. Plan section 7 lists 14 roles, one pick each, the runners-up, and why the pick wins. Free tiers come first; paid lines appear only where nothing free is good enough.

- Coding tool: Cursor Pro. Already paid; its diff review (every change shown before you accept it) and Plan mode let a beginner learn instead of copying blindly. Runner-up: Cline, the free bench.
- Database: Neon, a hosted Postgres, the widely used open-source database. An idle database costs nothing, and cheap copies called branches allow safe experiments. Runner-up: Supabase Pro.
- Vectors: Pinecone Starter. A vector is a list of numbers that stands for the meaning of a text, so a vector store searches by meaning; free up to 2 GB (plan section 7). Runner-up: pgvector, an add-on that stores vectors inside Neon itself.
- Embeddings and rerank: Voyage. An embedding model turns text into a vector, and a reranker re-sorts search hits so the best come first; 200 million free tokens (plan section 7). Runner-up: Cohere Rerank 3.5.
- Model router: OpenRouter. A router is one account and one key that reaches many AI models, and OpenRouter alone enforces zero-data-retention routing, so the provider keeps no copy of your prompts. Runner-up: Vercel AI Gateway.
- Models: GLM-5.3 for memos and answers, GLM-5.3-Flash batch for bulk work, Kimi K3 as judge, a second model that grades the first (plan section 7). GLM has the lowest hallucination rate, the rate of confident false statements, among strong open-weight models; DeepSeek V4 Pro is excluded for a 94% rate (plan section 7). Runner-up: DeepSeek V4.1 Flash.
- Dashboard and notebooks: Hex, Community free, later Professional at $36 per month (plan section 7). The only tool within budget with SQL against Neon, real Python, charts and private sharing. Runner-up: Deepnote at $39 (plan section 7).
- Observability and evals: Langfuse Hobby. Observability records every model call so you can see what happened; evals are tests that score model output. Open source, with evals free. Runner-up: Braintrust.
- Job runner: GitHub Actions, the robot that runs code on a schedule or after each change. The code already lives there, so the pipeline does not depend on the editor vendor. Runner-up: Inngest.
- Raw file storage: Cloudflare R2. 10 GB free with zero egress, the fee some vendors charge to read files back out (plan section 7). Runner-up: Backblaze B2.
- OCR: Mistral Document AI 4.1. OCR turns a scanned page image into text; batch price $2 per 1,000 pages, and best on the only independent 2026 OCR benchmark at 74.9%, tables 94.3% (plan section 7). Runner-up: Reducto.
- Web search, optional: Parallel. Top on quality, bottom on cost in the AA Search Index of 2026-08-18 (plan section 7). Runner-up: Exa; Tavily is rejected.
- India fundamentals: EODHD at $59.99 per month (plan section 7). Fundamentals are the financial statement numbers, and EODHD alone documents long-history Indian statements in one tidy schema. Runner-up: indianapi.in.
- India prices and your holdings: INDstocks API from INDmoney, free, or Kite Connect at 500 rupees (plan section 7). Official and read-only; scraping the app is forbidden. Runner-up: NSE bhavcopy files.

> **Comment**
> **What it means for you:** Fourteen roles, fourteen picks, all chosen already (plan section 7); you will not compare vendors yourself.
> **Decision needed:** none, already decided in the plan.
> **Money:** Cursor Pro $20 per month, already paid; every other line is $0 today, and the full stack later runs about $120 to 200 per month under a $200 ceiling (plan section 6).
> **When:** M0, me, done today 2026-09-14; the paid lines switch on later, EODHD only from M4, weeks 4 to 8.

**Read more.** 4-the-guide.pdf, "Chapter 7. OpenRouter and benchmark literacy: one door to every model, and how to read the scoreboard", explains the model picks, and its "Chapter 9. Data sources: where every number comes from, and what you may do with it" covers the India feeds.

## Accounts to create, in order

**In short.** An account is a login at one vendor, and most come with an API key, a long secret string that lets code act as you. Each key will live in a `.env` file, a private text file on your computer, and in GitHub Actions secrets, the locked drawer the nightly robot reads from. Two-factor authentication (2FA) is a second check at login, usually a code from your phone. Plan section 7 lists 12 rows in order; the table restates them, and 1-read-this-first.pdf, section 10, has the click-by-click version.

| # | Vendor | Plan | Dollars per month (plan section 7) | What it is for | Security note |
|---|---|---|---|---|---|
| 1 | GitHub, plus a free organization | Free | 0 | Code, history, nightly robot | 2FA on; recovery codes kept offline; root of trust |
| 2 | Cursor, your existing account | Pro | 20 | Editor you type into | Privacy Mode on; never paste keys into its BYOK settings |
| 3 | OpenRouter | Pay-as-you-go | 30 to 70 | One key, many models | Spend limit $75; logging off; zero-data-retention routing on; 2FA |
| 4 | Neon | Free, later Launch | 0 to 20 | Database holding every number | Sign up with email and password, not only GitHub; 2FA |
| 5 | Pinecone | Starter | 0 | Search by meaning | 2FA |
| 6 | Voyage | Free | 0 | Turns text into vectors | Billing alert before the free grant ends |
| 7 | Cloudflare | Free, R2 | 0 | Raw filings and decks | Hardware key or TOTP; token scoped to one bucket, the named folder that holds the files |
| 8 | Langfuse | Hobby | 0 | Records every model call | 2FA |
| 9 | Mistral | Pay-as-you-go | about 2, one-off | Scanned pages into text | Use the batch endpoint, the cheaper queue for jobs that need not finish immediately |
| 10 | Hex | Community | 0, later 36 | Private dashboard over Neon | Private workspace; Neon connection set inside Hex |
| 11 | EODHD, from M4 | Fundamentals | 60 | Indian financial statements | Read the redistribution clause; test 20 NSE tickers free first |
| 12 | Optional: INDstocks API, Kite Connect, Parallel, Braintrust | Various | 0, about 6 (500 rupees), about 18, 0 | India prices, news search, evals | Broker tokens expire daily, so plan a re-login step |

BYOK means "bring your own key", and TOTP is a time-based one-time password, the six-digit code from an authenticator app. Plan section 7 puts Mistral at about $2 one-off for the account, while plan section 6 budgets about $10 one-off for all the scanning work.

> **Comment**
> **What it means for you:** In M1 you will open the free accounts (GitHub, Neon, Pinecone, Voyage, Cloudflare, Langfuse, Hex), plus OpenRouter and Mistral, which are pay-as-you-go, name one project `valuation` at each, and paste each key into `.env` and GitHub Actions secrets (plan section 5).
> **Decision needed:** decision 3, yes or no to opening those accounts, taken in M1 after you say "go"; decision 1, go or wait, comes first, after you read PDF 1 and PDF 2.
> **Money:** the first OpenRouter purchase is $20 of credits with a $75 spend limit (plan section 6); Cursor Pro $20 per month is already paid; everything else in M1 is $0.
> **When:** M1, you, 3 evenings, starts only when you say "go".

**Read more.** 1-read-this-first.pdf, "10. The accounts you will create, in order", walks through every screen. 4-the-guide.pdf, "Chapter 2. Cursor and Cline: the tool you type into, and the free bench beside it", covers row 2 and the free bench.

## Hygiene

**In short.** Hygiene here means the small habits that keep secrets out of the shared code and limit the damage if one leaks, like keeping the spare key with a neighbor rather than under the mat. Plan section 7 sets five rules.

- Never commit `.env`. To commit is to save a file into the repo's permanent history, so a committed secret is a leaked secret. Commit `.env.example` instead, the same file with every value blank.
- Use a distinct email alias per vendor, an extra address that lands in your normal inbox, so a leak is traceable and one stolen login does not open the rest.
- Set hard spend caps at OpenRouter, Mistral and Parallel, so a runaway job stops at the cap.
- Rotate the GitHub token and the OpenRouter key every 90 days (plan section 7); rotating means issuing a new key and deleting the old one.
- Create a Neon branch before any migration the AI agent proposes. A migration changes the shape of the database tables, and a branch is a cheap copy, so a bad one can be thrown away.

> **Comment**
> **What it means for you:** Five habits, none technical; four are one-time settings in M1, and the fifth is a reflex whenever an agent proposes a database change.
> **Decision needed:** none, already decided in the plan.
> **Money:** none; the caps exist to protect the $200 per month ceiling (plan section 6).
> **When:** M1, you, 3 evenings after "go", for the first four; the Neon branch rule starts in M2, me, days 3 to 7 after go, and stays for good.

**Read more.** 4-the-guide.pdf, "Chapter 14. Security hygiene for a solo builder", covers every rule, and 1-read-this-first.pdf, "12. Budget at up to $200 a month", shows where the spend caps sit.
