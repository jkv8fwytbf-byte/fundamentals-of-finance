# HANDOFF

Live state for Claude Code. Chat history is not kept between sessions; only files on disk are. Keep this file current after each meaningful step, not only at the end. If nothing is in flight, say so plainly.

## Now

Nothing in flight. Milestone M0, reading stage. Waiting for Siddharth.

- He reads the colorful editions in `output/pdf/`, in the order given by `docs/0-START-HERE.txt`: PDF 1 tonight, then PDF 2 one chapter an evening.
- After PDF 1 and PDF 2 he may say "go" (or "page X confused me"). Until "go", M1 (accounts) and M2 (code) stay parked.

## Done recently

- Round 2 (2026-09-15, Claude Code): only `main`, and the repo made self-contained.
  - `dev` and `dev2` deleted. `main` is the only branch.
  - The full plan (v4) copied in as `docs/plan.md` (original left at `~/.claude/plans/help-me-out-here-abstract-wilkinson.md`). The nine research reports the documents cite copied in as `docs/sources/*.txt`, with a `README.md` that maps the short names the documents use.
  - Stale paths rewritten in 31 markdown files: `/Users/siddharth/Valuation/` and `~/Valuation/` now point at `~/Desktop/Valuation/`; citations of the plan and the reports now point at `docs/plan.md` and `docs/sources/`. `docs/_build/breaklong.lua` updated so the PDFs still print those paths short. All ten PDFs rebuilt.
  - Old Claude Code memory (his profile, working preferences, project direction) imported from the `~/Downloads` project into this folder's memory.
- Consolidation (2026-09-15, Claude Code): one folder, one branch, one tool.
  - Folder is `/Users/siddharth/Desktop/Valuation`, branch `main`. The old `~/Valuation` (branch `dev`, Cursor) and `~/Valuation-dev2` (branch `dev2`, Codex worktree) folders are gone. Their content is all here: `main` was fast-forwarded to `dev2` (`3e6af79`, the docs plus the colorful reading editions), and the briefing files were brought over from `dev`. Nothing was lost; `dev2` already contained every source edit that had been made on `dev`.
  - `dev` (`25fb538`) and `dev2` (`3e6af79`) were kept as backups at first; deleted in round 2.
  - Briefing simplified for a single tool: `AGENTS.md` folded into `CLAUDE.md` and deleted; `.cursor/` and `.vscode/` deleted; `README.md` shortened; this file rewritten. `docs/0-START-HERE.txt` and `docs/_build/READING-EDITION.md` lost their branch/worktree wording.
  - Stale worktree registration pruned. Old build logs in `docs/_build/` removed.
  - Both PDF pipelines were run from the new location and succeeded: `docs/_build/build.sh` (five plain PDFs, 16 s) and `docs/_build/build.sh reading` (five colorful editions, 21 s, diagrams rendered via Chrome). The test builds were then discarded and the committed PDFs kept, since no PDF source changed and `output/validation/verification.json` records their hashes.
- Colorful reading editions (2026-09-15, Codex, commit `3e6af79`): reading markup in the markdown, a `./docs/_build/build.sh reading` target, five colorful PDFs in `output/pdf/`. The plain PDFs under `docs/` stay as the standard copies. How to rebuild and how the markup works: `docs/_build/READING-EDITION.md`.
- Document 5 (`docs/plan-explained/`, chapters 00–12) and its PDF exist. `docs/_build/build.sh` builds all five plain PDFs, numbered as on disk.
- Milestone M0. Documents only. No calculator, database, or application code. No GitHub remote.

## Next

- Wait for "go". Then M1 (accounts) and M2 (code) per `docs/plan-explained/07-s5-milestones.md`.
- After "go", revisit the content that still describes Cursor as the daily editor (`docs/read-this-first.md` section 11 "Setting up Cursor for this repo", `docs/guide/02-cursor-and-cline.md`, `docs/_build/reading-maps/4-the-guide.md` chapter 2 entry). Those describe the planned dev stack, and the stack decision is his; do not rewrite them on your own.
- Small dependency to know about: `docs/_build/render-reading-diagrams.cjs` (used by the PDF 1 reading build) looks for Playwright locally first and falls back to the copy bundled with the Codex runtime under `~/.cache/codex-runtimes/`. If Codex is uninstalled and that cache goes, the reading build of PDF 1 needs `npm install playwright` in this folder (or globally) before it will run again. The committed `output/pdf/1-read-this-first.pdf` is unaffected.

## Decisions

- This project is local and private. No GitHub for this repo. Do not add a remote. Do not push.
- One tool: Claude Code. One folder: `/Users/siddharth/Desktop/Valuation`. One branch: `main`. No worktrees or side branches unless he asks.
- `CLAUDE.md` is the briefing. This file is the live state. Do not add a third instruction file (`AGENTS.md`, `CODEX.md`, `CONTINUE.md`, or the like).
- Commit on `main` when a chunk is done. Do not leave finished work uncommitted for days.
- `docs/plan.md` is the full plan (v4). Document 5 restates it; when they differ, `docs/plan.md` wins. Change it only when he changes the plan. `docs/sources/` are frozen inputs.
- Estimates, not advice. No buy, sell, hold, or target price.
- Markdown is the source; PDFs are built copies. Edit the markdown, then rebuild.

## Blocked / wait-for-Siddharth

- "Go" (after he has read PDF 1 and PDF 2).
- Watchlist names and free-account yes/no are later (M2 and M1). Not now.
