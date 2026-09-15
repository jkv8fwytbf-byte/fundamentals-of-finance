# Chapter 5: Growth, Terminal Value, and the Dark Side {#r2-growth}

::: {.reading-only .read-first}
**Read growth, terminal value, and ranges carefully.** These sections explain why an exact spreadsheet answer can still be highly sensitive to the assumptions.
:::

## What this chapter is

Chapter 3 walked through the workbook's arithmetic station by station. This chapter covers the two places where that arithmetic is most easily abused: growth and terminal value. Then it covers the companies where the standard recipe breaks, which Damodaran calls the "dark side" of valuation. Every rule below exists because someone, often Damodaran himself, has shown how easy it is to make a spreadsheet say anything.

## Growth is bought, not given

### The growth equation

Growth in operating income comes from two things: how much a company reinvests, and what return it earns on that reinvestment. Reinvestment rate is the share of after-tax operating income put back into the business. Return on capital is after-tax operating income divided by the capital already invested. Multiply them and you get expected growth. The packet's worked example: a reinvestment rate of 83.33% times a return of 12% gives 10% growth. Think of a bakery. To bake more bread next year you must add an oven this year. The oven must then produce bread worth more than it cost.

Source: /Users/siddharth/Downloads/financeMD/valpacket1spr25.md, slides near lines 2251 and 2407 (Spring 2025)

Why it matters for the calculator: the simple ginzu asks for revenue growth and a sales-to-capital ratio, and derives reinvestment from them. The full ginzu goes the other way, growth from return times reinvestment. Same equation, read in different directions.

Source: bkdrkpfng.txt, section 2.5 and the full-ginzu comparison note

### Sales to capital, the efficiency lever

Sales to capital is revenue divided by invested capital. It answers: how much revenue does one unit of invested capital produce? A high ratio makes growth cheap. A low ratio means each extra unit of revenue needs a lot of new capital. In the simple ginzu, reinvestment each year equals the change in revenue divided by this ratio. So it is the single lever that decides how much of the growth story the company must pay for. Chapter 3, station 4, has the exact formula and the lag switch.

Source: bkdrkpfng.txt, section 2.5; fcffsimpleginzu.md, "Valuation output" row 8 (2026-02-01)

Why it matters for the calculator: the workbook shows the company's ratio next to the US industry, the global industry, and the global quartiles. A ratio above the industry's third quartile needs a written justification before it enters a base case.

Source: bkdrkpfng.txt, section 1.7 (feedback block, rows 25 to 31)

### Growth that destroys value

[Growth is not automatically good.]{.reading-highlight} If the return on new capital is below the cost of capital, every unit reinvested is worth less than it cost, and growth shrinks value. The packet's table shows this. When return on capital equals cost of capital, terminal value sits at 1,000 whatever the growth rate. With a 6% return, raising growth from 0% to 3% drops it to 714. With a 14% return, the same change lifts it to 1,122. In his words, "It is not growth per se that creates value but growth with excess returns."

Source: /Users/siddharth/Downloads/financeMD/valpacket1spr25.md, slides 206 to 208 (Spring 2025); /Users/siddharth/Downloads/financeMD/damodaran/blog/2016/11/myth-53-growth-is-good-more-growth-is.md (2016-11-30)

Why it matters for the calculator: the year-by-year return on invested capital row exists so you can see whether the story's growth earns its keep. Revenue tripling while ROIC stays below the cost of capital should print a warning.

Source: bkdrkpfng.txt, section 2.5 (rows 39 and 40)

## All good things end

### How long can high growth last

Most companies cannot grow fast for long, and almost none can do it while earning excess returns, meaning returns above the cost of capital. Damodaran's four propositions: a larger potential market allows longer growth; a smaller company relative to that market allows longer growth; stronger and more durable competitive advantages allow longer value-creating growth; and such advantages are rare. His practical cap: a growth period much longer than ten years means "you are already building in the expectation that your firm is an exceptional firm."

Source: /Users/siddharth/Downloads/financeMD/valpacket1spr25.md, slides 206 and 294 (Spring 2025)

Why it matters for the calculator: the simple ginzu fixes the high-growth window at ten years. That is a design choice. Do not extend the grid.

Source: bkdrkpfng.txt, comparison table row "Horizon"

### Convergence: what fades and what it fades to

By the terminal year a company must look like a stable company, so several things fade at once. Revenue growth falls to the stable rate. Operating margin converges to a target. The tax rate converges to the marginal rate. Cost of capital converges to that of a mature company. Return on capital converges to cost of capital, so excess returns approach zero. Chapter 3 shows how the workbook phases each over years 6 to 10. Damodaran notes the McKinsey view that return on capital should always equal cost of capital in stable growth. He adds his own reservation: "excess returns seem to persist for very long time periods." The workbook defaults to full convergence but lets you override the stable return on capital.

Source: /Users/siddharth/Downloads/financeMD/valpacket1spr25.md, slides 209 to 210 (Spring 2025); bkdrkpfng.txt, section 2.5 (ROC_stable)

Why it matters for the calculator: every override of a convergence default is a claim that the company is unusual. Log the override and its justifying sentence together in the run record.

## Terminal value discipline

::: {.reading-only .watch-out}
**Keep all three rules together.** Growth, return on capital, and reinvestment must tell a consistent long-run story.
:::

### The three rules

[Terminal value]{.reading-highlight} is one number standing in for every cash flow after year ten. Chapter 3, station 7, has the formula and the Almarai numbers. Three rules keep it honest.

| Rule | What it says | Why |
|---|---|---|
| Growth cap | Stable growth at or below the risk-free rate, in the currency of the cash flows | The risk-free rate is a proxy for nominal growth in the economy, and no company outgrows its economy forever |
| Excess returns fade | Stable return on capital equals cost of capital by default | Competition erodes advantages; assuming otherwise is a claim you must defend |
| Consistent reinvestment | Terminal reinvestment rate equals stable growth divided by stable return on capital | Growth forever still has to be paid for forever |

On the growth cap, Damodaran does not forecast the economy. He uses the risk-free rate because it is observable, carries the currency's inflation automatically, and tracks nominal growth. In the US from 1954 to 2015 nominal GDP growth ran about 0.74% above the risk-free rate, and since 1981 it has lagged it by about 0.58%. His conclusion: stable growth below the economy's rate cannot hurt you, above it can make valuations implode. Negative stable growth is allowed and sometimes right for declining businesses.

Source: /Users/siddharth/Downloads/financeMD/damodaran/blog/2016/11/myth-52-as-g-rto-infinity-and-beyond.md (2016-11-30); /Users/siddharth/Downloads/financeMD/damodaran/blog/2016/11/myth-54-negative-growth-rates-forever.md (2016-11-30); valpacket1spr25.md, slides 201 to 205

On consistent reinvestment, the common mistake is to grow the year-ten free cash flow by one more year and call it the terminal cash flow. That silently locks the year-ten reinvestment rate in forever. The workbook instead recomputes terminal reinvestment as growth divided by return on capital. For Almarai that is 4.58% divided by 8.81%, a 51.99% rate, which is why reinvestment jumps in the terminal column.

Source: /Users/siddharth/Downloads/financeMD/damodaran/blog/2016/11/myth-53-growth-is-good-more-growth-is.md (2016-11-30); bkdrkpfng.txt, section 2.5 (Reinv_T)

Why it matters for the calculator: the terminal cost of capital is risk-free rate plus mature-market equity risk premium (ERP), whatever the sheet label says. Code the formula, not the label, or the golden test fails.

Source: bkdrkpfng.txt, section 1.6 note on the label mismatch

### Why terminal value dominates, and what that means

In the Almarai golden case the present value of the terminal value is 21,122.99 and the present value of the ten explicit years is 16,394.54. So the terminal piece is about 56% of operating value. For growth companies it can be 80%, 90%, or more than 100%, because early cash flows are small or negative. Critics call this a flaw. Damodaran's answer has two parts. First, it is normal: most of the historical return on stocks came from price appreciation, not dividends, so most of a DCF's value should sit at the end. Second, a large terminal share means the growth-phase assumptions matter more, not less. Terminal value is computed from year-ten earnings, and those are whatever the first ten years produced.

Source: bkdrkpfng.txt, section 2.7 (B19 and B20); /Users/siddharth/Downloads/financeMD/damodaran/pdfiles/CLC/slides/Ch11.md, lines 105 to 109; /Users/siddharth/Downloads/financeMD/damodaran/blog/2016/11/myth-55-terminal-value-ate-my-dcf.md (2016-11-30)

Why it matters for the calculator: print the terminal share on every run. A share far above the industry norm is a prompt to reread the margin and growth story, not a reason to distrust the method.

## The Dark Side of Valuation

### What the book is

"The Dark Side of Valuation" began as a paper valuing Amazon in March 2000, when his DCF gave about 34 dollars a share against a price of 80. The first edition covered young technology companies. The second, after 2008, added distressed companies, commodity firms, and banks. The third edition is built around three macro problems: very low or negative interest rates, risk premiums that move violently and often, and rising political risk as globalization reverses. It has twenty chapters in five parts and ends with "Lighting the Way: Vanquishing the Dark Side." The thesis: the dark side is not a different model. It is the same model applied where data is thin, and the temptation is to abandon it for "paradigm shifts," invented metrics, and stories that outrun numbers. Refusing to value something because it is uncertain "is a cop-out, since not dealing with uncertainty does not make it go away."

Source: /Users/siddharth/Downloads/financeMD/damodaran/New_Home_Page/darkside/preface.md; /Users/siddharth/Downloads/financeMD/damodaran/New_Home_Page/DSV3/dsv3edpreface.md; valpacket1spr25.md, slide 291; /Users/siddharth/Downloads/financeMD/damodaran/blog/2014/06/a-disruptive-cab-ride-to-riches-uber.md (2014-06-09); bkm2kob5x.txt, Part 1

### What changes, by company type

The plan requires every memo to name the company's uncertainty type and pull the matching passages. Here is the map.

| Type | What breaks | What Damodaran changes | Calculator hook |
|---|---|---|---|
| Young or growth | Little history, small revenue, losses, real chance of failure | Work top down from market size and share; let cost of capital fall over time; keep failure risk out of the discount rate; expect share count to rise | Failure probability on; cost-of-capital path from high to mature; option and dilution inputs |
| Distressed or declining | DCF assumes survival to the terminal year | Blend going-concern value with distress-sale value; allow negative growth and negative reinvestment | Probability of failure and proceeds rule; negative stable growth allowed |
| Cyclical or commodity | Base-year earnings are a point on a cycle, not a level | Normalize earnings across the cycle, or forecast the commodity price and say so; keep macro views separate from company views | Base year flagged as normalized, with the method stored |
| Financial service | Debt is raw material, not capital; cash flows are hard to define; regulators set capital ratios | Value equity directly, often with a dividend model; treat book equity as meaningful | The free-cash-flow-to-firm (FCFF) workbook is the wrong tool; the type label should raise a hard warning |
| Complex holding structures | Consolidated statements mix parent and holdings; cross holdings are opaque | Value the parent alone, then each holding, then add and subtract | Non-operating assets and minority interests as separate, cited rows |
| Emerging market | Country risk, currency and inflation shifts, governance, nationalization, more cross holdings | Add a country risk premium scaled from default spreads; strip the sovereign spread from the local risk-free rate | Country-risk vintage id on every run; INR risk-free equals the 10-year Indian government bond (G-sec) yield minus India's default spread |

Source: /Users/siddharth/Downloads/financeMD/valpacket1spr25.md, slides 292 to 321 and 339 (Spring 2025); /Users/siddharth/Downloads/financeMD/damodaran/pdfiles/CLC/slides/Ch13.md; bafb6h9rb.txt (India rows); /Users/siddharth/.claude/plans/help-me-out-here-abstract-wilkinson.md, memo section

For India, the January 2026 vintage carries a default spread of 1.87% and a country risk premium of 2.85% on top of the mature premium of 4.23%. That is the concrete form "emerging market" takes in the numbers.

Source: bafb6h9rb.txt (India, January 2026 vintage)

### Failure probability and recovery

A DCF "values a firm as a going concern." If the firm may die before reaching stable growth, the DCF overstates value. The fix is one blend: going-concern value times one minus the probability of failure, plus distress-sale value times that probability. Chapter 3, station 8, shows the cells. Three ways to estimate the probability: the bond rating and its cumulative default table, a statistical model, or the market price of the company's bonds. The workbook's Failure Rate worksheet holds the rating table. For example, the ten-year cumulative default probability is 11.78% for BB and 50.38% for CCC and below. It also holds US Bureau of Labor Statistics survival rates by company age. It has no formula links; you read a number and type it in. His own choices show the range: Tesla in September 2013 at 10% failure with 50% recovery, Tesla in March 2014 at 0% after its bond issue, Uber in June 2014 at 10%.

Source: /Users/siddharth/Downloads/financeMD/valpacket1spr25.md, slide 310 and the Uber narrative slide (Spring 2025); bkdrkpfng.txt, section 3.5; /Users/siddharth/Downloads/financeMD/damodaran/blog/2014/03/return-to-firing-line-revisiting-tesla.md (2014-03-25)

Why it matters for the calculator: the probability and the proceeds rule are inputs the memo must state, with the table row they came from. A blank here should block the run for any company typed young or distressed.

## DCF is gameable

### The sales-to-capital 10 example

The strongest sensitivity critique of DCF is Damodaran's own. In March 2014 his Tesla valuation used a sales-to-capital ratio of 1.55 and gave a value between 110 and 115 dollars a share. Then he showed the trick. Set the ratio to 10, meaning ten dollars of revenue per dollar invested, and the value jumps to 302 dollars a share. His comment: "Magical, right?" The catch is that this assumes Tesla adds about 68 billion dollars of revenue and 9 billion dollars of profit over a decade without building factories. Tesla had just announced a 5 billion dollar battery plant. His line on fake DCFs: cash flows and a discount rate on a spreadsheet no more make a DCF than "wearing tights and ballet shoes makes you a ballerina."

Source: /Users/siddharth/Downloads/financeMD/damodaran/blog/2014/03/return-to-firing-line-revisiting-tesla.md (2014-03-25); bkm2kob5x.txt, Part 1 bullet 9 and section 3.4

### Published ranges

He publishes the gameability as a feature. In February 2020 his Tesla grid crossed three stories with three revenue scales and gave values from 106 dollars to 2,106 dollars a share. In the same post the median global auto company generated 1.37 dollars of revenue per dollar of capital, and the 75th percentile 2.42. His own estimate of 3 was, he wrote, "more aspirational than based on observable efficiencies." A twenty-fold range from one company on one day is the honest picture of how much inputs matter.

Source: /Users/siddharth/Downloads/financeMD/damodaran/blog/2020/02/a-do-it-yourself-diy-valuation-of-tesla.md (2020-02-06); bkm2kob5x.txt, section 3.4

Why it matters for the calculator: the guard rail is not a smarter formula. It is a plausibility band on each input, taken from his cross-sectional data, plus a written justification for anything outside it.

## Ranges instead of points

::: {.reading-only .key-idea}
**This is how the reader sees uncertainty.** Follow the link between varying the inputs, the sensitivity table, and the range of results.
:::

### Monte Carlo over his industry quartiles

His answer to input uncertainty is to stop pretending you know the number. If a key variable is uncertain, "why not quantify the uncertainty in a distribution (rather than a single price) and use that distribution in your valuation." That is a Monte Carlo simulation. You draw each uncertain input from a distribution many times, run the model each time, and look at the spread of values. The output is a value distribution, plus the probability that value sits below price. The plan commits the system to this from M2, with distributions from his industry quartiles, and the dashboard will show the ranges.

Source: /Users/siddharth/Downloads/financeMD/valpacket1spr25.md, slide 340 (Spring 2025); the approved plan, M2 section; /Users/siddharth/Valuation/docs/read-this-first.md, section 3.5

### The "Input Stat Distributioons" sheet

The workbook already carries the raw material, in a sheet whose name is misspelled exactly like that. It holds 94 global industry groups. For each it gives the first quartile, median, and third quartile of six inputs: revenue growth over the last three years, pre-tax operating margin, sales to invested capital, cost of capital, beta, and debt to capital. Almarai's group, Food Processing, has 1,450 firms. Its sales-to-invested-capital quartiles are about 0.90, 1.54, and 2.47. Its cost-of-capital quartiles are about 6.62%, 7.18%, and 7.91%. The Input sheet's feedback block reads this table to show where the company sits against its peers.

Source: /Users/siddharth/Downloads/financeMD/damodaran/pc/fcffsimpleginzu.md, "Input Stat Distributioons" sheet, Food Processing row (2026-02-01); bkdrkpfng.txt, sections 1.7 and 3.3

Why it matters for the calculator: this lookup is an exact match on the global industry name, unlike the other industry tables. Load the sheet into its own table, keep the misspelling as the source label, and draw Monte Carlo inputs from it with the vintage id attached. A triangle across the three quartiles is a reasonable first distribution; that is a modeling choice you state, not a rule from the source.

## The 2020 COVID series: the method under stress

The best test of a method is a crisis. From February to November 2020 Damodaran published fourteen posts while valuing through the crash. He kept computing the implied equity risk premium as prices fell; on April 1, 2020 it stood at 6.01%, up from 5.20% at the start of the year. He refused to switch to multiples and argued that prices have no bounds but "Value on the other hand has both upper and lower bounds," set by cash flows, growth, and risk. In June he valued the S&P 500 with a simulation: the median value was 2,932 while the index traded near 3,100, around the 80th percentile of his distribution. He also lowered perpetual growth to match the lower risk-free rate, the growth cap doing its job in a low-rate world. The March 2020 snapshot of the simple ginzu, the corona variant, used a risk-free rate of 0.85% and had no failure-rate or distribution sheets yet.

Source: /Users/siddharth/Downloads/financeMD/damodaran/blog/2020/03/a-viral-market-meltdown-iii-pricing-or.md (2020-03-16); /Users/siddharth/Downloads/financeMD/damodaran/blog/2020/04/a-viral-market-meltdown-vi-price-of-risk.md (2020-04); /Users/siddharth/Downloads/financeMD/damodaran/blog/2020/06/a-viral-market-update-ix-do-it-yourself.md (2020-06-04); bkdrkpfng.txt, corona variant note; bkm2kob5x.txt, section 2.9

Why it matters for the calculator: a crisis changes the market vintage, not the engine. The ERP series, the risk-free rate, and the country spreads move; the formulas do not. That is why every run stores three vintage ids and why the regime panel is descriptive rather than predictive.

Source: bafb6h9rb.txt and the approved plan (three vintage ids per run)

## Where this comes from

- /Users/siddharth/Downloads/financeMD/valpacket1spr25.md, slides 201 to 211 (terminal value), 206 (growth propositions), 291 to 321 (dark side by company type), 339 to 340 (macro views and simulation)
- /Users/siddharth/Downloads/financeMD/damodaran/New_Home_Page/DSV3/dsv3edpreface.md, the third edition's plan and chapter list
- /Users/siddharth/Downloads/financeMD/damodaran/New_Home_Page/darkside/preface.md, the original book's origin in the Amazon 2000 paper
- /Users/siddharth/Downloads/financeMD/damodaran/blog/2016/11/, DCF myths 5.1 to 5.5 on growth caps, growth and value, negative growth, and terminal value share
- /Users/siddharth/Downloads/financeMD/damodaran/blog/2014/03/return-to-firing-line-revisiting-tesla.md, the sales-to-capital 10 demonstration
- /Users/siddharth/Downloads/financeMD/damodaran/blog/2020/02/a-do-it-yourself-diy-valuation-of-tesla.md, the published grid of values and the auto-industry efficiency distribution
- /Users/siddharth/Downloads/financeMD/damodaran/blog/2020/, the fourteen "Viral Market" posts, especially III, VI, and IX
- /Users/siddharth/Downloads/financeMD/damodaran/pdfiles/CLC/slides/Ch11.md, Ch12.md and Ch13.md, terminal value at growth, mature, and declining firms
- /Users/siddharth/Downloads/financeMD/damodaran/pc/fcffsimpleginzu.md, the "Input Stat Distributioons" and "Failure Rate worksheet" sheets
- /Users/siddharth/Valuation/docs/other-side/, Document D, for the critics' side of terminal value and input sensitivity

## Three things to remember

::: {.reading-emphasis .key-idea}
1. Growth is reinvestment times return, so every growth story has a bill. Sales to capital is where the bill is set, and a ratio above the industry's third quartile needs a sentence of defense before it enters a base case.
2. Terminal value follows three rules: growth at or below the risk-free rate, excess returns fading to zero by default, reinvestment equal to growth divided by return on capital. A large terminal share is normal and means the ten-year path matters more, not less.
3. The dark side is the same model with less data. Name the company's uncertainty type, state the failure probability and recovery rule, and report [a range]{.reading-highlight} from his industry quartiles. A point estimate with no range hides the uncertainty; it does not remove it.
:::
