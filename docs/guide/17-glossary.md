# Chapter 17. Glossary: every term in the guide and Document A, in plain words {#r4-glossary}

::: {.reading-only .optional}
**Your lookup chapter.** When a term interrupts your reading, find it here and return to the passage. No need to read the glossary straight through.
:::

## What it is (plain words and an analogy)

A glossary is an alphabetical list of terms, each with a short definition. This one covers the words used across the guide and Document A. It extends the glossary in Document A section 15 and never contradicts it. Where a term has a full chapter, the entry here is the short version and names the chapter.

The analogy is a phrase book you carry in a foreign country. You do not learn the language from it. You use it to stop being stuck, and then you go back to the lesson.

Source: /Users/siddharth/Desktop/Valuation/docs/read-this-first.md, section 15 (2026-09-14)

## Why this tool now (for this project)

Two vocabularies arrive at once: software words like "migration" and finance words like "sales to capital". Each chapter defines its terms once, but the definitions are scattered across seventeen chapters and Document A. One searchable page saves you from re-reading a chapter to recover one word. It also keeps a memo, a database column and a chapter meaning the same thing by "vintage".

## How it is used in this project

- The glossary uses the same names as the code and the database. `vintage` and `licence_class` are column names, not only ideas.
- When Cursor, a memo or a Damodaran post uses a word that is not here, look it up, then add it through a pull request, as chapter 1 shows.
- Entries about milestones after M0 say "will". Nothing beyond M0 is built yet.

## The glossary

Terms are alphabetical. Numbers sort before letters. A source line sits under each block.

### 3 to C

- **3P test.** Damodaran's filter for a story: possible means it could happen, plausible means it could reasonably happen, probable means you would put weight on it today. Only the probable story sets the base case. See Document C chapter 1.
- **Batch mode.** Sending many model requests together and accepting a slower answer in exchange for a lower price. GLM-5.3-Flash in batch mode will do bulk cleaning at $0.075 in and $0.25 out per million tokens.
- **Beta.** A number that says how much a stock tends to move when the whole market moves. The engine uses an industry average, re-levered for the company's debt.
- **Bias.** The average signed error of estimated value against a later price, across many valuations. Positive bias means the values ran too high on average.
- **Branch.** In git, a parallel draft of the code. In Neon, a parallel copy of the whole database.
- **CI.** Continuous integration. Checks that run automatically on every pull request, and `main` cannot change unless they pass.
- **Commit.** One saved snapshot of the files in a repo, with a short message. Chapter 1's analogy: putting the pencil down and dating the margin.
- **Context window.** The amount of text a model can hold during one call, measured in tokens. A sub-agent gets its own.
- **Cost per task.** The dollars a model needs to finish one benchmark task. It maps to your bill better than price per token, because reasoning tokens are billed as output.
- **Country risk premium (CRP).** The extra return demanded for a company's exposure to a riskier country, added on top of the mature-market ERP. India, January 2026 vintage: CRP 2.85%, total ERP 7.08%.
- **Crawler.** A program that starts at one page and follows links to list a whole site. A search API returns ranked pages for a question; a scraper fetches one known page.

Source: /Users/siddharth/Desktop/Valuation/docs/damodaran-essentials/c1-why-value-story-and-the-3p-test.md; /Users/siddharth/Desktop/Valuation/docs/read-this-first.md sections 3.1, 3.4, 4.1, 6 and 15; /Users/siddharth/Desktop/Valuation/docs/guide/01-git-github-and-pull-requests.md; /Users/siddharth/Downloads/financeMD/damodaran/New_Home_Page/definitions.md, row "Beta (CAPM)"; /Users/siddharth/Desktop/Valuation/docs/sources/bj0fbejiq.txt, CHECK 3 sections 3, 4 and 5; bafb6h9rb.txt India rows (2026-09-14)

### D to H

- **Deploy.** Putting a new version of code where it actually runs. Here it means merging to `main` so the nightly robots use the new code, and applying any migration to Neon. The local reports do not define this word; this is general usage.
- **Diff.** The list of exact lines added and removed by a change. Chapter 0 says read the diff, not the summary.
- **Embedding.** A list of numbers that places a passage in a space where similar meanings sit close together. Also called a vector.
- **ERP (equity risk premium).** The expected return on the stock market minus the risk-free rate. It is multiplied by beta to get the cost of equity.
- **FCFF.** Free cash flow to the firm: after-tax operating income minus reinvestment. "To the firm" means before any debt payments, so it belongs to lenders and shareholders together.
- **Golden test.** A test that pins a known-correct answer so any drift is caught. Here the engine must reproduce Almarai's value per share, 7.187840270062114, within 0.000001.
- **Harness.** The scaffolding around a model: prompt, tools, loop, permissions and interface. Cursor is a harness; the model inside it is not.

Source: /Users/siddharth/Desktop/Valuation/docs/read-this-first.md sections 3.1 and 15; /Users/siddharth/Desktop/Valuation/docs/guide/00-how-to-learn-with-an-ai-tool.md; /Users/siddharth/Downloads/financeMD/damodaran/New_Home_Page/definitions.md, rows "Equity Risk Premium (ERP)" and "Free Cash Flow to Firm (FCFF)"; /Users/siddharth/Desktop/Valuation/docs/sources/bkdrkpfng.txt (2026-09-14)

### I to M

- **Implied ERP.** The ERP solved backwards from today's index level, expected cash flows and the risk-free rate. September 2026: 4.09%, with an expected return on US stocks of 8.84%.
- **Judge model.** A model used to grade another model's answers during evaluations. Kimi K3 will be the judge here, and the judge must never be the model being judged.
- **Licence class.** Our label on every stored fact saying what you may do with it. Seven classes exist, three are refused from the librarian's index, and the column is spelled `licence_class` in code.
- **LoRA.** Low-Rank Adaptation: fine-tuning by training a small adapter on top of frozen weights, which is why it is cheap. It changes form, not facts, and is not part of v1.
- **MCP.** Model Context Protocol, the standard plug that lets Cursor call our tools.
- **Migration.** A versioned script that changes the database's structure, checked into git and applied in order. It is the database equivalent of a commit.
- **Model router.** One service that forwards a request to any of many models under one key and one bill. OpenRouter is the router here.
- **Monte Carlo.** Drawing each uncertain input many times from a range, running the calculator each time, and looking at the spread of results. The ranges come from Damodaran's own industry quartiles.

Source: /Users/siddharth/Desktop/Valuation/docs/read-this-first.md sections 2, 3.3, 3.5, 4.1 and 15; /Users/siddharth/Desktop/Valuation/docs/damodaran-essentials/c6-relative-valuation-and-what-the-market-prices-in.md; /Users/siddharth/Downloads/financeMD/damodaran/New_Home_Page/definitions.md, row "Equity Risk Premium - Implied"; /Users/siddharth/Downloads/financeMD/damodaran/pc/implprem/ERPbymonth.md; /Users/siddharth/Desktop/Valuation/docs/sources/bj0fbejiq.txt, CHECK 3 sections 1c and 7 (2026-09-14)

### N to R

- **OCR.** Optical character recognition: turning a picture of text into text. Mistral will do it once, for three image-only lecture decks.
- **Open-weight.** A model whose weights are public, so many hosts can serve it. Every runtime model here is open-weight.
- **PR (pull request).** A request to merge a branch into `main`, shown as a diff with a comment thread.
- **Pricing versus valuing.** Pricing asks what the crowd pays for similar assets today, using multiples. Valuing asks what cash flows, growth and risk are worth; the system shows both side by side, never blended.
- **Repo.** A folder of code with its full history, hosted on GitHub.
- **Reranker.** A second, slower model that reads the question and each candidate passage together and re-scores the top results.
- **Reverse DCF.** Solving the valuation backwards: what growth or margin does today's price require?
- **Risk-free rate.** The return on an investment with no default risk, and the base of every discount rate. For rupees it is the 10-year government bond yield minus India's default spread.

Source: /Users/siddharth/Desktop/Valuation/docs/read-this-first.md sections 2, 3.4, 4 and 15; /Users/siddharth/Desktop/Valuation/docs/guide/01-git-github-and-pull-requests.md; /Users/siddharth/Desktop/Valuation/docs/damodaran-essentials/c6-relative-valuation-and-what-the-market-prices-in.md; /Users/siddharth/Desktop/Valuation/docs/sources/bj0fbejiq.txt, CHECK 3 sections 2 and 6 (2026-09-14)

### S to Z

- **Sales to capital.** Revenue produced per unit of capital invested. The workbook divides next year's extra revenue by it to get this year's reinvestment; Almarai's default, 1.7085, is an industry average.
- **Sub-agent.** A helper AI session spawned by another to do one sub-task in its own context window. It hands back a short summary.
- **Synthetic rating.** A bond rating estimated from interest coverage, meaning operating income divided by interest expense. It sets the company's default spread inside the cost of debt.
- **Terminal value.** One number that stands for every cash flow after year 10: terminal cash flow divided by terminal cost of capital minus terminal growth. The terminal cost of capital is the risk-free rate plus the mature-market ERP, whatever the sheet label says.
- **Token.** A word piece, roughly four characters. Models are billed per token, separately for what you send in and what they write out.
- **Variance.** The spread of the error between estimated value and later price. Bias says which way the estimates lean; variance says how wide they scatter.
- **Vector index.** The store that holds embeddings and finds the nearest ones to a question. Pinecone will hold about 60,000 passage vectors here.
- **Vintage.** Which dated snapshot of Damodaran's tables a number came from. Every run stores three vintage ids: market, country risk and industry.
- **WACC.** Weighted average cost of capital: the cost of equity and the after-tax cost of debt, weighted by market values. It is the rate that discounts FCFF.
- **Zero data retention.** A provider's promise not to store your prompts and outputs. It is a required setting on OpenRouter.

Source: /Users/siddharth/Desktop/Valuation/docs/damodaran-essentials/c3-the-dcf-chain.md, stations 4, 6 and 7; /Users/siddharth/Desktop/Valuation/docs/sources/bkdrkpfng.txt, synthetic rating and terminal cost of capital notes; /Users/siddharth/Desktop/Valuation/docs/read-this-first.md sections 2, 3.2, 4.1, 6, 10 and 15; /Users/siddharth/Downloads/financeMD/damodaran/New_Home_Page/definitions.md, row "Cost of Capital"; bj0fbejiq.txt CHECK 3 section 4 (2026-09-14)

## Learn it

| # | Resource | Format | Hours | Why |
|---|---|---|---|---|
| 1 | Damodaran's definitions page, local copy at /Users/siddharth/Downloads/financeMD/damodaran/New_Home_Page/definitions.md (live page on pages.stern.nyu.edu, verify the link) | Table, one row per term | 1 | His own one-line definitions of beta, ERP, FCFF, WACC and reinvestment rate, with a "why it matters" column |
| 2 | Document C chapters 1, 3 and 6 in /Users/siddharth/Desktop/Valuation/docs/damodaran-essentials/ | Markdown chapters | 3 | The full versions of the finance entries above, worked through on Almarai |
| 3 | https://docs.github.com/en/get-started/learning-about-github/github-glossary | Reference page | 0.5 | Official definitions of repo, branch, commit, PR, merge and check |
| 4 | https://www.pinecone.io/learn/series/rag/ | Course, free | 3 | Embeddings, chunks, vector index and reranker explained in order, with code |
| 5 | https://artificialanalysis.ai/methodology/intelligence-benchmarking | Methodology page | 1 | Where cost per task, tokens and the index numbers in Document A section 4.1 come from |
| 6 | https://www.postgresql.org/docs/current/tutorial.html | Official tutorial | 3 | Tables, rows and constraints, the ground under migration, branch and licence class |

Source: /Users/siddharth/Desktop/Valuation/docs/sources/bj0fbejiq.txt, CHECK 3 resource tables in sections 5, 6 and 7 (2026-09-14). Resource 3 is from general web knowledge, not covered by the local reports.

## 10-minute exercise

::: {.reading-only .optional}
**For the practical stage.** Use this exercise when working on this chapter's tool. The following "Done when" checklist tells you how to judge completion.
:::

1. Open the valuation chain board, https://www.figma.com/board/SNaMV0lrKHeDRQgelrbPsp, or the PNG at /Users/siddharth/Desktop/Valuation/docs/diagrams/png/valuation-chain.png.
2. Pick five boxes on the board. Without opening this file, write one sentence for each term in your decisions log from chapter 0.
3. Open this file and compare. Mark each of your five as "same meaning", "close" or "wrong".
4. Find one word on the board, or in Document A, that this glossary lacks. Write its entry in the same style, on a branch, and open a PR titled `docs: add <term> to glossary`.

## Done when

::: {.reading-emphasis .key-idea}
- You can say what vintage, licence class and golden test mean, out loud, in under fifteen seconds each.
- You can explain the difference between pricing and valuing, and between bias and variance, without the file open.
- At least one term you found missing has been merged into this chapter through a PR with passing checks.
- You have not written any sentence that tells a reader what to do with a stock in any entry you added.
:::
