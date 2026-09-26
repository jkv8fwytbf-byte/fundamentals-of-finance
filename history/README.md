# History

This file is the changelog of the project, newest first, and the guide to the archive branches.
The fuller day-by-day story is section 2 of `docs/6-where-we-are.md` (PDF 6), written for you when you came back lost.

## Changelog

All times are India time. Git is the program on your Mac that keeps a saved history of every change to a folder. A commit is one saved snapshot in that history; the seven-character codes such as `c9e0551` are commit names.

### 26 September 2026, afternoon: one public repository for everything

- You chose one public GitHub repository for the whole project, and this is it: https://github.com/jkv8fwytbf-byte/fundamentals-of-finance. It was renamed today from `fundamentas_of_finance`, the empty repository that had appeared on your account in the morning.
- The folder `/Users/siddharth/Desktop/Valuation` was linked to it and pushed. A remote is a saved link from a folder to its online copy; a push uploads your commits along that link. The folder keeps its old name. Git does not care what the folder is called.
- Before the push, one commit was amended: the recap commit became `c9e0551`, with its message and some wording reworded in `CLAUDE.md`, `HANDOFF.md`, `docs/0-START-HERE.txt` and document 6, PDF 6 rebuilt, and the author set to the GitHub no-reply address. Amending rewrites a commit in place, which is safe only when nobody else has the old version. This one had never left the Mac, so it was allowed. It carries the tag `before-github`. A tag is a named bookmark on one commit; this one marks the last commit made under the old never-push rule.
- The branch `main` is now protected. A branch is a parallel line of history inside the same folder, and `main` is the line that counts. Protected means three things: changes reach `main` only through pull requests, nobody can force-push (overwrite its history), and nobody can delete it. A pull request is a request, made on GitHub, to merge one branch into another, with a page where the change can be read and discussed first. To merge is to bring one branch's commits into another. A direct push to `main` is refused.
- Three archive branches were created from old commits that had survived in the folder's history. See the table below.
- The rest of the project came in on import branches, in this order. Each was merged with a merge commit (a commit that records the join) rather than squashed into one, and each was kept after merging, so the branch list stays a map of what came from where.
  1. `github-rules`: `CLAUDE.md`, `HANDOFF.md`, `.gitignore`, the pull request template, decision 001 ([PR #11](https://github.com/jkv8fwytbf-byte/fundamentals-of-finance/pull/11)). A `.gitignore` is a list of file names that git must never save; it is how keys and junk stay out.
  2. `front-page`: `README.md` and `docs/README.md` ([PR #12](https://github.com/jkv8fwytbf-byte/fundamentals-of-finance/pull/12)).
  3. `plan-history`: the `history/` folder, including every draft of the plan ([PR #13](https://github.com/jkv8fwytbf-byte/fundamentals-of-finance/pull/13)).
  4. `reports`: `reports/how-indian-business-groups-work.pdf`, made by Codex on 7 September 2026, without its third-party source PDFs; and `reports/learn-openrouter.html`, a page that teaches OpenRouter with real code and outputs, made with Claude on 16 September and exported today from a private Claude artifact. It contains no key ([PR #14](https://github.com/jkv8fwytbf-byte/fundamentals-of-finance/pull/14)).
  5. `diversify`: `projects/diversify`, the Next.js website started on 17 September, source only, without the `node_modules` folder of downloaded packages. It was imported with git subtree, a way of copying another repository's history into a folder of this one, so its own two commits survive ([PR #15](https://github.com/jkv8fwytbf-byte/fundamentals-of-finance/pull/15)).
  6. `ai-learning-kit`: `projects/ai-learning-kit`, the eight-week AI curriculum Codex made on 16 September, with its `.env.example` but not the `.env` that holds the OpenRouter key ([PR #16](https://github.com/jkv8fwytbf-byte/fundamentals-of-finance/pull/16)).
  7. `xts-backend`: `projects/xts-backend`, a file snapshot of the "Finance Watchlist & Notes Backend" from your siddhartxts GitHub account, repository `backend-xts-latest`, one commit (`b6b392c`) dated 22 June 2026; the copy on this Mac was cloned on 2 September. It is built with FastAPI (a Python toolkit for web services) and Postgres with pgvector (a database that can also search by meaning). No git history was imported, because sibling copies had tracked a `.env`; only `.env.example` was kept ([PR #17](https://github.com/jkv8fwytbf-byte/fundamentals-of-finance/pull/17)).
  8. `record-the-move`: the pull request numbers in this list and on the front page, and the updated `HANDOFF.md` (this entry itself came in with `plan-history`) ([PR #18](https://github.com/jkv8fwytbf-byte/fundamentals-of-finance/pull/18)).
- One more branch, `your-first-merge`, is left as an open pull request for you to merge yourself ([PR #19](https://github.com/jkv8fwytbf-byte/fundamentals-of-finance/pull/19)).
- Tags and a release. The tag `m0` sits on the `main` commit that merged the front page (`e63790a`, PR #12). Its GitHub Release, "M0: the documents, 14 September 2026", attaches six PDFs: the five reading editions from `output/pdf/` (`1-read-this-first.pdf` to `5-the-plan-explained.pdf`) and `docs/6-where-we-are.pdf`. A release is a GitHub page attached to a tag, with files to download. The tags `plan-v1`, `plan-v2`, `plan-v3`, `plan-v4` and `plan-v5-draft` sit on the plan-history commits.
- Milestones, labels and issues were set up on GitHub. An issue is a note on GitHub that tracks one task or one open decision. A milestone groups issues towards one goal; here each milestone is one numbered stage of the plan, from "M0: Documents and diagrams" (closed) to "M5: Only if others use it". A label is a short word attached to an issue to sort it; the five labels made for this project are `decision`, `docs`, `repo`, `project` and `later`. The Labels page also shows the ten labels GitHub adds to every new repository (such as `bug` and `documentation`); they are not used here. Each open decision has an issue:
  - go or wait;
  - free accounts at M1;
  - the daily editor;
  - where the corpus goes;
  - rebuild the corpus;
  - rotate the OpenRouter key;
  - first watchlist names;
  - add CI later (CI means automatic checks that run whenever code changes);
  - revisit the Cursor wording;
  - keep or delete the private Valuation copy.
- From now on the daily workflow is the loop in section 6 of the front page (`README.md`), which follows chapter 1 of the guide (`docs/guide/01-git-github-and-pull-requests.md`). Make a branch named for the change (`git switch -c <branch>`), edit, check with `git diff`, commit with a plain sentence, push the branch, and open a pull request with `gh pr create`. Merge daily changes with `gh pr merge --squash --delete-branch`, which folds the branch into one commit and removes it. Then `git switch main && git pull`; a pull downloads the new commits from GitHub. Today's imports used merge commits and kept their branches on purpose; daily changes do not need that. Commits you make on the Mac use the GitHub no-reply address, set in this folder's git config. Merges are made by GitHub and use your account's own email unless "Keep my email addresses private" is ticked in GitHub Settings, Emails.

### 26 September 2026, morning: the recap and the mistaken push

- 10:09 to 10:18. In a chat that had no folder open, you asked how to work in the cloud with GitHub, then "can you help me do it". That chat created a public repository, `jkv8fwytbf-byte/Valuation`, and pushed all six commits of this folder to it. It never read `CLAUDE.md` or `HANDOFF.md`, which had said since 15 September: local and private, no GitHub, never push. No key or password was in the upload; this was checked twice.
- 10:19. An empty public repository, `fundamentas_of_finance`, appeared on the same account, made outside any Claude chat. In the afternoon it became this repository.
- 10:41. You opened a session in this folder and asked for a recap.
- About 11:35. With your approval, the `Valuation` repository was made private and the folder's remote was removed. The folder was local-only again.
- 12:03. The recap, document 6 (`docs/6-where-we-are.md` and its PDF), was first committed, together with a new status block at the top of `docs/0-START-HERE.txt` and updated `CLAUDE.md` and `HANDOFF.md`. Eleven read-only helper agents had first read all 29 chat transcripts from 12 to 26 September, and the recap was then checked claim by claim. In the afternoon, at 12:53 and before the first push, that commit was amended; the amended version is `c9e0551`, which is why git shows 12:53 for it.

### 23 September 2026: orientation

- 18:35 to 18:54. You came back after nine days away saying "haywire, I don't know what to do, resume". Claude found milestone M0 finished, nothing running, the folder on the Desktop, and the Damodaran corpus missing from the Mac.
- It wrote a dated status block at the top of `docs/0-START-HERE.txt`, updated `HANDOFF.md`, `CLAUDE.md` and its memory notes, and committed `5b46007`. Nothing was pushed. No project work started.

### 18 to 22 September 2026: no sessions

- No Claude conversations at all. This matches the week away.

### 17 September 2026: Docker day, and diversify

- Open WebUI was torn down, rebuilt in Docker at `~/Docker/open-webui`, and wiped again minutes later. At 16:38 you had Docker Desktop removed, and at 16:52 you reinstalled it yourself. None of this is part of the plan.
- About 15:24 the small website `diversify` was started on the Desktop with Next.js, a toolkit for making websites. Its starter files were committed; the four pages added that afternoon (portfolio, audit, library, map) were not. It now lives at `projects/diversify` in this repository.
- Around this day the Damodaran corpus folders vanished from Downloads. No Claude session deleted or moved them, and nobody knows where they went.

### 16 September 2026: side projects

- Codex built an eight-week AI learning kit at `~/Desktop/remaining`. It now lives at `projects/ai-learning-kit`, without its `.env`.
- From 15:35 you learned OpenRouter with Claude in `~/Desktop/openrouter`, added $10 of credits yourself, and got a readable guide, `LEARN_OPENROUTER.html`. That session used about $0.12 of the credits. The guide is now `reports/learn-openrouter.html`.
- At 16:55 you used Cursor to save your OpenRouter key into the learning kit's `.env` file. That file stays out of this repository.
- From 17:10 Open WebUI ran in Docker on top of OpenRouter, outside the plan.

### 15 September 2026: one folder, one branch, Claude Code only

- In the afternoon, with you, Cursor and Codex all working in the folder, Codex made the colorful reading editions of the five PDFs (commit `3e6af79`, "Add colorful reading editions of all five PDFs"). The folder moved from `~/Valuation` to `~/Desktop/Valuation`, and the repository was left half broken across three tools.
- 15:47: "I only want to work in Claude Code". Claude merged the other branches into `main`, removed the Cursor and Codex setup files, folded `AGENTS.md` into `CLAUDE.md`, and rewrote `HANDOFF.md` (commit `06d9650`, 15:55). 15:56: keep `main` only, so Claude then deleted the other branches.
- The plan (v4) was copied in as `docs/plan.md` and the nine research reports as `docs/sources/`. Old paths were fixed in 31 files and all ten PDFs were rebuilt. Commit `90f8db1`.
- The rule written that day for this folder: local and private, no GitHub, never push. It stood until this morning's mistake and was replaced this afternoon.
- Two archive branches, `archive/dev-2026-09-15` and `archive/first-attempt-plan-v5`, keep this day's leftover work. See the table below.

### 14 September 2026: the plan, the documents, the first commits

- 10:40 to 14:28. You turned the plan down five times: once each for v1, v2 and v3, and twice for v4. At 14:28 you approved v4 for M0 only. The drafts are in `history/plan/`.
- 14:30 to 16:25. Five diagrams were drawn as FigJam boards, document 1 was sent at 14:38, and after a resume pass all four documents existed by 16:25.
- 16:44 to 18:22. The PDFs were numbered 1 to 4 in reading order and `docs/0-START-HERE.txt` was written. PDF 5, The Plan Explained, was written that evening. A bug that dropped colons from every web link was fixed, and all five PDFs were rebuilt and sent at 18:22.
- 17:40 to 17:45. The AI assistant inside Cursor turned the folder into a git repository: an empty `main` (`d7d7ece`) and a `dev` branch holding all the files (`5b614b5`). It also uploaded a private copy to Cursor's own git host. A Cursor cloud-agent environment was committed the same day (`0f165a2`), now kept as `archive/cursor-cloud-agent`.

### 13 September 2026: the corpus, then the project begins

- 03:00 to 13:00. Claude sorted Downloads into four folders. Two of them became the Damodaran corpus: `finance-and-valuation`, a copy of Damodaran's NYU website plus 12 finance PDFs (6,188 files, 1.1 GB), and `financeMD`, the same files turned into 3,916 markdown files (89 MB). Markdown is the plain-text format the PDFs are built from.
- 20:18. The valuation project began. You described the goal, asked about many tools, and answered four questions. Plan v1 arrived at 21:27.

### 12 September 2026: side jobs

- Two jobs unrelated to valuation. Every markdown file on the Mac was copied into one folder, 18,935 files, now `~/Documents/md files`. A classroom JupyterHub was built with Docker, now `~/Documents/DockerAgain` and public on GitHub as `jkv8fwytbf-byte/DockerAgain`.
- Late that night Damodaran's NYU website was downloaded into about 70 zip files in Downloads. They became the corpus the next morning.

## The archive branches

Three old lines of work are kept as branches whose names start with `archive/`. All three grow from commit 2 of `main`, `5b614b5` "Add project files on the dev branch". The old `dev2` tip, `3e6af79` "Add colorful reading editions of all five PDFs", needs no branch: it is simply commit 3 of `main`.

| Branch | Commit | Date | What it contains | Why it is frozen |
|---|---|---|---|---|
| `archive/dev-2026-09-15` | `25fb538` (on top of `6958ba8`) | 15 Sep 2026 | The tip of the old `dev` branch: two checkpoint commits that add `AGENTS.md`, `.cursor/rules`, `HANDOFF.md`, the thirteen plan-explained chapters and PDF 5, among other edits. 28 files, 941 lines added. | Its useful content reached `main` on 15 September: `dev2` already had every source edit, and the briefing files were carried over. Merging it would bring back `AGENTS.md`, which `CLAUDE.md` forbids. |
| `archive/first-attempt-plan-v5` | `d2b2279` (on top of `7e778aa`) | 15 Sep 2026 | An abandoned first attempt at the consolidation. It briefly held a withdrawn "Plan v5: public" draft, plus wording edits across 49 files (925 lines added, 161 removed). | The draft was withdrawn and the attempt abandoned the same day. The draft text is kept in `history/plan/v5-withdrawn.md`; nothing on the branch is wanted on `main`. |
| `archive/cursor-cloud-agent` | `0f165a2` | 14 Sep 2026 | A Cursor cloud-agent environment: `.cursor/environment.json`, `.cursor/install.sh`, a font-substitute script and a `.gitignore`. 4 files, 154 lines. | The `.cursor/` files were removed on 15 September when the project moved to Claude Code only. Merging would put them back. |

Frozen means: never commit to an archive branch, and never merge one into `main`. To look at one, move your folder onto it:

```
git switch archive/dev-2026-09-15
```

`git switch` changes the files on disk to that branch's state. Look, do not edit, then come back with `git switch main`. To compare an archive branch with `main` without moving anywhere:

```
git diff main...archive/dev-2026-09-15 --stat
```

The three dots mean "what the archive branch has that `main` does not, counted from where they parted". Swap in the other two branch names for the same two commands.

## The plan drafts

Every version of the plan, from v1 to the withdrawn v5, is in `history/plan/`. Start with `history/plan/README.md`, which says what each draft is and what you said about it. The tags `plan-v1` to `plan-v5-draft` point at the commits on the `plan-history` branch. The plan that counts is `docs/plan.md`, the full v4.

## Not in this repository

The Damodaran corpus (the website mirror and its markdown conversion) is not here; it has been missing from the Mac since about 17 September and is needed again at M1. Also never here: chat transcripts, Claude's memory folders, any `.env` file or key, the resume, certificates, photos, personal notes, the fair-value-2036 folders, and files over 50 MB. A clone (a full copy of this repository downloaded to another computer) will contain none of them. The future code for the valuation system (plan section 5, M2) goes in a separate private repository named `valuation`, inside a free GitHub organisation you will own (plan section 5: created at M1, the repository at M2; the organisation does not exist yet); this repository is not that.
