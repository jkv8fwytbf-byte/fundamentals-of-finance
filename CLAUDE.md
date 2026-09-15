# Claude Code briefing

This folder is Siddharth's local, private copy of the Valuation project. Claude Code is the only AI tool that works here now (Cursor and Codex were dropped on 2026-09-15). There is no GitHub for this repo. Do not add a remote. Do not push. Chat history does not survive a session; files on disk are the memory.

This file is the briefing. `HANDOFF.md` is the live state. Do not add a third instruction file (`AGENTS.md`, `CODEX.md`, `CONTINUE.md`, or the like).

## What this is

A private Damodaran valuation system, still in the reading stage (milestone M0). The product in this folder is the documents. There is no calculator, database, or application code yet. Work after M0 is parked until Siddharth says "go".

The system in plain words: `docs/read-this-first.md`.

## Where to start (every new session)

1. This file.
2. `HANDOFF.md` — immediately after this file. Live state: what is in flight, what was just done, what is next. Do not skip it.
3. Then only the markdown you need for the current **Now** item in `HANDOFF.md`. Do not ingest the whole tree.

If **Now** is empty, say so plainly. Do only what Siddharth asked in this chat, or wait.

Humans read the PDFs. Claude reads the markdown under `docs/`. Never open a `.pdf` as text. The human reading order of the five PDFs is `docs/0-START-HERE.txt`.

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
| Start here | `docs/0-START-HERE.txt` | — | — |
| The system in plain words | `docs/read-this-first.md` | `docs/1-read-this-first.pdf` | `output/pdf/1-read-this-first.pdf` |
| Damodaran refresher | `docs/damodaran-essentials/` | `docs/2-damodaran-essentials.pdf` | `output/pdf/2-damodaran-essentials.pdf` |
| Critics | `docs/other-side/` | `docs/3-the-other-side.pdf` | `output/pdf/3-the-other-side.pdf` |
| Tools manual | `docs/guide/` | `docs/4-the-guide.pdf` | `output/pdf/4-the-guide.pdf` |
| The plan, section by section | `docs/plan-explained/` | `docs/5-the-plan-explained.pdf` | `output/pdf/5-the-plan-explained.pdf` |
| The full plan (v4) | `docs/plan.md` | — | — |
| Research reports the documents cite | `docs/sources/` (see its `README.md`) | — | — |

`docs/plan.md` is the full plan (v4, 2026-09-14). Document 5 (`docs/plan-explained/`) restates it in shorter sentences; when they differ, `docs/plan.md` wins. Change it only when Siddharth changes the plan. `docs/sources/` holds the nine research reports the documents cite; they are frozen inputs, not documents to edit.

Rebuild from `docs/` with `docs/_build/build.sh` (plain PDFs into `docs/`) or `docs/_build/build.sh reading` (colorful editions into `output/pdf/`). Needs pandoc and tectonic; the reading build also needs node, Playwright, and Chrome. How the reading markup works: `docs/_build/READING-EDITION.md`. Edit the markdown, then rebuild. Do not treat a PDF as the source.

## Outside this folder

- The Damodaran corpus: `/Users/siddharth/Downloads/financeMD/` (markdown mirror of his site, about 3,900 files, 89 MB), with the raw archives next to it in `~/Downloads/` (`damodaran-full-part*.tar.gz`, `damodaran-notes-part*.tar.gz`, `damodaran-data-01.zip`, `damodaran-data-02.zip`, `fcffsimpleginzu.xlsx`). The documents cite it by full path. It stays there; do not copy it into this repo.
- Sessions before 2026-09-15 ran from `~/Downloads`, so their transcripts sit under `~/.claude/projects/-Users-siddharth-Downloads/`. Their memory has been imported into this folder's Claude Code memory; there is nothing to fetch from there routinely.

## How to work

- One folder, one branch: this folder, `main`. There are no other branches. Do not create worktrees or side branches unless asked.
- Match the writing: plain, calm, terms defined on first use. See `docs/read-this-first.md`.
- Prefer editing existing docs over duplicating them.
- Commit on `main` when a chunk of work is done, with a plain message. Never push; there is nowhere to push to.
- Do not paste API keys or secrets. There should be no `.env` here yet.
- Estimates, not advice: do not print buy, sell, hold, or a target price.
- When you write about the future system, keep the six rules in `docs/read-this-first.md` section 3: golden test, vintage, source and licence class, India rules, ranges not points, no advice.
- The planned public GitHub code repo (`valuation`) is after "go". This folder is not that repo.

## What not to do

- Do not invent a GitHub remote, a public repo, or a sharing service.
- Do not start M1 (accounts) or M2 (code) until Siddharth says "go".
- Do not convert PDFs to markdown as a workaround.
- Do not copy chat transcripts into the repo.
