# Chapter 0. How to learn with an AI coding tool without becoming dependent on it {#r4-learning}

::: {.reading-only .read-first}
**Read this before the tools manual.** Focus on the attempt-then-ask habit, explaining changes in your own words, and the learning checkpoints.
:::

## What it is (plain words and an analogy)

An AI coding tool is a program that reads your files, writes code, and runs commands when you ask in plain English. In this project the tool is Cursor, with Cline as a free second tool (chapter 2). People also call such a tool a "harness" or an "agent". All three words mean the same thing here.

Think of it as a very fast junior colleague who never sleeps and never says "I am not sure". The speed is the gift. The false confidence is the trap. A junior colleague who is wrong once a day is fine if you check the work. The same colleague is dangerous if you stop checking.

Damodaran has a name for the trap. He calls it "the Google curse", the growing habit of retrieving answers rather than reasoning toward them. He adds: "Reasoning is a muscle. If you stop using it, evolution takes it away." He has drawn a related line since 2012. Using first principles and using the market as a check are healthy responses to uncertainty. "Outsourcing by off-loading the decision making to others" is not.

Source: /Users/siddharth/.claude/projects/-Users-siddharth-Downloads/edcdeb19-7793-4e1b-9e73-4cf6186716bf/tool-results/bkm2kob5x.txt, section "How to learn with an AI harness", quoting https://imaa-institute.org/blog/investing-age-of-ai-damodaran-imaa-webinar/ and https://rpc.cfainstitute.org/blogs/enterprising-investor/2012/addressing-uncertainty-in-investment-valuations (2026-09-14)

He also says where a machine should do the work. In Data Update 1 for 2026 he writes that AI bots "will not only match, but be better than I am, at mechanical and rule-based tasks". He plans to hand almost his entire data-compilation process to a bot. So the split is his own: the machine does the mechanical half, and the person keeps the reasoning half.

Source: /Users/siddharth/Downloads/financeMD/damodaran/blog/2026/01/data-update-1-for-2026-push-and-pull-of.md (2026-01-09)

## Why this matters now (for this project)

This project's whole value is being right about numbers that other people may one day trust. The one thing a harness cannot supply is the instinct that a number is off by a factor you have not found yet. That instinct is built by doing the arithmetic yourself, many times. Nothing in the tooling will budget for that on your behalf, so you must.

The approved plan lists "dependence on the AI tool" as a named risk. Its mitigations are the rules below: [attempt-then-ask]{.reading-highlight}, own the tests, one no-AI evening a week, and a decisions log.

Source: /Users/siddharth/.claude/plans/help-me-out-here-abstract-wilkinson.md, section 9 (2026-09-14)

## How it is used in this project

- Week 1 you create accounts and read, with no code. From week 2 you drive Cursor, one small change at a time.
- Milestone M3 ("you take the wheel") ends when five pull requests are merged by you, the watchlist has 20 names, and you can explain every rule in `AGENTS.md` out loud. `AGENTS.md` is a plain text file at the top of the repository that every AI tool reads first. A pull request (PR) is explained in chapter 1.
- M3 also asks you to track your ratio of lines written to lines accepted (rule 8 below).
- The day-one exercise in M1 is the pattern for everything after it: ask the tool, then find the answer yourself in the workbook, then compare.

Source: /Users/siddharth/.claude/plans/help-me-out-here-abstract-wilkinson.md, sections 4 and 5 (M1, M3) (2026-09-14)

## The ten operational rules, each with a 5-minute exercise

These are the rules from the learning-path report, restated in plain words. Rule 9 was written for a terminal tool called pi and is translated here for Cursor.

Source for all ten: /Users/siddharth/.claude/projects/-Users-siddharth-Downloads/edcdeb19-7793-4e1b-9e73-4cf6186716bf/tool-results/bkm2kob5x.txt, section "How to learn with an AI harness" (2026-09-14)

### Rule 1. Attempt, then ask

Before any prompt, write two or three sentences in a scratch file. Say what you think the answer is and why. Then ask the tool. Compare the two. The difference is your learning signal. With no attempt there is no difference, and nothing is learned. This single rule does most of the work.

Five-minute exercise: create `~/Valuation/scratch/attempts.md`. Write today's date and one guess: "I think a branch in git is ...". Do not look anything up yet. You will check it in chapter 1.

### Rule 2. You own the test; the tool owns the implementation

A test is a small program that checks a bigger program and reports pass or fail. Never let the tool write both the check and the code that satisfies it. The golden number for the Almarai example, 7.187840270062114 value per share, is the model. The expected values are extracted from the workbook by a script, and the fixture file (the file of expected answers the test compares against) is protected in CI (continuous integration, the automatic check that runs on every pull request; chapter 1) so an agent can never "fix" the test instead of the code. If the tool proposes changing a test, that is a design conversation, not an edit.

Source: /Users/siddharth/.claude/plans/help-me-out-here-abstract-wilkinson.md, sections 1 and 10.1 (2026-09-14)

Five-minute exercise: open `/Users/siddharth/Downloads/financeMD/damodaran/pc/fcffsimpleginzu.md` and search for "Estimated value /share". Write the number you find in your attempts file, with the line number. That is the first invariant you own.

Source: /Users/siddharth/Downloads/financeMD/damodaran/pc/fcffsimpleginzu.md, line 111 shows 7.18784027 (workbook dated 2026-02-01 on the Almarai row)

### Rule 3. Explain back before you merge

No PR merges until you can say out loud, without looking, what each changed file does and why. If you cannot, you have a PR you cannot maintain. Revert it and redo it in smaller pieces. This is the review step a solo developer otherwise skips.

Five-minute exercise: pick any file in `~/Valuation/docs/`. Close it. Say in two sentences what it is for. Open it and check.

### Rule 4. One no-AI evening a week

Pick the second evening of each week. Type it yourself. Look things up in the official docs. Be slow. You are training recall, and recall is what lets you notice when the tool is confidently wrong. Expect this to feel bad for about four weeks and then to stop feeling bad.

Five-minute exercise: put a repeating calendar block on the second evening of each week named "no-AI evening". Keep it for twelve weeks.

### Rule 5. Read the diff, not the summary

A diff is the list of lines added and removed. The summary of a change is written by the same tool that made the change. `git diff` and `gh pr view` show the ground truth. Make it a physical habit: diff first, summary second, never summary only.

Five-minute exercise: in Cursor, open the Source Control panel (the branch icon in the left bar). Note where a file's diff appears. You will use this view in every PR.

### Rule 6. Keep a decisions log, written by you

A decisions log is a folder of short notes, one per decision. The format is `docs/decisions/NNN-title.md`, about ten lines each, written by a human. Each note says what was decided, what was rejected, and why. It is the only artifact that proves you made the call. It is also the context you hand the tool next month, so it stops re-opening settled choices.

Five-minute exercise: create `~/Valuation/docs/decisions/001-daily-tool-is-cursor.md`. Write: decided (Cursor as the daily tool), rejected (pi, a second paid tool), why (already paid, shows diffs, has a plan mode). The reasons are in plan section 2.

Source: /Users/siddharth/.claude/plans/help-me-out-here-abstract-wilkinson.md, section 2 (2026-09-14)

### Rule 7. Spend the tool on mechanical work, spend yourself on judgment

Mechanical work you may delegate freely: mapping XBRL tags (the labels inside SEC filings), parsers for CSV and spreadsheet files, boilerplate, migration scaffolding, test fixtures, document formatting, regular expressions. Judgment you never delegate: which vintage (data snapshot) applies, whether a seven-firm India industry falls back to the emerging-markets table or the global one, whether a cash flow is real, and what the app is allowed to say to a user. This is Damodaran's own split. He hands the bot the data compilation and keeps the narrative.

Five-minute exercise: draw a two-column table titled "mechanical" and "judgment". Add five items to each from your own week. Keep it in the attempts file.

### Rule 8. Measure your ratio, honestly

Once a week, note two numbers. First: lines you wrote against lines you accepted from the tool. Second: how many times you accepted something you could not explain. The second number should trend to zero by week 6. If it does not, you are accumulating a codebase you rent rather than own.

Five-minute exercise: add a table to the attempts file with columns week, lines written, lines accepted, unexplained acceptances. Fill in week 1 with zeros. Ratios only mean something once the row is there.

### Rule 9. Use branches as a thinking tool, not an answer machine

The original rule says to fork the session before a risky change and explore two approaches in parallel. In Cursor the same move is a git branch (chapter 1). Before a risky change, make a branch for approach A and another for approach B. Let the tool try both. Then you choose, and you write the choice in the decisions log. The tool generates options. You exercise the muscle that picks.

Five-minute exercise: in the attempts file, write one change you fear making to a valuation formula. Name the two branches you would create, for example `try-lag-on` and `try-lag-off`.

### Rule 10. The corpus is the antidote to the tool

You have a world expert's own reasoning on disk, roughly 30 million tokens of it. A token is a piece of a word, about three quarters of a word on average. When you do not understand why the stable-growth cost of capital is the risk-free rate plus a mature-market premium, the right move is not "ask the model". The right move is to find the passage where he says it, then ask the model to check your restatement. Retrieval from a primary source is not the Google curse. Retrieval instead of reasoning is. The librarian in this system (the search tool over the corpus) is built to always show you the source passage, which pushes you toward the first behavior.

Five-minute exercise: run this in a terminal and read the two lines it prints.

```
grep -n "riskfree rate + 4.5%" /Users/siddharth/Downloads/financeMD/damodaran/pc/fcffsimpleginzu.md
grep -n "Mature Market ERP +" /Users/siddharth/Downloads/financeMD/damodaran/pc/fcffsimpleginzu.md
```

The first line is the workbook's own note that a mature company's cost of capital is about the risk-free rate plus 4.5%. The second is the mature-market equity risk premium cell, 0.0423, updated January 1, 2026. Notice that they are not the same number. Write one sentence about why that might be. Do not ask the tool yet.

Source: /Users/siddharth/Downloads/financeMD/damodaran/pc/fcffsimpleginzu.md, lines 48 and 608 (ERP cell dated January 1, 2026)

## Learn it

| Resource | Format | Hours | Why |
|---|---|---|---|
| IMAA Institute write-up of Damodaran's "Investing in the age of AI" webinar, https://imaa-institute.org/blog/investing-age-of-ai-damodaran-imaa-webinar/ | article | about 0.5 (my estimate, not from a source) | The source of "the Google curse" and "reasoning is a muscle" |
| CFA Institute Enterprising Investor, "Addressing uncertainty in investment valuations" (2012), https://rpc.cfainstitute.org/blogs/enterprising-investor/2012/addressing-uncertainty-in-investment-valuations | article | about 0.5 (my estimate) | His healthy versus unhealthy responses to uncertainty; "outsourcing" is the unhealthy one |
| Data Update 1 for 2026, local copy at /Users/siddharth/Downloads/financeMD/damodaran/blog/2026/01/data-update-1-for-2026-push-and-pull-of.md, online at https://aswathdamodaran.blogspot.com/2026/01/data-update-1-for-2026-push-and-pull-of.html | blog post | about 0.5 (my estimate) | Where he says which half of the work goes to the bot |
| The corpus itself, /Users/siddharth/Downloads/financeMD/, searched with `grep -rn "phrase" path` | local markdown | ongoing | Rule 10. Every "why" question has a primary source on disk |

All free. Hours marked "my estimate" are not from any report; they are reading-time guesses.

## 10-minute exercise

::: {.reading-only .optional}
**For the practical stage.** Use this exercise when working on this chapter's tool. The following "Done when" checklist tells you how to judge completion.
:::

This is the day-one exercise from the plan, with rule 1 added.

1. In the attempts file, write two sentences: why you think the cost of capital after year 10 is the risk-free rate plus a mature-market premium.
2. Ask Cursor (chapter 2, plan mode, do not execute): "Explain why the terminal cost of capital in fcffsimpleginzu is the risk-free rate plus the mature-market ERP."
3. Open the workbook markdown yourself and find the cell label `Mature Market ERP +` and the note "riskfree rate + 4.5%".
4. Write three lines: what you guessed, what the tool said, what the workbook says. Note any place the tool was more confident than the workbook.

Source: /Users/siddharth/.claude/plans/help-me-out-here-abstract-wilkinson.md, section 5, M1 step 6 (2026-09-14); /Users/siddharth/Downloads/financeMD/damodaran/pc/fcffsimpleginzu.md, lines 48 and 608

## Done when

::: {.reading-emphasis .key-idea}
- `~/Valuation/scratch/attempts.md` exists with at least one attempt-then-ask entry and the week-1 ratio row.
- `~/Valuation/docs/decisions/001-daily-tool-is-cursor.md` exists and is under fifteen lines.
- The no-AI evening is on your calendar for twelve weeks.
- You can list the ten rules from memory, in any order, in your own words.
- You have found one answer in the corpus with grep before asking the tool about it.
:::
