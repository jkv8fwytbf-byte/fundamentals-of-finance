# Chapter 11. Evals and Langfuse: how you find out whether the model is right {#r4-evals}

::: {.reading-only .optional}
**For checking model quality.** Start with what an evaluation measures, then use the examples when building the project's checks.
:::

## What it is (plain words and an analogy)

An "eval" is short for evaluation. It is a test for a program that has a language model inside it. Chapter 4 showed you normal tests in Vitest. A normal test gives one input and expects the exact same output every time. A model does not behave like that. Ask it the same question twice and the wording changes. So you need a different kind of test.

Think of a driving license. The written test has one correct answer per question, and a machine can mark it. The road test has an examiner who grades you against a checklist. This project has both kinds, and they must never be mixed up.

Three more terms, defined once:

- **Error analysis.** You read a pile of real outputs yourself and write down what went wrong in each. You do this before writing any automatic check. A teacher reads twenty essays before writing the rubric, not after.
- **LLM-as-judge.** A second model grades the first model's answer against a rubric you wrote. The judge is never the same model as the writer. A student does not mark their own exam.
- **Tracing** (also called observability). A recorder that stores every model call: prompt, answer, time, cost, and labels you attach. It is the system's flight recorder. Langfuse is the recorder this project uses.

Source: /Users/siddharth/.claude/projects/-Users-siddharth-Downloads/edcdeb19-7793-4e1b-9e73-4cf6186716bf/tool-results/bkm2kob5x.txt, section 11 (2026-09)

## Why this tool now (for this project)

The calculator is protected by the golden test. It must reproduce Almarai's value per share, 7.187840270062114, within 0.000001, before any code merges. That proves the arithmetic and nothing else. A memo can cite the wrong page and still read beautifully. A librarian answer can quote a 2025 risk premium while calling it 2026. Nobody would notice by eye. Evals are how you notice.

Source: /Users/siddharth/Valuation/docs/read-this-first.md, section 3.1 (2026-09-14)

The timing is set by the plan. In M2 the librarian ships with an "exam-based eval set". In M4 the plan adds Langfuse tracing of every model call, error analysis on 100 real memos and answers, and a nightly eval issue. Nothing beyond M0 exists today, so everything below is "will".

Source: /Users/siddharth/.claude/plans/help-me-out-here-abstract-wilkinson.md, section 5, M2 item 5 and M4 item 3 (2026-09-14)

The cost is zero at this size. Langfuse's Hobby tier is free: 50,000 units a month, 30-day data access, 2 users, unlimited projects, no card. Datasets and evaluations are included on every tier, including the free one. That is why the research picked it.

Source: /Users/siddharth/.claude/projects/-Users-siddharth-Downloads/edcdeb19-7793-4e1b-9e73-4cf6186716bf/tool-results/bo0hrclp7.txt, section 6 "LLM observability / evals" (2026-09)

## How it is used in this project

### Two suites, two runners

The research is blunt about this: the two suites "must not share a runner". Here is the split.

| | Deterministic golden tests | Generative evals |
|---|---|---|
| What is checked | Arithmetic | Retrieval, faithfulness, citations, vintages, refusals |
| Examples | Almarai within 1e-6; terminal cost of capital equals risk-free rate plus mature ERP; reinvestment lag; synthetic rating from interest coverage | Is the cited passage the source of the claim? Is the vintage right? Are advice words refused? |
| Who marks it | Code, exact comparison | Kimi K3 as judge, against a rubric |
| Where it runs | Vitest in CI (continuous integration: the robot that runs the tests on every pull request) | A nightly job over a hand-built set of about 50 questions |
| When it fails | The merge is refused | A GitHub issue is opened; it never blocks a merge |

Source: /Users/siddharth/.claude/projects/-Users-siddharth-Downloads/edcdeb19-7793-4e1b-9e73-4cf6186716bf/tool-results/bkm2kob5x.txt, section 11 and summary line "The two eval suites must not share a runner" (2026-09)

Why report-only? Because the judge is itself a model and can be wrong. A red generative eval means you read the failing case. It does not refuse code.

One refusal check is deliberately not a judge. The rule that no report, memo or chat answer may contain the advice words (listed in read-this-first, rule 3.6) is a plain text scan. It is deterministic, so it lives with the golden tests and does block merges.

Source: /Users/siddharth/.claude/plans/help-me-out-here-abstract-wilkinson.md, section 10.1 "No advice" (2026-09-14)

### The judge never equals the generator

GLM-5.3 writes the memos and answers. Kimi K3 grades them. The research states the rule bluntly: "Never self-judge." A model grading its own work shares its own blind spots. If it misread a passage when answering, it will misread it again when checking.

Kimi K3 is the judge because it is the best-calibrated open-weight model on the AA-Omniscience test (chapter 7 explains that test). "Calibrated" means it says "I do not know" rather than inventing an answer. That is the habit you want in an examiner. One judged case costs about $0.0298, so a 200-case suite is about $5.96 per run.

Source: /Users/siddharth/.claude/projects/-Users-siddharth-Downloads/edcdeb19-7793-4e1b-9e73-4cf6186716bf/tool-results/bcy86uopa.txt, row (d) "judge / eval" (2026-09); /Users/siddharth/Valuation/docs/read-this-first.md, section 4.1

### Error analysis first, scorers second

This is the part most people skip, and the part that matters most. The method, from Hamel Husain's writing:

1. Collect 100 real outputs. Here that will be memos and librarian answers from actual runs.
2. Read every one yourself. Write one line per failure, in plain words, in a spreadsheet.
3. Group the lines into failure modes. Expect five to ten groups.
4. Only now write a scorer per group. Some scorers are code. Some are a judge prompt with a rubric.

Husain's field guide says teams who skip step 2 "build dashboards that measure nothing".

Source: /Users/siddharth/.claude/projects/-Users-siddharth-Downloads/edcdeb19-7793-4e1b-9e73-4cf6186716bf/tool-results/bkm2kob5x.txt, section 11, "Recommendation for you" (2026-09)

Failure modes to expect here, based on the system's rules: a claim with no citation; a cited passage that does not contain the claim; two vintages mixed in one answer; an India industry row with fewer than 10 firms and no fallback note; an invented number where the corpus has none.

Source: /Users/siddharth/.claude/plans/help-me-out-here-abstract-wilkinson.md, section 10.1 (2026-09-14)

### What Langfuse logs

A **trace** is one request, such as "value Trent" or one librarian question. Inside it are **observations**, one per step: retrieval, rerank (a second pass that reorders the retrieved passages by relevance), the model call, the citation check. **Scores** are numbers or labels attached to a trace, by the judge or by you. Each of these is one "unit". A trace with five steps is about six units, so the free tier holds roughly 8,000 traces a month.

Source: /Users/siddharth/.claude/projects/-Users-siddharth-Downloads/edcdeb19-7793-4e1b-9e73-4cf6186716bf/tool-results/bo0hrclp7.txt, section 6 (2026-09)

Every model call will carry the same labels, so that evals can be sliced by them later:

```text
metadata: { vintage, source_ids, license_class, model_id, prompt_version }
```

Two budget rules follow. Log 100% of interactive chat. Sample the nightly batch at 10%. Logging 5,000 companies every night unsampled would be about 900,000 units a month, about $93 a month on the Core plan.

Source: /Users/siddharth/.claude/projects/-Users-siddharth-Downloads/edcdeb19-7793-4e1b-9e73-4cf6186716bf/tool-results/bo0hrclp7.txt, section 6 and section 8.2 (2026-09)

**Datasets and evals inside Langfuse.** A dataset is a table of questions with expected answers and sources. Your 50 golden questions will live there. An eval run sends each question through the librarian, asks Kimi K3 to score the answer, and stores the scores. Two runs can be compared side by side, so a prompt change or a model swap shows up as better or worse.

Source: /Users/siddharth/.claude/projects/-Users-siddharth-Downloads/edcdeb19-7793-4e1b-9e73-4cf6186716bf/tool-results/bj0fbejiq.txt, Role 5 (2026-09); the mechanics of a dataset run come from Langfuse's own docs at https://langfuse.com/docs, which the local reports do not describe

Practical details. The account is row 8 on the accounts list. The keys are `LANGFUSE_PUBLIC_KEY`, `LANGFUSE_SECRET_KEY` and `LANGFUSE_BASEURL`; they go into GitHub secrets, never the repo. Langfuse is open source and was acquired by ClickHouse on 2026-01-16. Self-hosting stays free, the escape hatch if pricing changes.

Source: /Users/siddharth/Valuation/docs/read-this-first.md, section 10, row 8; /Users/siddharth/.claude/projects/-Users-siddharth-Downloads/edcdeb19-7793-4e1b-9e73-4cf6186716bf/tool-results/bj0fbejiq.txt, Role 5 (2026-09)

### Braintrust, optional

Braintrust is an eval-first product. Its core idea is `Eval()`, a dataset plus a task plus scorers, with per-row diffs and a regression view. The free Starter tier gives 10,000 scores, then $2.50 per 1,000. Billing by score punishes a suite you re-run often, which is what the golden set is. So it is optional, row 12 on the accounts list. Open it only if you want its regression screen.

Source: /Users/siddharth/.claude/projects/-Users-siddharth-Downloads/edcdeb19-7793-4e1b-9e73-4cf6186716bf/tool-results/bo0hrclp7.txt, section 6; /Users/siddharth/Valuation/docs/read-this-first.md, section 10, row 12 (2026-09)

### The accuracy scoreboard: bias and variance

The two suites above grade the system against your rubric. The scoreboard grades it against the world. Every valuation will be stored with a timestamp, its inputs, its memo version and its three vintages. After 90, 180 and 365 days a job records the realized price. Two statistics follow, by sector, region, vintage and memo version:

- **Bias** is the average signed error of value versus the later price. Picture arrows at an archery bullseye. If they all land left of center, that is bias.
- **Variance** is the spread of those errors. If the arrows are scattered widely, that is variance, even when their average is dead center.

The page carries one banner: "The engine is tested (Almarai 1e-6). The forecast is not." Chapter 12 shows how Hex draws it from Neon.

Source: /Users/siddharth/Valuation/docs/read-this-first.md, section 6; /Users/siddharth/.claude/plans/help-me-out-here-abstract-wilkinson.md, section 5, M4 item 4 (2026-09-14)

Why log now and score later? Because Damodaran's own step five is "Keep the feedback loop open", and he admits the three hardest words are "I was wrong". A scoreboard makes those words a table instead of a feeling. His data also shows that no risk-premium method forecasts next year's return well, so one month of results is noise. The first scored horizon appears 90 days after the first stored valuation. The scoreboard shows estimates and their errors, never a recommendation.

Source: /Users/siddharth/Downloads/financeMD/damodaran/blog/2014/06/numbers-and-narrative-modeling-story.md (2014-06-24); /Users/siddharth/Downloads/financeMD/damodaran/blog/2026/03/the-price-of-risk-equity-risk-premium.md (2026-03)

## Learn it

All free. About 6 hours in total. Read them in this order.

| Resource | Format | Hours | Why |
|---|---|---|---|
| Hamel Husain, "Your AI Product Needs Evals", https://hamel.dev/blog/posts/evals/ | Article | 1 | The case for error analysis before tooling |
| Hamel Husain, "Creating an LLM-as-a-Judge That Drives Business Results", https://hamel.dev/blog/posts/llm-judge/ | Article | 1 | How to write a judge rubric that agrees with a human |
| Hamel Husain, "A Field Guide to Rapidly Improving AI Products", https://hamel.dev/blog/posts/field-guide/ | Article | 1 | The loop: read outputs, label, fix, re-run |
| Hamel Husain, "AI Evals FAQ", https://hamel.dev/blog/posts/evals-faq/ | Long FAQ, about 40 questions | 2 | The densest single page; answers the "but what about" questions |
| Langfuse docs, https://langfuse.com/docs | Documentation | 1 | Read the tracing page, then datasets, then evaluations |
| Braintrust docs, https://www.braintrust.dev/docs/start | Documentation | 0.5, optional | Only if you want to see the regression view |

The paid Maven course by Husain and Shreya Shankar exists. The research says skip it: the free writing contains the method.

Source: /Users/siddharth/.claude/projects/-Users-siddharth-Downloads/edcdeb19-7793-4e1b-9e73-4cf6186716bf/tool-results/bkm2kob5x.txt, section 11 (2026-09)

## 10-minute exercise

::: {.reading-only .optional}
**For the practical stage.** Use this exercise when working on this chapter's tool. The following "Done when" checklist tells you how to judge completion.
:::

You can start the golden question set today, with no code. It feeds M2 item 5 directly.

1. Open a blank file called `eval-questions.md` in your notes, not in the repo yet.
2. Write five questions you would ask the librarian, each answerable from the corpus.
3. Under each, write the expected answer in one line and the exact corpus path.
4. Under that, write one line saying how a judge should mark a wrong answer.

One row is done for you, so you can copy the shape:

```text
Q: For a rupee valuation in 2025, how does Damodaran get the risk-free rate?
Expected: India government bond 6.32%, minus the Baa3 default spread 2.16%, gives 4.16%.
Source: /Users/siddharth/Downloads/financeMD/damodaran/pdfiles/country/val2dayIndia2025.md (Vedant row)
Judge rubric: fail if the answer does not subtract the default spread, or cites a different file.
```

Source: /Users/siddharth/Downloads/financeMD/damodaran/pdfiles/country/val2dayIndia2025.md (2025)

Ten minutes gives you five rows. Fifty is the goal for M2. Nobody but you can write these, because they encode what a correct answer looks like to you.

## Done when

::: {.reading-emphasis .key-idea}
- You can say, in one sentence each, what error analysis, LLM-as-judge and tracing are.
- You can explain why the two suites use different runners, and which one blocks a merge.
- You can name the generator and the judge here, and say why they must differ.
- You can say what bias and variance mean on the scoreboard, and why nothing is scored before 90 days.
- You have five golden questions written, each with an expected answer, a corpus path and a rubric line.
:::
