# Chapter 7: India and the Rules of Thumb {#r2-india}

::: {.reading-only .key-idea}
**Notice what changes when the country changes.** Use the six steps and the rules-of-thumb page to keep currency, risk, tax and peer-table choices straight.
:::

## What this chapter is

Chapter 3 walked the DCF chain with Almarai, in Saudi riyals. Chapter 6 covered pricing. This chapter changes the country. Damodaran's claim is that the first principles do not change when you cross a border. What changes is a short list of inputs: the currency, the risk-free rate, the risk premium, the tax rate, and the peer tables. In his words, "the first principles of valuation are the same in all markets". Get those five inputs right and the rest of the chain runs unchanged. The chapter ends with his rules of thumb, gathered from across the corpus.

Source: /Users/siddharth/Downloads/financeMD/damodaran/blog/2021/07/the-zomato-ipo-bet-on-big-markets-and.md (2021-07-22)

## Step 1: pick a currency and keep it

A currency is a unit of measurement, like meters or kilograms. It is not a source of risk. You can value an Indian company in rupees (INR) or in US dollars (USD). Both are correct if you are consistent, meaning every input is in the same currency: revenues, debt, cash, the risk-free rate, the growth rate, the share price, and the share count. The workbook has only two per-share cells, the price and the number of shares. Everything else is in whole-company currency units. The sheet warns explicitly about mixing millions with a raw share count. Indian filings add a second trap. They report in crore or lakh, and one crore equals ten million (a definition, not a corpus number). Convert once, at the door, and never again.

Source: /Users/siddharth/.claude/projects/-Users-siddharth-Downloads/edcdeb19-7793-4e1b-9e73-4cf6186716bf/tool-results/bkdrkpfng.txt, sections 6 and 7 (2026-09)

The currency choice also sets the terminal growth rate. The workbook's default is that growth in perpetuity equals the risk-free rate. In INR, that means the INR risk-free rate. Do not import a 2.5% dollar growth number into a rupee model. Do not import a 7% rupee growth number into a dollar model. The packet's rule for nominal cash flows is that "the growth rate should be nominal in the currency in which the valuation is denominated". For the calculator, this will become a single field, `currency`, stamped on every run, and a test will check that the growth cap uses the same currency's risk-free rate.

Source: /Users/siddharth/Downloads/financeMD/valpacket1spr25.md, slide 202 (Spring 2025); /Users/siddharth/.claude/projects/-Users-siddharth-Downloads/edcdeb19-7793-4e1b-9e73-4cf6186716bf/tool-results/bkdrkpfng.txt, section 1.6 (2026-09)

## Step 2: the INR risk-free rate

A risk-free rate is the return on an investment with no chance of default. A government bond only qualifies if the government is close to default-free. India is rated Baa3 by Moody's, which is not that. So the 10-year Indian government bond yield, the G-sec yield, contains a default spread. A default spread is the extra yield lenders charge for the chance of not being repaid. His fix is subtraction: INR risk-free rate equals the 10-year G-sec yield minus India's default spread. The reason is double counting. The cost of debt already adds the country default spread. If the risk-free rate also carried it, sovereign risk would be counted twice.

Source: /Users/siddharth/Downloads/financeMD/damodaran/pdfiles/country/val2dayIndia2025.md, slide 29 (2025); /Users/siddharth/Valuation/docs/read-this-first.md, section 3.4 (2026-09)

His own India examples, all from the same seminar slide:

| Case | Year | Rating and spread | G-sec yield | INR risk-free rate |
|---|---|---|---|---|
| Tata Motors | 2010 | Ba2, 3.00% | 8.00% | 5.00% |
| Vedant | 2025 | Baa3, 2.16% | 6.32% | 4.16% |

In the Zomato posts he used 4.25% for July 2021 and 4.78% for July 2022, both after the same subtraction. When a currency has no trusted long bond, he uses inflation instead: the USD risk-free rate scaled by the ratio of expected local inflation to expected US inflation. His illustration, with a 4% dollar rate and 4% local inflation against 2.5% US inflation, gives 5.52%. That formula is also a sanity check on a G-sec yield you do not trust.

Source: /Users/siddharth/Downloads/financeMD/damodaran/pdfiles/country/val2dayIndia2025.md, slides 29 and 31 (2025); /Users/siddharth/Downloads/financeMD/damodaran/blog/2022/07/a-zomato-2022-update-value-pricing-and.md (2022-07-27)

Why it matters for the calculator: from milestone 4 the RBI 10-year G-sec yield will be hand-entered monthly as a `market` vintage row, and the engine will subtract the India default spread from the `country risk` vintage. Two vintages, one number, both ids stored on the run.

Source: /Users/siddharth/.claude/plans/help-me-out-here-abstract-wilkinson.md, M4 (2026-09)

## Step 3: the equity risk premium, mature plus country

The equity risk premium (ERP) is the extra return investors demand for holding stocks instead of the risk-free asset. For an Indian company, Damodaran builds it in two layers. Layer one is the mature-market ERP. Since the US lost its Aaa rating he computes it as the implied US ERP minus the Aa1 default spread. On 2026-07-01, with the S&P 500 at 7499.36, that was 4.42% minus 0.22%, giving 4.20%. Layer two is the country risk premium (CRP). He takes India's default spread and scales it up by the volatility of emerging-market stocks relative to emerging-market bonds, a ratio of 1.55 in July 2026. Total ERP for India is mature ERP plus CRP.

Source: /Users/siddharth/Downloads/financeMD/damodaran/blog/2026/07/country-risk-drivers-measures-and.md (2026-07-15)

The two 2026 vintages the calculator will store:

| Vintage | Moody's rating | Default spread | Mature ERP | CRP | Total India ERP |
|---|---|---|---|---|---|
| January 2026 | Baa3 | 1.87% | 4.23% | 2.85% | 7.08% |
| July 2026 | Baa3 | 1.75% | 4.20% | 2.72% | 6.92% |

The older seminar illustration uses the same logic with rounder numbers: a 2% default spread times 21 over 14, the Sensex volatility over Indian bond volatility, gives a 3% CRP.

Source: /Users/siddharth/.claude/projects/-Users-siddharth-Downloads/edcdeb19-7793-4e1b-9e73-4cf6186716bf/tool-results/bafb6h9rb.txt, section 1 (2026-09); /Users/siddharth/Downloads/financeMD/damodaran/pdfiles/country/val2dayIndia2025.md, slide 45 (2025)

One refinement matters for Indian names. Country risk comes from where a company operates, not where it is incorporated. His seminar pairs Tata Motors, with 91.37% of 2009 revenues in India, against TCS, with 7.62%. The workbook offers three ERP choices: country of incorporation, operating countries weighted by revenue, or operating regions weighted by revenue. Why it matters for the calculator: default to country of incorporation, but store revenue weights when the filing gives them, so an IT exporter is not charged full India risk.

Source: /Users/siddharth/Downloads/financeMD/damodaran/pdfiles/country/val2dayIndia2025.md, slide 52 (2025); /Users/siddharth/.claude/projects/-Users-siddharth-Downloads/edcdeb19-7793-4e1b-9e73-4cf6186716bf/tool-results/bkdrkpfng.txt, section 2.6 (2026-09)

## Step 4: the tax rate

The workbook needs two tax rates. The effective rate is what the company actually paid last year, read from its own tax note. The marginal rate is the statutory rate on the next rupee of profit. The chain fades one into the other over years 6 to 10, as Chapter 3 explained. For India the marginal rate is a choice, not a lookup, because Indian companies can elect a regime:

| Regime | Marginal rate |
|---|---|
| New regime (22% plus surcharge and cess; cess is an extra levy charged as a percentage of the tax itself) | 25.17% |
| Old regime | 34.94% |
| New manufacturing companies | 17.16% |

The country table inside the workbook shows 30% for India. That column is never read by any formula. It is information, not an input. Why it matters for the calculator: `marginal_tax_rate` will be a typed field with those three options, never copied from the country table.

Source: /Users/siddharth/.claude/projects/-Users-siddharth-Downloads/edcdeb19-7793-4e1b-9e73-4cf6186716bf/tool-results/bkdrkpfng.txt, sections 3.2 and 6 (2026-09)

## Step 5: industry averages and the fallback

The workbook ships two peer tables, US and Global, each with 94 industries. There is no India table inside it. Damodaran does publish India averages as separate files, 29 families over the same 94 industry names, built from 5,170 Indian companies. The catch is thinness. An average of three firms is not an average, it is three anecdotes. Counting from his beta file, 27 of the 94 Indian industries have fewer than 10 firms:

| Firms | Industries |
|---|---|
| 0 | Utility (General) |
| 1 | Homebuilding, Oil/Gas (Integrated), Precious Metals, Reinsurance, Retail (REITs), Utility (Water) |
| 2 | Insurance (General), Semiconductor Equip |
| 3 | Insurance (Prop/Cas.), Retail (Building Supply), Transportation (Railroads) |
| 4 | Software (Entertainment), Telecom (Wireless) |
| 5 | Air Transport, Beverage (Soft), Coal & Related Energy, R.E.I.T. |
| 6 | Banks (Regional), Software (Internet) |
| 7 | Oil/Gas (Production and Exploration), Tobacco |
| 8 | Cable TV, Chemical (Diversified) |
| 9 | Drugs (Biotechnology), Electronics (Consumer & Office), Insurance (Life) |

Why it matters for the calculator: the rule is India first, then emerging markets, then Global, switching whenever the row has fewer than 10 firms. The tier actually used will be written on every run as `industry_tier_used`, so a memo can say "peer margins are global, because only five Indian airlines exist".

Source: /Users/siddharth/Downloads/financeMD/damodaran/pc/datasets/betaIndia.md (2026-01-05); /Users/siddharth/.claude/projects/-Users-siddharth-Downloads/edcdeb19-7793-4e1b-9e73-4cf6186716bf/tool-results/bafb6h9rb.txt, sections 2 and 3 (2026-09); /Users/siddharth/Valuation/docs/read-this-first.md, section 3.4 (2026-09)

## Step 6: dollar-based averages and the inflation differential

Most of Damodaran's industry averages are computed in US dollars. Ratios travel across currencies without change: a margin, a sales-to-capital ratio, or a beta is the same number in INR and USD. Rates do not travel. A cost of capital or a growth rate carries the inflation of its currency inside it. The workbook says so next to the price cell: "If you are not working in US dollars, you should add the inflation differential to the industry averages."

Source: /Users/siddharth/Downloads/financeMD/damodaran/pc/fcffsimpleginzu.md, Input sheet note (valuation date 2026-02-01)

The workbook handles the cost of capital itself. Its industry-average and distribution approaches add the difference between your risk-free rate and 4.58%, the dollar risk-free rate of that vintage. The emerging-market distribution it offers is 7.63% at the first quartile, 8.95% at the median and 10.69% at the third quartile, all in dollars before that adjustment. His India file shows the full conversion for the whole market: 8.28% in dollars becomes 10.92% in rupees, using 5% expected INR inflation and 2.5% expected US inflation. The arithmetic is one plus the dollar rate, times one plus INR inflation, divided by one plus US inflation, minus one. Why it matters for the calculator: growth averages pulled from a dollar table will get the same treatment before they touch an INR run, and the rule will be logged. Margins pass through untouched.

Source: /Users/siddharth/.claude/projects/-Users-siddharth-Downloads/edcdeb19-7793-4e1b-9e73-4cf6186716bf/tool-results/bkdrkpfng.txt, sections 2.6 and 6 (2026-09); /Users/siddharth/Downloads/financeMD/damodaran/pc/datasets/waccIndia.md (2026-01-05)

## His Indian cases, as published estimates

These are estimates he published, with the prices of the day. They show the method, nothing about the companies now.

### Zomato, July 2021

Zomato is a food-delivery platform that listed in July 2021. His story: the Indian food-delivery market reaches about 25 billion dollars in ten years, Zomato holds about 40% of it, keeps 22% of order value as revenue, and its operating margin trends toward 30%. He assigned a 10% probability of failure and used a rupee cost of capital that carried India's country risk. The value of equity came to about 394 billion INR, or 41 INR per share. The IPO price was 76 INR. He then replaced three point inputs with ranges in a simulation: market size from 10 to 40 billion dollars, share from 20% to 50%, margin from 15% to 45%. He noted that market size and share moved the value far more than the cost of capital did.

Source: /Users/siddharth/Downloads/financeMD/damodaran/blog/2021/07/the-zomato-ipo-bet-on-big-markets-and.md (2021-07-22)

### Zomato, July 2022

A year later the price had peaked at 169 INR and fallen to 41.65 INR. He refused to call the fall a vindication, for three reasons worth copying. First, he also published a Paytm estimate that ended far above the price. Second, an intrinsic value should itself grow at the cost of equity, so 41 INR in 2021 becomes about 46 INR in 2022. Third, the company and the macro picture had changed, so it had to be revalued. India's ERP had risen from 6.85% to 9.08% and the rupee risk-free rate from 4.25% to 4.78%, adding roughly 1.5 to 2 percentage points to the cost of capital. The revalued estimate was 35.32 INR, down from 40.79 INR, most of the drop coming from macro inputs.

Source: /Users/siddharth/Downloads/financeMD/damodaran/blog/2022/07/a-zomato-2022-update-value-pricing-and.md (2022-07-27)

### Paytm, October 2021

Paytm is a mobile-payments platform. Its take rate, revenue as a share of payment volume, had fallen from 2.18% in 2016-17 to 0.79% in 2020-21. His story: the take rate stays low, reaching 1% in 2026, then doubles to 2% as the focus shifts from users to revenues. Operating margin reaches 5% in 2026 and 30% in stable growth. The rupee cost of capital was 10.43%, just below the median Indian company. The failure probability was 5%. The value of equity came to about 1,500 billion INR, close to 2,000 INR per share, against an unlisted price of 2,950 INR. His simulation showed a 3% chance the equity was worth nothing and a 90th percentile above 2,000 billion INR. By July 2022 the stock traded at 713 INR.

Source: /Users/siddharth/Downloads/financeMD/damodaran/blog/2021/10/the-indian-smartphone-revolution-paytms.md (2021-10-04); /Users/siddharth/Downloads/financeMD/damodaran/blog/2022/07/a-zomato-2022-update-value-pricing-and.md (2022-07-27)

Why these matter for the calculator: they are the template for an Indian run. A story in five drivers, a rupee risk-free rate by subtraction, a country-loaded ERP, an explicit failure probability, and a range around the point. They also show why the accuracy scoreboard will store the estimate, the price and the vintages on the day, so later revisions are honest about what changed.

Source: /Users/siddharth/.claude/plans/help-me-out-here-abstract-wilkinson.md, M4 (2026-09)

### The 2025 India seminar themes

The two-day India seminar repeats the same frame with local cases. Its risk-free slide is the subtraction table above. Its country-risk slides argue that exposure comes from operations, not incorporation. Its stable-growth table is the clearest picture of a rule from Chapter 3: for Tata Motors, with return on capital equal to the cost of capital at 10.39%, the value stays at 435,686 million INR whether terminal growth is 0% or 5%. Growth adds nothing when the return on it only covers its cost. The seminar closes with the story-to-numbers steps, ending with "Keep the feedback loop open", and two warnings named "The Runaway Story" and "Willy Wonkitis", his labels for narratives that outrun any plausible market.

Source: /Users/siddharth/Downloads/financeMD/damodaran/pdfiles/country/val2dayIndia2025.md, slides 29, 52, 60 and 149 onward (2025)

## Rules of thumb, one page

::: {.reading-only .key-idea}
**Use this as your recap.** Return to the earlier chapters for the reasoning behind each rule.
:::

Each rule below is his, with where it comes from and what it becomes in the calculator.

| Rule | Where he says it | In the calculator (planned) |
|---|---|---|
| Terminal growth never exceeds the risk-free rate, in the same currency. The risk-free rate is inflation plus a real rate; nominal GDP growth is inflation plus real growth; a mature firm cannot outgrow the economy forever. | valpacket1spr25.md, slides 202 and 203 | A hard cap: `g_terminal <= rf` in the run's currency. A run that breaks it fails. |
| Return on capital converges to the cost of capital in stable growth. Excess returns fade because competition arrives. | val2dayIndia2025.md, slide 60; workbook default assumption 2 | Stable ROC defaults to the year-10 cost of capital. Overriding it is allowed but flagged. |
| A dollar cost of capital of 14% for a listed company is suspect. It sits above the 90th percentile for US firms. Eighty percent of US firms fall between 5.26% and 9.88%, global firms between 6.28% and 11.66%. | blog 2026/02, data update 5 | A diagnostics warning when the dollar-equivalent cost of capital leaves the 10th to 90th percentile band. |
| Time spent finessing the cost of capital is mostly wasted. Cash-flow drivers move value more. | blog 2026/02, data update 5; Zomato 2021 post | Sensitivity tables rank inputs by effect on value, so the memo talks about the ones that matter. |
| Separate valuing from pricing. A DCF gives value. Multiples give price. Never blend them into one number. | Chapter 6; Zomato 2021 post, "The Pricing Game" | Two tables in every memo, never a weighted average of the two. |
| Keep the feedback loop open. Listen to people who know the business, and work out the value of alternative narratives. | val2dayIndia2025.md, slide 149 | Every run keeps its story text, and a rerun with a changed story is stored next to the old one. |
| Do not trust a point estimate. Replace the three inputs you are least sure of with ranges and look at the distribution. | Zomato 2021 and Paytm 2021 posts | A Monte Carlo range (a simulation that draws each uncertain input from a range many times) built from his industry quartiles will ship with every valuation. |
| A currency is a unit. Pick one and stay consistent through the share count. | Model schema, section 6 | One `currency` field per run and a consistency test on every input. |
| Country risk comes from where you operate, not where you are incorporated. | val2dayIndia2025.md, slide 52; blog 2026/07 | Revenue-weighted ERP when weights exist; incorporation otherwise. |
| A big market is not a premium. The size is already inside growth and margin. The danger with big-market companies is an estimate that is too high, not too low. | Zomato 2021 post, "Big market delusion" | No premium fields exist. Market size enters only through revenue. |
| Your own scoreboard must record misses as loudly as hits. | Zomato 2022 post | The accuracy scoreboard will store every estimate against later prices. |

Source: /Users/siddharth/Downloads/financeMD/valpacket1spr25.md (Spring 2025); /Users/siddharth/Downloads/financeMD/damodaran/pdfiles/country/val2dayIndia2025.md (2025); /Users/siddharth/Downloads/financeMD/damodaran/blog/2026/02/data-update-5-for-2026-risk-and-hurdle.md (2026-02-05); /Users/siddharth/Downloads/financeMD/damodaran/blog/2021/07/the-zomato-ipo-bet-on-big-markets-and.md (2021-07-22); /Users/siddharth/Downloads/financeMD/damodaran/blog/2022/07/a-zomato-2022-update-value-pricing-and.md (2022-07-27); /Users/siddharth/.claude/projects/-Users-siddharth-Downloads/edcdeb19-7793-4e1b-9e73-4cf6186716bf/tool-results/bkdrkpfng.txt (2026-09)

## Where this comes from

- /Users/siddharth/Downloads/financeMD/damodaran/pdfiles/country/val2dayIndia2025.md, the two-day India seminar; slides 29 to 31 for risk-free rates, 45 to 52 for country risk, 60 for stable growth, 149 onward for story to numbers.
- /Users/siddharth/Downloads/financeMD/damodaran/blog/2021/07/the-zomato-ipo-bet-on-big-markets-and.md, the full Indian worked case, including the simulation and the big-market delusion.
- /Users/siddharth/Downloads/financeMD/damodaran/blog/2022/07/a-zomato-2022-update-value-pricing-and.md, how to revise an estimate honestly when macro inputs move.
- /Users/siddharth/Downloads/financeMD/damodaran/blog/2021/10/the-indian-smartphone-revolution-paytms.md, take rates, a rupee cost of capital, and a wide Monte Carlo range.
- /Users/siddharth/Downloads/financeMD/damodaran/blog/2026/07/country-risk-drivers-measures-and.md, the 2026 method for mature ERP and CRP, and why operations matter more than incorporation.
- /Users/siddharth/Downloads/financeMD/damodaran/blog/2026/02/data-update-5-for-2026-risk-and-hurdle.md, the cost-of-capital distribution and the 14% test.
- /Users/siddharth/Downloads/financeMD/valpacket1spr25.md, slides 202 and 203, the growth cap and the risk-free rate as nominal growth.
- /Users/siddharth/Downloads/financeMD/damodaran/pc/datasets/betaIndia.md and waccIndia.md, the India peer files, firm counts, and the rupee conversion.
- /Users/siddharth/.claude/projects/-Users-siddharth-Downloads/edcdeb19-7793-4e1b-9e73-4cf6186716bf/tool-results/bkdrkpfng.txt, section 6, the cell-by-cell edit list for an Indian run.
- /Users/siddharth/.claude/projects/-Users-siddharth-Downloads/edcdeb19-7793-4e1b-9e73-4cf6186716bf/tool-results/bafb6h9rb.txt, the dataset catalog with the India rows and vintages.

## Three things to remember

::: {.reading-emphasis .key-idea}
1. [Five inputs change for India]{.reading-highlight}, nothing else does: the currency, a risk-free rate found by subtracting the default spread from the G-sec yield, an ERP of mature plus country, a chosen marginal tax rate, and peer tables that fall back to emerging then Global below 10 firms.
2. [Rates carry inflation]{.reading-highlight} and ratios do not. Convert dollar costs of capital and growth rates with the inflation differential before they enter a rupee run. Margins, betas and sales to capital pass through as they are.
3. His Indian cases are templates, not verdicts. Zomato at 41 INR against an IPO price of 76, Paytm near 2,000 INR against 2,950, both published with ranges, both revisited in print. Store the estimate, the price and the vintages, then let the scoreboard judge.

Source: recap of figures sourced in Steps 2, 5 and the Indian cases above (bafb6h9rb.txt; blog 2021/07 Zomato IPO; blog 2021/10 Paytm).
:::
