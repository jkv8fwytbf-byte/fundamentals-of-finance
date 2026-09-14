# Chapter 1: Why value, the story, and the 3P test

This is the first chapter of "Damodaran, the important parts". It is a revision brain-dump from a friend, not a textbook. Every concept ends with one line on why it matters for the calculator we are building. Terms are defined the first time they appear.

## Why value anything at all

Valuation is the act of estimating what an asset is worth. An asset is anything that can produce money for its owner in the future, such as a business or a building. Damodaran's starting rule is that a sensible investor does not pay more for an asset than it is worth. He calls the opposite belief, that any price is fine if someone will pay more later, "a very expensive game of musical chairs". We own financial assets for the cash they are expected to produce, not for how they make us feel. So the price we pay should be tied to those cash flows, their uncertainty, and their growth.

Source: /Users/siddharth/Downloads/financeMD/damodaran/New_Home_Page/background/valintro.md (no date in file)

He also warns you about three myths before you touch a spreadsheet. First, valuation is not an objective search for a true value; every valuation is biased, and the only questions are how much and in which direction. Second, no valuation is precise, and the payoff to valuing something is greatest exactly when the numbers are least precise. Third, a more complicated model is not a better model; your understanding of a model falls as its inputs multiply. The cure is parsimony, which means using the simplest model you can get away with. In his words, "if we can value an asset with three inputs, we should not be using five."

Source: /Users/siddharth/Downloads/financeMD/damodaran/pdfiles/eqnotes/ValIntroSpr25.md (Spring 2025); /Users/siddharth/Downloads/financeMD/damodaran/New_Home_Page/background/valintro.md (no date in file)

Why it matters for the calculator: the engine must be exact in its arithmetic, but the inputs are guesses, so every run also produces a range from Monte Carlo draws and a sensitivity table. Monte Carlo means running the model many times with inputs drawn at random from a chosen spread. That design is the three myths turned into code.

Source: /Users/siddharth/.claude/plans/help-me-out-here-abstract-wilkinson.md (2026-09)

## Price versus value

Price and value are two different things that people use as one word. Value is driven by the cash flows an asset produces, the growth in those cash flows, and the risk that they do not show up. Price is driven by demand and supply, which in practice means mood and momentum. Damodaran's line is that markets are pricing mechanisms, not value mechanisms. Think of a house: the value is what the rent stream is worth, the price is what the neighbor paid last week.

Source: /Users/siddharth/Downloads/financeMD/damodaran/blog/2020/03/a-viral-market-meltdown-iii-pricing-or.md (2020-03-16)

He draws three consequences. Price has no upper or lower bound, but value has both, set by the most optimistic and most pessimistic sensible forecasts. Price is reactive, moving on each bit of news, while value is proactive, because news must pass through your expectations first. And price may never converge on value in your lifetime, so working on value is an act of faith. His India lecture reduces the subject to three questions: is there a gap between price and value, will it close, and what will close it.

Source: /Users/siddharth/Downloads/financeMD/damodaran/blog/2020/03/a-viral-market-meltdown-iii-pricing-or.md (2020-03-16); /Users/siddharth/Downloads/financeMD/damodaran/pdfiles/country/val2dayIndia2025.md (2025)

Why it matters for the calculator: the calculator computes value, and the market price is a separate input typed in beside it. The output is a gap, nothing more. A rule in the plan scans every memo and answer for advice language and fails the build if it finds any.

Source: /Users/siddharth/.claude/plans/help-me-out-here-abstract-wilkinson.md (2026-09)

## The three ways to value anything

Damodaran says there are hundreds of valuation models but only three approaches. The table is the whole map.

| Approach | What it does | What you need | Works best when | Calculator |
|---|---|---|---|---|
| Intrinsic valuation (usually DCF) | Value equals the present value of the cash flows the asset will produce | The life of the asset, the cash flows over that life, and a discount rate | You have a long horizon and can wait for price to move | This is the engine itself |
| Relative valuation, also called pricing | Estimates what to pay from what others pay for comparable assets, scaled by a shared metric | Comparable assets, a standardized price such as price to earnings, and controls for differences | Many comparables exist and you are judged against a benchmark | A later module; the memo also asks what the current price already requires |
| Contingent claim, also called real option valuation | Adds value for assets whose payoff depends on an event happening | An underlying asset value, an exercise price, a life, and a measure of variability | Distressed equity, patents, natural resource reserves, rights to expand | Off by default; the "possible" bucket of the 3P test lands here |

Some vocabulary. DCF stands for discounted cash flow, which means shrinking future cash by a rate that reflects risk and time. A multiple is a price divided by a common measure, such as earnings, so that companies of different sizes can be compared. An option is a right, not an obligation, to do something later. Two cautions from the same packet stay with me. An intrinsic model can find every stock in a market worth less than its price, which troubles anyone who must stay fully invested. Pricing assumes the market is right on average and wrong only on individual names, so it fails when the whole market is off. And option models sit on top of another valuation, so counting a patent in the growth rate and again as an option is double counting.

Source: /Users/siddharth/Downloads/financeMD/damodaran/pdfiles/eqnotes/ValIntroSpr25.md (Spring 2025)

Why it matters for the calculator: the engine is an intrinsic model, so it will disagree with prices for long stretches. That is expected behavior, not a bug.

## Story to numbers: the five steps

Damodaran describes two tribes. Number crunchers build spreadsheets and distrust stories; storytellers pitch visions and distrust spreadsheets. Numbers without a story are just modeling, and a story without numbers is just storytelling. Numbers-only models suffer from three illusions: precision, objectivity, and control. Story-only pitches drift into fantasy and give you no yardstick for progress. A good valuation binds the numbers to one coherent story.

Source: /Users/siddharth/Downloads/financeMD/damodaran/blog/2014/06/numbers-and-narrative-modeling-story.md (2014-06-24); /Users/siddharth/Downloads/financeMD/damodaran/New_Home_Page/NNPreface.md (no date in file)

The process has five steps, and he is not rigid about the order.

1. Develop a narrative for the business. Keep it simple and focused, and make it your own, not management's.
2. Test the narrative against history, experience, and common sense. This is where the 3P test lives; the packet says "No fairy tales or runaway stories."
3. Convert the key parts of the narrative into drivers of value: market size, market share, margins, reinvestment, and risk.
4. Connect the drivers to a valuation, which for him is a DCF.
5. Keep the feedback loop open. Listen to people who know the business better, and be ready to say "I was wrong".

Source: /Users/siddharth/Downloads/financeMD/damodaran/blog/2014/06/numbers-and-narrative-modeling-story.md (2014-06-24); /Users/siddharth/Downloads/financeMD/damodaran/pdfiles/country/val2dayIndia2025.md (2025)

The Uber post shows why the story matters more than the small inputs. In June 2014 he ran four narratives through the same model.

| Narrative | Total market | Share | Cost of capital | Value |
|---|---|---|---|---|
| Car service company facing competitive and regulatory hurdles | 100 billion dollars | 10 percent | 12 percent | 3.2 billion dollars |
| Car service company with sustained profitability (his own) | 100 billion dollars | 10 percent | 12 percent falling to 8 | 5.9 billion dollars, plus 2 to 3 billion for a disruption option |
| Car service company with dominant share from network effects | 100 billion dollars | 50 percent | 12 percent falling to 8 | 29.1 billion dollars |
| Logistics company expanding into other businesses | 600 billion dollars | 5 percent | 12 percent falling to 8 | 17.5 billion dollars |

His conclusion: "big differences in valuation almost always result from differing narratives".

Source: /Users/siddharth/Downloads/financeMD/damodaran/blog/2014/06/numbers-and-narrative-modeling-story.md (2014-06-24)

Why it matters for the calculator: his workbook has a sheet called "Stories to Numbers" with the story in a text box, then one row per assumption with a "Link to story" column. The shipped example carries Amazon's story text over Almarai's numbers, and the sheet does not notice, because the story column is free text with no checks. Our memo writer uses the same template but forces every proposed input to cite a filing page or a Damodaran passage, and a second opposing memo per company is mandatory.

Source: /Users/siddharth/Downloads/financeMD/damodaran/pc/fcffsimpleginzu.md (valuation date 2026-02-01 in sheet); /Users/siddharth/.claude/plans/help-me-out-here-abstract-wilkinson.md (2026-09)

## The 3P test: possible, plausible, probable

The 3P test is the filter for step 2. A possible story could happen. A plausible story could reasonably happen, given how businesses and people behave. A probable story is one you would put weight on today. In his words, "not everything that is possible is plausible, and not all plausible opportunities make the transition to the probable." Picture three nested circles: the outer one is huge and nearly worthless, the inner one is small and carries the value.

Source: /Users/siddharth/Downloads/financeMD/damodaran/blog/2014/07/possible-plausible-and-probable-big.md (2014-07-16)

The test was born in a public disagreement. Bill Gurley, an Uber board member, argued for a far bigger market and strong network effects, which are benefits each user gets from other users joining. Damodaran did not say Gurley was wrong; he said they drew the lines between probable, plausible, and possible in different places. He kept the car ownership market as a possibility with an option value of about 2 to 3 billion dollars, outside the base case. His slides name the two classic failures: the "Big Market Delusion" for the implausible, and "Willy Wonkitis" for the improbable, his term for pitches built on magical thinking.

Source: /Users/siddharth/Downloads/financeMD/damodaran/blog/2014/07/possible-plausible-and-probable-big.md (2014-07-16); /Users/siddharth/Downloads/financeMD/valpacket1spr25.md (Spring 2025)

To run the test, use his three checks. History asks whether any company has ever lived this story. Experience asks what road bumps you hit last time you believed a similar story. Common sense asks what economics and arithmetic say about the weakest link. The workbook's Diagnostics sheet turns this into blunt questions: how big is the total market today, how much do the biggest companies in it make, and what share are you forecasting in year 10.

Source: /Users/siddharth/Downloads/financeMD/damodaran/blog/2014/06/numbers-and-narrative-modeling-story.md (2014-06-24); /Users/siddharth/Downloads/financeMD/damodaran/pc/fcffsimpleginzu.md (valuation date 2026-02-01 in sheet)

Why it matters for the calculator: the plan hard-codes the test as a rule. Only probable claims may set a base-case input. Plausible claims become a scenario. Possible claims are recorded at zero, which is where an option value would go if we ever add one.

Source: /Users/siddharth/.claude/plans/help-me-out-here-abstract-wilkinson.md (2026-09)

## The corporate life cycle lens

The corporate life cycle is the idea that a company ages like a person: young, growth, mature, declining. Value is always cash flows, growth, and risk, but which inputs you sweat over changes with age. He does not invent new models for each stage; "we use the same models" and move the estimation effort.

Source: /Users/siddharth/Downloads/financeMD/damodaran/pdfiles/CLC/slides/Ch1.md (no date in file)

| Stage | Revenue growth | Margins | Reinvestment | Cost of capital and failure | Where the value sits |
|---|---|---|---|---|---|
| Young or start-up | The one number you can see | Negative, slow to turn positive | From sales-to-capital, the revenue each unit of capital supports | Split operating risk from failure risk; failure is its own probability | Almost all in the future |
| High growth | High, fading toward the sector | Rising as growth spending stops hiding profit | Sales-to-capital again, with lags allowed | A year-specific cost of capital that falls as growth moderates | Terminal value can be 80 or 90 percent of value, or more than 100 percent |
| Mature | Close to the economy's growth rate | Stable; use historic norms | Shifts toward acquisitions; ask whether they create value | An established financing mix; failure risk near zero | In assets already in place; financing and dividend policy matter more |
| Declining | Flat or negative, often from selling assets | Compressing | Can be negative, because divestitures bring cash in | Distress raises the cost of debt and equity; failure probability rises | Depends on the management path: denial, desperation, acceptance, or reinvention |

Source: /Users/siddharth/Downloads/financeMD/damodaran/pdfiles/CLC/slides/Ch10.md, Ch11.md, Ch12.md, Ch13.md (no date in files)

A few details are worth keeping. Venture capitalists price young companies with target rates of return, 50 to 70 percent for a start-up and 25 to 35 percent at the bridge or IPO stage. Damodaran calls that a forward pricing, not a valuation, because the target rate mixes operating risk and failure risk with no stated logic. His Zomato example instead uses a rupee cost of capital of 10.25 percent falling to about 9 percent, plus a 10 percent chance of failure. His Unilever example uses a cost of capital of 8.97 percent, 78 percent equity and 22 percent debt, and no failure risk. Terminal value, the value of all cash flows after the forecast period, is the input to watch in growth companies. The 3P test is mostly unnecessary for a mature company whose story extends its history, with two exceptions: imminent macro or regulatory change, and disruption.

Source: /Users/siddharth/Downloads/financeMD/damodaran/pdfiles/CLC/slides/Ch10.md, Ch11.md, Ch12.md (no date in files)

The preface to Narrative and Numbers gives the manager's side. Early on, the masterful storytellers win; as the company grows, the skill shifts to delivering numbers that back the story; a mature company's narrative is "mostly written"; a declining company's is about finding a decent ending.

Source: /Users/siddharth/Downloads/financeMD/damodaran/New_Home_Page/NNPreface.md (no date in file)

Why it matters for the calculator: the workbook's five levers (growth next year, growth for years 2 to 5, target margin, years to converge, sales-to-capital) plus its failure-probability switch are how the life cycle enters the numbers. The memo must also name the company's uncertainty type so the right chapter of "The Dark Side of Valuation" is pulled before inputs are proposed.

Source: /Users/siddharth/.claude/projects/-Users-siddharth-Downloads/edcdeb19-7793-4e1b-9e73-4cf6186716bf/tool-results/bkdrkpfng.txt (2026-09); /Users/siddharth/.claude/plans/help-me-out-here-abstract-wilkinson.md (2026-09)

## Narrative breaks, shifts, and tweaks

A story is never finished, because the world delivers surprises. Damodaran sorts them into three kinds and pairs each with a tool.

| Kind | What happened | Effect on your valuation | Tool |
|---|---|---|---|
| Narrative break or end | A legal, political, economic, or credit event makes the story no longer operative | The old cash flows, growth, and risk numbers are void | Estimate a probability of the break and its consequences |
| Narrative shift | The business model works better or worse than expected; market size, share, or margins move | Update the inputs with the new data | Monte Carlo simulation or scenario analysis |
| Narrative change, expansion or contraction | Unexpected entry into a new market, or exit from an existing one | Redo the valuation with a new market potential | Real options |

Source: /Users/siddharth/Downloads/financeMD/damodaran/blog/2014/08/reacting-to-earnings-reports-narrative.md (August 2014); /Users/siddharth/Downloads/financeMD/valpacket1spr25.md (Spring 2025)

The book chapter is titled "Narrative breaks, shifts and tweaks", and a tweak is the smallest move: keep the story, nudge a number. The label depends on your starting story. Uber succeeding in the suburbs was a change for Damodaran, whose base case was urban, but only a shift for Gurley, whose base case already included suburbs. His warning is that a rigid DCF responds to all three with denial, keeping inputs fixed and blaming the market. The right posture is proactive: bring failure in as a probability for young or indebted firms, use distributions where shifts are likely, and treat true changes as options. And seek out "people who think least like you".

Source: /Users/siddharth/Downloads/financeMD/damodaran/New_Home_Page/NNPreface.md (no date in file); /Users/siddharth/Downloads/financeMD/damodaran/blog/2014/08/reacting-to-earnings-reports-narrative.md (August 2014); /Users/siddharth/Downloads/financeMD/damodaran/pdfiles/CLC/slides/Ch10.md (no date in file)

Why it matters for the calculator: every run is stored with its inputs and data vintage, so a shift is a new run with changed levers, a break is the failure-probability switch, and a change is a new memo with a new story. The nightly jobs re-value the watchlist, so the feedback loop is a schedule rather than a good intention.

Source: /Users/siddharth/.claude/plans/help-me-out-here-abstract-wilkinson.md (2026-09)

## Where this comes from

Go deeper in this order. Paths are under /Users/siddharth/Downloads/financeMD/ unless shown in full.

- damodaran/New_Home_Page/background/valintro.md: the standalone primer on bias, uncertainty, complexity, and the three approaches.
- damodaran/pdfiles/eqnotes/ValIntroSpr25.md: the Spring 2025 class opener; myths and truths, the three approaches side by side.
- valpacket1spr25.md (corpus root), slides 264 to 272: the narrative session, the Big Market Delusion, Willy Wonkitis, and the break, shift, and change table.
- damodaran/pdfiles/country/val2dayIndia2025.md, slides 4 to 9 and 148 to 149: the price-versus-value gap and the five steps, taught in India.
- damodaran/blog/2014/06/numbers-and-narrative-modeling-story.md: the original five steps and the four Uber narratives.
- damodaran/blog/2014/07/possible-plausible-and-probable-big.md: the 3P test, argued against Bill Gurley.
- damodaran/blog/2014/08/reacting-to-earnings-reports-narrative.md: breaks, shifts, and changes, with the tool for each.
- damodaran/blog/2020/03/a-viral-market-meltdown-iii-pricing-or.md: price versus value, written during a crash.
- damodaran/pdfiles/CLC/slides/Ch1.md and Ch10.md to Ch13.md: the life-cycle lens with the Zomato, Unilever, and declining-firm examples.
- damodaran/pc/fcffsimpleginzu.md, the "Stories to Numbers" and "Diagnostics" sheets: the template the memo writer imitates.

## Three things to remember

1. Value comes from cash flows, growth, and risk; price comes from demand and supply. The calculator computes the first, reports the gap to the second, and never turns that gap into advice.
2. Every number must be tied to a sentence in a story, and every sentence must pass the 3P test. Only the probable sets the base case; the plausible gets a scenario; the possible is written down at zero.
3. The model does not change with a company's age, but the inputs you fight over do. Young companies live or die on growth and failure risk, mature ones on financing and dividend policy, declining ones on the path management takes.
