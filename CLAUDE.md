# Claude Code briefing

This folder is the working copy of Siddharth's public GitHub repository `jkv8fwytbf-byte/fundamentals-of-finance` (remote `origin`; the folder keeps its old name, Valuation, and git does not mind). Claude Code is the only AI tool that works here (Cursor and Codex were dropped on 2026-09-15). The repository is public: nothing secret and nothing personal may ever be committed (see "What not to do"). How the move to GitHub happened on 2026-09-26 is recorded in `history/README.md` and `docs/decisions/001-one-public-repo-for-everything.md`. Chat history does not survive a session; files on disk are the memory.

This file is the briefing. `HANDOFF.md` is the live state. Do not add a third instruction file at the root (`AGENTS.md`, `CODEX.md`, `CONTINUE.md`, or the like). The side projects in `projects/` keep the files they came with (`projects/diversify/AGENTS.md` and `CLAUDE.md`, `projects/xts-backend/CLAUDE.md`); Claude Code reads them only when working inside those folders. Leave them in place.

## What this is

A Damodaran valuation system. Milestone M0 (the documents and diagrams) is done and closed on GitHub; Siddharth is reading them, and M1 starts when he says "go". The product in this folder is the documents, plus the plan's history (`history/`), three side projects (`projects/`) and two one-off reports (`reports/`), all brought in on 2026-09-26. There is no calculator, database, or application code for the system yet. Work after M0 is parked until Siddharth says "go".

Siddharth was away from the project for about a week from 2026-09-19 and came back without the context. `docs/6-where-we-are.md` (PDF 6) is the recap written for him on 2026-09-26: what happened day by day, what exists, the rules, what comes next. If he arrives lost, point him there first, then to `docs/0-START-HERE.txt`.

The system in plain words: `docs/read-this-first.md`.

## Where to start (every new session)

1. This file.
2. `HANDOFF.md`, immediately after this file. Live state: what is in flight, what was just done, what is next. Do not skip it.
3. Then only the markdown you need for the current **Now** item in `HANDOFF.md`. Do not ingest the whole tree.

If **Now** is empty, say so plainly. Do only what Siddharth asked in this chat, or wait.

Humans read the PDFs. Claude reads the markdown under `docs/`. Never open a `.pdf` as text. The human reading order of the PDFs (1 to 5, plus PDF 6, the recap he should open first if he is lost) is `docs/0-START-HERE.txt`.

## Keep `HANDOFF.md` current as work happens

Usage limits often cut a session with no goodbye. A "update the handoff when you finish" habit will fail. So:

- After each meaningful step (an edit, a decision, a completed chunk), update `HANDOFF.md` **before** doing more. If the session dies, the last write is the trail.
- If Siddharth says he is near a limit or is stopping: update `HANDOFF.md` first, then stop.
- Write decisions into files. Do not leave the real answer only in chat.
- If nothing is in flight, `HANDOFF.md` must say so plainly.
- Do not redo work that `HANDOFF.md` says is done. Do not ignore work it says is in flight.

## The map (markdown is canonical)

| Read as | Source | Plain PDF | Colorful reading edition |
|---|---|---|---|
| Start here | `docs/0-START-HERE.txt` |  |  |
| The system in plain words | `docs/read-this-first.md` | `docs/1-read-this-first.pdf` | `output/pdf/1-read-this-first.pdf` |
| Damodaran refresher | `docs/damodaran-essentials/` | `docs/2-damodaran-essentials.pdf` | `output/pdf/2-damodaran-essentials.pdf` |
| Critics | `docs/other-side/` | `docs/3-the-other-side.pdf` | `output/pdf/3-the-other-side.pdf` |
| Tools manual | `docs/guide/` | `docs/4-the-guide.pdf` | `output/pdf/4-the-guide.pdf` |
| The plan, section by section | `docs/plan-explained/` | `docs/5-the-plan-explained.pdf` | `output/pdf/5-the-plan-explained.pdf` |
| Where we are (recap of 2026-09-26) | `docs/6-where-we-are.md` | `docs/6-where-we-are.pdf` |  |
| Front page of the repository | `README.md` |  |  |
| Decisions log (guide chapter 0, rule 6) | `docs/decisions/` |  |  |
| Changelog and the archive branches | `history/README.md` |  |  |
| Every draft of the plan, with his comments | `history/plan/` |  |  |
| Side projects (diversify, ai-learning-kit, xts-backend) | `projects/` (see its README) |  |  |
| One-off reports | `reports/` (see its README) |  |  |
| The full plan (v4) | `docs/plan.md` |  |  |
| Research reports the documents cite | `docs/sources/` (see its `README.md`) |  |  |

`docs/plan.md` is the full plan (v4, 2026-09-14). Document 5 (`docs/plan-explained/`) restates it in shorter sentences; when they differ, `docs/plan.md` wins. Change it only when Siddharth changes the plan. `docs/sources/` holds the nine research reports the documents cite; they are frozen inputs, not documents to edit.

Rebuild from `docs/` with `docs/_build/build.sh` (plain PDFs into `docs/`) or `docs/_build/build.sh reading` (colorful editions into `output/pdf/`). `build.sh` covers PDFs 1 to 5 only and stamps them 2026-09-14. PDF 6 has no build target and no colorful edition: it was built by hand from `docs/` with the same pandoc line as the `build()` function in `build.sh`, but with `--metadata date="2026-09-26"` (input `6-where-we-are.md`, output `6-where-we-are.pdf`, errors to `_build/6-where-we-are.err`). To rebuild it after an edit, run that line again; do not use `build.sh build 6-where-we-are ...`, which would stamp the wrong date. On 2026-09-26 `_build/header.tex` gained `HyphenChar=None` on the mono font so paths in code spans are never hyphenated; PDFs 1 to 5 were not rebuilt with it (no source changed). Needs pandoc and tectonic; the reading build also needs node, Playwright, and Chrome. How the reading markup works: `docs/_build/READING-EDITION.md`. Edit the markdown, then rebuild. Do not treat a PDF as the source.

## Outside this folder

- The Damodaran corpus is **missing** (checked 2026-09-23). It used to be `/Users/siddharth/Downloads/financeMD/` (markdown mirror of his site, about 3,900 files, 89 MB) with the raw archives next to it in `~/Downloads/` (`damodaran-full-part*.tar.gz`, `damodaran-notes-part*.tar.gz`, `damodaran-data-01.zip`, `damodaran-data-02.zip`, `fcffsimpleginzu.xlsx`). None of that is on the Mac any more (not in Downloads or iCloud Drive, and Spotlight finds nothing; the Trash could not be checked because Claude cannot open it, so he should look there first; no Claude session removed it; most likely a manual clean-up around 2026-09-17). The `Source:` lines in `docs/` still cite the old path on purpose: the text is already written and does not depend on the files. It is needed again from M1 (the day-one exercise in plan section 5 has him find a cell in the workbook) and throughout M2: the golden fixture comes out of the workbook, the datasets go into Neon, and the librarian indexes the blog posts (plan section 5, M1 item 6 and M2 items 2, 3 and 5). Everything in it was a public download from Damodaran's site, so the originals can be fetched again then; Where they go is his call (open decision, see `HANDOFF.md`, Blocked); suggest the same path, `~/Downloads/financeMD/`, because that keeps the 133 `Source:` citations valid, and ask before restoring anywhere. Note that `financeMD/` was not a download but a conversion: a script made on 2026-09-13 (in a temporary folder, now gone; its code survives only in that day's chat transcript under `~/.claude/projects/-Users-siddharth-Downloads/`) turned the site mirror into markdown. Restoring it means re-downloading and re-converting. The four books and `booksMD` are safe in his personal notes folder under `~/Documents` (exact path in Claude's local memory, not in this public repo). Do not rewrite the citations. Do not copy the corpus into this repo when it returns.
- Almost every Claude Code session on this project ran from `~/Downloads`, including the 23 September status check and the 26 September recap; only the 15 September consolidation session ran from this folder. So nearly all transcripts sit under `~/.claude/projects/-Users-siddharth-Downloads/`. Claude Code memory lives in two places, `~/.claude/projects/-Users-siddharth-Downloads/memory/` and `~/.claude/projects/-Users-siddharth-Desktop-Valuation/memory/`; both were updated on 2026-09-26 and they are not identical, so when memory changes, update both.

## How to work

- One folder; `main` is the trunk. Every change goes on a branch named for the change, then a pull request, then a merge (the loop in section 6 of `README.md`; guide chapter 1 has the same loop but was written for the future private code repo). Daily changes merge with squash. The import branches of 2026-09-26 were merged with merge commits and are kept on purpose, so the branch list stays a map. `main` is protected on GitHub: a direct push is refused. Never commit to or merge an `archive/*` branch; they are frozen history (GitHub itself only blocks deleting them or force-pushing), and merging `archive/dev-2026-09-15` would bring back a top-level `AGENTS.md`.
- Match the writing: plain, calm, terms defined on first use. See `docs/read-this-first.md`.
- Prefer editing existing docs over duplicating them.
- Commit on the branch when a chunk of work is done, with a plain message. Then `git push -u origin <branch>` and `gh pr create` with the three headings (What changed, Why, For the reviewer). Siddharth merges, or asks Claude to. Then `git switch main && git pull`. Update `HANDOFF.md` "PRs in flight" when opening or merging. Commits made on the Mac use the GitHub noreply address, set in this folder's git config; do not change it. Merges are made by GitHub and use the account's own email unless "Keep my email addresses private" is on in his GitHub settings (it was off on 2026-09-26; the merges of PRs #11 to #18 carry an Apple private-relay address).
- Do not paste API keys or secrets. There should be no `.env` here yet.
- Estimates, not advice: do not print buy, sell, hold, or a target price.
- When you write about the future system, keep the six rules in `docs/read-this-first.md` section 3: golden test, vintage, source and licence class, India rules, ranges not points, no advice.
- The planned code repo (`valuation`, private, inside a free GitHub organisation he will own; plan section 5 creates the organisation at M1, and none exists yet) is after "go". This repository is not that repo and never holds keys or licensed data.

## What not to do

- Do not commit anything from the never-committed list: `.env` files or keys, the resume, certificates, photos, personal notes, the Damodaran corpus, chat transcripts, memory folders, files over 50 MB. Do not push to `main` directly. Do not force-push anywhere. Do not add a second remote.
- This repository is public. Do not write health details, private account names or addresses, private URLs (Claude artifacts, Cursor's git host), or personal folder paths beyond the project folder into any committed file, commit message, pull request, issue or release note. Keep such details in Claude's local memory.
- Do not start M1 (accounts) or M2 (code) until Siddharth says "go".
- Do not convert PDFs to markdown as a workaround.
- Do not copy chat transcripts into the repo.
