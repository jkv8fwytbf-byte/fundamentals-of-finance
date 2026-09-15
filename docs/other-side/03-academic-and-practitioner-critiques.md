# The Other Side, Chapter 3: Academic and Practitioner Critiques {#r3-critiques}

::: {.reading-only .read-first}
**For each critique, connect the claim to the proposed response.** Start with input sensitivity, reverse DCF, forecasting tests, and the final critique-to-feature map.
:::

This chapter collects the formal attacks on the method your engine copies. An academic critic publishes in a journal and argues from theory. A practitioner critic runs money and argues from results. Both appear here, because both have been right about something. Every entry has four parts: the claim in one sentence, why it matters, his reply if any, and what the app will do about it. Chapter 2 covers his misses company by company. Chapter 4 keeps the scoreboard.

Source: /Users/siddharth/.claude/projects/-Users-siddharth-Downloads/edcdeb19-7793-4e1b-9e73-4cf6186716bf/tool-results/bkm2kob5x.txt, Part 3 (2026-09-14)

Below, "the Report" means that same file, compiled 2026-09-14. Nothing past milestone M0 is built yet, so every app feature is written as "will".

## 3.1 Kruschwitz, Löffler and Mandl (2012): the country risk premium has no theory

**The claim.** The country risk premium (CRP), the extra return added for operating in a riskier country, has no theoretical basis and no empirical support.

**The paper.** Lutz Kruschwitz, Andreas Löffler (also written Loeffler) and Gerwald Mandl, "Damodaran's Country Risk Premium: A Serious Critique", *Business Valuation Review* 31(2 to 3): 75 to 84, March 2012. SSRN abstract id 1651466. Journal page: https://meridian.allenpress.com/bvr/article/31/2-3/75/66392/. Their conclusion: the CRP "is of no relevance in academic circles, has no theoretical basis neither is the CRP concept empirically supported."

**Why it matters.** They attack all three of his routes to a CRP: the sovereign default spread, the relative volatility of the stock market, and the blend of the two. None comes from an equilibrium asset-pricing model, meaning a model where prices settle as investors trade risk against return. A global investor can spread country risk across many countries, so a CRP on top of CAPM may count the same risk twice.

**His reply.** A formal response in the same journal, volume 31, pages 85 to 86 (2012). His standing defense, restated in July 2026, is that treating a Brazilian and a Swiss company as equally risky is worse. His words: "whatever those improvements may be, they will have to work across 180 countries." He also concedes, "I have made simplistic assumptions and cut corners." Ernst and Gleißner extended the critique in SSRN 2888500.

**Outcome.** A split decision. Academia rejects the construct. Practice adopted it wholesale, because no maintained free alternative exists.

**Link warning.** The widely cited free PDF at ivc-forum.org now returns a 301 redirect to an unrelated domain, perrosysusrazas.com. Do not fetch it or put it in any crawl list. Use SSRN or AllenPress.

**What the app will do.** It will use his 192-country table, but never silently. Every run will store a country-risk vintage id, meaning the dated snapshot of his data it used. For India the January 2026 vintage reads Moody's Baa3, default spread 1.87%, CRP 2.85%, total ERP 7.08%. The July 2026 vintage reads 1.75%, 2.72% and 6.92%. The rupee risk-free rate will be the 10-year G-sec (Indian government bond) yield minus India's default spread, so sovereign risk is not counted twice.

Source: the Report, Part 3.1 and Part 4 row 10 (2026-09-14); /Users/siddharth/Downloads/financeMD/damodaran/blog/2026/07/country-risk-drivers-measures-and.md (2026-07-15); /Users/siddharth/.claude/projects/-Users-siddharth-Downloads/edcdeb19-7793-4e1b-9e73-4cf6186716bf/tool-results/bafb6h9rb.txt (2026-09-14); /Users/siddharth/.claude/plans/help-me-out-here-abstract-wilkinson.md, section 10.1 (2026-09-14)

## 3.2 Pablo Fernandez (IESE): there is no "the" risk premium, and beta is noise

**The claim.** Professionals do not agree on the market risk premium, and a historical beta says almost nothing about a future beta.

**The papers.** "CAPM: An Absurd Model" (October 2014), SSRN 2505597, Spanish original SSRN 2499455: "it is an enormous error to use the historical beta as a proxy for the expected beta." "CAPM: The Model and 307 Comments About It", SSRN 2523870, where 234 of 307 respondents agreed with "absurd". The annual surveys, for example "Market Risk Premium Used in 82 Countries in 2012: A Survey with 7,192 Answers", doi 10.2139/ssrn.2084213.

**Why it matters.** The equity risk premium (ERP) is the single most important input. The surveys show professionals in one country in one year using widely different values. If the key input has no consensus, "the" value of a company is not a well-defined quantity.

**His reply.** He uses bottom-up betas, an average across an industry, precisely because single-firm regression betas are noise. He uses an implied ERP solved from today's prices, not a survey. Read honestly, both are concessions, not refutations. He also disowned "total beta", a spin-off of his own work, which "has taken on a life of its own and is being used in ways I never intended" (BVWire, 26 April 2012).

**What the app will do.** Betas will come from his industry tables, stamped with an industry vintage id. For India the fallback chain will be India, then emerging markets, then Global, switching when an industry has fewer than 10 firms. Today 27 of 94 Indian industry rows are that thin, and every run will print which table it used.

Source: the Report, Part 3.2 (2026-09-14); /Users/siddharth/.claude/projects/-Users-siddharth-Downloads/edcdeb19-7793-4e1b-9e73-4cf6186716bf/tool-results/bkdrkpfng.txt, section 6 (2026-09-14)

## 3.3 Fama and French (1992): the beta and return relation is flat

**The claim.** Once you allow for company size, average stock returns show no reliable relation to beta.

**The paper.** Eugene Fama and Kenneth French, "The Cross-Section of Expected Stock Returns", *Journal of Finance* 47(2): 427 to 465, 1992. https://onlinelibrary.wiley.com/doi/10.1111/j.1540-6261.1992.tb04398.x. Their words: "when the tests allow for variation in β that is unrelated to size, the relation between market β and average return is flat."

**Why it matters.** Every Damodaran cost of equity is the risk-free rate plus beta times ERP, plus a CRP where needed. If beta does not track realized returns, the discount rate is a convention, not a measurement. Counter-attacks exist: Berk 1995 on theory, Kothari and others 1995 on data, Kim 1995 on econometrics, Jagannathan and Wang 1996 on a conditional CAPM. Nobody, however, has restored the simple CAPM.

**His reply.** The Report records none. His practice is the answer: industry betas, plausibility bands for the cost of capital, and ranges rather than points.

**What the app will do.** It will show the cost of capital as a labeled convention with its parts visible, checked against his plausibility bands from Data Update 5 for 2026, with a Monte Carlo range (the spread of results from re-running the model many times with inputs drawn at random) beside the point value.

Source: the Report, Part 3.3 (2026-09-14); /Users/siddharth/.claude/plans/help-me-out-here-abstract-wilkinson.md, section 10.5 (2026-09-14)

## 3.4 Terminal value dominance and input sensitivity: his own published ranges {#r3-sensitivity}

::: {.reading-only .watch-out}
**The same company can produce very different values under different inputs.** Read the numerical examples and the proposed response together.
:::

**The claim.** One or two inputs, especially those feeding the terminal value, can swing a DCF (discounted cash flow model) result tenfold.

Terminal value is the value of every cash flow beyond the forecast years, folded into one number. In a ten-year model it is usually the largest piece. There is no canonical paper. The strongest evidence is a table of his own published ranges.

| Date | Company | The single change | The move |
|---|---|---|---|
| 25 Mar 2014 | Tesla | Sales-to-capital ratio set to 10 | About $110 to $302 per share; his comment: "Magical, right?" |
| 26 Apr 2018 | Amazon | Prime fee $99 to $119 per year | About $100 per share added |
| 6 Feb 2020 | Tesla | Same day, four named stories | $106, $111, $227, $298, $333, $459, $855, $2,106 per share |
| Dec 2014 | Uber | Reader-chosen inputs in his crowd template | Under $1bn to about $100bn; the post states $799 million to $90.5 billion |

**Why it matters.** The sales-to-capital ratio is revenue earned per dollar invested, and it sets how much growth costs. A small change there, or in terminal growth, moves the biggest block of value. A beginner sees one precise number and forgets the 20-fold range behind it.

**His reply.** He publishes the ranges as a feature. On the Uber table he wrote that readers may find their fear "that they can be used to deliver whatever number you want, vindicated, but that is not the way I see it."

**What the app will do.** It will always show the range, never only the point. The terminal value's share of total value and a sensitivity table will be on every screen. The golden case, Almarai at 7.187840270062114 per share against a price of 72.28, pins the terminal cost of capital to the risk-free rate plus the mature-market ERP. The sheet label saying "+4.5%" is misleading, and the engine will not copy it.

Source: the Report, Part 3.4 and Part 6 item 5 (2026-09-14); /Users/siddharth/Downloads/financeMD/damodaran/blog/2014/03/return-to-firing-line-revisiting-tesla.md (2014-03-25); /Users/siddharth/Downloads/financeMD/damodaran/blog/2018/04/amazon-glimpses-of-shoeless-joe.md (2018-04-26); /Users/siddharth/Downloads/financeMD/damodaran/blog/2020/02/a-do-it-yourself-diy-valuation-of-tesla.md (2020-02-06); /Users/siddharth/Downloads/financeMD/damodaran/blog/2014/12/up-up-and-away-crowd-valuation-of-uber.md (2014-12); /Users/siddharth/.claude/projects/-Users-siddharth-Downloads/edcdeb19-7793-4e1b-9e73-4cf6186716bf/tool-results/bkdrkpfng.txt (2026-09-14)

## 3.5 Mauboussin and Rappaport: run the model backwards {#r3-reverse}

::: {.reading-only .key-idea}
**Start from the price and ask what it requires.** This gives you assumptions to debate alongside a forward valuation.
:::

**The claim.** Forecasting cash flows is the weakest link, so start from the price, extract the expectations it implies, and judge whether those are achievable.

**The book.** Michael J. Mauboussin and Alfred Rappaport, *Expectations Investing: Reading Stock Prices for Better Returns*, revised edition, Columbia Business School Publishing, 2021. Reviewed by the CFA Institute's *Enterprising Investor*, 2022: https://rpc.cfainstitute.org/blogs/enterprising-investor/2022/book-review-expectations-investing. About ten free tutorials and a reverse-DCF spreadsheet live at expectationsinvesting.com.

**Why it matters.** A reverse DCF is the same model run the other way. It turns an unfalsifiable point ("worth $427") into a testable operating claim ("this price requires $600 to 800bn of revenue at margins above 20%"). That is anti-forecast, not anti-DCF.

**His reply.** He does this himself. His November 2021 Tesla post is the clearest case, and the most defensible thing in his Tesla arc. Justifying the market value, he wrote, "will require a real stretch."

**What the app will do.** Every memo will compute the reverse DCF first: keep margin and cost of capital fixed, solve for the year-10 revenue the price implies, convert it to an implied market share, and run that share through the 3P test from Chapter C1.

Source: the Report, Part 3.5 and Part 6 item 1 (2026-09-14); /Users/siddharth/Downloads/financeMD/damodaran/blog/2021/11/teslas-trillion-dollar-moment-valuation.md (2021-11); /Users/siddharth/.claude/plans/help-me-out-here-abstract-wilkinson.md, section 10.5 (2026-09-14)

## 3.6 Marcos López de Prado: discretionary valuation is not science {#r3-testing}

::: {.reading-only .watch-out}
**Distinguish an arithmetic test from a forecasting record.** Read what would make a valuation claim testable after it is published.
:::

**The claim.** A valuation built by hand cannot be falsified, so it is not a scientific claim.

**The papers.** "Causal Factor Investing: Can Factor Investing Become Scientific?", SSRN 4205613. "Pseudo-Mathematics and Financial Charlatanism" (Bailey, Borwein, López de Prado and Zhu, *Notices of the AMS*, 2014) and "The Probability of Backtest Overfitting". *Advances in Financial Machine Learning* (Wiley, 2018), which you own at /Users/siddharth/Downloads/finance-and-valuation/Advances in Financial Machine Learning Marcos Lopez de Prado.pdf, with a markdown copy in financeMD.

**Why it matters.** A backtest tests a rule on past data. With enough trials on one dataset, an attractive result appears even in random data, so he asks that every trial be reported. Against Damodaran the sharp form has three parts: no out-of-sample test, no record of how many input sets were tried, and no failure criterion, since "the price converges eventually" can never be wrong on a finite horizon.

**His reply.** Partial but real. He timestamps and publishes every valuation before the outcome, publishes the spreadsheet, and reports his losses. That is closer to preregistration, meaning declaring your test before you run it, than most of the industry manages.

**What the app will do.** The Almarai golden test at 1e-6 makes the implementation falsifiable even though the forecast is not. Every screen will carry the banner "The engine is tested (Almarai 1e-6). The forecast is not." Every run will be stored with its inputs, an input hash and three vintage ids. From M4 an accuracy scoreboard will record the realized price at 90, 180 and 365 days, and compute bias and variance by sector, region and vintage. That is the record of trials he asks for.

Source: the Report, Part 3.6 and Part 6 item 2 (2026-09-14); /Users/siddharth/.claude/plans/help-me-out-here-abstract-wilkinson.md, sections 5 (M4) and 10.1 (2026-09-14)

## 3.7 Cliff Asness and AQR: cheapness works, except when it does not for a decade

**The claim.** The systematic evidence for cheapness is strong, and single-name story valuation is the weakest way to harvest it.

**The record.** "Is (Systematic) Value Investing Dead?" (AQR, May 2020) measured the value spread, the price gap between cheap and expensive stocks, as the widest ever, beyond the 2008 crisis and the dot-com peak. In 2025 Asness said, "basically, every aspect of what we do is working, with the exception of famous value investing." He remains "really confident" at a three-year horizon, with the spread near late-1990s extremes.

**Why it matters.** AQR supplies the most honest counter to the Tesla and Nvidia record. Being right on value and early is, over any investable horizon, indistinguishable from being wrong. That sentence is the thesis of this whole reader.

**What the app will do.** The scoreboard will measure at fixed horizons, so "eventually" gets a date. A test will reject any output containing advice words.

Source: the Report, Part 3.7 (2026-09-14); /Users/siddharth/.claude/plans/help-me-out-here-abstract-wilkinson.md, section 10.1 (2026-09-14)

## 3.8 Cathie Wood and ARK versus Damodaran on Tesla

**The claim.** Tesla is not a car company, so its worth lies far above anything a car-company DCF can reach.

**The record, as history.** In February 2018 ARK published a figure of $4,000 per share, before the splits. It was widely mocked and reached ahead of schedule. In January 2020 ARK projected $7,000 by 2024, about $1,400 after the splits. In June 2024 ARK published $2,600 by 2029 or 2030 and reaffirmed it through 2025, while Tesla traded around $240 to $320 in 2025.

**His reply.** ARK's work was "a forward pricing for Tesla, not a valuation", with no discounted cash flows and incomplete scaling costs. The robotaxi line of about $1 trillion "strikes me as more fairy tale than valuation."

**Scorecard.** Wood wins 2018 to 2021 decisively. Damodaran wins 2022 to 2026, and his method point has aged well: a figure with no discounting and no charge for capital is a pricing, not a valuation.

**What the app will do.** Every driver in a memo will link to a named story line, following the workbook's "Stories to Numbers" sheet, and every claim will pass the 3P gate. Pricing and valuation will be labeled as different things, as Chapter C6 explains.

Source: the Report, Part 3.8 (2026-09-14); /Users/siddharth/Downloads/financeMD/damodaran/blog/2019/06/teslas-travails-curfew-for-corporate.md (2019-06-03)

## 3.9 Bill Gurley: twice, from both directions

**The claims.** In 2014, that Damodaran picked the wrong total addressable market (TAM) for Uber. In 2016, that his own industry's private marks were not prices.

**The record.** "How to Miss By a Mile" (11 July 2014) is Chapter 4, episode 1. "On the Road to Recap" (21 April 2016), https://abovethecrowd.com/2016/04/21/on-the-road-to-recap/, counted unicorns rising from about 80 in February 2015 to 229 in January 2016, with zero VC-backed tech IPOs in the first quarter of 2016. His line: "the last round is not the permanent price."

**Why it matters.** Gurley beat Damodaran with a better narrative and the same discipline, then turned that skepticism on his own side. He is not a growth cheerleader. He is a better storyteller.

**His reply.** He emailed Gurley, re-ran his own model on Gurley's story, got $54bn instead of $5.9bn, and published both spreadsheets.

**What the app will do.** A second, opposing memo per company will be mandatory. The memo table will carry a `story_kind` field with values base and opposing. The plan calls this the "Gurley field".

Source: the Report, Parts 3.9 and 2.5 (2026-09-14); /Users/siddharth/Downloads/financeMD/damodaran/blog/2014/07/possible-plausible-and-probable-big.md (2014-07-16); /Users/siddharth/.claude/plans/help-me-out-here-abstract-wilkinson.md, sections 1 and 10.3 (2026-09-14)

## 3.10 Nassim Taleb: the distributions are wrong

**The claim.** Financial returns have fat tails, meaning extreme moves are far more common than a bell curve allows, so sample averages, variances and regressions are unreliable.

**The book.** *Statistical Consequences of Fat Tails: Real World Preasymptotics, Epistemology, and Applications* (2020), free at https://arxiv.org/pdf/2001.10488.

**Why it matters.** Three hits. A historical ERP is the average of a fat-tailed series, so its error bar is enormous. A regression beta is a ratio of variances, so it is unstable, which is Fernandez's point from another direction. Monte Carlo runs with normal or triangular inputs understate the tails. His Paytm simulation gave a "3% chance the equity is worth nothing", and the realized fall was about 70% within a year.

**The balance.** Critics of Taleb say he confuses statistical extremeness with economic significance. Damodaran's truncation term, an explicit failure probability times a recovery value, is a crude but real fat-tail bolt-on.

**What the app will do.** Failure probability and the recovery fraction will be visible inputs, from workbook cells B51 to B54, where the default recovery is 50%. Monte Carlo draws will come from the workbook's industry quartile tables rather than a bell curve. Even so, the UI copy will say the range understates the tails.

Source: the Report, Part 3.10 (2026-09-14); /Users/siddharth/.claude/projects/-Users-siddharth-Downloads/edcdeb19-7793-4e1b-9e73-4cf6186716bf/tool-results/bkdrkpfng.txt, Input rows B51 to B54 (2026-09-14)

## 3.11 Andrew Lo: the premium is not a constant

**The claim.** Market efficiency and risk premia drift with the mix of participants, their learning and the environment, so no premium is a fixed parameter.

**The work.** *Adaptive Markets: Financial Evolution at the Speed of Thought* (Princeton, 2017); "The Adaptive Markets Hypothesis: Market Efficiency from an Evolutionary Perspective", SSRN 602222; Lo and Zhang, *The Adaptive Markets Hypothesis* (Oxford University Press, 2024).

**Why it matters.** One stamped "mature market ERP" is a convenience, not a measurement. One 2026 US snapshot already carries three risk-free rates (3.95%, 4.58% and 4.75%) and three premiums (4.46%, 4.23% and 4.20%), depending on which of his files you open; the guide's database chapter pairs them. His 15 July 2026 post derives the 4.20% as a 4.42% implied ERP minus the 0.22% default spread for the US Aa1 rating, with a 1.55 scalar for equity against bond volatility.

**What the app will do.** Every run will stamp three vintage ids, market, country risk and industry, and show them. A number with no vintage will be refused. The regime panel will show the September 2026 implied ERP of 4.09% and expected return of 8.84% as dated readings, never as constants.

Source: the Report, Part 3.11 and Part 6 item 6 (2026-09-14); /Users/siddharth/Downloads/financeMD/damodaran/blog/2026/07/country-risk-drivers-measures-and.md (2026-07-15); /Users/siddharth/.claude/projects/-Users-siddharth-Downloads/edcdeb19-7793-4e1b-9e73-4cf6186716bf/tool-results/btzaixzyh.txt, regime spec (2026-09-14)

## 3.12 Ben Thompson and Aggregation Theory: the narrative critique from the other side

**The claim.** Aggregators own the customer relationship and turn suppliers into commodities, so a DCF that pulls their margins toward an industry average is biased against them by construction.

**The essays.** "Defining Aggregators" (2017), https://stratechery.com/2017/defining-aggregators/, and "Neither, and New: Lessons from Uber and Vision Fund" (2019), https://stratechery.com/2019/neither-and-new-lessons-from-uber-and-vision-fund/.

**Why it matters.** This is not "DCF is bad". It is "your convergence defaults encode a theory of competition that may not fit this business". The default margin path and the sector sales-to-capital ratio quietly deny the mechanism that makes an aggregator valuable. That is fixable in software.

**What the app will do.** The margin the model converges to, the year of convergence (workbook cell B30, default 5) and the sales-to-capital source will be selectable and labeled with the theory each encodes. No silent sector median. Stratechery is a paid newsletter, so it will be stored as `link_only` and never ingested.

Source: the Report, Part 3.12 and Part 6 item 4 (2026-09-14); /Users/siddharth/.claude/projects/-Users-siddharth-Downloads/edcdeb19-7793-4e1b-9e73-4cf6186716bf/tool-results/bkdrkpfng.txt, Input row B30 (2026-09-14)

## 3.13 The 2024 to 2026 debate cluster

These arguments are live as of September 2026. The Report drew them from the web and from his 2026 posts.

| Debate | His position | The other side | Status, Sep 2026 |
|---|---|---|---|
| AI TAM | Ceiling about $26tn, realistically far less; AI product revenue about $250bn against $1.7tn of capital spending (capex) | xAI bankers: $22tn TAM; OpenAI and Anthropic valuations toward $2tn | Unresolved; Anthropic annual recurring revenue (ARR) $65bn, OpenAI about $40bn, both growing fast, Anthropic $10 to 15bn below estimates |
| AI macro | Framework first, refuses a point scenario | Citrini Research (22 Feb 2026): unemployment above 10%, market down 40% by June 2028, private credit collapse | Unresolved; drove a real market drop |
| Private credit | "Setting itself up for a beating"; contagion risk | Private-credit sponsors funding data centers | Unresolved |
| Conviction and concentration | Conviction is not a virtue | Aschenbrenner's Situational Awareness fund | Resolved against the other side: up 450%, then a 67% loss on the public book in 4 weeks, then a forced sale to Citadel |
| Rates and equities | Higher rates do not lower all stocks equally; it depends on sector and cash-flow timing | The reflexive "rates up, stocks down" trade | Live, Sep 2026 (US debt above $40tn, Warsh Fed) |
| VC scaling | Scaling and profitability trade off; VC's weakest link | Vinod Khosla | Live |

**What the app will do.** The market-regime panel will be descriptive only. Like him, it will refuse a point scenario and print his own market-timing caveats on the panel.

Source: the Report, Part 3.13 (2026-09-14); /Users/siddharth/Downloads/financeMD/damodaran/blog/2026/08/ais-bar-mitzvah-moment-from-hype-hope.md (2026-08-20); /Users/siddharth/Downloads/financeMD/damodaran/blog/2026/08/the-situational-awareness-blow-up.md (2026-08-10); /Users/siddharth/.claude/plans/help-me-out-here-abstract-wilkinson.md, section 10.7 (2026-09-14)

## What he got right, in one list

His usual reply to a critique is "I know, and here is my workaround." Fairness requires the list.

- Bottom-up industry betas, because single-firm betas are noise (Fernandez).
- An implied ERP solved from prices, not a historical average (Taleb, Lo).
- An explicit failure probability with a recovery value (Taleb).
- Published ranges 20 times wide, and public spreadsheets before the outcome (López de Prado).
- Re-running his own model on an opponent's story (Gurley).
- The method objection to a pricing without discounting (ARK).
- A country-risk table that works across 180 countries when nothing else does (Kruschwitz, Löffler and Mandl).

Source: the Report, Parts 3.1 to 3.11 (2026-09-14)

## The map from critique to feature {#r3-feature-map}

::: {.reading-only .key-idea}
**Use this table to connect the argument to the build.** It is the shortest route from the critiques to their practical consequences.
:::

| Critique | App response | Milestone |
|---|---|---|
| CRP has no theory | Country-risk vintage id; risk-free net of default spread | M2, India in M4 |
| No consensus ERP, beta is noise | Industry betas, fallback chain printed, Monte Carlo range | M2, M4 |
| Beta and return flat | Cost of capital shown as a labeled convention with plausibility bands | M2 |
| Input sensitivity | Range always; terminal-value share; sensitivity table | M2, M4 |
| Invert the model | Reverse DCF computed first in every memo | M2 |
| Not falsifiable | Golden test at 1e-6; stored runs; scoreboard at 90, 180, 365 days | M2, M4 |
| Right and early equals wrong | Fixed-horizon scoring; no advice test | M4 |
| Not a valuation | Every driver linked to story; 3P gate | M2 |
| Better story beat him | Mandatory opposing memo | M2 |
| Fat tails | Visible failure inputs; quartile-based draws; honest UI copy | M4 |
| Premia drift | Three vintage ids on every run | M2 |
| Convergence bias | Labeled, selectable convergence and sales-to-capital sources | M4 |

Source: the Report, Part 6 (2026-09-14); /Users/siddharth/.claude/plans/help-me-out-here-abstract-wilkinson.md, sections 5 and 10 (2026-09-14)
