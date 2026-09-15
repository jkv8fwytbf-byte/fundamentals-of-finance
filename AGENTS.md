# Agent briefing

This folder is Siddharth's local, private copy of the Valuation project. Cursor, Claude Code, and Codex all work from the same files here. There is no GitHub for this repo. Do not add a GitHub remote. If git already has a remote, leave it. Do not push unless he asks. Chat history is not shared across tools; files on disk are the shared memory.

This file is the canonical briefing. `CLAUDE.md` and the Cursor rule in `.cursor/rules/` only point here. Change this file, not the pointers. A one-line mention of `HANDOFF.md` on the pointers is allowed so nobody misses it.

## What this is

A private Damodaran valuation system, still in the reading stage (milestone M0). The product in this folder is the documents. There is no calculator, database, or application code yet. Work after M0 is parked until Siddharth says "go".

The system in plain words: `docs/read-this-first.md`.

## Where to start (every new session)

1. This file.
2. `HANDOFF.md` — immediately after this file. Live state: what is in flight, what was just done, what is next. Do not skip it.
3. Then only the markdown you need for the current **Now** item in `HANDOFF.md`. Do not ingest the whole tree.

If **Now** is empty, say so plainly. Do only what Siddharth asked in this chat, or wait.

Humans read the PDFs. Agents read the markdown under `docs/`. Never open a `.pdf` as text. The human reading order of the five PDFs is `docs/0-START-HERE.txt`.

## One worker, three seats

Siddharth may start in Cursor, Claude Code, or Codex, in any order, often because a tool hit a usage limit. Treat them as one worker with three seats. Do not redo work that `HANDOFF.md` says is done. Do not ignore work it says is in flight.

Usage limits often cut a session with no goodbye. A "update the handoff when you finish" protocol will fail. Keep `HANDOFF.md` current **as work happens**.

- After each meaningful step (an edit, a decision, a completed chunk), update `HANDOFF.md` **before** doing more. If the session dies, the last write is the trail.
- If Siddharth says he is switching tools, or that he is near a limit: update `HANDOFF.md` first, then stop.
- Write decisions into files. Do not leave the real answer only in chat.
- If nothing is in flight, `HANDOFF.md` must say so plainly.

Do not add a fourth instruction file (`CODEX.md`, `CONTINUE.md`, or the like). This file is the briefing. `HANDOFF.md` is the live state.

## The map (markdown is canonical)

| Read as | Source | Built PDF |
|---|---|---|
| Start here | `docs/0-START-HERE.txt` | — |
| The system in plain words | `docs/read-this-first.md` | `docs/1-read-this-first.pdf` |
| Damodaran refresher | `docs/damodaran-essentials/` | `docs/2-damodaran-essentials.pdf` |
| Critics | `docs/other-side/` | `docs/3-the-other-side.pdf` |
| Tools manual | `docs/guide/` | `docs/4-the-guide.pdf` |
| The plan, section by section | `docs/plan-explained/` | `docs/5-the-plan-explained.pdf` |

`docs/plan-explained/00-preface.md` names `docs/plan.md` as the full plan. That file is not in this folder. Until it is, use `docs/plan-explained/`. Do not invent `docs/plan.md`.

Rebuild PDFs from `docs/` with `docs/_build/build.sh` (needs pandoc and tectonic). Edit the markdown, then rebuild. Do not treat a PDF as the source.

## How the three tools get this briefing

| Tool | What it reads on its own | What we keep in this folder |
|---|---|---|
| Cursor | `AGENTS.md`, `.cursor/rules/*.mdc` | This file, plus a short rule that points here |
| Codex | `AGENTS.md` | This file |
| Claude Code | `CLAUDE.md` (and `@` imports) | `CLAUDE.md` imports this file |

All three then immediately read `HANDOFF.md`. Do not add a fourth instruction file.

## How to work

- Match the writing: plain, calm, terms defined on first use. See `docs/read-this-first.md`.
- Prefer editing existing docs over duplicating them.
- Keep the PDF previewer mapping (`*.pdf` → `pdf.preview`). See `.cursor/rules/pdf-preview.mdc`.
- Do not commit unless asked. Do not push.
- Do not paste API keys or secrets. There should be no `.env` here yet.
- Estimates, not advice: do not print buy, sell, hold, or a target price.
- When you write about the future system, keep the six rules in `docs/read-this-first.md` section 3: golden test, vintage, source and licence class, India rules, ranges not points, no advice.
- The planned public GitHub code repo (`valuation`) is after "go". This folder is not that repo.

## What not to do

- Do not invent a GitHub remote, a public repo, or a sharing service.
- Do not start M1 (accounts) or M2 (code) until Siddharth says "go".
- Do not convert PDFs to markdown as a workaround.
- Do not copy chat transcripts into the repo.
