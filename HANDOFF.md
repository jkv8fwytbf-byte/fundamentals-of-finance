# HANDOFF

Live state for Cursor, Claude Code, and Codex. One worker, three seats. Chat history is not shared; only files on disk are. Keep this file current after each meaningful step, not only at the end. If nothing is in flight, say so plainly.

There are two copies of this file, one in each worktree. Keep it current in the folder you are actually working in. If you change it in one folder, the other copy can drift until someone copies it again.

## Now

Two folders, two branches. Do not merge them unless Siddharth asks.

- Cursor folder: `/Users/siddharth/Valuation` on branch **`dev`**.
- Codex folder: `/Users/siddharth/Valuation-dev2` on branch **`dev2`**. Colorful PDFs: `/Users/siddharth/Valuation-dev2/output/pdf/`.
- Briefing files now exist in both worktrees: `AGENTS.md` (canonical), `CLAUDE.md`, `HANDOFF.md`, `README.md`, `.cursor/rules/shared-briefing.mdc`. On `dev2` they are uncommitted. Do not add `CODEX.md` or `CONTINUE.md`.

Nothing else in flight. M0 reading stage. Wait for Siddharth.

## Done recently

- Briefing copied (2026-09-15, not merged, not pushed): the files above now sit in both `/Users/siddharth/Valuation` (`dev`) and `/Users/siddharth/Valuation-dev2` (`dev2`). `pdf-preview.mdc` was already on `dev2`; it was left as-is. Docs, PDFs, and the build pipeline were not copied.
- Codex (2026-09-15, local only, not pushed): branch `dev2`, commit `3e6af79` "Add colorful reading editions of all five PDFs". One commit on top of `dev` (`5b614b5`). Adds reading markup in the markdown, a `./docs/_build/build.sh reading` pipeline, and the five colorful PDFs in `output/pdf/`. The plain PDFs under `docs/` stay as the standard copies. `dev2` has no upstream. Do not push unless he asks.
- Three tools intertwined: every new session reads `AGENTS.md` then this file; updates this file after each meaningful step, not only at the end.
- `docs/plan-explained/` chapters 00–12 exist. `docs/5-the-plan-explained.pdf` is built. `docs/_build/build.sh` builds all five PDFs (on `dev2`, also the reading editions).
- Uncommitted on **`dev`** (`/Users/siddharth/Valuation`): this HANDOFF update; small edits to `docs/read-this-first.md`, `docs/guide/15-damodaran-watch-order.md`, `docs/_build/header.tex`, `docs/_build/build.sh`, `docs/0-START-HERE.txt`; PDFs 1–4 rebuilt; untracked `docs/plan-explained/` and `docs/5-the-plan-explained.pdf`. Several of those overlap `dev2`, but the `dev2` copies have extra reading markup. Do not discard the `dev` working tree to "catch up".
- Uncommitted on **`dev2`** (`/Users/siddharth/Valuation-dev2`): the briefing files copied today. Do not mix those with Codex's document/PDF/build work.
- Milestone M0. Documents only. No calculator, database, or application code. No GitHub remote. Existing remote is Cursor Private (`origin`). Nothing committed unless he asks.

## Next

- To read the colorful editions: open `/Users/siddharth/Valuation-dev2/output/pdf/` (order in that folder's `docs/0-START-HERE.txt`). After PDF 1 and PDF 2 he may say "go". Until then M1 (accounts) and M2 (code) stay parked.
- Keep new Cursor/Claude work in the `dev` folder unless he asks to move. Keep Codex's reading-edition work on `dev2`. Merge later only if he asks.
- He may bounce Cursor ↔ Claude Code ↔ Codex when a tool hits a usage limit. Pick up from this file in the folder you are working in. Do not redo work listed above.

## Decisions

- This project is local and private. No GitHub for this repo. Do not add a remote. Do not push unless he asks. Leave the existing Cursor Private `origin` alone.
- `AGENTS.md` is the briefing. This file is the live state. Do not add a fourth instruction file (`CODEX.md`, `CONTINUE.md`, or the like).
- `docs/plan.md` is not in this folder. Use `docs/plan-explained/`. Do not invent `docs/plan.md`.
- Estimates, not advice. No buy, sell, hold, or target price.
- Two worktrees until he says otherwise: `dev` = `/Users/siddharth/Valuation`; `dev2` = `/Users/siddharth/Valuation-dev2` (committed reading editions, plus the copied briefing). Do not force-reset, do not delete `dev2`. Do not merge unless he asks.

## Files touched

This copy: `HANDOFF.md`, `AGENTS.md`, `CLAUDE.md`, `.cursor/rules/shared-briefing.mdc`, `README.md`. Present in both worktrees. On `dev2` they are uncommitted.

Already dirty on **`dev`**, not from this copy: `docs/plan-explained/`, `docs/5-the-plan-explained.pdf`, `docs/_build/build.sh`, `docs/_build/header.tex`, `docs/read-this-first.md`, `docs/guide/15-damodaran-watch-order.md`, `docs/0-START-HERE.txt`, PDFs 1–4.

Codex on **`dev2`**: the commit `3e6af79` (73 files). Colorful PDFs live in `output/pdf/`. How to rebuild them: `docs/_build/READING-EDITION.md`.

## Blocked / wait-for-Siddharth

- "Go" (after he has read PDF 1 and PDF 2).
- Whether to merge `dev2` into `dev` (or the other way). Not now.
- Watchlist names and free-account yes/no are later (M2 and M1). Not now.
