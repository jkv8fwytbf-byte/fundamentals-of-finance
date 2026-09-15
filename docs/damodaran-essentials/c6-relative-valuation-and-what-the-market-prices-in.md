# Chapter 6: Relative Valuation and What the Market Prices In {#r2-pricing}

::: {.reading-only .key-idea}
**Keep pricing and valuing separate.** Read the beginning of each part and the final takeaways, then return to the detailed multiple and market-premium examples.
:::

Quick orientation before the dump. This chapter covers two things that look different but share one idea. First, pricing a single company against similar companies using multiples. Second, pricing the whole stock market using the implied equity risk premium. In both cases you are reading what the market is paying, not deciding what something is worth. Damodaran keeps those two activities apart, and so will your calculator. Corpus paths below are relative to /Users/siddharth/Downloads/financeMD/damodaran/ unless they start with a slash.

## Part A: Pricing one company against its neighbors

### What a multiple is

A multiple is a price divided by something that scales with the size of the business. Think of house prices per square foot. You cannot compare a large house with a small one on total price, but you can compare price per square foot. In stocks the numerator is the market price of equity or the enterprise value. Enterprise value means market equity plus debt minus cash, the price of the operating business. The denominator is earnings, book value, revenues, or EBITDA. EBITDA means earnings before interest, taxes, depreciation, and amortization, a rough operating cash flow before reinvestment. Damodaran's packet says standardizing prices "creates price multiples", and that "Almost 85% of equity research reports are based upon a multiple and comparable firms."

Source: pptfiles/val3E/valpacket2spr25.md, slides "The Essence of Relative Valuation" and "Relative valuation is pervasive" (Spring 2025)

His opening speaker note is blunt: "Most self proclaimed experts on valuation are really experts on pricing". Relative valuation is the formal name. Pricing is what it actually is.

Source: pptfiles/val3E/valpacket2spr25.md, title slide notes (Spring 2025)

**Why it matters for the calculator:** the industry averages sheet inside fcffsimpleginzu carries EV/EBITDA, EV/EBIT, Price/Book and Trailing PE, but the DCF never reads them. Only EV/Sales is used, and only to weight the parts of a multi-business company. Multiples belong in a separate pricing panel, never inside the value.

Source: /Users/siddharth/.claude/projects/-Users-siddharth-Downloads/edcdeb19-7793-4e1b-9e73-4cf6186716bf/tool-results/bkdrkpfng.txt, industry table rows 15 to 19 (2026)

### Pricing is not valuing

His closing proposition on the topic is one sentence: "Relative valuation is pricing, not valuation." A multiple tells you what the crowd is paying for similar assets today. It says nothing about whether the crowd is right. His warning: "Your relative valuation judgment can be right and your stock can be hopelessly over valued at the same time."

Source: pptfiles/val3E/valpacket2spr25.md, slide "Relative Valuation: Some closing propositions" (Spring 2025)

**Why it matters for the calculator:** every output screen labels a number as value (from the DCF chain) or price (from multiples or the market). The two never share a cell.

### The four steps: define, describe, analyze, apply

He deconstructs any multiple in four steps. The table is the whole method in one place.

| Step | The question | The trap it catches |
|---|---|---|
| Define | How exactly is this multiple computed? | Numerator and denominator belonging to different claimholders; trailing versus forward earnings |
| Describe | What does the distribution across all firms look like? | Judging a number as high or low with no sense of the range |
| Analyze | Which fundamentals drive it, and how? | Assuming the relationship is a straight line |
| Apply | Who is comparable, and how do I control for differences? | Treating "same sector" as "same fundamentals" |

Source: pptfiles/val3E/valpacket2spr25.md, slides "The Four Steps to Deconstructing Multiples" and "Reviewing: The Four Steps" (Spring 2025)

**Define.** Proposition 1: "Both the value (the numerator) and the standardizing variable ( the denominator) should be to the same claimholders in the firm." Equity price goes over equity earnings or equity book value. Enterprise value goes over operating numbers such as EBITDA or sales. Price to EBITDA is inconsistent, and firms carrying more debt show a lower multiple for no good reason. He also lists the many faces of PE: current or average price; last financial year, trailing twelve months, or forecast earnings. In the 1990s bullish analysts used forward PE and bearish analysts used trailing PE, because the two disagreed.

Source: pptfiles/val3E/valpacket2spr25.md, slides "Definitional Tests" and "Example 1: Price Earnings Ratio" with notes (Spring 2025)

**Describe.** Multiples have skewed distributions, so "The averages are seldom good indicators of typical multiples." Use medians and percentiles. Also check for bias: a PE cannot be computed for a loss-making firm, so a PE sample silently drops the weakest companies.

Source: pptfiles/val3E/valpacket2spr25.md, slides "Descriptive Tests", "Multiples have skewed distributions" and "Reviewing: The Four Steps" (Spring 2025)

**Why it matters for the calculator:** store the definition next to every stored multiple (which price, which earnings, which date), and store the sample median and quartiles, never just the mean.

### Analyze: the fundamentals hiding inside every multiple

Proposition 2 is the bridge between this chapter and the DCF chapters: "Embedded in every multiple are all of the variables that drive every discounted cash flow valuation - growth, risk and cash flow patterns." Take a stable-growth dividend discount model and divide both sides by earnings. Out comes a PE formula with three inputs: expected growth, risk (the cost of equity), and how much can be paid out after reinvesting for growth. The same trick works for any multiple. Start from an equity model for equity multiples and a firm model for enterprise value multiples.

Source: pptfiles/val3E/valpacket2spr25.md, slides "Analytical Tests", "A Simple Analytical device" and "I. PE Ratios" with notes (Spring 2025)

Each multiple has one driver that matters most. He calls it the companion variable: "Every multiple has one variable that can be considered its key determinant - its companion variable".

| Multiple | Consistent pair | Companion variable | Other drivers |
|---|---|---|---|
| PE | Equity price over equity earnings | Expected growth in earnings | Cost of equity, payout ratio, quality of growth |
| Price to book (PBV) | Market equity over book equity | Return on equity (ROE) against the cost of equity | Growth, payout, risk |
| EV/EBITDA | Enterprise value over pre-tax operating cash flow | Reinvestment rate (or return on capital) | Cost of capital, growth, tax rate |
| EV/Sales | Enterprise value over revenues | After-tax operating margin | Reinvestment rate, cost of capital, growth |

Source: pptfiles/val3E/valpacket2spr25.md, slides "Price to Book Ratio: Determinants", "EV to EBITDA - Determinants", "The Determinants of EV/EBITDA" and "EV/Sales Ratio: Determinants" with notes (Spring 2025)

Three non-obvious lessons come with the formulas. First, PE moves more with growth when interest rates are low, because growth is a present value. Second, growth is not automatically good. A firm that grows while earning less than its cost of equity sees its PE fall as growth rises. Third, for PBV the rule is clean: an ROE above the cost of equity deserves a PBV above one, and below deserves below one. For EV/EBITDA his summary is: "Firms that deliver low growth, with high reinvestment and substandard returns on capital deserve to trade at low multiples of EBITDA." For revenue multiples, "Operating margin dominates the regression in every market."

Source: pptfiles/val3E/valpacket2spr25.md, slides "a. PE, Growth and Interest Rates", "c. PE and Growth Quality", "Price Book Value Ratio: Stable Growth Firm", "The Determinants of EV/EBITDA" and "V. EV/Sales Regressions across markets" with notes (Spring 2025)

**Why it matters for the calculator:** the same inputs already sit in the model (growth, margin, sales to capital, cost of capital). A pricing panel can therefore show the multiple your own DCF inputs imply and set it beside the sector median.

### Apply: comparables, mismatches, and sector regressions

A comparable firm is one with similar risk, growth and cash flows, not one in the same industry. "You can have firms in different businesses that have similar cashflow, growth and risk characteristics." Since no two firms match exactly, you must control for differences. His four ways: direct comparison, story telling (this firm deserves a higher PE because it grows faster), a modified multiple such as PEG (PE divided by expected growth), or a regression when firms differ on several dimensions at once.

Source: pptfiles/val3E/valpacket2spr25.md, slides "Application Tests" and "The Control for Differences Choices" with notes (Spring 2025)

A mismatch is a company whose multiple does not sit where its companion variable says it should. His European bank example uses medians. A bank below the sector median PBV of 2.07, with ROE above the median of 11.82%, and volatility below the median of 21.93%, is a mismatch worth a closer look. The regression version for those 18 banks was PBV = 2.27 + 3.63 ROE minus 2.68 standard deviation, with an R squared of 79%. Read it as: each extra 1% of ROE adds about 0.036 to PBV. The book applies the same matrix logic to revenue multiples set against margins.

Source: pptfiles/val3E/valpacket2spr25.md, slides "3: An Eyeballing Exercise", "The median test" and "The Statistical Alternative" (Spring 2025); /Users/siddharth/Downloads/financeMD/Aswath Damodaran - Investment Valuation, University Edition _ Tools and Techniques for Determining the Value of Any Asset (2023).md, Chapter 20, "Looking for Mismatches"

A sector regression is a small statistical model that predicts a firm's multiple from its fundamentals across a group. His market-wide PE regression on about 1,600 US firms in January 2025 predicted a PE of 33.75 for a firm with 15% growth, a beta of 0.90 (beta measures how much a stock moves with the market; 1.0 is average) and 20% payout, against a traded PE of 40.4. He then warns about the three usual problems: non-linearity, non-stationarity (the coefficients drift from year to year), and multicollinearity (growth and risk move together). Rules of thumb: a t statistic (how many standard errors a coefficient is away from zero) above 2 is good, 1 to 2 is marginal, below 1 is noise. Add one variable for every 10 to 15 observations. And a firm-level trap: Ryder showed a much lower EV/EBITDA than other truckers, most likely because it had the oldest fleet and a large fleet purchase ahead.

Source: pptfiles/val3E/valpacket2spr25.md, slides "Example 5: Overlooked fundamentals?", "A Test on EBITDA", "PE Ratio: Standard Regression for US stocks - January 2025", "Problems with the regression methodology", "Statistically insignificant?" and "Using the PE ratio regression" with notes (Spring 2025)

**Why it matters for the calculator:** a sector regression is a weekend project once the industry tables sit in Postgres, but it must carry its R squared and its date, because a low R squared means a wide prediction range.

### When pricing beats valuing

Damodaran is honest about why pricing dominates. It is quicker, it needs fewer explicit assumptions, and "There is safety in numbers". DCF ignores market mood, so it produces contrarian answers, and "if you are wrong, you will be wrong alone." Pricing is the right tool when the goal is the price something will fetch today, as in an IPO. It also fits momentum strategies and managers who are judged against peers. The market also decides which denominator counts. In social media in 2013, enterprise value per user correlated with market cap at 0.98, better than revenues did. His instruction: "In pricing, it is the market that determines what matters."

Source: pptfiles/val3E/valpacket2spr25.md, slides "Why relative valuation?", "The Market Imperative", "The Market sets the rules", "Read the tea leaves" and "Statistically insignificant?" with notes (Spring 2025)

**Why it matters for the calculator:** the product values companies, but the memo always shows the price beside the value, and a pricing panel explains why the market disagrees with you.

## Part B: What the whole market prices in

### The implied ERP as a composite indicator

The equity risk premium (ERP) is the extra return investors demand for holding stocks instead of a riskfree bond. The implied ERP runs the valuation backwards. Take the index level as given, take expected cash flows (dividends plus buybacks) and expected growth, and solve for the discount rate that makes value equal to price. That rate is the expected return on stocks; subtract the Treasury bond rate and you have the ERP. The analogy is a bond's yield to maturity: you know the price and the coupons, so you solve for the yield. Damodaran calls this number "my composite indicator for whether the market is richly priced or not" and stresses it "is entirely a market-driven number and is model-agnostic."

Source: blog/2026/01/data-update-2-for-2026-equities-get.md (2026-01-23)

Here is the latest row he published, which your erp_monthly table mirrors column for column.

| Item (start of September 2026) | Value |
|---|---|
| S&P 500 level | 7686.14 |
| US T.Bond rate | 4.75% |
| Default-risk-adjusted dollar riskfree rate | 4.53% |
| Expected growth rate (top-down, code TD) | 13.99% |
| ERP (trailing 12 months, the headline) | 4.09% |
| ERP with adjusted riskfree rate | 4.31% |
| ERP with sustainable payout | 4.14% |
| ERP smoothed (ten-year average cash flow) | 6.05% |
| ERP normalized | 3.56% |
| ERP net cash yield | 3.80% |
| Expected return on stocks | 8.84% |

Source: pc/implprem/ERPbymonth.md, sheet "Historical ERP", row 2026-09-01 (2026-09-01)

Two notes on that table. The adjusted riskfree rate exists because Moody's downgraded the United States from Aaa to Aa1 on May 16, 2025. He nets out the 0.22% default spread for an Aa1 sovereign to get "a more consistent riskfree rate". And the spread between the six ERP definitions, from 3.56% to 6.05%, is your honest error bar. The regime spec shows it as a band and calls the headline "soft" whenever the band is wider than 150 basis points.

Source: pc/implprem/ERPSept26.md, sheet "Impl premium calculator" (September 2026); /Users/siddharth/.claude/projects/-Users-siddharth-Downloads/edcdeb19-7793-4e1b-9e73-4cf6186716bf/tool-results/btzaixzyh.txt, CHECK 3, SPEC 1 (2026)

The mechanics are simple. Base cash flow grows at the expected growth rate for five years, then at the riskfree rate forever. The discount rate is riskfree plus ERP. Excel goal-seeks the ERP until value equals the index. The September 2026 sheet solves to an implied expected return of 8.8437%, which is the 8.84% above (4.75% plus the 4.09% ERP). Its what-if row at an ERP of 4.25% gives an intrinsic index value of 7398.08 and an intrinsic trailing PE of 27.19. Those numbers are the golden test for impliedErp.ts.

Source: pc/implprem/ERPSept26.md, sheet "Impl premium calculator" (September 2026)

**Why it matters for the calculator:** the same ERP feeds every company valuation that month, so the regime panel and the company DCF read one stored vintage row.

### The interpretive rule, in his words

He frames the reading as a question about the ERP, never as a forecast. If the market is "pricing in too low an ERP", then you are contending that "stocks are over priced". If the "current ERP is too high", that equals arguing "stocks today are under priced". And: "If you are not a market timer", then "you are in effect arguing that the current ERP is, in fact, the right ERP for the market."

Source: blog/2026/01/data-update-2-for-2026-equities-get.md (2026-01-23)

### The fair-value grid

On January 1, 2026 the index stood at 6845.5, the expected return was 8.41%, and the ERP was 4.23% against a T.Bond rate of 4.18% (4.46% on the adjusted rate of 3.95%). To show how much the answer depends on the ERP you accept, he valued the index at ERPs from 2% to 6%.

| ERP assumed | Index value | His label |
|---|---|---|
| 2% | 14834 | "undervalued by 53%" |
| 4.23% (the implied ERP) | 6845.5 | equal to the price |
| 6% | 4790 | "overvaluation of 43%" |

Then he declined to pick: "Rather than make that judgment for you", he charted the implied ERP back to 1960. The current ERP is "almost exactly equal to the average for the 1960-2025 period", lower than the post-2008 average, and far above the 2.05% of late 1999. The dataset behind that chart gives the averages: 4.25% for 1960 to 2025, 5.16% for 2006 to 2025, and 5.00% for 2016 to 2025.

Source: blog/2026/01/data-update-2-for-2026-equities-get.md (2026-01-23); pc/datasets/histimpl.md, sheet "Historical Impl Premiums", benchmark rows under the 2025 row

**Why it matters for the calculator:** the panel shows the ERP's percentile against those three windows and reports a state (less risk priced than usual, near normal, more than usual), never a call.

### Earnings yield against bond yield: context, not signal

Earnings yield is earnings divided by price, the PE turned upside down. It can sit next to the bond rate because both are yields. For 2025 the S&P 500 earnings yield was 3.97%, the T.Bond rate 4.18% and the T.Bill rate 3.65%. His 1960 to 2025 regression reads E/P = 0.0341 + 0.5618 times the T.Bond rate minus 0.1161 times the term spread (the T.Bond rate minus the T.Bill rate), with an R squared of 47.4%. About half of the movement in earnings yield is explained by rates. Use this as background only. His verdict on PE as a market gauge is that it "is noisy and an unreliable indicator" and "would have suggested staying out of US equities for much of the last decade."

Source: pc/datasets/histimpl.md, row 2025; pptfiles/val3E/valpacket2spr25.md, slides "A Counter", "The Tie Breaker" and "Regression Results" (Spring 2025); blog/2026/01/data-update-2-for-2026-equities-get.md (2026-01-23)

### His market-timing caveats, verbatim

- "I am not a market timer, but I do value the market at regular intervals", and he does it "more to get a measure of what the market is pricing in, than to forecast future movements."
- "I am a terrible market timer and try to avoid it in my investing".
- "In bad news for market timers, none of the equity risk premium approaches does well at forecasting next year's actual return".
- "waiting on the sidelines for this to happen has not been a good strategy for the last decade".
- His preferred outcome for 2026: "the healthiest development for the market would be for it to deliver a return roughly equal to its expected return (8-9%)".

Source: blog/2024/01/data-update-2-for-2024-stock-comeback.md (2024-01-17); blog/2026/03/the-price-of-risk-equity-risk-premium.md (2026-03-15); blog/2026/01/data-update-2-for-2026-equities-get.md (2026-01-23)

Cadence matters for your cron jobs. He moved from an annual to a monthly ERP in September 2008. During crises (Brexit 2016, COVID 2020, tariffs 2025, the March 2026 oil shock) he estimates it daily.

Source: blog/2026/03/the-price-of-risk-equity-risk-premium.md (2026-03-15)

### Why news sentiment never enters the computation

The implied ERP is computed from three things: the index level, trailing cash flows, and an earnings growth estimate. News is not one of them. Damodaran's reason is a doctrine, not a technicality: "markets are pricing mechanisms, not value mechanisms", and "Price is reactive, Value is proactive!" His 2026 opener is the proof. Someone who read only the news in 2025 "would have guessed" that stocks "had a bad year", and "You would have been wrong". The regime spec turns this into a rule. Sentiment may annotate the ERP chart with dated events and flag a divergence between news tone and the ERP. It may never be an input, and the panel may never be sorted by it. Store it in a separate market_context_events table and draw it as an overlay.

Source: blog/2020/03/a-viral-market-meltdown-iii-pricing-or.md (2020-03-16); blog/2026/01/data-update-2-for-2026-equities-get.md (2026-01-23); /Users/siddharth/.claude/projects/-Users-siddharth-Downloads/edcdeb19-7793-4e1b-9e73-4cf6186716bf/tool-results/btzaixzyh.txt, CHECK 3, "What licensed news-sentiment APIs may legitimately add" (2026)

**Why it matters for the calculator:** the no-advice test and the "numbers go to the database, not free text" rule both depend on the ERP being a pure function of stored numbers.

## Where this comes from

- pptfiles/val3E/valpacket2spr25.md: the whole relative valuation packet with speaker notes, slides 1 to 106. Read the notes, not just the bullets.
- New_Home_Page/lectures/multintr.md, pe.md, pbv.md, ps.md, vebitnote.md, relpe.md: short lecture notes, one per multiple.
- /Users/siddharth/Downloads/financeMD/Aswath Damodaran - Investment Valuation, University Edition _ Tools and Techniques for Determining the Value of Any Asset (2023).md: Chapters 17 to 20 (principles, earnings multiples, book value multiples, revenue multiples).
- blog/2026/01/data-update-2-for-2026-equities-get.md: the implied ERP, the fair-value grid, the PE critique, the "sidelines" line.
- pc/implprem/ERPbymonth.md and pc/implprem/ERPSept26.md: the monthly series and the live calculator with the goal-seek steps.
- pc/datasets/histimpl.md: annual implied ERP since 1960 with earnings yield, dividend yield and bond rates.
- blog/2024/01/data-update-2-for-2024-stock-comeback.md and blog/2026/03/the-price-of-risk-equity-risk-premium.md: the market-timing caveats and the forecasting evidence.
- blog/2020/03/a-viral-market-meltdown-iii-pricing-or.md: the price versus value doctrine.
- pdfiles/country/val2dayIndia2025.md: the India session, with "Relative valuation or Pricing" defined and the line "Much of what passes for valuation is pricing."
- /Users/siddharth/.claude/projects/-Users-siddharth-Downloads/edcdeb19-7793-4e1b-9e73-4cf6186716bf/tool-results/btzaixzyh.txt, CHECK 3: the regime panel spec built from all of the above.

## Three things to remember

::: {.reading-emphasis .key-idea}
1. A multiple is a price with a ruler on it. Define it, describe its distribution, find its companion variable, then apply it only to firms with [similar fundamentals]{.reading-highlight}.
2. [Pricing is not valuing.]{.reading-highlight} Your calculator produces value; the pricing panel shows what the market pays, side by side, never blended.
3. The implied ERP (4.09% in September 2026, expected return 8.84%) tells you what the market is pricing in. Damodaran reads it as a state, refuses to time the market with it, and never lets news sentiment touch the arithmetic.
:::
