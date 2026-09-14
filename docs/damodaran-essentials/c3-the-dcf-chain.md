# Chapter 3: The DCF Chain, Exactly As the Workbook Does It

## What this chapter is

A DCF (discounted cash flow) valuation is a way of putting a number on a business today. You forecast the cash the business will throw off each year. Then you shrink each year's cash to allow for waiting and for risk. The fcffsimpleginzu workbook does this in one fixed chain of steps. This chapter walks that chain in the order the spreadsheet computes it. Think of a conveyor belt with nine stations. Revenue goes in at one end. A value per share comes out at the other.

We follow one company through every station: Almarai, a Saudi food company, valued on 2026-02-01. It is the example that ships inside the workbook. Its answer, 7.187840270062114 per share against a share price of 72.28, is the golden test for your calculator. The calculator must reproduce that number to six decimals before it is trusted with anything else. All Almarai figures below are in millions of Saudi riyals, except the share count and the per-share numbers.

Source: /Users/siddharth/.claude/plans/help-me-out-here-abstract-wilkinson.md (2026-09); /Users/siddharth/Downloads/financeMD/damodaran/pc/fcffsimpleginzu.md (valuation date 2026-02-01)

## The grid you are filling in

The "Valuation output" sheet is a grid. One column is the base year, meaning the last twelve months of actual results. Ten columns are forecast years 1 to 10. One more column is the terminal year, the first year of "forever". Every station below fills one or two rows of that grid.

Almarai's starting inputs, as typed on the Input sheet:

| Input | Almarai value |
|---|---|
| Revenues, last twelve months | 21,765.4 |
| Operating income (EBIT) | 3,060.9 |
| Effective tax rate, then marginal tax rate | 17.5%, then 25% |
| Book value of debt | 45,063 |
| Cash and marketable securities | 19,000 |
| Cross holdings and other non-operating assets | 21,119 |
| Minority interests | 1,558 |
| Shares outstanding | 4,315 |
| Share price | 72.28 |
| Risk-free rate | 4.58% |
| Mature-market equity risk premium | 4.23% |
| Cost of capital, years 1 to 5 | 7.055% |
| Sales to capital ratio | 1.7085 |

EBIT means earnings before interest and taxes. It is the profit from running the business, before lenders and the tax office are paid. Every other term in the table gets defined at the station where it is used.

Source: /Users/siddharth/.claude/projects/-Users-siddharth-Downloads/edcdeb19-7793-4e1b-9e73-4cf6186716bf/tool-results/bkdrkpfng.txt, section 1 (2026-09)

## Station 1: the revenue growth path

Revenue is the money customers pay the company. The workbook needs only three growth inputs. Year 1 growth is cell B26. Growth for years 2 to 5 is cell B28, and it is one flat rate. Terminal growth is the growth rate in "forever", and by default it equals the risk-free rate (station 7 explains why). Years 6 to 10 are not typed at all. They glide from the year-5 rate to the terminal rate in five equal steps, so year 10 lands exactly on the terminal rate. Picture a plane descending on a straight glide path to the runway.

Almarai uses 5% for year 1 and 5% for years 2 to 5. The terminal rate is 4.58%. The step is (5% minus 4.58%) divided by 5, which is 0.084 percentage points a year. So years 6 to 10 grow at 4.916%, 4.832%, 4.748%, 4.664% and 4.580%. Revenue climbs from 21,765.4 to 22,853.7 in year 1, 27,778.8 in year 5, 35,030.0 in year 10 and 36,634.4 in the terminal year.

```
g_1        = B26
g_2 .. g_5 = B28
g_(5+k)    = g_5 - (g_5 - g_T) / 5 * k        for k = 1..5
Rev_t      = Rev_(t-1) * (1 + g_t)
Rev_T      = Rev_10 * (1 + g_T)
```

Why it matters for the calculator: compute all eleven revenue columns first, because station 4 looks one year ahead.

Source: bkdrkpfng.txt, section 2.2; /Users/siddharth/Downloads/financeMD/damodaran/pc/fcffsimpleginzu.md, "Valuation output" rows "Revenue growth rate" and "Revenues" (2026-02-01)

## Station 2: operating margin convergence

Operating margin is EBIT divided by revenue, the share of each sale left after operating costs. Three inputs control it. Year 1 margin (B27) defaults to the base-year margin. The target margin (B29) defaults to the year 1 margin. The year of convergence (B30) defaults to 5. Between year 1 and the convergence year, the margin moves in equal steps toward the target. After that year it stays at the target. Think of a thermostat set to a temperature and a fixed number of minutes to get there.

```
m_1 = B27
m_t = target - ((target - m_1) / Y) * (Y - t)    for t <= Y     (Y = B30, target = B29)
m_t = target                                     for t > Y
EBIT_t = m_t * Rev_t
```

Almarai's base margin is 3,060.9 divided by 21,765.4, which is 14.063%. The defaults were left untouched, so the margin line is flat at 14.063% in every year. EBIT is therefore just 14.063% of each year's revenue: 3,213.9 in year 1 and 4,926.3 in year 10.

Why it matters for the calculator: B27 and B29 are pre-filled formulas that the user is meant to overwrite. Store them as initial values, not permanent links.

Source: bkdrkpfng.txt, sections 1.3 and 2.3; fcffsimpleginzu.md, "Valuation output" rows "EBIT (Operating) margin" and "EBIT (Operating income)" (2026-02-01)

## Station 3: the tax fade

The effective tax rate is what the company actually paid, as a share of pre-tax profit. The marginal tax rate is the statutory rate on the next unit of profit. The workbook applies the effective rate for years 1 to 5. In years 6 to 10 the rate fades in five equal steps to the marginal rate. The terminal year uses the marginal rate. The logic is that tax breaks run out as a company matures.

Almarai pays 17.5% in years 1 to 5. The step is (25% minus 17.5%) divided by 5, which is 1.5 points a year. So years 6 to 10 are 19%, 20.5%, 22%, 23.5% and 25%. After-tax operating income, written EBIT(1-t), is 2,651.5 in year 1 and 3,694.7 in year 10.

There is also an NOL branch. NOL means net operating loss carryforward, a bank of past losses that shields future profit from tax. Losses are not taxed. If the NOL bank is bigger than this year's EBIT, no tax is paid. Otherwise only the excess is taxed. Almarai's NOL is zero in every year. The terminal year ignores the NOL bank.

Why it matters for the calculator: port both the linear fade and the NOL shield, because the model will meet loss-making companies.

Source: bkdrkpfng.txt, section 2.4; fcffsimpleginzu.md, "Valuation output" rows "Tax rate", "EBIT(1-t)" and "NOL" (2026-02-01)

## Station 4: reinvestment, or why growth is not free

Reinvestment is the money a company plows back to grow: new plants, more inventory, more credit extended to customers. Invested capital is the money already tied up in the business, measured as book equity plus book debt minus cash. The sales to capital ratio is revenue produced per unit of invested capital. A ratio of 2 means one riyal of capital supports two riyals of sales.

The workbook does not forecast capital spending line by line. It asks how much extra revenue you want next year, then divides by the sales to capital ratio. That is the capital you must put in this year. The one-year lag is the point: you build the shop before you sell from it.

```
Reinv_t = (Rev_(t+1) - Rev_t) / s2c_t        (default lag = 1)
InvCap_t = InvCap_(t-1) + Reinv_t
ROIC_t   = EBIT(1-t)_t / InvCap_(t-1)
```

Almarai year 1: (23,996.4 minus 22,853.7) divided by 1.7085 gives 668.8. By year 10 the figure is 939.0. Invested capital rises from 36,730.8 to 44,796.6. ROIC (return on invested capital, after-tax operating income divided by the prior year's capital) rises from 6.875% in the base year to 8.42% in year 10.

Now the catch. The default sales to capital ratio, 1.7085, is the Global industry average for Food Processing, pulled from a lookup table. Almarai's own ratio is 21,765.4 divided by 36,730.8, which is 0.59. The Diagnostics sheet prints both side by side. If you believed the company's own history, each unit of growth would cost nearly three times the capital the default assumes. Damodaran's own words on this: "Growth is not free and it has to be paid for with reinvestment".

Why it matters for the calculator: the lag switch accepts 0 to 3 years, there is no floor, and shrinking revenue produces negative reinvestment. Record that the default came from the Global table.

Source: bkdrkpfng.txt, sections 1.3, 2.5 and 4; fcffsimpleginzu.md, "Valuation output" rows "Reinvestment", "Invested capital", "ROIC" and "Diagnostics" step 4 (2026-02-01); /Users/siddharth/Downloads/financeMD/damodaran/blog/2016/11/myth-53-growth-is-good-more-growth-is.md (2016-11-30)

## Station 5: free cash flow to the firm

FCFF stands for free cash flow to the firm. It is after-tax operating income minus reinvestment. "To the firm" means before any debt payments, so it belongs to lenders and shareholders together. Damodaran's definitions page writes it as EBIT(1-t) minus net capital spending minus the change in working capital. The workbook collapses those last two items into the single reinvestment line from station 4.

Almarai's FCFF is 1,982.7 in year 1 and 2,755.7 in year 10. It grows more slowly than EBIT because the tax fade takes a bigger bite each year.

Why it matters for the calculator: FCFF is one subtraction per column. All the difficulty lives upstream.

Source: /Users/siddharth/Downloads/financeMD/damodaran/New_Home_Page/definitions.md, row "Free Cash Flow to Firm (FCFF)"; fcffsimpleginzu.md, "Valuation output" row "FCFF" (2026-02-01)

## Station 6: the cost of capital path and cumulative discount factors

The cost of capital, often called WACC, is the blended annual return that lenders and shareholders together require. Chapter 4 builds Almarai's starting figure of 7.055%. The workbook holds it flat for years 1 to 5. The terminal cost of capital is the risk-free rate plus the mature-market equity risk premium: 4.58% plus 4.23%, which is 8.81%. Years 6 to 10 glide there in five equal steps of 0.351 points: 7.406%, 7.757%, 8.108%, 8.459% and 8.81%. The idea is that a maturing company drifts toward the risk of an average company.

Because the rate changes each year, you cannot discount with one rate raised to a power. Instead the sheet keeps a cumulative discount factor. Each year's factor is last year's factor divided by (1 plus this year's rate). Almarai's factor is 1 divided by 1.07055, or 0.9341, in year 1, and 0.4816 in year 10. Present value of each year's FCFF is FCFF times that factor: 1,852.0 in year 1, 1,327.2 in year 10. The ten present values add up to 16,394.5.

```
CumDF_1 = 1 / (1 + WACC_1)
CumDF_t = CumDF_(t-1) / (1 + WACC_t)
PV_t    = FCFF_t * CumDF_t
```

Why it matters for the calculator: the Input sheet label says the terminal rate is "riskfree + 4.5%". The formula actually adds the mature-market premium from the Country ERP sheet. Code the formula, not the label.

Source: bkdrkpfng.txt, sections 1.6 and 2.6; fcffsimpleginzu.md, "Valuation output" rows "Cost of capital", "Cumulated discount factor" and "PV(FCFF)" (2026-02-01)

## Station 7: terminal value

Terminal value is one number that stands for every cash flow after year 10. The workbook uses the perpetuity formula: terminal cash flow divided by (terminal cost of capital minus terminal growth). Three defaults feed it.

First, terminal growth equals the risk-free rate. The packet's rule: "The stable growth rate cannot exceed the growth rate of the economy, but it can be lower." The risk-free rate is expected inflation plus an expected real interest rate. Nominal economic growth is expected inflation plus expected real growth. So the risk-free rate is a handy ceiling, in the same currency as the cash flows.

Second, the stable return on capital equals the terminal cost of capital. In words, the company stops earning more than its capital costs. The packet: "The excess returns at stable growth firms should approach (or become) zero." Terminal reinvestment then follows the packet's stable-period rule, reinvestment rate = g divided by ROC, and the sheet multiplies that rate by terminal after-tax income.

Third, the terminal cost of capital is risk-free plus mature-market premium, as in station 6.

Almarai's terminal year: revenue 36,634.4, EBIT 5,151.9, after-tax income at 25% of 3,864.0. The reinvestment rate is 4.58% divided by 8.81%, or 51.99%, so reinvestment is 2,008.7. Note the jump from 939.0 in year 10 to 2,008.7. That is not a bug. The formula switches from sales to capital to g divided by ROC. FCFF is 1,855.2. Terminal value is 1,855.2 divided by (8.81% minus 4.58%), which is 43,858.8. Multiplied by the year-10 factor of 0.4816, its present value is 21,123.0.

Adding the two pieces: 16,394.5 plus 21,123.0 gives 37,517.5. By my arithmetic the terminal piece is about 56% of the total. Damodaran's terminal value post argues this is normal, because most equity returns come from price appreciation rather than dividends. His warning cuts the other way too: high terminal share does not mean growth-phase assumptions matter less, because they set the level the terminal value grows from.

Why it matters for the calculator: the "Stories to Numbers" sheet labels the after-year-10 cell "Sales to Capital" but it holds 0.5199, the reinvestment rate. Name it correctly in code.

Source: /Users/siddharth/Downloads/financeMD/valpacket1spr25.md, slides 201 to 211 (Spring 2025); bkdrkpfng.txt, sections 2.5 and 2.7; fcffsimpleginzu.md, "Valuation output" and "Stories to Numbers" (2026-02-01); /Users/siddharth/Downloads/financeMD/damodaran/blog/2016/11/myth-55-terminal-value-ate-my-dcf.md (2016-11-30)

## Station 8: failure probability and truncation

A DCF assumes the company survives to enjoy its terminal value. The packet says so directly: a DCF "values a firm as a going concern". If failure is plausible, the sheet blends two outcomes. Value of operating assets equals the DCF sum times (1 minus the probability of failure), plus the distress proceeds times that probability. Proceeds are a percentage (B54) of either book capital, code "B", or the DCF value itself, code "V" (B53).

Almarai's probability is 0, so the DCF sum of 37,517.5 passes through unchanged. The proceeds cell still computes 18,758.8, which is 50% of 37,517.5, and then multiplies it by zero. The Failure Rate worksheet holds rating-based default tables and survival-by-age tables, but has no formula links. You read a number off it and type it into B52.

Why it matters for the calculator: truncation is one multiplication after the sum, but B53 and B54 are always read, even when the switch says No.

Source: valpacket1spr25.md, slide 310 (Spring 2025); bkdrkpfng.txt, sections 1.6, 2.7 and 3.5; fcffsimpleginzu.md, "Valuation output" rows "Probability of failure" and "Proceeds if firm fails" (2026-02-01)

## Station 9: the equity bridge to value per share

The DCF sum values the operating business. Shareholders own what is left after other claims, plus assets the operations did not use. The bridge for Almarai:

| Step | Almarai |
|---|---|
| Value of operating assets | 37,517.5 |
| Minus debt | 45,063 |
| Minus minority interests | 1,558 |
| Plus cash | 19,000 |
| Plus non-operating assets | 21,119 |
| Equals value of equity | 31,015.5 |
| Minus value of employee options | 0 |
| Divided by shares | 4,315 |
| Value per share | 7.1878 |
| Share price | 72.28 |

Minority interests are the slice of consolidated subsidiaries owned by outsiders, so it is subtracted. Non-operating assets are things like stakes in other companies, which produce no revenue in the forecast, so they are added at book. Employee options are rights to buy new shares cheaply, and they dilute existing holders. The sheet values them with a dilution-adjusted Black-Scholes model that is circular, which is why the workbook needs Excel's iterative calculation switched on. With the options switch set to No, that line is zero. Trapped cash, override number 9, can reduce the cash line by the tax due on bringing it home.

Two honest observations. Almarai's debt, 45,063, is larger than its operating asset value, 37,517.5. The equity value is carried by cash and cross holdings. The Diagnostics sheet computes value divided by price as 0.0994 and prints "Value seems low. See below". Treat Almarai as the arithmetic fixture, not a study of the company. Also, the "Stories to Numbers" sheet still carries leftover Amazon narrative text from an earlier example, so read the numbers there, not the words.

Why it matters for the calculator: the golden test is this exact bridge, to six decimals.

Source: bkdrkpfng.txt, sections 2.7 and 2.8; fcffsimpleginzu.md, "Valuation output", "Stories to Numbers" and "Diagnostics" step 6 (2026-02-01); /Users/siddharth/Downloads/financeMD/damodaran/blog/2018/07/share-count-confusion-dilution-employee.md (2018-07-25)

## The nine default assumptions you can override

Each override is a Yes/No switch plus a value cell that is read only when the switch says Yes.

| # | Switch | What happens if No | What you can override |
|---|---|---|---|
| 1 | B45 stable cost of capital | Terminal rate = risk-free + mature premium (8.81%) | B46, your own terminal rate |
| 2 | B48 stable return on capital | Stable ROC = year-10 cost of capital | B49, a higher or lower ROC |
| 3 | B51 probability of failure | 0% | B52 probability; B53 and B54 always read |
| 4 | B56 reinvestment lag | Lag = 1 year | B57, lag of 0 to 3 |
| 5 | B59 tax convergence | Effective fades to marginal over years 6 to 10 | Yes keeps the effective rate forever |
| 6 | B61 NOL carryforward | 0 | B62, opening loss bank |
| 7 | B64 risk-free after year 10 | Today's risk-free forever | B65, a different long-run rate |
| 8 | B67 growth in perpetuity | g = risk-free (or B65 if #7 is Yes) | B68, your own g, negative allowed |
| 9 | B70 trapped cash | Cash added at face | B71 amount and B72 foreign tax rate |

Why it matters for the calculator: every override is an optional field with a documented default, and override 2 changes terminal reinvestment, so it changes the terminal value.

Source: bkdrkpfng.txt, section 1.6 (2026-09)

## The Diagnostics sheet checks

The Diagnostics sheet puts your forecast beside history and industry data, then asks questions. It never blocks anything. Almarai's numbers:

- Step 1, revenue growth: industry average 7.16%, most recent year 7.63%, forecast 5% for years 1 to 5. The question asked is why the forecast differs from recent history.
- Step 2, revenue in currency: 21,765.4 today, 35,030.0 in year 10. The questions are about the size of the total market and the implied share.
- Step 3, margins: 14.063% flat. The questions are about industry margins and unit economics.
- Step 4, reinvestment: sales to capital 0.59 most recent versus 1.71 in the forecast. The reinvestment drag is shown too: present value of after-tax operating income over ten years is 21,877.6, of which 5,483.1 (25.06%) is consumed by reinvestment, leaving 16,394.5 of FCFF.
- Step 4, return on capital ladder: 6.875% most recent, 14.50% marginal over years 1 to 10, 8.42% in year 10, 8.81% stable. Marginal ROC is the extra after-tax income divided by the extra capital, and it is the "is the growth worth it" test.
- Step 5, risk: industry cost of capital 5.79%, compounded 7.58%, years 1 to 5 7.055%, stable 8.81%. Failure rate 0.
- Step 6, value versus price: 0.0994, with a verdict string when the ratio is above 2 or below 0.5, and a fix-it matrix naming which input to move.

Why it matters for the calculator: the sheet has no hard validations, only dropdowns and text. The plan turns these checks into real errors and warnings, so the calculator should compute every number above.

Source: fcffsimpleginzu.md, "Diagnostics" (2026-02-01); bkdrkpfng.txt, section 4; /Users/siddharth/.claude/plans/help-me-out-here-abstract-wilkinson.md, milestone 2 (2026-09)

## Simple ginzu versus full ginzu

The simple ginzu treats revenue growth as the primitive. Margin turns revenue into operating income, and sales to capital turns revenue growth into reinvestment, over a fixed ten-year horizon with a built-in cost of capital worksheet and a failure module. The full ginzu (fcffginzu) is a different model family. Growth in operating income comes from fundamentals, meaning return on capital times reinvestment rate. Capital spending, depreciation and working capital are explicit lines. The high-growth period length is a user choice, beta and debt ratios are set separately for the growth and stable phases, an earnings normalizer sheet handles odd base years, and non-traded companies are supported. It has no failure probability module. The calculator ports the simple ginzu; the full one is only needed for fundamentals-driven growth or private companies.

Source: bkdrkpfng.txt, section 5 (2026-09)

## Where this comes from

- /Users/siddharth/Downloads/financeMD/damodaran/pc/fcffsimpleginzu.md, the workbook itself; read "Valuation output", "Stories to Numbers" and "Diagnostics" together.
- /Users/siddharth/.claude/projects/-Users-siddharth-Downloads/edcdeb19-7793-4e1b-9e73-4cf6186716bf/tool-results/bkdrkpfng.txt, the formula-by-formula schema, including the nine overrides and the simple-versus-full table.
- /Users/siddharth/Downloads/financeMD/valpacket1spr25.md, slides 191 to 211 (growth, sales to capital, terminal value and stable growth) and slide 310 (distress).
- /Users/siddharth/Downloads/financeMD/damodaran/blog/2016/11/myth-55-terminal-value-ate-my-dcf.md, why a large terminal share is normal.
- /Users/siddharth/Downloads/financeMD/damodaran/blog/2016/11/myth-53-growth-is-good-more-growth-is.md, growth must be paid for with reinvestment.
- /Users/siddharth/Downloads/financeMD/damodaran/blog/2015/02/dcf-myth-1-if-you-have-ddiscount-rate.md, what a DCF is and is not.
- /Users/siddharth/Downloads/financeMD/damodaran/blog/2015/08/dcf-myth-2-dcf-is-exercise-in-modeling.md, why the numbers need a story.
- /Users/siddharth/Downloads/financeMD/damodaran/blog/2018/07/share-count-confusion-dilution-employee.md, options and share counts in the equity bridge.
- /Users/siddharth/Downloads/financeMD/damodaran/New_Home_Page/definitions.md, one-line definitions of FCFF, reinvestment rate and fundamental growth.

## Three things to remember

1. The chain is revenue, margin, tax, reinvestment, FCFF, discount, terminal value, failure, bridge. Nine stations, in that order, and station 4 needs station 1 finished one year ahead.
2. Growth is not free. Every riyal of extra revenue costs one divided by the sales to capital ratio, and in the terminal year the cost becomes g divided by ROC.
3. Three terminal defaults do most of the work: growth equals the risk-free rate, stable ROC equals the cost of capital, and the terminal cost of capital equals risk-free plus the mature-market premium. Code the formulas, not the labels.
