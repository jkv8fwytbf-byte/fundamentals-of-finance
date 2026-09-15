# The Other Side: Read Me First {#r3-orientation}

::: {.reading-only .read-first}
**Read this after the essentials.** The aim is to understand where the method can mislead you and how to recognize the limits of its evidence.
:::

This folder is the critics reader. It collects the best arguments against Aswath Damodaran and against the valuation method your system copies. It also collects his own admissions, with the numbers. The point is not to knock him down. The point is to make sure you [never mistake a model for the truth]{.reading-highlight}.

A note on sources. Every paragraph in this folder ends with a "Source" line. "Report" means the local research file at /Users/siddharth/Desktop/Valuation/docs/sources/bkm2kob5x.txt, compiled 2026-09-14. "blog/" means the folder /Users/siddharth/Downloads/financeMD/damodaran/blog/. "Survey" means the corpus survey at /Users/siddharth/Desktop/Valuation/docs/sources/bfxevcj1s.txt. Where the Report used the live web, the chapter says so.

## Why a critics reader exists

Your system will produce a number for a company. That number will look precise. A critics reader is the antidote to that false precision. Think of it as the list of known side effects printed on a medicine box. You still take the medicine. You just take it with your eyes open.

Damodaran is the best-known teacher of intrinsic valuation. Intrinsic valuation means estimating what a business is worth from its own cash flows, growth, and risk. The main tool is the discounted cash flow model, or DCF. A DCF forecasts future cash and shrinks it back to today using a discount rate. Your engine is a DCF, built from his public spreadsheet. So his weaknesses are your weaknesses, inherited at birth.

Source: Report, introduction and Part 1 (2026-09-14).

## The honesty rule

This reader follows one rule. Every miss is reported with its numbers, and every win is reported too. The Report puts it plainly: a reader that only lists defeats is propaganda, not research. You should distrust any document that breaks this rule, including this one.

Source: Report, Part 4, honourable mention (2026-09-14).

### What he got right, in short

- The 2020 COVID series. Between 26 February 2020 and 5 November 2020 he published fourteen posts titled "A Viral Market Meltdown". All fourteen are in your local corpus. He kept valuing companies through the crash. He published the implied equity risk premium as it moved, reaching 6.01% on 1 April 2020. He refused to switch to pricing multiples. He purchased shares during the drawdown.
- The 2020 series also contains data against his own camp. On 24 April 2020 he wrote that the market was punishing low-PE, high-dividend stocks more than high-PE non-payers. His words: "That is disappointing news for value purists." He published evidence that hurt his own tribe.
- WeWork, 2019. Two posts, at blog/2019/11/the-softbank-wework-end-game-savior.md and blog/2019/09/insights-on-vc-pricing-lessons-from.md, called the private valuation wrong before the collapse.
- Tesla, on method. In June 2019 he wrote that ARK's projection was "a forward pricing for Tesla, not a valuation". His price calls on Tesla were wrong for years. That methodological objection has aged well.
- Uber, on conduct. When Bill Gurley beat his Uber estimate in 2014, he emailed Gurley to say he loved the post. Then he re-ran his own model on Gurley's story and published both spreadsheets. Losing well is a skill, and he has it.

Source: Report, Parts 2.5, 2.9, 3.8 and 4 (2026-09-14); blog/2020/04/a-viral-market-update-vii-mayhem-with.md (2020-04-24); blog/2019/06/teslas-travails-curfew-for-corporate.md (2019-06-03); blog/2014/07/possible-plausible-and-probable-big.md (2014-07-16).

## The gaps in the local corpus

Your local blog mirror holds 803 markdown files. The years present are 2008 to 2011, 2013 to 2024, and 2026. Two years are missing: 2012 and 2025. The Survey confirms the gap is in the original crawl, not just the copy. It estimates the hole at roughly 55 to 65 posts, including the entire 2025 data-update series.

Source: Report, corpus gap warning and "Local files used" (2026-09-14); Survey, lines 32 and 281 (2026-09-14).

Those two holes matter for this reader. The Facebook IPO valuation was published in February 2012. The Nvidia markdown after DeepSeek was published on 31 January 2025. Both episodes are cited in Chapter 2 from the live web, not from your files. If you build a chat feature over this corpus, it will confidently invent answers about those two years unless you backfill them first.

Source: Report, corpus gap warning (2026-09-14).

There is a second gap. Damodaran's own "Dark Side of Valuation" material exists as three free PDF decks on his website. All three are image-heavy scanned decks. A normal PDF-to-text pass does not extract clean text from them. They need OCR, which means optical character recognition, software that reads letters from pictures. Chapter 1 lists the three links.

Source: Report, Part 1, free sources table and ingestion note (2026-09-14).

There is a third, smaller warning. One widely cited free copy of the main academic critique lives at a domain called ivc-forum.org. That link now redirects to an unrelated website. Chapter 3 gives the safe alternatives. Do not put the stale link in any crawl list.

Source: Report, Part 3.1, link hygiene (2026-09-14).

## How to read this document

The reader has seven chapters. The first four are the critique itself; the last three are the scorecard, the reading list, and what it all means for your product.

| Chapter | File | What it holds | Read it when |
|---|---|---|---|
| 0 | 00-read-me-first.md | The rules, the gaps, the glossary | Now |
| 1 | 01-his-own-dark-side.md | His own book, in ten claims, plus the free decks | Before you touch the model |
| 2 | 02-his-misses-with-numbers.md | Tesla, Nvidia, Amazon, Apple, Uber, Facebook, Zomato, Paytm, Bitcoin | When your model output feels too certain |
| 3 | 03-academic-and-practitioner-critiques.md | The formal attacks on the method, and the live 2026 debates | When you choose an input and wonder if it is real |
| 4 | 04-twelve-episodes.md | Twelve public disagreements, dated, with outcomes | When you want the scorecard in one table |
| 5 | 05-reading-order.md | Seventeen sources, ordered for a beginner | When you are ready to read the critics themselves |
| 6 | 06-what-this-means-for-the-app.md | The design rules the critiques force on the app | Before the first line of code |

Three reading tips. First, every table in Chapter 2 compares his published value with the market price on the same day. Value is his estimate. Price is what people paid. The gap between them is the whole story. Second, stock splits change the numbers you see today. A split divides one share into several, so old prices look bigger than new ones. Chapter 2 shows the conversion each time. Third, do not skip the "his own words afterwards" sections. His admissions are the most valuable lines in the corpus.

Source: Report, Part 2 (2026-09-14).

A note on language. This folder reports what he and his critics did with their own money as history. It never recommends any action. Your system has the same rule, and a test scans every output for recommendation language. When a critic's published estimate is quoted, it is quoted as a historical fact about that critic.

Source: /Users/siddharth/Desktop/Valuation/docs/plan.md, section 10.1, "No advice" (2026-09-14).

## Terms you will meet

| Term | Plain meaning |
|---|---|
| Intrinsic value | What a business is worth from its own cash flows, growth, and risk |
| Price | What the market paid on a given day; it can move with mood, value cannot |
| DCF | Discounted cash flow model; forecast cash, then shrink it back to today |
| Discount rate | The yearly haircut applied to future cash; higher risk means a bigger haircut |
| Risk-free rate | The return on a government bond assumed to carry no default risk |
| Equity risk premium (ERP) | The extra return investors demand for owning stocks instead of that bond |
| Implied ERP | The ERP that makes the market's current price equal to its expected cash flows |
| Country risk premium (CRP) | An extra premium added for operating in a riskier country |
| Beta | A number describing how much a stock moves with the whole market |
| CAPM | Capital asset pricing model; cost of equity equals risk-free rate plus beta times ERP |
| Terminal value | The value of all cash flows beyond the forecast years, folded into one number |
| TAM | Total addressable market; the size of the whole market a company could serve |
| Sales-to-capital ratio | Revenue generated per dollar of capital invested; sets how much growth costs |
| Failure probability | The chance the firm dies before reaching stable growth; used to trim the DCF |
| Stock split | Dividing one share into several; the company is unchanged, per-share numbers shrink |
| Sum-of-the-parts | Valuing each business unit separately, then adding them |
| Monte Carlo | Running the model thousands of times with random inputs to get a range |
| Reverse DCF | Starting from the price and solving for the assumptions it requires |
| PE ratio | Price divided by earnings per share; a quick gauge of how expensive a stock is |
| Pricing multiple | A shortcut that values a company by comparing a ratio such as price-to-earnings with peers, instead of forecasting cash flows |

Source: Report, Parts 1 to 3 (2026-09-14). The definitions are written in plain English for this reader.

## The one sentence to remember

The Report's thesis is one line from the AQR section. Being right on value and early is, over any investable horizon, indistinguishable from being wrong. Every table in Chapter 2 is an example of that sentence. Every critique in Chapter 3 is a reason it keeps happening.

Source: Report, Part 3.7 (2026-09-14).
