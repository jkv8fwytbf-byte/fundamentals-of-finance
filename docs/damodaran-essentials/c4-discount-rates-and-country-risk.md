# Chapter 4: Discount Rates and Country Risk

This chapter is about one number: the cost of capital. Chapter 3 showed where it sits in the DCF chain and how it glides toward a terminal rate. This chapter opens the number up and shows the parts inside it. Each part has a source table, a formula in the workbook, and a trap. Every concept ends with one line on why it matters for the calculator.

## The map in one block

The cost of capital is the blended return that lenders and owners together demand from a company. Damodaran calls it a hurdle rate, because a project must clear it to add value. It mixes a cost of equity and a cost of debt by market-value weights.

```
Cost of equity      = risk-free rate + levered beta x equity risk premium
Pre-tax cost of debt = risk-free rate + company default spread + country default spread
After-tax cost of debt = pre-tax cost of debt x (1 - marginal tax rate)
Cost of capital     = E/(D+E) x cost of equity + D/(D+E) x after-tax cost of debt
```

Every symbol in that block is a section below. The risk-free rate appears twice, so an error there travels everywhere.

Source: /Users/siddharth/Downloads/financeMD/damodaran/blog/2026/02/data-update-5-for-2026-risk-and-hurdle.md (2026-02); bkdrkpfng.txt section 2.6

## The risk-free rate

A risk-free rate is the return on an investment whose payoff you know for certain. In practice it is the yield on a long-term government bond. Damodaran's rule is that the bond must be in the currency of your cash flows, and the government must be close to default-free. A currency is a unit of measurement, like meters versus feet. Pick one, and the risk-free rate, the growth rate and the cash flows all live in it.

Source: /Users/siddharth/Downloads/financeMD/damodaran/pdfiles/country/val2dayIndia2025.md, slides 28 to 30 (2025); bkdrkpfng.txt section 6

### Stripping out the default spread

Most governments are not default-free. A default spread is the extra yield a borrower pays because it might not repay. Damodaran's fix is to subtract the country's default spread from the bond yield. His India session shows a 2025 example: an Indian bond yield of 6.32%, a default spread of 2.16% at the Baa3 rating, so a rupee risk-free rate of 4.16%.

Source: /Users/siddharth/Downloads/financeMD/damodaran/pdfiles/country/val2dayIndia2025.md, slide 29 (2025)

### The 2025 US downgrade and the 0.22%

On May 16, 2025, Moody's lowered the United States from Aaa to Aa1. It had been the last agency still rating the US at the top grade. By his own rule the treasury rate is no longer a pure risk-free rate. So his calculators now show two versions: the conventional one on the treasury rate, and an adjusted one that nets out the Aa1 default spread. The September 2026 calculator carries that spread as 0.22%, with a treasury rate of 4.75% and an adjusted dollar risk-free rate of 4.53%. His July 2025 India slide used 0.27%, so the spread itself moves from vintage to vintage.

Source: /Users/siddharth/Downloads/financeMD/damodaran/pc/implprem/ERPSept26.md, "Impl premium calculator" sheet (2026-09); /Users/siddharth/Downloads/financeMD/damodaran/pdfiles/country/val2dayIndia2025.md, slide 29 (2025)

### Three rates in one year

The 2026 files hold three US risk-free rates: 3.95%, 4.58% and 4.75%. Each belongs to a different dated table, called a vintage. The workbook hard-codes 4.58% inside two formulas on the cost-of-capital sheet. That is why every run in our system will store three vintage ids: the market file, the country-risk file and the industry file.

Source: /Users/siddharth/Valuation/docs/read-this-first.md section 3.2 (2026-09); bkdrkpfng.txt section 7, note 3; bafb6h9rb.txt

### The India rule and a cross-check

For an Indian company valued in rupees, the risk-free rate is the 10-year government bond yield minus India's default spread. Otherwise sovereign risk is counted twice, because the cost of debt adds that spread back later. When you distrust the bond yield, take the dollar risk-free rate and add the expected inflation gap. His February 2026 post uses IMF forecasts of 2.24% for the US and 4.00% for India, a gap of 1.76%. If the two routes disagree by a lot, an input is stale.

Source: /Users/siddharth/Valuation/docs/read-this-first.md section 3.4 (2026-09); /Users/siddharth/Downloads/financeMD/damodaran/blog/2026/02/data-update-5-for-2026-risk-and-hurdle.md (2026-02)

Why it matters for the calculator: the risk-free rate is an input with a currency and a vintage attached, never a bare number, and the India module subtracts the default spread before anything else runs.

## The equity risk premium

The equity risk premium, or ERP, is the extra annual return investors demand for owning the stock market instead of the risk-free bond. It is the price of risk for the whole market. There are two ways to measure it, and Damodaran spent a career arguing for the second.

### Historical versus implied

The historical premium is the average past gap between stock returns and bond returns. At the start of 2026 it ranged from 5.5% to 14.5%, depending on the period, the averaging method and the risk-free choice. He lists three problems. It looks backward. It is noisy, with large standard errors. And it moves the wrong way, falling after a crash because the bad year drags the average down.

Source: /Users/siddharth/Downloads/financeMD/damodaran/blog/2026/03/the-price-of-risk-equity-risk-premium.md (2026-03)

The implied premium looks forward. Think of a bond: you know its price and its coupons, so you can solve for the yield. He does the same for the S&P 500. Take the index level, the cash returned through dividends and buybacks, and an expected growth rate. Solve for the discount rate that makes the present value equal the index level. That rate is the expected return on stocks. Subtract the risk-free rate, and the remainder is the implied ERP. In Excel he uses Goal Seek, which is a root finder.

Source: /Users/siddharth/Downloads/financeMD/damodaran/pc/implprem/ERPSept26.md, "Impl premium calculator" sheet (2026-09)

### The September 2026 numbers

| Input or output, start of September 2026 | Value |
|---|---|
| S&P 500 level | 7686.14 |
| Cash yield (dividends plus buybacks, trailing 12 months) | 2.63% |
| Expected earnings growth, next five years | 13.99% |
| 10-year treasury rate | 4.75% |
| Implied expected return on stocks | 8.84% |
| Implied ERP over the treasury rate | 4.09% |
| Adjusted dollar risk-free rate (4.75% minus 0.22%) | 4.53% |
| Implied ERP over the adjusted rate | 4.31% |

For scale, the same sheet lists the historical US premium at 5.61%, the average implied premium of the last decade at 5.08%, and the average since 1960 at 4.25%.

Source: /Users/siddharth/Downloads/financeMD/damodaran/pc/implprem/ERPSept26.md (2026-09); /Users/siddharth/Downloads/financeMD/damodaran/pc/implprem/ERPbymonth.md, row 2026-09-01 (2026-09)

### What "mature market premium" means after the downgrade

Until 2025 the US implied ERP was his mature-market premium, because the US was Aaa. Now he starts from the US premium and removes the piece that belongs to US sovereign risk. His country-risk file states the January 2026 arithmetic as 4.61% minus 0.23% times 1.52, which gives 4.23%. Two honest footnotes. That subtraction does not compute exactly (4.61% minus 0.35% is 4.26%). And his ERP spreadsheet for the same month shows 4.23% as the S&P 500 premium over the unadjusted T-bond of 4.18%, with 4.46% over the adjusted 3.95%. His files disagree on the derivation, not on the number the workbook uses. Code the workbook's 4.23%, and store which file it came from. The July 2026 update starts at 4.42%, nets out 0.22%, and lands on 4.20%. The workbook keeps the mature premium in one cell, and that cell drives every country premium and the terminal cost of capital.

Source: /Users/siddharth/Downloads/financeMD/damodaran/pc/datasets/ctryprem.md, "Explanation" rows (2026-01); /Users/siddharth/Downloads/financeMD/damodaran/blog/2026/07/country-risk-drivers-measures-and.md (2026-07); bkdrkpfng.txt section 3.2

Chapter 6 covers the other use of this number, reading what the market is pricing in.

Why it matters for the calculator: the ERP is refreshed monthly and the mature premium quarterly, so the engine will read both from the vintage tables and never keep either as a constant in code.

## The country risk premium

A country risk premium, or CRP, is the extra premium for equity in a riskier country, added on top of the mature-market premium. Damodaran builds it in three steps.

1. Start with the sovereign rating. A rating is an agency's letter grade for a government's ability to repay, such as Baa3 for India.
2. Convert the rating to a default spread using his ratings-to-spreads table. A CDS spread, which is the price of insuring the bond, is a market-based alternative that exists for only 84 countries.
3. Scale the spread up, because stocks are more volatile than government bonds. The scalar is the volatility of an emerging-market equity index divided by the volatility of an emerging-market government bond index. It was 1.52 in January 2026 and 1.55 in July 2026.

The total ERP for a country is the mature premium plus its CRP. His India teaching example: a 2% default spread, Sensex volatility of 21%, bond volatility of 14%, so a CRP of 3.00%.

Source: /Users/siddharth/Downloads/financeMD/damodaran/blog/2026/07/country-risk-drivers-measures-and.md (2026-07); /Users/siddharth/Downloads/financeMD/damodaran/pc/datasets/ctryprem.md (2026-01); /Users/siddharth/Downloads/financeMD/damodaran/pdfiles/country/val2dayIndia2025.md, slide 45 (2025)

### India, two vintages

| Item | January 2026 vintage | July 2026 vintage |
|---|---|---|
| Moody's rating | Baa3 | Baa3 |
| Adjusted default spread | 1.87% | 1.75% |
| Mature-market ERP | 4.23% | 4.20% |
| Country risk premium | 2.85% | 2.72% |
| Total ERP for India | 7.08% | 6.92% |

Same rating, different numbers, six months apart. The spread table moved and the scalar moved. A run that takes the July ERP with the January industry table has mixed two vintages without noticing.

Source: bafb6h9rb.txt section 1 (ctryprem.xlsx and ctrypremJuly26.xlsx); /Users/siddharth/Downloads/financeMD/damodaran/pc/datasets/ctryprem.md, India row (2026-01)

### Where the company operates, not where it is registered

He argues that exposure comes from where a company earns, not where it is registered. The workbook offers four ERP choices: type it in, use the country of incorporation, weight by operating countries, or weight by operating regions. The weights are revenue shares. He notes revenues suit consumer companies, production suits natural-resource companies, and a mix suits manufacturers. Almarai, the golden case, uses region weights and gets a blended ERP of 5.58% rather than the Saudi premium.

Source: /Users/siddharth/Downloads/financeMD/damodaran/blog/2026/07/country-risk-drivers-measures-and.md (2026-07); bkdrkpfng.txt section 2.6; /Users/siddharth/Downloads/financeMD/damodaran/pc/fcffsimpleginzu.md, "Cost of capital worksheet" (2026-02)

Why it matters for the calculator: the country table is a dated file of about 200 rows looked up by name, and the revenue-weighted option needs a segment table the memo writer will extract from the filing.

## Betas

A beta measures how much a stock moves when the whole market moves. A beta of 1 moves with the market, 0.5 moves half as much. In the cost-of-equity formula it scales the ERP for one company.

### Regression betas are noisy

The textbook way is to regress the stock's past returns on the market's past returns. Damodaran's verdict is blunt: regression betas "will almost always be either too noisy or skewed by estimation choices". The standard error, the statistical uncertainty around the slope, can be as large as the estimate. The result also shifts with the index, the period and the return interval you picked.

Source: "/Users/siddharth/Downloads/financeMD/Aswath Damodaran - Investment Valuation, University Edition _ Tools and Techniques for Determining the Value of Any Asset (2023).md", chapter 8, "Bottom-Up Betas" (2023)

### Bottom-up betas

The fix is averaging. Find the companies in the same business, average their regression betas, and strip out their debt to get an unlevered beta. An unlevered beta is the beta the business would have with no debt. If a company is in several businesses, weight the business betas by value, or by revenue if value is unavailable. Then add back the company's own debt. The arithmetic: if each firm's beta has a standard error of 0.50 and there are 100 firms, the average has a standard error of 0.05.

Source: same book, chapter 8, "The Case for Bottom-Up Betas" (2023)

### Unlevering, relevering, and cash

Debt makes equity riskier, so a beta must be adjusted for how much debt sits under it. The formula, usually called the Hamada equation, is the one the workbook uses.

```
Levered beta   = unlevered beta x (1 + (1 - tax rate) x Debt/Equity)
Unlevered beta = levered beta / (1 + (1 - tax rate) x Debt/Equity)
```

Debt and equity are at market value. Cash has a beta near zero, so a company with a lot of cash looks safer than its business is. His industry tables carry an "unlevered beta corrected for cash" column, which divides by one minus cash as a share of firm value. That is the column the workbook reads.

For Almarai the workbook takes the US industry unlevered beta of 0.469, a market debt-to-equity ratio of 39,954 over 311,888, and a 25% tax rate. That produces a levered beta of 0.515.

Source: bkdrkpfng.txt section 2.6; /Users/siddharth/Downloads/financeMD/damodaran/pc/datasets/betaIndia.md, "Explanation" rows (2026-01); /Users/siddharth/Downloads/financeMD/damodaran/pc/fcffsimpleginzu.md, "Cost of capital worksheet" (2026-02)

### Industry averages and the India fallback

His industry betas average each firm's 2-year and 5-year weekly regression betas, with the 2-year beta weighted two thirds. The workbook ships only US and Global tables of 94 industries each. India has its own table over the same 94 industries, built from 5,170 companies, but it is thin in places. Software (System and Application) has 82 firms and a cash-corrected unlevered beta of 0.91. Air Transport has 5 firms. Utility (General) has none. When an Indian industry has fewer than 10 firms, true for 27 of the 94, the engine will use the emerging-markets table, then Global, and print which one it used.

Source: /Users/siddharth/Downloads/financeMD/damodaran/pc/datasets/betaIndia.md (2026-01-05); bafb6h9rb.txt sections 3 and 4; /Users/siddharth/Valuation/docs/read-this-first.md section 3.4 (2026-09)

Why it matters for the calculator: beta will come from a lookup keyed on industry name and vintage, relevered with the company's own market debt-to-equity, and the output will state the tier that supplied it.

## The cost of debt

The cost of debt is the rate the company would pay today to borrow long-term. Not the coupon on old bonds, and not interest expense divided by book debt. It is the risk-free rate plus the company's default spread plus the country's default spread.

### Synthetic ratings from interest coverage

Most companies have no bond rating. Damodaran plays the rating agency himself with one ratio: interest coverage, which is operating income divided by interest expense. Higher coverage means interest is paid more comfortably. He maps coverage bands to ratings and spreads in three tables: large non-financial firms, smaller and riskier firms, and financial-service firms. The table choice is the "type of firm" input.

Almarai's coverage is 3,060.9 over 493.4, or 6.20. In the smaller-firm table that is A2/A with a 0.7751% spread. Add the Saudi default spread of 0.51% and the 4.58% risk-free rate, and the synthetic cost of debt is 5.8651%. The workbook's chosen route for Almarai is an actual rating of A1/A+, spread 0.7003%, giving 5.2803%. The actual-rating formula adds no country spread. The golden test must match that behavior, and the audit will flag it.

Source: bkdrkpfng.txt sections 2.6 and 3.4; /Users/siddharth/Downloads/financeMD/damodaran/pc/fcffsimpleginzu.md, "Synthetic rating" sheet (2026-02)

### Two special cases

Negative operating income sends coverage below every band and returns a D rating. The sheet warns not to use that as a going-concern cost of debt and suggests BB instead. Missing interest expense is the opposite trap. The formula sets coverage to one million when interest is zero, which awards Aaa. That is harmless for a company with no debt, because debt then has no weight. It is wrong for a company with debt that did not break out interest in the filing. The plan lists "interest missing" as an audit field, so the engine will record the gap instead of quietly rewarding it.

Source: bkdrkpfng.txt section 3.4; /Users/siddharth/.claude/plans/help-me-out-here-abstract-wilkinson.md section 10.2 (2026-09)

Why it matters for the calculator: the rating module is three banded tables plus a country lookup, and the 2026 spreads run from 0.40% at Aaa to 19% at D.

## Weights, and the four approaches

Weights must be market values, not book values. Book value is the accounting record of what was raised long ago. Market value is what the claims are worth today, which is what a discount rate is about. Equity is shares times price. Most debt does not trade, so the workbook treats book debt as one bond: interest expense is an annuity over the average maturity, book value is the final repayment, both discounted at the pre-tax cost of debt.

Almarai's pieces come together like this. Cost of equity is 4.58% plus 0.515 times 5.58%, or 7.45%. After-tax cost of debt is 5.2803% times 0.75, or 3.96%. Market equity is 311,888 and market debt is 39,954, so the weights are 88.6% and 11.4%. The cost of capital is 7.055%, the rate Chapter 3 carried through years 1 to 5.

Source: /Users/siddharth/Downloads/financeMD/damodaran/pc/fcffsimpleginzu.md, "Cost of capital worksheet" (2026-02); bkdrkpfng.txt section 2.6

The worksheet lets you reach that number four ways.

| Approach | What it does | When he uses it |
|---|---|---|
| I will input | You type the cost of capital | Reverse engineering, or a quick pass |
| Detailed | Builds it from the parts above | The default for a real valuation |
| Industry Average | Reads the industry cost of capital from the US or Global table | Young firms, or as a cross-check |
| Distribution | Picks a decile (a cut point that splits all firms into tenths) or quartile (quarters) from the histogram of all firms in a region | Firms whose risk is in flux |

The last two carry a hidden conversion. The industry tables are in US dollars at the vintage's risk-free rate. The sheet adds your risk-free rate minus 4.58% to bring the figure up to date and into your currency. The India cost-of-capital table also publishes a local-currency column: 10.92% for the whole market against 8.28% in dollars, and 12.67% against 9.99% for Software (System and Application).

Source: bkdrkpfng.txt section 2.6; /Users/siddharth/Downloads/financeMD/damodaran/pc/datasets/waccIndia.md (2026-01-05)

Why it matters for the calculator: the engine will store each table's embedded risk-free rate next to the table, so the conversion is "your rate minus the table's rate", never a literal 4.58%.

## Plausibility bands

His most-used table is the histogram of costs of capital for all 48,156 firms in his sample. He uses it as a starting input for young firms, as a plausibility check on other people's work, and as a reminder not to spend the day polishing the fourth decimal.

| Region, start of 2026, US dollars | First decile | Median | Ninth decile |
|---|---|---|---|
| US | 5.26% | 7.79% | 9.88% |
| Global | 6.28% | 8.65% | 11.66% |
| Emerging markets | 6.65% | 8.95% | 12.55% |

His rule of thumb: 80% of US companies sit between 5.26% and 9.88%, and 80% of global companies between 6.28% and 11.66%. A dollar cost of capital of 14% for a listed US company "goes on my suspect list". A small, newly listed AI firm might start at 11.66% and drift toward 8.65%. For rupee valuations, add the 1.76% inflation gap to every band first.

Source: /Users/siddharth/Downloads/financeMD/damodaran/blog/2026/02/data-update-5-for-2026-risk-and-hurdle.md (2026-02); /Users/siddharth/Downloads/financeMD/damodaran/pc/fcffsimpleginzu.md, "Cost of capital worksheet", distribution table (2026-02)

Why it matters for the calculator: the diagnostics step will compare each run's cost of capital against these bands, in the right currency, and raise a warning outside the first-to-ninth decile range.

## Where this comes from

Go deeper in this order. Paths are under /Users/siddharth/Downloads/financeMD/ unless shown in full.

- damodaran/blog/2026/02/data-update-5-for-2026-risk-and-hurdle.md: risk measures, hurdle rates, and the 2026 cost-of-capital histogram with the plausibility bands.
- damodaran/blog/2026/03/the-price-of-risk-equity-risk-premium.md: historical versus implied ERP, the 2008 daily series, and the three lessons.
- damodaran/blog/2026/07/country-risk-drivers-measures-and.md: the full country-risk method, the 1.55 scalar, and the case for operating exposure over incorporation.
- damodaran/pc/implprem/ERPSept26.md and ERPbymonth.md: the implied-ERP calculator and the monthly series the regime layer will load.
- damodaran/pc/datasets/ctryprem.md and ctrypremJuly26.md: the country tables, the "Explanation" rows on the mature premium, and the relative volatility sheet.
- damodaran/pc/datasets/betaIndia.md and waccIndia.md: the India industry tables with firm counts, cash-corrected betas, and the local-currency column.
- damodaran/pdfiles/country/val2dayIndia2025.md, slides 28 to 52: risk-free rates in rupees, the CRP arithmetic, and lambda, taught in India.
- The 2023 book at the corpus root, chapters 7 and 8: standard errors on historical premiums, and the case for bottom-up betas.
- damodaran/pc/fcffsimpleginzu.md, the "Cost of capital worksheet", "Synthetic rating" and "Country equity risk premiums" sheets: the formulas the engine must reproduce.

## Three things to remember

1. The cost of capital is five inputs, and four of them come from dated tables: the risk-free rate, the mature ERP, the country spread and the industry beta. A run without its three vintage ids is not a run.
2. Strip default risk out of the risk-free rate and add it back only in the cost of debt and the country premium. Counting it twice is the most common India error.
3. Do not polish the number; check it. Bottom-up betas beat regressions, the implied ERP beats history, and a result outside his deciles is a signal to reread the inputs, not a discovery.
