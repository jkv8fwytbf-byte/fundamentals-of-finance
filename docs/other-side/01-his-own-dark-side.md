# The Other Side, Chapter 1: His Own Dark Side

Damodaran wrote a whole book about where his own method breaks. It is called The Dark Side of Valuation. This chapter turns it into ten claims. Each claim gets one sentence, a plain explanation, and a note on where it will show up in your app. Source names follow Chapter 0. "Report" is the critics research file. "Preface" is the local copy of his third-edition preface. "Survey" is the corpus survey. "Schema" is the model schema report for the fcffsimpleginzu workbook.

Source: Report, Part 1 (2026-09-14); /Users/siddharth/Valuation/docs/other-side/00-read-me-first.md.

## The book in one paragraph

The full title is The Dark Side of Valuation: Valuing Young, Distressed, and Complex Businesses. The third edition came out in 2018 from Pearson/FT Press, ISBN 9780134854243. It has five parts and twenty chapters: the tools, macro inputs, the life cycle, company types, and a finale. Chapter 20 is "Lighting the Way: Vanquishing the Dark Side". Three things pushed him to a third edition. Interest rates had hit historic lows, and gone negative in places. Risk premiums had turned volatile, with a crisis almost every year. And globalization had stalled, so political risk mattered again.

Source: Report, Part 1 (2026-09-14); Preface, /Users/siddharth/Downloads/financeMD/damodaran/New_Home_Page/DSV3/dsv3edpreface.md.

What does "dark side" mean? In his preface the idea dates to late 1999, at the end of the dot-com boom. Standard models could not explain technology stock prices. So analysts dropped the models and justified prices with new metrics and storytelling. That is the dark side: abandoning the model when the company does not fit it. His preface says the temptation returns whenever "analysts have trouble fitting companies into traditional models and metrics". The book is his answer: keep the model, and do the harder estimation honestly.

Source: Preface, /Users/siddharth/Downloads/financeMD/damodaran/New_Home_Page/DSV3/dsv3edpreface.md (accessed 2026-09-14).

## Where the material lives, and what is missing

The three free Dark Side decks are not in your local corpus. The folder financeMD/damodaran/pdfiles/country/ holds one file, the 208-page India seminar val2dayIndia2025. The Report explains why. All three decks are image-heavy scans. A normal PDF-to-text pass returns nothing useful. They need OCR, which is software that reads letters out of pictures. Until then, this chapter quotes the preface, because the preface is clean text in the corpus.

Source: Survey, line 45 (2026-09-14); Report, Part 1, free sources table and ingestion note (2026-09-14).

| Item | URL | Note from the Report |
|---|---|---|
| Core deck | https://pages.stern.nyu.edu/~adamodar/pdfiles/country/darkside.pdf | Short, start here |
| Full-day seminar deck (2012) | https://pages.stern.nyu.edu/~adamodar/pdfiles/country/darkside2012full.pdf | The most complete free version |
| Extended "Jedi Guide" deck (2013) | https://pages.stern.nyu.edu/~adamodar/pdfiles/country/darksideextended13.pdf | About 3.5 MB, image-heavy, needs OCR |
| Third-edition preface and chapter map | https://pages.stern.nyu.edu/~adamodar/New_Home_Page/DSV3/dsv3edpreface.html | Free, and mirrored locally |

Source: Report, Part 1, free sources table (2026-09-14).

One warning about names. The corpus also has New_Home_Page/darkside.md, a first-edition chapter list, and New_Home_Page/darkside/darkside.md, the first-edition book site that valued five technology firms: Amazon, Ariba, Cisco, Motorola and Rediff. They are history, not the current book.

Source: /Users/siddharth/Downloads/financeMD/damodaran/New_Home_Page/darkside.md and darkside/darkside.md (accessed 2026-09-14).

## The ten claims

### 1. The dark side is not a different model, it is the same model with no data

When a company is young, losing money, or in trouble, he does not switch tools. He keeps the DCF (discounted cash flow model, which values a company as the sum of its future cash flows discounted to today) and makes every estimate harder and more explicit. In his 2014 Uber post he calls refusing to value uncertain companies a cop-out, because ignoring uncertainty does not remove it. Think of a doctor with a patient who has no medical history. The doctor still examines the patient, and labels each guess as a guess.

In the app: the memo writer will never refuse a company. It will name the uncertainty type and pull the matching Dark Side passages before proposing any input.

Source: Report, Part 1, bullet 1 (2026-09-14); blog/2014/06/a-disruptive-cab-ride-to-riches-uber.md (2014-06-09); plan, /Users/siddharth/.claude/plans/help-me-out-here-abstract-wilkinson.md, item 4.

### 2. The risk-free rate is not risk-free

Chapter 6 is titled "A Shaky Base: A Risky Risk free Rate". A risk-free rate is the return on a bond that cannot default. Governments can default, and some bonds carry negative yields. His fix is to subtract the default spread, the extra yield that pays for default risk. He now does this to the United States. His July 2026 post starts from an implied premium of 4.42%, with the S&P 500 at 7,499.36 on 1 July 2026. He nets out the 0.22% Aa1 default spread to reach a 4.20% mature-market premium.

In the app: the risk-free rate will be a labeled input with a vintage id, never a hard-coded number. One 2026 US snapshot holds three different risk-free rates (3.95%, 4.58% and 4.75%) and three different premiums (4.46%, 4.23% and 4.20%), depending on which of his files you open; the guide's database chapter shows which goes with which. For India the rate will be the 10-year G-sec (Indian government bond) yield minus the India default spread.

Source: Report, Part 1, bullet 2 (2026-09-14); blog/2026/07/country-risk-drivers-measures-and.md (2026-07); datasets catalog bafb6h9rb.txt; plan, M4 item 1.

### 3. The equity risk premium moves, so a fixed number is wrong by construction

The equity risk premium, or ERP, is the extra return investors demand for stocks over safe bonds. Chapter 7 argues it changes with time. He estimates an implied ERP, meaning the premium today's prices already contain. During COVID he republished it almost daily. On 1 April 2020 it stood at 6.01%, then 6.27% on stale earnings and 5.60% assuming a 30% earnings drop. The September 2026 value is 4.09%, with an expected return on US stocks of 8.84%.

In the app: every run will store three vintage ids, for market, country risk, and industry. The market-regime panel will plot his monthly implied ERP against history, descriptively only.

Source: Report, Part 1, bullet 3 (2026-09-14); blog/2020/04/a-viral-market-update-vii-mayhem-with.md (2020-04-24); regime spec in btzaixzyh.txt; financeMD/damodaran/pc/implprem/ERPbymonth.md.

### 4. Country risk is real, additive, and estimated by scaling default spreads

His method has three steps. Take the sovereign rating. Convert it to a default spread. Scale that spread up by the ratio of stock volatility to bond volatility, which was 1.55 in July 2026. The result is the country risk premium, or CRP, added on top of the mature-market premium. He admits the method is crude. In the same post he confesses to simplistic assumptions and cut corners, and says any fix must still work across 180 countries. That admission is the hinge of the academic attack in Chapter 3.

In the app: India's January 2026 row is Moody's Baa3, default spread 1.87%, total ERP 7.08%, CRP 2.85%. The July 2026 row is 1.75%, 6.92% and 2.72%. They are separate vintages and never mixed.

Source: Report, Part 1, bullet 4 (2026-09-14); blog/2026/07/country-risk-drivers-measures-and.md (2026-07); datasets catalog bafb6h9rb.txt.

### 5. Growth is not free, and it is not always good

Growth must be paid for with reinvestment, the money a company plows back into plants, stock and software. In the workbook, reinvestment equals the change in revenue divided by the sales-to-capital ratio. That ratio says how many units of revenue each unit of invested capital produces. A low ratio means expensive growth. Growth that earns less than its cost of capital destroys value.

In the app: sales-to-capital will be a labeled input whose default will come from the Global industry table. For Indian firms the fallback order will be India, then emerging markets, then Global, switching when a row has fewer than 10 firms. 27 of the 94 Indian industry rows are that thin.

Source: Report, Part 1, bullet 5 (2026-09-14); Schema, sections 1.3 and 6; datasets catalog bafb6h9rb.txt.

### 6. All good things end, so excess returns must converge

Excess return means earning more on capital than that capital costs. Chapter 20 is about the discipline of the endgame. In terminal value, return on capital must fall to the cost of capital, and growth must fall to the risk-free rate. The workbook enforces this by default. Terminal cost of capital equals the risk-free rate plus the mature-market ERP. The cell label says "+4.5%", but the formula adds the vintage's mature ERP, 4.23% for January 2026. Code the formula, not the label.

In the app: the three terminal overrides (stable cost of capital, stable return on capital, perpetuity growth) will be labeled switches, and turning one on will be recorded in the run.

Source: Report, Part 1, bullet 6 (2026-09-14); Schema, section 1.6 and note on the label mismatch.

### 7. A going-concern DCF over-values firms that can die

A DCF assumes the company survives to reach stable growth. Many young or indebted firms do not. So he bolts on a truncation term: a probability of failure, and what is recovered if it fails. His own settings: Tesla 2013 at 10% failure with 50% recovery; Tesla 2014 at 0%; Tesla 2019 at 20%; Uber 2014 at 10% with zero liquidation value. The workbook holds this in four cells: the switch, the probability, whether proceeds are tied to book or fair value, and the recovery percentage. Its Failure Rate worksheet offers priors, for example a 10-year default probability of 11.78% for a BB rating and 50.38% for CCC/C. That sheet has zero formula links; a human reads a number and types it in.

In the app: the truncation probability will be a required field in every memo, with its source. The BLS (US Bureau of Labor Statistics) business survival tables in the sheet are US data, so for India they will be a prior only.

Source: Report, Part 1, bullet 7 (2026-09-14); blog/2013/09/valuation-of-week-1-tesla-test.md (2013-09-04); blog/2019/06/teslas-travails-curfew-for-corporate.md (2019-06-03); Schema, sections 1.6, 3.5 and 6.

### 8. Cyclical and commodity firms must be normalized, not extrapolated

Chapter 14 covers companies whose earnings swing with the economy or a commodity price. Their base-year earnings are one point on a cycle, not a level. Normalizing means replacing this year's number with an average across a full cycle. The alternative is to forecast the commodity price itself. Either is allowed, but the analyst must disclose which. The simple ginzu workbook has no earnings normalizer; the full ginzu does.

In the app: the memo will state whether the base year was normalized, and how, before the calculator runs.

Source: Report, Part 1, bullet 8 (2026-09-14); Schema, section 5.

### 9. A DCF is trivially gameable, and he shows you how

His 25 March 2014 Tesla post is the strongest input-sensitivity critique in the literature, and it is his own. He compares a spreadsheet of cash flows to a costume: wearing the outfit does not make you a dancer. Then he sets the sales-to-capital ratio to 10.0 and the value per share jumps to $302. His own estimate at that moment was about $110 to $115. That is a 2.7 times swing from one input.

In the app: every valuation will carry a sensitivity table and a Monte Carlo range (thousands of runs with randomly drawn inputs) drawn from his industry quartiles. Guard rails will reject inputs outside his published plausibility bands.

Source: Report, Part 1, bullet 9 (2026-09-14); blog/2014/03/return-to-firing-line-revisiting-tesla.md (2014-03-25); read-this-first.md, sections 3.5 and 4.

### 10. Value is story plus numbers, and the story is the binding constraint

His test is possible, then plausible, then probable. A claim that cannot get past plausible does not earn its cash flows. Chapter 1 of Document C explains the test in full. Both camps attack this frame. Venture investors say his stories are too small. Quantitative critics say stories cannot be falsified. Chapters 3 and 4 contain those arguments.

In the app: only probable claims may set a base-case input. Plausible claims set a scenario. Possible claims are recorded at zero. A second, opposing memo per company will be mandatory.

Source: Report, Part 1, bullet 10 (2026-09-14); plan, item 4; /Users/siddharth/Valuation/docs/damodaran-essentials/c1-why-value-story-and-the-3p-test.md.

## The hard company types, and where the app will meet them

| Company type | Book chapter | Why it is hard | What the app will do |
|---|---|---|---|
| Start-up or idea business | 9, 10 | No revenue, no history, high failure odds | Uncertainty type "young", truncation probability required |
| Growth company | 11 | Fast revenue growth, margins not yet visible | Convergence year and target margin as labeled inputs |
| Mature company | 12 | Value hides in restructuring and control | Standard run; opposing memo tests the restructuring story |
| Distressed or declining | 13 | Negative growth, real bankruptcy risk | Failure probability and recovery percentage required |
| Cyclical or commodity | 14 | Earnings are one point on a cycle | Memo must state the normalization method |
| Financial service | 15 | Debt is raw material, regulation moves value | Synthetic rating (a credit rating estimated from interest coverage) uses the financial-service band (firm type 3) |
| Intangible-heavy | 16 | Accounting treats R&D as an expense | R&D converter switch, labeled |
| Emerging market | 17 | Country risk, currency, thin data | CRP vintage, INR risk-free rule, industry fallback recorded |
| Multi-business, global | 18 | Pieces interact across countries | Cost of capital by business weights and operating regions |
| Unusual entities | 19 | Infrastructure, sports teams, cryptocurrency | Out of scope for v1 |

Source: Preface chapter outline; Schema, sections 2.6, 3.4 and 6; plan, item 4 (2026-09-14).

## What he got right here

Three things deserve credit. First, he wrote the gaming critique in claim 9 against himself, with his own numbers. Second, he publishes his failure probabilities, so anyone can check them years later, as Chapter 2 does. Third, claim 3 was tested live in 2020, when he republished the implied ERP through the crash instead of freezing it. Chapter 4 lists that series among his wins.

Source: Report, Parts 1, 2.1 and 4 (2026-09-14); /Users/siddharth/Valuation/docs/other-side/04-twelve-episodes.md.

## Three things to remember

- The dark side is a behavior, not a company type. It is abandoning the model when the model gets hard.
- Every one of the ten claims becomes a labeled input, a range, or a required field in your app. None becomes a bare point estimate.
- The three free decks need OCR before the librarian can quote them. Until then, quote the preface.

Source: Report, Part 1 (2026-09-14); plan, items 1, 2 and 4.
