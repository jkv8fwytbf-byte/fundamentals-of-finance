# The Other Side, Chapter 6: What This Means for the App {#r3-app}

::: {.reading-only .read-first}
**This is the payoff of the critics reader.** Trace each criticism into a concrete rule: reverse DCF, an opposing story, recorded assumptions, ranges, and later scoring.
:::

Chapters 1 to 5 collected the case against the method your system copies. This chapter turns that case into rules for the build. Each rule names the critique it answers. Think of the critiques as crash reports and the rules as the seat belts fitted afterwards. Nothing beyond the documents is built yet, so every rule says "will".

Sources. "Report" means /Users/siddharth/Desktop/Valuation/docs/sources/bkm2kob5x.txt (compiled 2026-09-14). "Plan" means /Users/siddharth/Desktop/Valuation/docs/plan.md. "Document A" means /Users/siddharth/Desktop/Valuation/docs/read-this-first.md. "blog/" means /Users/siddharth/Downloads/financeMD/damodaran/blog/.

Source: Report, Part 6 (2026-09-14).

## The rules at a glance

| # | Rule | The critique it answers | Read it in |
|---|---|---|---|
| 1 | Reverse DCF before forward DCF | Mauboussin and Rappaport; López de Prado | Chapter 3 |
| 2 | Log every run with a timestamp, score it later | López de Prado, "no out-of-sample test" | Chapters 2 and 3 |
| 3 | Opposing narrative field, mandatory | Gurley on Uber, July 2014 | Chapter 4, episode 1 |
| 4 | Terminal-value share and convergence as labeled inputs | Thompson's aggregation theory; input sensitivity | Chapter 3 |
| 5 | Always the range, always the truncation probability | His own 20 times grid; Taleb on fat tails | Chapters 2 and 3 |
| 6 | Vintage-stamp everything, show the stamp | Andrew Lo's drifting premium | Chapter 3 |
| 7 | The banner: engine tested, forecast not | López de Prado | Chapter 3 |
| 8 | The licensing line | Corpus and reading-list hygiene | Chapters 0 and 5 |
| 9 | Estimates and ranges, never advice | Every episode in Chapter 4 | Chapter 4 |

Source: Report, Part 6 (2026-09-14).

## Rule 1: the reverse DCF comes first

A forward DCF forecasts cash flows and turns them into a value. A reverse DCF starts from today's price and solves for the assumptions that price needs. Mauboussin and Rappaport call the result "[price-implied expectations]{.reading-highlight}". Forecasting is the weakest link, so start from the one thing you know, the price.

The Report says this turns an unfalsifiable number into a testable claim. "Tesla is worth $427" cannot be checked today. "The price requires $600 to 800 billion of revenue at margins above 20%" can be argued about now. Damodaran did this himself in his November 2021 Tesla post.

So every valuation screen will answer "what does the price require?" before "what is it worth?". The memo writer will compute the reverse DCF first, then run the implied market share through the possible, plausible, probable test.

Source: Report, Parts 3.5 and 6, item 1 (2026-09-14); Expectations Investing, revised edition, 2021, reviewed at https://rpc.cfainstitute.org/blogs/enterprising-investor/2022/book-review-expectations-investing ; blog/2021/11/teslas-trillion-dollar-moment-valuation.md (2021-11-09); Plan, section 10.5.

## Rule 2: log every valuation with a timestamp and score it later

López de Prado's charge has three parts. A discretionary DCF has no out-of-sample test. It keeps no record of how many input sets were tried. And "the price will converge eventually" cannot be proven wrong on any finite horizon. Damodaran's partial answer is that he publishes every valuation before the outcome and reports his own losses. The Report calls that closer to preregistration than most of the industry. Preregistration means writing your prediction down before you see the result.

The Report puts it bluntly: the most credible thing in his 803 posts is the habit of publishing first and grading later. The app copies it. A `valuation_run` table will store the as-of date, every input, the output and the [three vintage ids]{.reading-highlight}. After 90, 180 and 365 days a job will record the realized price. The scoreboard will then show bias (average signed error) and variance (its spread).

Source: Report, Parts 3.6 and 6, item 2 (2026-09-14); Document A, section 6; Plan, sections 10.3 and 10.6.

## Rule 3: the opposing narrative field is mandatory

On 9 June 2014 Damodaran valued Uber's equity at $5.895 billion, on a $100 billion taxi market. On 11 July 2014 Bill Gurley published "How to Miss By a Mile", arguing the market was $1.3 trillion of car ownership. On 16 July 2014 Damodaran re-ran his own model on Gurley's story and got $54 billion. He wrote that Gurley's story "has the advantage over mine". The pair taught more than either number alone.

So every company will carry [two memos]{.reading-highlight}, a base story and an opposing one, marked `story_kind = opposing`. The pipeline will refuse to finish without it. Two stories, two values, one screen.

Source: Report, Parts 2.5 and 6, item 3 (2026-09-14); blog/2014/07/possible-plausible-and-probable-big.md (2014-07-16); https://abovethecrowd.com/2014/07/11/how-to-miss-by-a-mile-an-alternative-look-at-ubers-potential-market-size/ (2014-07-11); Plan, section 1, item 4.

## Rule 4: terminal-value share and convergence are labeled inputs

Terminal value is the value of all cash flows after the forecast years, folded into one number. Convergence is the assumption that a company's margins drift toward an industry average. Ben Thompson's aggregation theory says some companies own the customer relationship and get stronger with scale. A model that quietly pulls their margins to a sector median denies what makes them valuable.

The Report calls this the most useful critique for the product, because software can fix it. The margin the model converges to, and the source of the sales-to-capital ratio (how many rupees or dollars of revenue each unit of invested capital produces; a high number means growth needs little reinvestment), will be editable inputs labeled with the theory they encode. The screen will also show what share of value sits in the terminal value. His own posts show why. Sales-to-capital set to 10 moved his Tesla value from about $110 to $302 on 25 March 2014. A Prime fee change from $99 to $119 added about $100 per share to Amazon on 26 April 2018.

Source: Report, Parts 3.4, 3.12 and 6, item 4 (2026-09-14); https://stratechery.com/2017/defining-aggregators/ (2017); Plan, section 10.5.

## Rule 5: always show the range, and make the truncation probability explicit

On 6 February 2020 Damodaran published a do-it-yourself Tesla grid. Same company, same day, values from $106 to $2,106 per share. He published a 20 times range as a feature. A single point estimate in the app would be less honest than the source.

Truncation probability is the chance the company fails before reaching stable growth. Taleb's critique is that Monte Carlo runs (re-running the model thousands of times with inputs drawn at random from assumed ranges) with normal or triangular input shapes understate the tails. The Report's example is Paytm: the simulation gave a 3% chance the equity was worth nothing, and the stock fell about 70% within a year. The balancing view is that the truncation term is a crude but real fat-tail bolt-on. So the app will always show the range and the sensitivity table, with the failure probability and recovery assumption as named inputs.

Source: Report, Parts 3.4, 3.10 and 6, item 5 (2026-09-14); blog/2020/02/a-do-it-yourself-diy-valuation-of-tesla.md (2020-02-06, "$2,106/share"); Document A, section 3.5.

## Rule 6: vintage-stamp everything, and show the stamp

A vintage is one dated snapshot of Damodaran's tables. Andrew Lo's adaptive markets hypothesis says risk premiums drift as the people in the market change and learn. So a single "mature market ERP" is a convenience, not a constant. The 2026 data alone carries three risk-free rates, 3.95%, 4.58% and 4.75%, and three equity risk premiums (ERPs, the extra return investors demand for holding stocks over a risk-free bond), 4.20%, 4.23% and 4.46%. The Report says this is not a data bug. It is Lo's critique made concrete. His own 15 July 2026 update shows the drift: the 4.20% mature premium is a 4.42% implied ERP minus the 0.22% US Aa1 default spread.

Every run will store three vintage ids, market, country risk and industry. The database will refuse a run without all three. The screen will show the stamp, not just store it.

Source: Report, Parts 3.11 and 6, item 6 (2026-09-14); Document A, section 3.2; Plan, section 10.1.

## Rule 7: the banner

::: {.reading-only .watch-out}
**Keep this distinction visible.** Matching the workbook validates the implementation; forecasting quality still needs evidence over time.
:::

The Almarai golden test is the engineering answer to López de Prado. The engine must reproduce 7.187840270062114 per share within 0.000001 before any code merges. That makes the implementation falsifiable even though the forecast is not. The scoreboard page will carry one banner: "The engine is tested (Almarai 1e-6). The forecast is not."

Source: Report, Part 3.6 (2026-09-14); Document A, sections 3.1 and 6.

## Rule 8: the licensing line

A license class is a label saying what the app may do with a fact. The Report's line is short. Stratechery and the books are link-only, never ingested. SSRN author-posted PDFs, arXiv, AQR Insights, abovethecrowd.com and Damodaran's own site are ingestible, with source and license class stamped on every fact. The librarian's index refuses `link_only`, `licensed_personal` and `proprietary_personal`. Chapter 5 applies this item by item. The ivc-forum.org copy of the country risk critique now redirects off-domain and must never enter a crawl list.

Source: Report, Part 6 licensing line and Part 3.1 (2026-09-14); Document A, section 3.3.

## Rule 9: estimates and ranges, never advice

Every episode in Chapter 4 is a person acting on a number, and the number being wrong, sometimes in his favor and sometimes not. So the app prints estimates only: value, price as a percentage of value, the probability that value is below price, what the price requires, and how past calls did. A test scans every memo, report and chat answer for recommendation language. A critic's published figure is quoted as history, nothing more.

Source: Plan, section 10.1, "No advice"; Document A, section 3.6.

## What he got right, and why the rules are mostly his

Fairness requires one closing note. Most of these rules copy Damodaran's own best habits: publish before the outcome, publish the spreadsheet, publish the range, publish the scorecard, re-run the rival's story, admit the miss. The critics supplied the theory. He supplied the practice. The app makes the practice mandatory instead of optional.

Source: Report, Parts 2.5 and 3.6, and Part 4, the honorable mention (2026-09-14).
