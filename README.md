# Fundamentals of finance

This repository holds the documents of a Damodaran valuation system, the plan and every draft of it, three side projects and two reports. It is also the place where Siddharth learns GitHub, so its branches and pull requests are practice as much as record. On the Mac the folder is still called Valuation, at `/Users/siddharth/Desktop/Valuation`; git does not care what a folder is called.

Git is a program that keeps a history of every change to the files in a folder. GitHub is a website that stores a copy of that folder and its history, and adds pull requests, issues and releases on top. The words below are the ones you will meet on this page and on GitHub.

## 1. Words you will see

| Word | What it means here |
|---|---|
| repository | A folder plus the history of every change to it, or repo for short. This one is public, at `jkv8fwytbf-byte/fundamentals-of-finance`. |
| clone | A full copy of a repository on another machine, history included. The folder on the Mac is the clone you work in. |
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
| protected branch | A branch that can change only through a pull request. `main` is protected: no direct push, no force push, no deletion. |
| tag | A fixed name for one commit, such as `m0` or `before-github`, so you can find it later. |
| release | A page on GitHub attached to a tag, with a title, notes and files to download. |
| milestone | A named goal on GitHub that issues are grouped under. Here they run from M0 to M5. |
| issue | One item on the to-do list attached to the repository. The open decisions live there. |
| archive branch | A frozen branch kept so old work stays visible. Never commit to one and never merge one. |
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
| `output/validation/` | Codex's validation record of the 15 September reading-edition build (its checksums predate a rebuild made later that day). |
| `history/` | `history/README.md` is the changelog and lists the archive branches. `history/plan/` holds every draft of the plan, v1 to the withdrawn v5. |
| `projects/` | Three side projects; `projects/README.md` introduces them. `diversify` is a Next.js website started on 17 September (source only). `ai-learning-kit` is an eight-week AI curriculum made by Codex on 16 September. `xts-backend` is a file snapshot of a FastAPI and Postgres backend, the "Finance Watchlist & Notes Backend", whose one commit is dated 22 June 2026 (the copy on this Mac was cloned on 2 September). |
| `reports/` | Two reports, with a `README.md`: `how-indian-business-groups-work.pdf` (Codex, 7 September) and `learn-openrouter.html`, a page that teaches OpenRouter with real code and outputs (Claude, 16 September). |

## 3. The branches

Every branch that mattered is still here, so the branch list is a map of how the repository was built. Today is 26 September 2026.

| Branch | What it holds | State |
|---|---|---|
| `main` | Everything below, merged in. | Protected. Changes only through pull requests. |
| `github-rules` | `CLAUDE.md`, `HANDOFF.md`, `.gitignore`, the PR template, decision 001. | Merged today with a merge commit, kept. |
| `front-page` | `README.md` and `docs/README.md`. | Merged today, kept. |
| `plan-history` | `history/`. | Merged today, kept. |
| `reports` | `reports/`. | Merged today, kept. |
| `diversify` | `projects/diversify`, brought in with git subtree (a git command that copies another repository's files and commits into a folder of this one) so its two commits survive. | Merged today, kept. |
| `ai-learning-kit` | `projects/ai-learning-kit`. | Merged today, kept. |
| `xts-backend` | `projects/xts-backend`. | Merged today, kept. |
| `record-the-move` | The changelog entry for today and the `HANDOFF.md` update. | Merged today, kept. |
| `your-first-merge` | Left for you. | Open pull request. You merge it yourself. |
| `archive/dev-2026-09-15` | Commit `25fb538`, the old `dev` branch tip of 15 September: `AGENTS.md`, `.cursor/rules`, the plan-explained chapters, PDF 5. | Frozen. |
| `archive/first-attempt-plan-v5` | Commit `d2b2279`, an abandoned first attempt of 15 September that briefly held a withdrawn "Plan v5: public" draft. | Frozen. |
| `archive/cursor-cloud-agent` | Commit `0f165a2` of 14 September, a Cursor cloud-agent environment: `.cursor/environment.json`, `install.sh`, a font-substitute script. | Frozen. |

Git subtree is a git command that copies another repository's files and commits into a folder of this one.

To look at an archive branch, and then to compare it with `main` file by file:

```
git switch archive/dev-2026-09-15
git diff main...archive/dev-2026-09-15 --stat
```

`git switch main` brings you back. Do not commit while on an archive branch, and never merge one: the first would bring back `AGENTS.md`, which `CLAUDE.md` forbids.

## 4. Reading order

Open `docs/0-START-HERE.txt` first. It gives the order: PDF 1 tonight (about 40 minutes), then PDF 2 one chapter an evening, PDF 5 after PDF 1, PDFs 3 and 4 later. The colorful editions are in `output/pdf/`. The same six PDFs are attached to the release "M0: the documents, 14 September 2026" on the tag `m0`, for download without cloning. If you feel lost, read `docs/6-where-we-are.pdf` (PDF 6) first: it says what happened from 12 to 26 September, what exists and what comes next.

Nothing to install, nothing to pay for, no accounts yet.

## 5. Status, 26 September 2026

Milestone M0, the reading documents, is done. Nothing after it starts until Siddharth has read PDF 1 and PDF 2 and says "go" (or "page X confused me"). Until then: no accounts, no code, no money.

Today the folder moved from "local only, never push" to this one public repository. The last commit made under the old rule is tagged `before-github`. The open decisions are issues, grouped under milestones from "M0: Documents and diagrams" (closed) to "M5: Only if others use it". They are:

- go or wait;
- free accounts at M1;
- the daily editor;
- where the corpus goes;
- rebuild the corpus;
- rotate the OpenRouter key;
- the first watchlist names;
- add CI later;
- revisit the Cursor wording;
- keep or delete the private Valuation copy.

One pull request, `your-first-merge`, is open and waiting for you.

## 6. How a change gets in

`main` is protected, so a direct push to it is refused. Every change, however small, takes this loop. The commit email is GitHub's no-reply address, set in this folder's git configuration.

```
git switch -c add-costco-to-watchlist     # new branch, named for the change
# ... edit files, then read the diff ...
git diff                                  # read what changed
git add -A
git commit -m "Add Costco to the watchlist"
git push -u origin add-costco-to-watchlist
gh pr create                              # opens the PR
gh pr checks                              # wait for green
gh pr merge --squash --delete-branch      # after explain-back
git switch main && git pull               # back to the trunk
```

`gh` is GitHub's command-line tool. The PR body has three headings, which the template fills in for you: What changed, Why, For the reviewer. Explain-back means you explain every changed file out loud before you merge. There are no automatic checks yet, so `gh pr checks` has nothing to report; adding CI (checks that run on every PR) is an open issue.

Today's imports did it differently, on purpose. Each import branch was merged with a merge commit and kept, so the history of each import stays visible and the branch list stays a map. Daily changes from now on use a squash merge and delete the branch, so `main` reads like a diary with one line per change.

## 7. What is not here and why

- No `.env` file and no key of any kind. `projects/ai-learning-kit` and `projects/xts-backend` each keep an `.env.example`; the real files stay on the Mac. `xts-backend` came in as a file snapshot without its git history, because sibling copies had tracked a `.env`.
- No `node_modules` in `projects/diversify`; source only.
- No resume, certificates, photos or personal notes (the TheOdessy folder), and none of the fair-value-2036 folders.
- Not the Damodaran corpus (his website mirror and its markdown conversion). It has been missing from the Mac since about 17 September and is needed again at M1. It will not be copied into this repository when it returns.
- No chat transcripts, no Claude memory folders, no file over 50 MB.
- Not the third-party source PDFs behind `reports/how-indian-business-groups-work.pdf`.
- Not the future code. The valuation system itself (plan section 5, milestone M2) goes in a separate private repository named `valuation` on the same account. This repository is not that.

## 8. History

`history/README.md` is the changelog, from 12 September to today, and lists the archive branches. `history/plan/` holds the drafts: v1, v2, v3, v4-1, v4-2, v4-3-approved, v4-4-resume-plan, v4-5-addendum-stopped and v5-withdrawn, with the tags `plan-v1` to `plan-v5-draft` on the matching commits.

In short: the project began on 13 September at 20:18, and plan v1 followed at 21:27. On 14 September v1 to v4 were rejected and questioned; v4 was approved for M0 only at 14:28. The five documents followed that day, and at 17:40 Cursor's agent made the folder a git repository. On 15 September Codex made the colorful reading editions, the folder moved to the Desktop, and the rule became "only Claude Code, keep main, local and private, never push". 16 and 17 September were side projects only; 18 to 22 September had no sessions; 23 September was the orientation. On 26 September at 10:18 a separate chat pushed the folder to a public repository by mistake; it was made private and unlinked at 11:35. PDF 6 was committed at 12:03, and in the afternoon Siddharth chose one public repository for everything: this one.

The pull requests of 26 September, in merge order:

1. `github-rules` (PR number filled in after the merge)
2. `front-page` (PR number filled in after the merge)
3. `plan-history` (PR number filled in after the merge)
4. `reports` (PR number filled in after the merge)
5. `diversify` (PR number filled in after the merge)
6. `ai-learning-kit` (PR number filled in after the merge)
7. `xts-backend` (PR number filled in after the merge)
8. `record-the-move` (PR number filled in after the merge)
9. `your-first-merge`, open, for you

The release "M0: the documents, 14 September 2026", on the tag `m0`, attaches six PDFs: the five colorful editions from `output/pdf/` and `docs/6-where-we-are.pdf`.
