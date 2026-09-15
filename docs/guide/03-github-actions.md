# Chapter 3. GitHub Actions: the robot that tests your code and runs it at night

## What it is (plain words and an analogy)

GitHub Actions is a service built into GitHub. It runs commands on a rented computer whenever something happens to your repository. "Something happens" can be a push, a pull request, a timer, or a button you click. The rented computer is called a runner. GitHub creates it, runs your steps, and throws it away.

It does two jobs for you. The first is continuous integration, usually shortened to CI. CI means that every time code changes, the tests run automatically before a human merges. The second job is scheduling. A scheduled workflow runs at a set time with nobody at the keyboard.

Analogy: a night-shift lab assistant. You hand the assistant a checklist, which is the workflow file. The assistant reruns the checklist on every change to your work, and also at 6:17 every morning. If any step fails, the assistant puts a red mark on the change, and you see it before it lands.

Source: https://docs.github.com/en/actions/get-started/understand-github-actions (listed in bkm2kob5x.txt, learning path section 2, verified 2026-09-14). The analogy is mine.

## Why this tool now (for this project)

There are two reasons, and both come from the plan.

First, the golden test lives here. Damodaran's spreadsheet ships with a worked example, Almarai, whose value per share is 7.187840270062114. Our calculator must reproduce that number to 1e-6, which means to six decimal places. CI turns that rule from a promise into a gate. A pull request that moves the number goes red and cannot merge.

Source: docs/plan.md, sections 1 and 10.1 (2026-09-14); bkm2kob5x.txt, learning path section 2.

Second, it is the free scheduler. Vercel, which hosts web pages, allows its Hobby plan only one cron run per day, fired at any minute inside the stated hour. A cron is a timer that starts a job on a fixed calendar. GitHub Actions has a `schedule` trigger with no such daily cap. This repo is public, so standard Linux runners are free. Every nightly robot in this system will run on Actions and will write its results to the Neon database. Vercel only serves pages.

Source: bkm2kob5x.txt, learning path sections 0 and 5 (2026-09-14); bo0hrclp7.txt, section 1.4 (Vercel cron docs, last updated 2026-07-15).

## How it is used in this project

The plan lists nine jobs: `load-damodaran`, `ingest-edgar`, `value-watchlist`, `watch-erp-crp`, `rag-index`, `rag-eval`, `news-headlines`, `realised-prices`, and `report`. Four run nightly (`ingest-edgar`, `value-watchlist`, `rag-eval`, `news-headlines`). Three run on demand (`load-damodaran`, `rag-index`, `report`). `realised-prices` runs weekly. `watch-erp-crp` checks Damodaran's site monthly and quarterly for a new file. Every job will write a heartbeat row to the database when it finishes.

Source: plan section 10.6 (2026-09-14).

### The workflow file, piece by piece

A workflow is one YAML file in the folder `.github/workflows/`. YAML is a plain-text format where indentation shows nesting, much like Python. Here is the shape of the nightly revaluation job, cut down to its bones:

```yaml
name: value-watchlist

on:
  schedule:
    - cron: "17 6 * * *"        # 06:17 UTC every day, deliberately off the hour
  workflow_dispatch:             # adds a "Run workflow" button in the Actions tab

concurrency:
  group: value-watchlist
  cancel-in-progress: true       # a new run cancels a stale one

jobs:
  run:
    runs-on: ubuntu-latest       # a 2-core Linux runner, the cheapest kind
    timeout-minutes: 45          # never let a hung job sit for six hours
    steps:
      - uses: actions/checkout@v4
      - uses: pnpm/action-setup@v4
      - run: pnpm install --frozen-lockfile
      - run: pnpm -F engine value-watchlist
        env:
          DATABASE_URL: ${{ secrets.DATABASE_URL }}
          OPENROUTER_API_KEY: ${{ secrets.OPENROUTER_API_KEY }}
```

What each keyword means:

| Keyword | Plain meaning |
|---|---|
| `name` | The label you see in the Actions tab. |
| `on` | The list of events that start the workflow. |
| `schedule` / `cron` | A timer. The five fields are minute, hour, day of month, month, day of week. Times are UTC. |
| `workflow_dispatch` | Lets you start the job by hand from the website. Always add it, so you can test. |
| `concurrency` | If two runs of the same group overlap, cancel the older one. Saves minutes. |
| `jobs` | The units of work. Each job gets its own fresh runner. |
| `runs-on` | Which kind of rented computer to use. |
| `timeout-minutes` | Kill the job after this long. |
| `steps` | The checklist, run top to bottom. |
| `uses` | Borrow a ready-made step published by someone else. The `@v4` pins a version. |
| `run` | Run a shell command. |
| `env` / `secrets` | Pass a stored secret into the command as an environment variable (a named value the shell hands to a program when it starts). |

Source: the keyword meanings follow the GitHub "Write workflows" documentation at https://docs.github.com/en/actions/how-tos/write-workflows/ (bkm2kob5x.txt, section 2). The action version numbers in the example are illustrative; check the current major version before copying.

### Secrets

A secret is a value like an API key that must never appear in code. You paste it once into the repository settings, under Secrets and variables. Actions then hands it to a job only through `${{ secrets.NAME }}`. The logs mask it. For this project the names are fixed in the plan: `DATABASE_URL`, `DATABASE_URL_UNPOOLED`, `OPENROUTER_API_KEY`, `PINECONE_API_KEY`, `VOYAGE_API_KEY`, the four `R2_*` values, the three `LANGFUSE_*` values, `MISTRAL_API_KEY`, and later `EODHD_API_TOKEN`. The same names go into the local `.env` file, which is never committed.

Source: plan section 7, accounts table (2026-09-14); https://docs.github.com/en/actions/how-tos/write-workflows/choose-what-workflows-do/use-secrets (bkm2kob5x.txt, section 2).

### Schedule gotchas

These are the things that make a nightly job silently skip a day. Read them twice.

- **Off-hour minutes.** Runs queued at the top of the hour are delayed, and under load they are dropped. GitHub's own docs advise picking a different minute. Use `17 6 * * *`, never `0 6 * * *`.
- **The 5-minute floor.** The shortest allowed interval is 5 minutes. You will never need that. Nightly is the cadence here.
- **The 6-hour cap.** A job's default `timeout-minutes` is 360, which is six hours. A hung API call sits there for six hours at $0.006 per minute, which is about $2.16 in silence. Set a real timeout on every job.
- **Minute rounding.** GitHub rounds each job up to the whole minute. Fifty jobs of 20 seconds cost 50 minutes, not 17. For fan-out work, loop inside one job instead of spreading it across a matrix of many jobs (a matrix is an Actions feature that clones one job once per input value, each clone billed separately).
- **The 60-day sleep.** In a public repo, a scheduled workflow is switched off after 60 days with no new commits. Use the heartbeat below rather than trusting a silent cron.
- **The spending cap.** Set a hard Actions spending limit of $25 in the organization's billing settings before the first scheduled workflow exists. A retry loop in an ingest job is the realistic way to burn money.

Source: bj0fbejiq.txt, CHECK 1 part 2, sections 2.3 and 2.7 (fetched 2026-09-14), citing https://docs.github.com/en/actions/reference/workflows-and-actions/events-that-trigger-workflows; plan sections 5 (M2) and 9.

### Public-repo minutes

Public repos get standard runners free. Private-repo minute pools do not apply here. Keep a $25 Actions spending cap anyway, in case a job is moved onto a paid runner later.

Cost math for this project: the plan budgets $0 for CI on the public repo. The $25 cap is belt and suspenders.

Source: bj0fbejiq.txt, CHECK 1 part 2, section 2.1 (fetched 2026-09-14); plan section 6 (2026-09-15).

### Blacksmith, optional later

An organization on GitHub is a shared account that owns repositories. This repo does not need one for privacy. A vendor called Blacksmith sells faster runners, but only to GitHub organizations, not personal repos. Create an organization later only if you want those runners.

Blacksmith: you change `runs-on: ubuntu-latest` to `runs-on: blacksmith-2vcpu-ubuntu-2404`. They claim about twice the speed. They give 3,000 free minutes a month per organization, then charge $0.004 a minute for Ubuntu x64. Start on GitHub's own runners.

Source: bj0fbejiq.txt, sections 2.4, 2.6 and 2.7 (Blacksmith pricing and quickstart fetched 2026-09-14); plan sections 2 and 5 (M2).

One risk to keep in view: GitHub announced a $0.002 per minute charge for self-hosted runners on 2025-12-16, then postponed it within two days. It is postponed, not cancelled. If revived, it would apply on top of every third-party runner.

Source: bj0fbejiq.txt, section 2.2 (2026-09-14).

### The dead-man's-switch heartbeat

A dead man's switch is a control on a train that stops the train if the driver lets go. The idea here is the same. A scheduled job can be dropped, disabled, or hung, and GitHub will not tell you. So each job will write a row to the `job_heartbeat` table in Neon when it succeeds, with the job name and the time. A separate, cheap check will read that table and raise an alarm if any nightly job's row is older than 36 hours. The rule in the report: never trust a cron you cannot observe.

Source: bj0fbejiq.txt, sections 2.3 and 2.7; plan sections 10.3 and 10.6 (2026-09-14).

## Learn it

All free. Total about 5 hours.

| # | Resource | Format | Hours | Why |
|---|---|---|---|---|
| 1 | https://docs.github.com/en/actions/get-started/quickstart | Official docs | 0.5 | Your first workflow runs in ten minutes. |
| 2 | https://docs.github.com/en/actions/get-started/understand-github-actions | Official docs | 1 | The vocabulary: workflow, event, job, step, runner. |
| 3 | https://docs.github.com/en/actions/how-tos/write-workflows/ | Official docs | 2 | Every keyword in the YAML above, with examples. |
| 4 | https://docs.github.com/en/actions/reference/workflows-and-actions/events-that-trigger-workflows | Official reference | 0.5 | The `schedule` section carries the off-hour and 60-day warnings in GitHub's own words. |
| 5 | https://github.com/skills/hello-github-actions | Interactive course inside a real repo | 1 | You write and run a workflow, graded by Actions itself. |
| 6 | https://github.com/skills/test-with-actions | Interactive course | 1 | Adds a test step and a status check, which is exactly the golden-test setup. |

Source: bkm2kob5x.txt, learning path section 2 (all URLs verified 2026-09-14).

## 10-minute exercise

This assumes the repo from milestone M2 exists, with the golden test green in CI.

1. Create a branch: `git switch -c break-golden`.
2. Open the engine's reinvestment code and change the lag switch by one year. The plan names this exact change as the M2 acceptance check.
3. Commit and push, then open a pull request with `gh pr create`.
4. Watch the check run with `gh pr checks` or the Actions tab. It should go red within a few minutes, with the failing assertion showing the expected value 7.187840270062114.
5. Close the pull request without merging and delete the branch.

If the repo does not exist yet, do the smaller version: add `.github/workflows/hello.yml` with only a `workflow_dispatch` trigger and one step, `run: echo "hello from a runner"`. Push it, open the Actions tab, click Run workflow, and read the log.

Source: plan sections 5 (M2 "Done when" and M3 exercises) and 10.1 (2026-09-14); the `gh` commands are two of the six listed in bkm2kob5x.txt, section 1.

## Done when

- You can read the YAML above and say what every keyword does without looking at the table.
- You have watched one pull request go red and one go green.
- A `$25` spending limit is set on the organization, and every job in the repo has `timeout-minutes`.
- Every schedule in the repo uses an off-hour minute.
- You can point at the `job_heartbeat` table and explain why it exists.
