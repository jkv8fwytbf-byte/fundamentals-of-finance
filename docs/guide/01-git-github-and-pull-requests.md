# Chapter 1. Git, GitHub, branches, pull requests and CI checks {#r4-git}

::: {.reading-only .optional}
**For the code-work stage.** Start with the vocabulary and history model; return to the commands and exercises when working on code.
:::

## What it is (plain words and an analogy)

Git is a program that keeps a history of every change to the files in a folder. It runs on your Mac. Each saved snapshot is called a commit, and each commit has a short message. The folder plus its history is called a repository, or repo.

A branch is a separate line of commits that starts from a copy of the main line. The main line is a branch too, and it is called `main`. You do work on a branch so that `main` stays clean until the work is checked.

GitHub is a website that stores a copy of your repo and adds three things on top of git. A pull request (PR) is a request to merge a branch into `main`, shown as a diff with a comment thread. A diff is the list of lines added and removed. Issues are a to-do list attached to the repo. GitHub Actions is a robot that runs scripts when something happens, for example on every PR or every night at a set time.

CI stands for continuous integration. It means "run the checks automatically on every PR". A check is a script that passes or fails, such as a test or a type check. Branch protection is a rule that `main` can change only through a PR whose checks pass. A merge conflict happens when two branches changed the same lines and git cannot pick one; you pick.

`gh` is GitHub's command-line tool. It lets you make PRs and watch checks from the terminal instead of the website.

The analogy: a family recipe book. `main` is the printed book on the shelf. A branch is a photocopy of one page that you scribble on. A commit is each time you put the pencil down and date the margin. A PR is handing the photocopy to the family with your changes marked in red. CI is the taste test that runs by itself before anyone reads the page. A merge is pasting the approved page back into the book. A merge conflict is two cousins who both rewrote step 3, and someone has to decide.

## Why this tool now (for this project)

Every week of the twelve-week plan ends with a merged PR that CI passed. That is the unit of progress. If you cannot make a branch, open a PR, and read a diff, you cannot do rule 5 from chapter 0.

Source: /Users/siddharth/Desktop/Valuation/docs/sources/bkm2kob5x.txt, "12-week evening schedule" (2026-09-14)

GitHub Actions is also where the correctness rules live. The golden test runs there. A PR that moves the Almarai value per share off 7.187840270062114 must go red, and red means it cannot merge. The same Actions robot runs the nightly jobs (pull new filings, re-value the watchlist, check for a new risk-premium file).

Source: /Users/siddharth/Desktop/Valuation/docs/sources/bkm2kob5x.txt, section 2 (2026-09-14); /Users/siddharth/Desktop/Valuation/docs/plan.md, section 10.6 (2026-09-14)

Cost: the repo is private, inside a free GitHub organization you own. A private repo on the free plan gets 2,000 Linux minutes of Actions per month, then $0.006 per minute, with a $25 spending cap set in the plan. Public repos get unlimited minutes, but this repo stays private.

Source: /Users/siddharth/Desktop/Valuation/docs/sources/bkm2kob5x.txt, section 0 (2026-09-14); /Users/siddharth/Desktop/Valuation/docs/plan.md, sections 2 and 5 M2 (2026-09-14)

## How it is used in this project

- The repo is named `valuation`. It is created in M2 inside your organization, then handed to you. Your GitHub account is `jkv8fwytbf-byte`.
- Week 1 security, before any code: turn on two-factor authentication (2FA, a second code from an app at login) and save the recovery codes offline. Turn on secret scanning and push protection, so GitHub physically refuses a commit that contains an API key. Use fine-grained personal access tokens, one per purpose, scoped to one repo, with an expiry.
- `main` is protected. Every change goes: branch, commits, PR, CI green, explain-back (rule 3), merge with squash. Squash means the branch's many commits become one commit on `main`, so the history reads like a diary.
- CI on every PR runs a type check, a linter (a style checker), and vitest (the test runner). The golden test is one of those tests. The fixture file holding the expected numbers is protected in CI, so an agent cannot edit the answer key.
- Nightly jobs are Actions too: `ingest-edgar`, `value-watchlist`, `watch-erp-crp`, `rag-eval`, `news-headlines`, `realised-prices`. Each writes a heartbeat row, and a staleness alarm fires after 36 hours of silence. Schedules run off the hour (for example 03:17, not 03:00), because GitHub drops many jobs scheduled exactly on the hour. A cron schedule is the line in the Actions file that says when a job runs.
- Nothing licensed ever enters git. `.gitignore` (a list of files git must ignore) covers `.env*` files, caches, and raw data dumps. Keys live in three places only: the local `.env` file, GitHub Actions secrets, and the hosting provider's environment settings.

Source: /Users/siddharth/Desktop/Valuation/docs/plan.md, sections 5 (M1, M2) and 10.6 (2026-09-14); /Users/siddharth/Desktop/Valuation/docs/sources/bkm2kob5x.txt, sections 1, 2 and 15 (2026-09-14)

### The six gh commands

Learn exactly these six and stop. Cursor's agent runs `gh` from the terminal, so knowing them lets you read what the agent did to your repo.

| Command | What it does, in plain words |
|---|---|
| `gh repo create` | Makes a new repo on GitHub from the folder you are in. |
| `gh pr create` | Opens a pull request for the branch you are on. It asks for a title and a description. |
| `gh pr view --web` | Opens the current PR in your browser so you can read the diff and comments. |
| `gh pr checks` | Lists the CI checks on the current PR and whether each passed, failed, or is still running. |
| `gh pr merge --squash --delete-branch` | Merges the PR as one commit and deletes the branch. Only works when checks are green and protection allows it. |
| `gh run watch` | Watches an Actions run live in the terminal, line by line, until it finishes. |

Source: /Users/siddharth/Desktop/Valuation/docs/sources/bkm2kob5x.txt, section 1 (2026-09-14). The one-line descriptions are mine, from using the tool; the manual at https://cli.github.com/manual/ is the reference.

### The daily loop, as commands

```
git switch -c add-costco-to-watchlist     # new branch, named for the change
# ... edit files, or let Cursor edit them, then read the diff ...
git diff                                  # rule 5: read it
git add -A
git commit -m "Add Costco to the watchlist"
git push -u origin add-costco-to-watchlist
gh pr create                              # opens the PR
gh pr checks                              # wait for green
gh pr merge --squash --delete-branch      # after explain-back
git switch main && git pull               # back to the trunk
```

## Learn it

All free. Hours are the ones stated in the learning-path report, which checked every link on 2026-09-14.

### GitHub Skills (interactive courses that run inside a real repo, graded by Actions)

| Course | URL | Hours |
|---|---|---|
| Introduction to GitHub | https://github.com/skills/introduction-to-github | under 1 |
| Communicate using Markdown | https://github.com/skills/communicate-using-markdown | about 0.5 |
| Review pull requests | https://github.com/skills/review-pull-requests | about 0.5 |
| Resolve merge conflicts | https://github.com/skills/resolve-merge-conflicts | under 0.5 |
| Release-based workflow | https://github.com/skills/release-based-workflow | about 1 |
| Connect the dots (issues to PRs) | https://github.com/skills/connect-the-dots | about 0.5 |

Why: you do the work in a real repo and a robot grades it. Go to the repo URLs directly; the github.com/skills front page now leads with Copilot exercises, but these classic courses still work.

### Pro Git, 2nd edition (Chacon and Straub), free online book

URL: https://git-scm.com/book/en/v2. Read only these, in this order: chapter 2 Git Basics (about 1.5 hours), chapter 3 Git Branching (about 2 hours, especially 3.1 to 3.3 and 3.6), chapter 6 GitHub (about 1 hour), and chapters 7.6 Reset Demystified and 7.7 Advanced Merging (about 1 hour) the first time you wreck a branch. Skip chapters 4, 9 and 10; they are server administration and internals. Why: it is the reference the tooling is written against, and chapter 3's diagrams are the best cure for "I do not know what a branch actually is".

### gh CLI manual

URL: https://cli.github.com/manual/, about 1 hour to skim. Why: you only need the six commands above, and the manual is where you check a flag.

### GitHub Actions

- Quickstart, https://docs.github.com/en/actions/get-started/quickstart, about 0.5 hours.
- Understand GitHub Actions, https://docs.github.com/en/actions/get-started/understand-github-actions, about 1 hour.
- Hands-on: https://github.com/skills/hello-github-actions (about 1 hour), then https://github.com/skills/test-with-actions (about 1 hour).

Why: this is where the golden test and the nightly robots live.

### Security, week 1

- 2FA: https://docs.github.com/en/authentication/securing-your-account-with-two-factor-authentication-2fa/about-two-factor-authentication
- Fine-grained tokens: https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens
- Secret scanning and push protection: https://docs.github.com/en/code-security/secret-scanning/introduction/about-secret-scanning

Total: about 8 hours for git, GitHub and `gh`, about 5 hours for Actions, and about 4 hours for the security set.

Source: /Users/siddharth/Desktop/Valuation/docs/sources/bkm2kob5x.txt, sections 1, 2 and 15 (2026-09-14)

## 10-minute exercise

::: {.reading-only .optional}
**For the practical stage.** Use this exercise when working on this chapter's tool. The following "Done when" checklist tells you how to judge completion.
:::

Create and resolve a merge conflict on a throwaway repo. No AI tool. This is the first item on the M3 exercise list, done early on scratch files so the real repo is safe.

```
mkdir -p ~/Desktop/Valuation/scratch/conflict-drill && cd ~/Desktop/Valuation/scratch/conflict-drill
git init
echo "growth = 0.05" > inputs.txt
git add inputs.txt && git commit -m "Start"
git switch -c cousin-a
echo "growth = 0.06" > inputs.txt
git commit -am "Cousin A raises growth"
git switch main
echo "growth = 0.04" > inputs.txt
git commit -am "Main lowers growth"
git merge cousin-a
```

Git will stop and say there is a conflict in `inputs.txt`. Open the file. You will see both versions between markers that look like `<<<<<<<`, `=======` and `>>>>>>>`. Delete the markers and keep the line you decide is right. Then:

```
git add inputs.txt
git commit -m "Resolve: keep 0.05, neither cousin cited a source"
git log --oneline --graph
```

Read the graph. That picture, two lines joining, is what a merge is. Write in the attempts file (chapter 0) what you guessed a branch was and what you now think it is.

Source: /Users/siddharth/Desktop/Valuation/docs/plan.md, section 5 M3 (2026-09-14). The commands are standard git; Pro Git chapter 3.2 covers the same drill.

## Done when

::: {.reading-emphasis .key-idea}
- You can draw `main`, a branch, a PR and a merge on paper and explain each word without notes.
- You have resolved one merge conflict by hand in the drill above.
- 2FA is on, the recovery codes are saved offline, and push protection is on for the `valuation` repo.
- You have run each of the six `gh` commands at least once (the merge one on a real PR).
- Your first PR is merged by you, with CI green, and you explained every changed file out loud first.
- The Skills courses "Introduction to GitHub" and "Resolve merge conflicts" show as completed in your GitHub account.
:::
