# Chapter 2: The Accounting Minimum and the Base Year {#r2-accounting}

::: {.reading-only .read-first}
**Focus on where the starting numbers come from.** Learn the three statements, the expense categories, and the updating rule before worrying about every accounting adjustment.
:::

## What this chapter is

Chapter 3 walks the calculator forward from a base year. This chapter is about that base year: the handful of numbers you type in before anything is forecast. Damodaran's view of accounting is simple and slightly rude. Accountants record the past carefully, and valuers want the future, so the statements are a starting point that needs repairs. You do not need to become an accountant. You need to know three statements, one distinction, two repairs, two tax rates, and one updating rule.

Source: /Users/siddharth/Downloads/financeMD/damodaran/New_Home_Page/AccPrimer/accstate.md (undated primer)

## The three statements and how they connect

A company publishes three tables. The balance sheet is a photograph: what the company owns (assets) and who paid for it (liabilities and equity) on one date. The income statement is a film: revenues earned and expenses used up over a period, ending in net income. The cash flow statement is the bank record: cash that moved in and out during the same period, split into operating, investing and financing activities.

They connect in two places. Net income from the income statement flows into equity on the balance sheet as retained earnings. The cash flow statement starts from net income, adds back non-cash charges such as depreciation, and ends at the change in the balance sheet's cash line. If you remember one link, remember this one: profit is an opinion, cash is a fact, and the cash flow statement is the reconciliation between them.

Why it matters for the calculator: every base-year input comes from one of these three tables, and the table tells you whether the number is a stock (a balance on a date) or a flow (a total over a period).

Source: /Users/siddharth/Downloads/financeMD/Aswath Damodaran - Investment Valuation, University Edition _ Tools and Techniques for Determining the Value of Any Asset (2023).md, Chapter 3, "Understanding Financial Statements", Figures 3.1 to 3.3

## Operating, financing, capital: the one distinction that matters

Damodaran sorts every expense into three bins. An operating expense buys benefits only in the current period; wages and raw materials are the classic cases. A financing expense is the cost of borrowed money, chiefly interest. A capital expense buys benefits over many years, such as a factory, and is spread across those years through depreciation.

The income statement is built in that order. Revenues minus operating expenses minus depreciation gives operating income, also called EBIT (earnings before interest and taxes). EBIT minus interest gives taxable income. Taxable income minus taxes gives net income. The trouble is that accountants put some items in the wrong bin. Research spending is a capital expense wearing an operating-expense costume. Lease rent, before 2019, was a financing expense in the same costume. He describes a financial expense as "any commitment that is tax deductible that you have to meet no matter what your operating results".

Why it matters for the calculator: the calculator forecasts operating income and treats interest separately, so anything mis-binned in the base year is mis-forecast for ten years.

Source: /Users/siddharth/Downloads/financeMD/damodaran/blog/2011/06/from-revenues-to-earnings-operating.md (2011-06-15); /Users/siddharth/Downloads/financeMD/valpacket1spr25.md, slides 121 to 122

## Cash versus accrual

Accrual accounting records a sale when the good is delivered, not when the cash arrives. It then matches the expenses that produced that sale to the same period. A cash basis would record only money that moved. Accrual is the better measure of performance, which is why the income statement uses it. But it also means revenue can be booked before it is collected, and inventory or receivables can hide the gap.

The practical consequence is that free cash flow, which is what the calculator discounts, must be rebuilt from accrual earnings. You start with after-tax operating income and subtract reinvestment. That is the bridge from accrual to cash, and chapter 3 covers the mechanics.

Why it matters for the calculator: the base-year EBIT is an accrual number, and the calculator turns it into cash by subtracting reinvestment, so the base EBIT must be clean of one-off items.

Source: /Users/siddharth/Downloads/financeMD/damodaran/New_Home_Page/AccPrimer/accstate.md, "How Accountants measure earnings"; /Users/siddharth/Downloads/financeMD/damodaran/New_Home_Page/AccPrimer/onetime.md

## Two repairs: capitalize R&D, and operating leases before 2019

### Research and development

Accounting rules force companies to expense R&D in the year it is spent. Damodaran argues it is a capital expense and should be capitalized, meaning turned into an asset and depreciated. The recipe has three steps. Choose an amortizable life, two to ten years depending on the industry. Collect past R&D for that many years. Sum the unamortized portions to get a research asset, and compute this year's amortization of it.

The adjustment to operating income is this year's R&D minus this year's amortization. In his worked example, in euros and with a five-year life, R&D of 1,020 and amortization of 903 raised operating income by 117 and created a research asset of 2,914. That asset is added to book equity and to invested capital, so return on capital changes as well.

Why it matters for the calculator: the workbook's "R& D converter" sheet does exactly this, and the engine must add the adjustment to base-year EBIT and the research asset to invested capital when the R&D switch is "Yes".

Source: /Users/siddharth/Downloads/financeMD/valpacket1spr25.md, slides 130 to 132; /Users/siddharth/Downloads/financeMD/damodaran/New_Home_Page/AccPrimer/research.md; bkdrkpfng.txt, section 3.7

### Operating leases

Before 2019 an operating lease, meaning a rental contract for a store or an aircraft, stayed off the balance sheet. The rent sat inside operating expenses. Damodaran treated the rent as a financing expense, discounted the future lease commitments at the pre-tax cost of debt, and called that present value debt. Operating income was then raised by the rent and lowered by depreciation on the created lease asset. In his Gap example the debt value of leases was 4,397 against conventional debt of 1,970, and adjusted operating income rose from 1,012 to 1,362.

In 2019 both IFRS and US GAAP changed the rules, so companies now report lease liabilities and right-of-use assets themselves. The workbook carries a warning: do not run the lease converter on a post-2019 filing, because the accountant has already done it and you would double count.

Why it matters for the calculator: for modern filings the lease switch stays "No", and the decision moves to whether reported lease liabilities are counted inside book debt.

Source: /Users/siddharth/Downloads/financeMD/valpacket1spr25.md, slides 123 to 126; /Users/siddharth/Downloads/financeMD/damodaran/New_Home_Page/AccPrimer/lease.md; bkdrkpfng.txt, section 1.2, row B17

## Effective versus marginal tax rate, and NOLs

The effective tax rate is taxes divided by taxable income, as reported in the statements. It is an average across everything the company earned, including low-tax foreign profits and deferrals. The [marginal tax rate]{.reading-highlight} is the statutory rate on the next unit of profit, found in the tax code of the home country. Most companies report an effective rate below their marginal rate.

Damodaran's rule is to start with the effective rate and drift toward the marginal rate over the forecast. Using only the marginal rate understates early cash flows. Using only the effective rate assumes the tax deferral lasts forever. The marginal rate is the right one for the tax benefit of interest, because interest is deducted from the last dollars of income. In his January 2026 country data, India shows an average effective rate of 22.33% against a marginal rate of 30%.

An NOL is a net operating loss carried forward: a bank of past losses that shields future profits from tax until it is used up. The workbook has an override to enter an opening NOL, and the tax computation skips tax on income until the bank is exhausted. The engine will port that logic, as chapter 3 shows.

For India the marginal-rate options are 25.17% under the new regime, 34.94% under the old regime, and 17.16% for new manufacturing companies. The workbook's country table lists 30% for India, but no formula reads it, so both tax rates are typed by hand.

Why it matters for the calculator: two tax inputs, effective for years 1 to 5 and marginal for the terminal year and the cost of debt, and an optional NOL bank.

Source: /Users/siddharth/Downloads/financeMD/valpacket1spr25.md, slides 138 to 140; /Users/siddharth/Downloads/financeMD/damodaran/New_Home_Page/definitions.md, rows "Effective tax rate" and "Marginal tax rate"; /Users/siddharth/Downloads/financeMD/damodaran/blog/2026/02/data-update-7-for-2026-debt-and-taxes.md (2026-02-20); bkdrkpfng.txt, sections 1.2 and 6

## The base-year inputs, and where each one lives

::: {.reading-only .watch-out}
**Check the units as well as the source.** The table links each starting input to the financial statements; the share count must use compatible units.
:::

The workbook's Input sheet asks for these numbers, in two columns: the most recent twelve months, and the last annual report before that. [Units must be consistent]{.reading-highlight} all the way through, including the share count. Apple's 2025 10-K reports in millions of dollars; Trent's Indian results report in rupees crore, where one crore is ten million.

The table below shows where each item sits. The Apple figures come from the fiscal year ended September 27, 2025. The Trent figures come from the standalone results for the year ended March 31, 2024, which is the annual column inside a quarterly filing.

| Input | What it is | US 10-K: Item 8, Apple 2025 | Indian filing: Trent, Rs crore |
|---|---|---|---|
| Revenues | Sales earned in the period | Statement of Operations, "Total net sales" 416,161 | "Revenue from operations" 11,926.56; exclude "Other income" |
| Operating income (EBIT) | Revenues minus operating costs and depreciation | "Operating income" 133,050 | Not printed; compute profit before tax 1,873.32 plus finance costs 309.37 minus other income and exceptional items |
| Interest expense | Cost of borrowed money | Not broken out; sits inside "Other income/(expense), net" of (321); estimate from the debt note | "Finance costs" 309.37 |
| Book value of equity | Paid-in capital plus retained earnings | Balance Sheet, "Total shareholders' equity" 73,733 | "Paid-up equity share capital" 35.55 plus "Other equity" 4,411.64, printed as "Net Worth" 4,447.19 |
| Book value of debt | Interest-bearing borrowings | Commercial paper 7,979 plus term debt 12,350 and 78,328; lease liabilities 13,720 are in the lease note | "Paid up Debt capital" 1,738.32, which by its own note includes lease liabilities under Ind AS 116 |
| Cash and marketable securities | Cash and near-cash investments | Cash 35,934 plus marketable securities 18,763 and 77,723 | Balance sheet, cash and bank balances plus investments; not in the quarterly results |
| Cross holdings | Stakes in other companies, not consolidated | "Other non-current assets" and the investments note | Associates and joint ventures, listed in the auditor's report |
| Minority interests | Outsiders' share of consolidated subsidiaries | Balance Sheet, "Noncontrolling interests" when present; Apple has none | Consolidated results, "Non controlling interest" |
| Shares outstanding | Count of shares | Cover page: 14,776,353,000 as of October 17, 2025 | Share capital 35.55 crore at face value Re 1, so 35.55 crore shares |
| Price | Market price per share | Not in the filing; take it from the market on the valuation date | Same |
| Effective tax rate | Taxes divided by pre-tax income | Management's Discussion and Analysis (MD&A, Item 7) tax table: 15.6%; statutory federal 21% | "Total tax expenses" 437.50 divided by profit before tax 1,873.32 |

Four things to notice. First, Apple's 2025 10-K does not print interest expense anywhere obvious, which is why the calculator's interest input sometimes has to be estimated from the debt note. Second, the operating income line is printed in a US 10-K but not in an Indian results statement, so the engine must rebuild it. Third, Indian "Other income" is interest and dividend income, not operations, and must be kept out of both revenue and EBIT. Fourth, Damodaran's definition of debt includes lease commitments, so the Apple lease liabilities of 13,720 belong in book debt if you follow him, and Trent's filing already does that.

Why it matters for the calculator: the memo pipeline will cite a filing page for every one of these inputs, and the nightly job will fill the same table from EDGAR (the SEC's free filing database) for US names and later from EODHD (a paid market-data feed) for Indian names.

Source: /Users/siddharth/Downloads/financeMD/Apple-2025-10-K.md, Item 8 pages 29 to 33 and the leases note; /Users/siddharth/Downloads/financeMD/Unaudited Financial Results (Standalone and Consolidated) - Q1 FY 2024.md (filed 2024-08-09); /Users/siddharth/Downloads/financeMD/damodaran/New_Home_Page/definitions.md, row "Debt"; bkdrkpfng.txt, section 1.2

### On cross holdings and minority interests

A minority interest, now called a non-controlling interest, appears when a company owns more than half of a subsidiary and consolidates all of it. The outsiders' slice is shown as a liability and must be subtracted from firm value. A cross holding below fifty percent is not consolidated; its book value sits among the assets and must be added back. Both are book values, and Damodaran converts them to market value with a sector price-to-book ratio when he can. Emerging market companies carry more cross holdings, often to preserve family control.

Why it matters for the calculator: two inputs, minority interests subtracted and cross holdings added, both in the equity bridge of chapter 3 (the steps that turn firm value into value per share).

Source: /Users/siddharth/Downloads/financeMD/valpacket1spr25.md, slides 227 to 229 and the emerging-market cross-holdings slides; /Users/siddharth/Downloads/financeMD/damodaran/New_Home_Page/definitions.md, row "Minority Interests"

## The trailing-twelve-month rule

Annual reports go stale. A company valued in April is working from numbers that ended the previous September. The fix is [trailing-twelve-month data]{.reading-highlight}, meaning the most recent twelve months built from one annual report and one interim report. The rule is: last annual figure, minus the same interim period of the prior year, plus the current interim period.

Damodaran's own Apple example makes it concrete. Annual revenue to September 2023 was 383,285. The six months to March 2023 were 211,990 and the six months to March 2024 were 210,328. Trailing revenue is 383,285 minus 211,990 plus 210,328, which is 381,623. Operating income by the same rule went from 114,301 to 118,240. The workbook ships a small "Trailing 12 month Worksheet" that does this for revenues, operating income, interest expense and the effective tax rate, but it is not wired to the Input sheet; you paste the results by hand.

The rule applies only to flows. Balance sheet items such as cash, debt and equity are stocks, so you simply take the latest interim balance. Some items, such as employee options, appear only in annual reports, so you carry them forward and accept a small inconsistency.

Why it matters for the calculator: the nightly job will compute exactly this, last annual minus prior interim plus current interim, for the flow inputs, and will store both columns with their vintage.

Source: /Users/siddharth/Downloads/financeMD/Aswath Damodaran - Investment Valuation, University Edition _ Tools and Techniques for Determining the Value of Any Asset (2023).md, Chapter 9, Illustration 9.1; /Users/siddharth/Downloads/financeMD/valpacket1spr25.md, slide 120; /Users/siddharth/Downloads/financeMD/damodaran/pc/fcffsimpleginzu.md, "Trailing 12 month Worksheet"; bkdrkpfng.txt, section 3.8

## Where this comes from

- /Users/siddharth/Downloads/financeMD/damodaran/New_Home_Page/AccPrimer/accstate.md, the primer on financial statements, the shortest full statement of his view of accounting.
- /Users/siddharth/Downloads/financeMD/damodaran/New_Home_Page/AccPrimer/research.md, lease.md and onetime.md, the three repairs in his own words.
- /Users/siddharth/Downloads/financeMD/damodaran/New_Home_Page/definitions.md, one-line definitions of every term in this chapter, with his remarks.
- /Users/siddharth/Downloads/financeMD/valpacket1spr25.md, slides 119 to 141, the "accounting earnings, flawed but important" run and the tax slides.
- /Users/siddharth/Downloads/financeMD/cfpacket1spr25.md, the financial balance sheet framing: assets in place, growth assets, debt and equity.
- /Users/siddharth/Downloads/financeMD/damodaran/blog/2011/06/from-revenues-to-earnings-operating.md, the Groupon post on operating, financing and capital expenses.
- /Users/siddharth/Downloads/financeMD/damodaran/blog/2010/03/accounting-inconsistencies.md, the opening of his series on accounting inconsistencies.
- /Users/siddharth/Downloads/financeMD/damodaran/blog/2026/02/data-update-7-for-2026-debt-and-taxes.md, marginal, effective and cash tax rates by country.
- /Users/siddharth/Downloads/financeMD/Aswath Damodaran - Investment Valuation, University Edition _ Tools and Techniques for Determining the Value of Any Asset (2023).md, Chapter 3 and Chapter 9.
- /Users/siddharth/Downloads/financeMD/Apple-2025-10-K.md and the Trent results file, as worked examples of where numbers live.

## Three things to remember

::: {.reading-emphasis .key-idea}
1. Sort every expense into operating, financing or capital, then fix the two that accountants mis-bin: capitalize R&D, and treat lease commitments as debt unless the filing already does.
2. Start at the effective tax rate and fade to the marginal rate; use the marginal rate for the tax benefit of debt; give loss-makers an NOL bank.
3. Flows are trailing twelve months, last annual minus prior interim plus current interim; stocks are the latest balance; units stay consistent through the share count.
:::
