# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this is

A FastAPI backend for tracking stock tickers (`watchlist`) and storing/searching finance notes (`finance_notes`), backed by PostgreSQL with the `pgvector` extension. Notes can be bulk-ingested idempotently from an external source/agent.

## Commands

All common workflows are in the `Makefile`:

- `make install` — install runtime + dev deps (`pip install -r requirements-dev.txt`)
- `make dev` — run the API locally with autoreload (`uvicorn main:app --app-dir src --reload`)
- `make test` — run the full pytest suite
- `make fmt` — format with black (`black src alembic tests`)
- `make migrate` — `alembic upgrade head`
- `make revision m="msg"` — autogenerate a migration
- `make up` / `make down` / `make logs` — full Docker stack (api + postgres + adminer)

Run a single test: `pytest tests/test_api.py::test_watchlist_crud` (the four tests live in `tests/test_api.py`).

There is no linter or type-checker configured — `black` is the only style tool.

## Critical: flat-import layout

The app runs with `--app-dir src`, so `src/` is the import root and **all imports inside `src/` are flat/top-level**, not package-relative: `from routers import ...`, `from database import Base`, `from deps import db_dependency`. There is no `src` package prefix and routers have no `__init__` re-exports beyond an empty `routers/__init__.py`. New modules must follow this convention or imports break.

This is also why:
- `pytest.ini` sets `pythonpath = src` so tests can `from main import app`.
- `alembic/env.py` does a bare `import models` (Alembic is invoked from the repo root where `src` is on the path via `pytest.ini`/`--app-dir`; for ad-hoc alembic runs ensure `src` is importable).

## Architecture

Request flow: `main.py` mounts three routers → each router declares an `APIRouter(prefix=...)` and depends on shared helpers → SQLAlchemy ORM models → PostgreSQL.

- **`main.py`** — creates `app`, exposes `/health`, includes the `watchlist`, `financenotes`, and `ingest` routers.
- **`models.py`** — SQLAlchemy 2.0 ORM models (`WatchlistItem`, `FinanceNote`). `created_at` uses `server_default=func.now()` so DB-side inserts get correct timestamps. `FinanceNote.external_id` is a unique nullable column that makes ingestion idempotent.
- **`schemas.py`** — Pydantic v2 models. Validators normalize input (tickers uppercased/stripped, tags coerced from CSV string→list, `source_url` must be http(s)). Note the `*Base` / `*Create` / `*Read` / `*Ingest` split; `*Read` uses `from_attributes=True`.
- **`deps.py`** — shared dependencies: `db_dependency` (injected `Session`), `get_or_404(db, Model, id, detail)` (replaces repeated query/None/404 blocks), and `Pagination`/`PaginationParams` (`?limit=&offset=`).
- **`database.py`** — engine/`SessionLocal`/`Base` and the `get_db` generator dependency.
- **`config.py`** — `pydantic-settings` `Settings`; the only setting is `sqlalchemy_database_url` (env var `SQLALCHEMY_DATABASE_URL`, loaded from `.env` if present).

### Routers
- **`watchlist.py`** — CRUD. `IntegrityError` on the unique `ticker` is translated to HTTP 409.
- **`financenotes.py`** — CRUD + list filters: `ticker` (exact), `q` (ILIKE over title/content), `tag`. The `tag` filter casts the JSON column to `JSONB` and uses the `@>` contains operator — **PostgreSQL-only**, not exercised by the SQLite test DB.
- **`ingest.py`** — `POST /ingest/finance-notes` bulk endpoint. Commits one note at a time so a single failure doesn't abort the batch; skips notes whose `external_id` already exists (and catches `IntegrityError` from concurrent inserts) for idempotency.

## Database & migrations

- Alembic migrations live in `alembic/versions/`. `env.py` reads the DB URL from `SQLALCHEMY_DATABASE_URL` (falling back to `alembic.ini`'s empty `sqlalchemy.url`), and uses `models.Base.metadata` as the autogenerate target.
- The `pgvector` extension is enabled by migration `c3e7f1a2b4d6`, but **no vector/embedding column exists on the models yet** — the extension is provisioned ahead of future semantic-search work. The Docker DB image is `pgvector/pgvector:pg16`.
- In Docker, `entrypoint.sh` waits for Postgres, runs `alembic upgrade head`, then starts uvicorn — migrations are applied automatically on container start.

## Testing

`tests/conftest.py` provides a `client` fixture: a fresh **in-memory SQLite** DB per test (via `StaticPool`), with `get_db` overridden through `app.dependency_overrides`. No running Postgres is needed for tests. Be aware that Postgres-specific behavior (the JSONB `tag` filter, `server_default` timestamp nuances) is not covered by these SQLite tests.

## Configuration

Copy `.env.example` → `.env` (gitignored). Key vars: `SQLALCHEMY_DATABASE_URL` (use host `db` inside Docker, `localhost` locally), Postgres credentials, and the published host ports (`API_PORT`, `POSTGRES_PORT`, `ADMINER_PORT`). Dev/test tools (`pytest`, `black`) are in `requirements-dev.txt` and intentionally kept out of the runtime Docker image.
