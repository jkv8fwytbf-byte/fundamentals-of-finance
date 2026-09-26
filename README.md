# Fundamentals of finance

This repository holds the documents of a Damodaran valuation system, the plan and every draft of it, three side projects and two reports. It is also the place where Siddharth learns GitHub, so its branches and pull requests are practice as much as record. On the Mac the folder is still called Valuation, at `/Users/siddharth/Desktop/Valuation`; git does not care what a folder is called.

Git is a program that keeps a history of every change to the files in a folder. GitHub is a website that stores a copy of that folder and its history, and adds pull requests, issues and releases on top. The words below are the ones you will meet on this page and on GitHub.

**Start here, Siddharth.** The rest of this page speaks to you as "you".

1. Your first pull request, [PR #19](https://github.com/jkv8fwytbf-byte/fundamentals-of-finance/pull/19), is waiting for you. Before you merge it, open GitHub Settings, Emails, and tick "Keep my email addresses private" (section 6 says why). Then open the pull request, read the one changed line under Files changed, and merge it: click the small arrow on the green button, choose Squash and merge, confirm, then press Delete branch.
2. Read [PDF 1](output/pdf/1-read-this-first.pdf) (about 40 minutes), then [PDF 2](output/pdf/2-damodaran-essentials.pdf), one chapter an evening.
3. When you have read both, write "go" (or "page X confused me") as a comment on [issue #1](https://github.com/jkv8fwytbf-byte/fundamentals-of-finance/issues/1).

If you feel lost, read [PDF 6](docs/6-where-we-are.pdf) first. It was written at midday on 26 September, before the move to GitHub that afternoon, so where it says "never push" or "local only", this page is right.

## 1. Words you will see

| Word | What it means here |
|---|---|
| repository | A folder plus the history of every change to it, or repo for short. This one is public, at `jkv8fwytbf-byte/fundamentals-of-finance`. |
| clone | A full copy of a repository on another machine, history included. The folder on the Mac is not a clone: the repository started there and was pushed up to GitHub. It is the working copy, the folder you edit in, and it behaves like a clone. |
| remote | The copy of the repository that lives somewhere else. Here it is the GitHub copy, and git calls it `origin`. |
| commit | One saved snapshot of the files, with a short message that says what changed. |
| branch | A separate line of commits that starts from a copy of the main line. You work on a branch so that `main` stays clean until the work is checked. |
| main | The main line. It is a branch too, and it is the one visitors read. |
| pull request | A request to merge a branch into `main`, shown as a diff with a comment thread. To merge is to paste the branch's changes into `main`. PR for short. |
| diff | The list of lines added and removed. |
| merge commit | A commit that joins a branch into `main` and keeps every commit of that branch visible in the history. |
| squash merge | A merge where the branch's many commits become one commit on `main`, so the history reads like a diary. |
| push | Upload your new commits from the Mac to the remote on GitHub. |
| pull | Download new commits from the remote to the Mac. |
| force push | A push that overwrites history on the remote instead of adding to it. |
| protected branch | A branch with rules on GitHub that block some kinds of change; GitHub marks it with a shield. `main` changes only through a pull request, with no force push and no deletion. The three archive branches are protected only against force push and deletion. |
| tag | A fixed name for one commit, such as `m0` or `before-github`, so you can find it later. |
| release | A page on GitHub attached to a tag, with a title, notes and files to download. |
| milestone | A named goal on GitHub that issues are grouped under. Here they run from M0 to M5. |
| issue | One item on the to-do list attached to the repository. The open decisions live there. |
| archive branch | A branch kept so old work stays visible. GitHub blocks deleting it or overwriting its history, but it would still accept a new commit, so "frozen" is a rule you keep: never commit to one and never merge one. |
| .gitignore | A list of files git must ignore, so they never enter the repository. |

## 2. What is in this folder

| Entry | What it is |
|---|---|
| `README.md` | This page. |
| `CLAUDE.md` | The briefing Claude Code reads at the start of every session. |
| `HANDOFF.md` | The live state: what is in flight, what was just done, what comes next. |
| `.gitignore` | The list of files git must ignore. |
| `.github/PULL_REQUEST_TEMPLATE.md` | The form every pull request starts from, with the headings What changed, Why and For the reviewer. |
| `docs/` | The six documents. `0-START-HERE.txt` is the reading order. PDFs 1 to 6 sit next to their markdown sources. Also `plan.md` (the full plan, v4), `sources/` (the nine research reports the documents cite), `diagrams/`, `_build/` (the PDF build scripts), `docs/README.md` and `docs/decisions/`. |
| `output/pdf/` | The five colorful reading editions of PDFs 1 to 5. Humans read these. |
| `output/validation/` | The validation record Codex (OpenAI's AI coding app) made of the 15 September reading-edition build. Its checksums, fingerprints of each file, predate a rebuild made later that day. |
| `history/` | `history/README.md` is the changelog and lists the archive branches. `history/plan/` holds every draft of the plan, v1 to the withdrawn v5. |
| `projects/` | Three side projects; `projects/README.md` introduces them. `diversify` is a Next.js website (Next.js is a toolkit for making websites) started on 17 September, source only. `ai-learning-kit` is an eight-week AI curriculum made by Codex on 16 September. `xts-backend` is a file snapshot of a FastAPI (a Python toolkit for web services) and Postgres (a database) backend, the "Finance Watchlist & Notes Backend", whose one commit is dated 22 June 2026 (the copy on this Mac was cloned on 2 September). |
| `reports/` | Two reports, with a `README.md`: `how-indian-business-groups-work.pdf` (Codex, 7 September) and `learn-openrouter.html`, a page that teaches OpenRouter (a service that puts one door in front of many AI models) with real code and outputs (Claude, 16 September). |

## 3. The branches

Every branch that mattered is still here, so the branch list is a map of how the repository was built. The eight branches from `github-rules` to `record-the-move` were all merged on 26 September 2026, each with a merge commit, and kept.

| Branch | What it holds | State |
|---|---|---|
| `main` | Everything below, merged in. | Protected. Changes only through pull requests. |
| `github-rules` | `CLAUDE.md`, `HANDOFF.md`, `.gitignore`, the PR template, decision 001. | Merged 26 September with a merge commit; branch kept. |
| `front-page` | `README.md` and `docs/README.md`. | Merged 26 September with a merge commit; branch kept. |
| `plan-history` | `history/`. | Merged 26 September with a merge commit; branch kept. |
| `reports` | `reports/`. | Merged 26 September with a merge commit; branch kept. |
| `diversify` | `projects/diversify`, brought in with git subtree (a git command that copies another repository's files and commits into a folder of this one) so its two commits survive, and `projects/README.md`, the index of the side projects. | Merged 26 September with a merge commit; branch kept. |
| `ai-learning-kit` | `projects/ai-learning-kit`. | Merged 26 September with a merge commit; branch kept. |
| `xts-backend` | `projects/xts-backend`. | Merged 26 September with a merge commit; branch kept. |
| `record-the-move` | The pull request numbers in the changelog and on this page, and the `HANDOFF.md` update. | Merged 26 September with a merge commit; branch kept. |
| `your-first-merge` | The owner line at the top of this page, left for you as your first pull request ([PR #19](https://github.com/jkv8fwytbf-byte/fundamentals-of-finance/pull/19)). | Yours to merge; the pull request page shows whether it is done. |
| `archive/dev-2026-09-15` | Commit `25fb538`, the old `dev` branch tip of 15 September: `AGENTS.md`, `.cursor/rules`, the plan-explained chapters, PDF 5. | Frozen by rule; GitHub blocks deletion and force push. |
| `archive/first-attempt-plan-v5` | Commit `d2b2279`, an abandoned first attempt of 15 September that briefly held a withdrawn "Plan v5: public" draft. | Frozen by rule; GitHub blocks deletion and force push. |
| `archive/cursor-cloud-agent` | Commit `0f165a2` of 14 September, a Cursor (an AI code editor) cloud-agent environment: `.cursor/environment.json`, `install.sh`, a font-substitute script. | Frozen by rule; GitHub blocks deletion and force push. |




To look at an archive branch, and then to compare it with `main` file by file:

```
git switch archive/dev-2026-09-15
git diff main...archive/dev-2026-09-15 --stat
```

`git switch main` brings you back. Do not commit while on an archive branch, and never merge one into `main`: merging `archive/dev-2026-09-15`, for example, would bring back a top-level `AGENTS.md`, which `CLAUDE.md` forbids.

## 4. Reading order

Read in this order: [PDF 1](output/pdf/1-read-this-first.pdf) tonight (about 40 minutes), then [PDF 2](output/pdf/2-damodaran-essentials.pdf) one chapter an evening, [PDF 5](output/pdf/5-the-plan-explained.pdf) after PDF 1, and [PDF 3](output/pdf/3-the-other-side.pdf) and [PDF 4](output/pdf/4-the-guide.pdf) later. These are the five colorful editions in `output/pdf/`. The full list, with times, is in [docs/0-START-HERE.txt](docs/0-START-HERE.txt). If you feel lost, read [PDF 6](docs/6-where-we-are.pdf) before PDF 1; it is in `docs/` only and says what happened from 12 to 26 September, what exists and what comes next. The five colorful editions and PDF 6 are also attached to the release [M0: the documents, 14 September 2026](https://github.com/jkv8fwytbf-byte/fundamentals-of-finance/releases/tag/m0), for download without cloning.

Nothing to install, nothing to pay for, no accounts yet.

## 5. Status, 26 September 2026

Milestone M0, the reading documents, is done. Nothing after it starts until you have read PDF 1 and PDF 2 and say "go" (or "page X confused me") as a comment on [issue #1](https://github.com/jkv8fwytbf-byte/fundamentals-of-finance/issues/1). Until then: no accounts, no code, no money.

On 26 September the folder moved from "local only, never push" to this one public repository. The last commit made under the old rule is tagged `before-github`. The open decisions and tasks are issues #1 to #10: nine under the milestone "M1: Accounts and the editor" and one, the watchlist names, under "M2: Foundation build". The six milestones run from "M0: Documents and diagrams" (closed) to "M5: Only if others use it". Decisions carry the label `decision`; tasks carry `docs` or `repo`.

- [#1](https://github.com/jkv8fwytbf-byte/fundamentals-of-finance/issues/1) go or wait;
- [#2](https://github.com/jkv8fwytbf-byte/fundamentals-of-finance/issues/2) free accounts at M1;
- [#3](https://github.com/jkv8fwytbf-byte/fundamentals-of-finance/issues/3) the daily editor;
- [#4](https://github.com/jkv8fwytbf-byte/fundamentals-of-finance/issues/4) where the corpus goes (the corpus is the copy of Damodaran's website and data that used to be on the Mac);
- [#5](https://github.com/jkv8fwytbf-byte/fundamentals-of-finance/issues/5) rebuild the corpus;
- [#6](https://github.com/jkv8fwytbf-byte/fundamentals-of-finance/issues/6) the first watchlist names;
- [#7](https://github.com/jkv8fwytbf-byte/fundamentals-of-finance/issues/7) add CI later (automatic checks on every pull request);
- [#8](https://github.com/jkv8fwytbf-byte/fundamentals-of-finance/issues/8) revisit the Cursor wording;
- [#9](https://github.com/jkv8fwytbf-byte/fundamentals-of-finance/issues/9) rotate the OpenRouter key;
- [#10](https://github.com/jkv8fwytbf-byte/fundamentals-of-finance/issues/10) keep or delete the private Valuation copy.

One pull request, `your-first-merge` ([PR #19](https://github.com/jkv8fwytbf-byte/fundamentals-of-finance/pull/19)), was left for you to merge yourself.

## 6. How a change gets in

`main` is protected, so a direct push to it is refused. Every change, however small, takes this loop.

About email addresses: commits you make on the Mac use GitHub's no-reply address, set in this folder's git configuration (a new clone needs `git config user.email` set again). Merges are made by GitHub itself, even when you type `gh pr merge`, and GitHub stamps them with your account's own email unless "Keep my email addresses private" is ticked in GitHub Settings, Emails. The eight import merges of 26 September carry an Apple private-relay address for that reason; tick the box before your next merge.

```
cd ~/Desktop/Valuation                    # the working copy
git switch main && git pull               # start from the latest main
git switch -c fix-typo-in-readme          # new branch, named for the change
# ... edit files ...
git diff                                  # read what changed
git add -A
git commit -m "Fix a typo in the README"
git push -u origin fix-typo-in-readme
gh pr create                              # opens the PR; the template gives the headings
# gh pr checks                            # skip for now: no checks exist until issue #7
gh pr merge --squash --delete-branch      # after explain-back
git switch main && git pull               # back to main
```

`gh` is GitHub's command-line tool. The PR body has three headings, which the template fills in for you: What changed, Why, For the reviewer. Explain-back means you explain every changed file out loud before you merge. There are no automatic checks yet, so `gh pr checks` has nothing to report; adding CI (checks that run on every PR) is issue #7.

The same loop is in chapter 1 of the tools guide (`docs/guide/01-git-github-and-pull-requests.md`, in PDF 4). That chapter was written for the future private `valuation` code repository (plan milestone M2), so its lines about a private repository, an organisation, Actions minutes and waiting for green checks describe that repository, not this one.

The eight pull requests of 26 September did it differently, on purpose. Each import branch was merged with a merge commit and kept, so the history of each import stays visible and the branch list stays a map. Daily changes from now on use a squash merge and delete the branch, so `main` reads like a diary with one line per change.

## 7. What is not here and why

- No `.env` file and no key of any kind. `projects/ai-learning-kit` and `projects/xts-backend` each keep an `.env.example`; the real files stay on the Mac. `xts-backend` came in as a file snapshot without its git history, because sibling copies had tracked a `.env`.
- No `node_modules` in `projects/diversify`; source only.
- No resume, certificates, photos or personal notes, and none of the fair-value-2036 folders.
- Not the Damodaran corpus (his website mirror and its markdown conversion). It has been missing from the Mac since about 17 September and is needed again at M1. It will not be copied into this repository when it returns.
- No chat transcripts, no Claude memory folders, no file over 50 MB.
- Not the third-party source PDFs behind `reports/how-indian-business-groups-work.pdf`.
- Not the future code. The valuation system itself (plan section 5, milestone M2) goes in a separate private repository named `valuation`, inside a free GitHub organisation you will own (the plan creates it at M1; it does not exist yet). This repository is not that, and neither is the private `Valuation` copy from the morning of 26 September.

## 8. History

`history/README.md` is the changelog, from 12 September to today, and lists the archive branches. `history/plan/` holds the drafts: v1, v2, v3, v4-1, v4-2, v4-3-approved, v4-4-resume-plan, v4-5-addendum-stopped and v5-withdrawn, with the tags `plan-v1` to `plan-v5-draft` on the matching commits.

In short: the project began on 13 September at 20:18, and plan v1 followed at 21:27. On 14 September v1 to v4 were rejected and questioned; v4 was approved for M0 only at 14:28. The five documents followed that day, and at 17:40 Cursor's agent made the folder a git repository. On 15 September Codex made the colorful reading editions, the folder moved to the Desktop, and the rule became "only Claude Code, keep main, local and private, never push". 16 and 17 September were side projects only; 18 to 22 September had no sessions; 23 September was the orientation. On 26 September at 10:18 a separate chat pushed the folder to a public repository by mistake; it was made private and unlinked at 11:35. PDF 6 was first committed at 12:03, and in the afternoon you chose one public repository for everything: this one.

The pull requests of 26 September, in merge order:

1. `github-rules` ([PR #11](https://github.com/jkv8fwytbf-byte/fundamentals-of-finance/pull/11))
2. `front-page` ([PR #12](https://github.com/jkv8fwytbf-byte/fundamentals-of-finance/pull/12))
3. `plan-history` ([PR #13](https://github.com/jkv8fwytbf-byte/fundamentals-of-finance/pull/13))
4. `reports` ([PR #14](https://github.com/jkv8fwytbf-byte/fundamentals-of-finance/pull/14))
5. `diversify` ([PR #15](https://github.com/jkv8fwytbf-byte/fundamentals-of-finance/pull/15))
6. `ai-learning-kit` ([PR #16](https://github.com/jkv8fwytbf-byte/fundamentals-of-finance/pull/16))
7. `xts-backend` ([PR #17](https://github.com/jkv8fwytbf-byte/fundamentals-of-finance/pull/17))
8. `record-the-move` ([PR #18](https://github.com/jkv8fwytbf-byte/fundamentals-of-finance/pull/18))
9. `your-first-merge`, open, for you

The release "M0: the documents, 14 September 2026", on the tag `m0`, attaches six PDFs: the five colorful editions from `output/pdf/` and `docs/6-where-we-are.pdf`.
