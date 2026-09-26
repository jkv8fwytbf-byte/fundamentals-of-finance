> **About this copy (added 26 September 2026).**
> This folder is a file snapshot of `backend-xts-latest` from the `siddhartxts` GitHub account, taken on 26 September 2026. That repository has a single commit, b6b392c "orignal"; the typo is in the original.
> Its git history was not imported. Git is the tool that records every saved version of a folder, and a commit is one such version. Sibling copies of this project on the Mac had recorded a real `.env` with local database credentials, so only the files came across.
> Only `.env.example` is here. It lists the setting names (ports, Postgres user, password, database and URL) with placeholder values; a `.env` is the same file filled in, and it is never committed.
> How it relates to the plan: this is the ancestor of the watchlist idea in plan section 5 (`docs/plan.md`), a stock watchlist with notes, filtering and bulk ingest. It is not the M2 code. That will live in a separate private repository named `valuation`.
> To run it: copy `.env.example` to `.env`, set a password of your own, then run `docker compose up --build`. Section 4 of the guide below walks through this step by step, including the health check at http://localhost:8000/health.
> The original stays on GitHub under `siddhartxts`. The copy in this repository is the one that counts from now on.
> The rest of this README is the project's own teaching guide, unchanged.

---

# Finance Watchlist & Notes Backend — A Learning Guide

> This README is written as a **teaching guide**, not a typical short GitHub readme.
> It walks a beginner through this exact codebase, slowly and in order. Every
> explanation is based on the code that is actually in this repository today.
> Where something is *not* built yet, this guide says so plainly.

---

## Table of contents

1. [Title and purpose](#1-title-and-purpose)
2. [Big-picture mental model](#2-big-picture-mental-model)
3. [Repository map](#3-repository-map)
4. [How to run the project](#4-how-to-run-the-project)
5. [Docker, explained deeply](#5-docker-explained-deeply)
6. [Startup flow (what happens when you press "up")](#6-startup-flow)
7. [FastAPI explanation](#7-fastapi-explanation)
8. [Database explanation](#8-database-explanation)
9. [Models vs. schemas](#9-models-vs-schemas)
10. [Alembic migrations](#10-alembic-migrations)
11. [API endpoints](#11-api-endpoints)
12. [The ingest endpoint](#12-the-ingest-endpoint)
13. [Testing explanation](#13-testing-explanation)
14. [Makefile and the dev workflow](#14-makefile-and-the-dev-workflow)
15. [Common beginner mistakes](#15-common-beginner-mistakes)
16. [How to read this repo as a learner](#16-how-to-read-this-repo-as-a-learner)
17. [What this repo teaches](#17-what-this-repo-teaches)
18. [What is intentionally not included yet](#18-what-is-intentionally-not-included-yet)
19. [Future roadmap](#19-future-roadmap)
20. [Quick command reference](#20-quick-command-reference)

---

## 1. Title and purpose

### What this project is

This is a small **backend API** for keeping track of stocks and writing notes
about them. It is a web server that other programs (a browser, a script, a
future mobile app, an automated agent) talk to over HTTP. It has no user
interface of its own beyond the automatic documentation page that FastAPI
generates.

It manages two kinds of things:

- **Watchlist items** — a ticker symbol you want to follow (e.g. `AAPL`), with an
  optional company name and free-text notes.
- **Finance notes** — longer notes attached to a ticker: a title, a body of
  content, a list of tags, and an optional source URL.

### What problem it is trying to solve

If you research stocks, you accumulate scattered notes — a price target here, an
earnings summary there. This backend gives those notes **one structured home**
with a stable schema, so they can be created, searched, filtered, and (later)
analyzed programmatically instead of living in random text files.

### What it currently supports

- Create / read / update / delete **watchlist items** (full CRUD).
- Create / read / update / delete **finance notes** (full CRUD).
- **Filtering and search** of notes by ticker, by a single tag, and by a text
  query that matches the title or content.
- **Pagination** on both list endpoints (`limit` / `offset`).
- A **bulk ingest** endpoint that accepts many notes at once and is *idempotent*
  (safe to re-send) when each note carries an `external_id`.
- A `/health` endpoint for monitoring.
- A fully **Dockerized** development stack (API + PostgreSQL + a database GUI).
- **Database migrations** managed by Alembic, applied automatically on startup.
- A small **test suite** that runs without needing a real database.

### What it may support later

The schema is intentionally laid a little ahead of the features. The PostgreSQL
**`pgvector` extension is already enabled** by a migration, even though no
embedding column exists yet — that is groundwork for future *semantic search*
(finding notes by meaning, not just keywords). The `external_id` field on notes
is groundwork for **automated/agent ingestion** from external sources. See the
[roadmap](#19-future-roadmap) for the honest list.

---

## 2. Big-picture mental model

Before any code, hold this picture in your head. A backend like this is a small
assembly line. A request comes in, passes through several stations, becomes a
database row, and a response comes back out.

The tools and their jobs:

| Tool | One-sentence job |
|------|------------------|
| **FastAPI** | Receives HTTP requests and routes them to Python functions. |
| **Pydantic** | Validates and cleans the JSON coming in, and shapes the JSON going out. |
| **SQLAlchemy** | Translates Python objects into SQL and talks to the database. |
| **PostgreSQL** | The actual database that stores the rows on disk. |
| **Alembic** | Versions and applies changes to the database's *structure* (tables/columns). |
| **Docker Compose** | Runs the API, the database, and a DB admin GUI together as one stack. |
| **entrypoint.sh** | Inside the API container: waits for the DB, runs migrations, then starts the server. |
| **uvicorn** | The web server process that actually runs the FastAPI app. |

Here is the flow of a single request, top to bottom:

```
              HTTP request (JSON)
                     │
                     ▼
        ┌──────────────────────────┐
        │   uvicorn (web server)   │   listens on port 8000
        └──────────────────────────┘
                     │
                     ▼
        ┌──────────────────────────┐
        │        FastAPI app       │   matches URL + method to a route function
        │       (src/main.py)      │
        └──────────────────────────┘
                     │
                     ▼
        ┌──────────────────────────┐
        │   Pydantic schema (in)   │   validates & cleans the request body
        │      (src/schemas.py)    │   e.g. "aapl" -> "AAPL"
        └──────────────────────────┘
                     │
                     ▼
        ┌──────────────────────────┐
        │   Router function        │   the business logic for this endpoint
        │  (src/routers/*.py)      │
        └──────────────────────────┘
                     │  uses a DB session (get_db)
                     ▼
        ┌──────────────────────────┐
        │   SQLAlchemy model       │   a Python object that maps to a table row
        │      (src/models.py)     │
        └──────────────────────────┘
                     │  SQLAlchemy turns it into SQL
                     ▼
        ┌──────────────────────────┐
        │       PostgreSQL         │   stores/reads the actual row
        └──────────────────────────┘
                     │
                     ▼
        ┌──────────────────────────┐
        │  Pydantic schema (out)   │   turns the DB row back into clean JSON
        └──────────────────────────┘
                     │
                     ▼
              HTTP response (JSON)
```

And the surrounding infrastructure:

```
   docker compose up
          │
          ├── service: db        (PostgreSQL + pgvector, stores data on a volume)
          ├── service: api       (your FastAPI app; runs entrypoint.sh on boot)
          └── service: adminer   (a web GUI to inspect the database)

   entrypoint.sh (inside api):
      1. wait until db answers "SELECT 1"
      2. alembic upgrade head      ← builds/updates the tables
      3. exec uvicorn ...          ← starts serving requests
```

Keep returning to these two diagrams as you read the rest of the guide.

---

## 3. Repository map

Every important file, what it is, why it exists, and when *you* would touch it.

### Top-level configuration and infrastructure

- **`.env.example`** — A template of the environment variables the project needs
  (ports, database credentials, the database URL). It is committed so others know
  *what* variables exist, but it holds no real secrets. **You touch it** when you
  add a new configuration value that should be documented. You copy it to `.env`
  before running anything.

- **`.gitignore`** — Tells Git which files to never commit. Critically it ignores
  `.env` and `.env.*` (your real secrets) while keeping `!.env.example`. It also
  ignores caches and virtual environments. **You touch it** rarely — when a new
  kind of generated file appears that shouldn't be committed.

- **`.dockerignore`** — Tells Docker which files to *not* copy into the image when
  it builds. It excludes the host virtualenv (wrong-architecture binaries),
  caches, `.git/`, and even `README.md`/`CLAUDE.md` (not needed at runtime). It
  also excludes `.env` so secrets are never baked into an image. **You touch it**
  when you add large files that shouldn't bloat the image.

- **`Dockerfile`** — The recipe for building the API's container image: start from
  Python 3.14-slim, install dependencies, copy the code, and define the startup
  command. **You touch it** when the build process changes (new system packages,
  different base image).

- **`docker-compose.yml`** — Describes the three services (`api`, `db`,
  `adminer`), how they connect, their ports, health checks, and the data volume.
  **You touch it** when you add a service or change how they're wired.

- **`entrypoint.sh`** — The script the API container runs on boot: wait for
  Postgres, apply migrations, start uvicorn. **You touch it** if the startup
  sequence needs to change.

- **`requirements.txt`** — The **runtime** Python dependencies (FastAPI,
  SQLAlchemy, Alembic, the Postgres driver, etc.), pinned to exact versions.
  These go into the Docker image. **You touch it** when you add a library the
  running app needs.

- **`requirements-dev.txt`** — The **development/test** tools (`pytest`,
  `pytest-asyncio`, `black`). It first pulls in `requirements.txt` via `-r`, then
  adds the extra tools. These are deliberately kept *out* of the runtime image.
  **You touch it** when you add a tool used only for development.

- **`Makefile`** — Short aliases for common commands (`make dev`, `make test`,
  `make migrate`, …). **You touch it** when you want a new shortcut. See
  [section 14](#14-makefile-and-the-dev-workflow).

- **`pytest.ini`** — Configures pytest. Two important lines: `pythonpath = src`
  (so tests can `import` modules like `main` directly) and `testpaths = tests`.
  **You touch it** rarely.

- **`alembic.ini`** — Configuration for Alembic (the migration tool). Notably its
  `sqlalchemy.url` is left **empty** on purpose — the real URL comes from an
  environment variable instead (see `alembic/env.py`). **You touch it** rarely.

### The migrations folder

- **`alembic/`** — Everything about database schema versioning.
  - `alembic/env.py` — The script Alembic runs. It reads the database URL from the
    `SQLALCHEMY_DATABASE_URL` environment variable and points Alembic at
    `models.Base.metadata` so autogeneration can compare code to database.
  - `alembic/script.py.mako` — The template used when generating a new migration
    file. You rarely read it.
  - `alembic/versions/*.py` — The actual migration files, each a small,
    timestamped, ordered change to the schema. **You touch this folder** every
    time you change a model — by generating a new migration (`make revision`).
  - `alembic/README` — A stock note from the Alembic template.

### The application source (`src/`)

The app uses a **flat import layout**: it runs with `--app-dir src`, which puts
`src/` on Python's import path. That is why files say `from models import ...`
and `from routers import ...` rather than `from src.models import ...`. Keep this
in mind — it trips up beginners (see [mistakes](#15-common-beginner-mistakes)).

- **`src/main.py`** — The entry point. Creates the FastAPI app, defines `/health`,
  and wires in the three routers. **You touch it** when you add a new router or a
  top-level concern (middleware, startup events).

- **`src/database.py`** — Sets up the SQLAlchemy *engine*, the *session factory*
  (`SessionLocal`), the declarative `Base` that models inherit from, and the
  `get_db` dependency that hands a session to each request. **You touch it** when
  changing how the app connects to the database.

- **`src/config.py`** — A Pydantic-Settings class that reads configuration from
  environment variables (and a `.env` file). Right now it holds exactly one
  setting: the database URL. **You touch it** when you add a new configuration
  value, so there's one typed place for all config.

- **`src/models.py`** — The **SQLAlchemy models**: `WatchlistItem` and
  `FinanceNote`. These Python classes describe the database *tables*. **You touch
  it** when the database structure should change (then you also create a
  migration).

- **`src/schemas.py`** — The **Pydantic schemas**: the shapes of request bodies
  and responses, plus validators that clean input. **You touch it** when the API's
  input/output contract changes.

- **`src/deps.py`** — Small reusable dependencies shared across routers:
  `db_dependency` (inject a session), `get_or_404` (fetch by id or raise 404), and
  `Pagination` (the `limit`/`offset` query parameters). **You touch it** when you
  find yourself repeating a piece of route plumbing.

- **`src/routers/`** — One file per area of the API:
  - `watchlist.py` — CRUD for watchlist items.
  - `financenotes.py` — CRUD plus filtering/search for notes.
  - `ingest.py` — the bulk, idempotent ingest endpoint.
  - `__init__.py` — empty; it just makes `routers` an importable package.
  **You touch this folder** when you add or change endpoints.

### Tests

- **`tests/conftest.py`** — Shared pytest setup. It builds a `client` fixture
  backed by an in-memory SQLite database, so tests need no running Postgres.
- **`tests/test_api.py`** — The actual tests: health, watchlist CRUD, note
  filtering/pagination, and ingest dedup.

### Other

- **`CLAUDE.md`** — Notes for the Claude Code AI assistant about this repo's
  conventions (the flat-import layout, the Postgres-only tag filter, etc.). Not
  required to run anything; useful orientation.

---

## 4. How to run the project

The intended way to run this is with **Docker Compose**, which starts the API,
the database, and a database GUI together. You need Docker installed.

### Step 1 — Create your `.env`

The compose file reads variables like `${API_PORT}` and `${POSTGRES_PASSWORD}`
from a file named `.env`. That file does not exist yet (it's gitignored); you
create it from the template:

```bash
cp .env.example .env
```

Then open `.env` and set real values, in particular `POSTGRES_PASSWORD` and the
matching `SQLALCHEMY_DATABASE_URL`. The template looks like this:

```env
API_PORT=8000
POSTGRES_PORT=5432
ADMINER_PORT=8080

POSTGRES_USER=postgres
POSTGRES_PASSWORD=change-me
POSTGRES_DB=fastapi

# Note the host is "db" — the name of the database service in docker-compose.
SQLALCHEMY_DATABASE_URL=postgresql://postgres:change-me@db:5432/fastapi
```

> If you change `POSTGRES_PASSWORD`, change the password inside
> `SQLALCHEMY_DATABASE_URL` to match, or the API can't log into the database.

### Step 2 — Start the stack

```bash
docker compose up --build
```

- `docker compose up` — start all services defined in `docker-compose.yml`.
- `--build` — (re)build the API image first, so your latest code is used. Use
  this whenever you've changed code or dependencies.

You'll see the database start, then the API container wait for it, run
migrations, and finally print that uvicorn is serving.

The same thing is available as `make up`.

### Step 3 — Check it's alive

In another terminal:

```bash
curl http://localhost:8000/health
# -> {"status":"ok"}
```

### Step 4 — Explore the API in your browser

FastAPI generates interactive documentation automatically. Open:

- **http://localhost:8000/docs** — Swagger UI. Every endpoint is listed; you can
  fill in a body and click "Execute" to make real requests. This is the fastest
  way to learn the API.
- **http://localhost:8000/redoc** — an alternative, read-only documentation view.

### Step 5 — Inspect the database with Adminer

Open **http://localhost:8080** (the `ADMINER_PORT`). Log in with:

- **System:** PostgreSQL
- **Server:** `db` (the service name; Adminer runs *inside* the Docker network)
- **Username / Password / Database:** the `POSTGRES_USER` / `POSTGRES_PASSWORD` /
  `POSTGRES_DB` from your `.env`.

You can browse tables, run SQL, and watch rows appear as you hit the API.

### Other everyday commands

```bash
docker compose logs -f api     # follow the API logs (or: make logs)
docker compose down            # stop and remove the containers (keeps data)
docker compose down -v         # stop AND delete the database volume (DESTROYS data)
docker compose up --build      # rebuild after a code change and restart
```

> **`down` vs `down -v`:** plain `down` stops containers but keeps the named
> volume `postgres_data`, so your rows survive a restart. Adding `-v` deletes the
> volume — every row is gone and migrations run again from scratch on the next
> boot. Use `-v` when you deliberately want a clean database.

---

## 5. Docker, explained deeply

If Docker is new to you: a **container** is an isolated mini-computer running one
process, built from an **image** (a frozen snapshot of an OS + your code +
dependencies). Compose runs several containers together and lets them talk.

### What the `Dockerfile` does

```dockerfile
FROM python:3.14-slim          # start from a small official Python image

ENV PYTHONDONTWRITEBYTECODE=1 \ # don't litter .pyc files
    PYTHONUNBUFFERED=1          # print logs immediately, don't buffer

WORKDIR /app                   # all following commands run inside /app

COPY requirements.txt .        # copy ONLY requirements first...
RUN pip install ... -r requirements.txt   # ...so this layer is cached
                                          # unless requirements change
COPY . .                       # now copy the rest of the source

EXPOSE 8000                    # document that the app listens on 8000

CMD ["sh", "/app/entrypoint.sh"]  # how the container starts
```

Two ideas worth absorbing:

1. **Layer caching.** Copying `requirements.txt` and installing *before* copying
   the rest of the code means Docker can reuse the (slow) dependency-install
   layer whenever only your application code changes. This makes rebuilds fast.
2. Note `requirements-dev.txt` is **not** installed — the runtime image stays lean
   and has no test tooling in it.

### What `docker-compose.yml` does

It defines three services:

- **`api`** — built from the `Dockerfile`. It publishes port
  `127.0.0.1:${API_PORT}:8000` (host port → container's 8000), passes
  `SQLALCHEMY_DATABASE_URL` in as an environment variable, and `depends_on` the
  `db` being *healthy* before it starts. It has its own health check that calls
  `/health` using Python (the slim image has no `curl`).
- **`db`** — the `pgvector/pgvector:pg16` image (PostgreSQL 16 with the `pgvector`
  extension already available). It stores data on the named volume
  `postgres_data`, and has a health check using `pg_isready`.
- **`adminer`** — a lightweight web GUI for the database, on `${ADMINER_PORT}`.

### Why API and DB are separate services

Separation of concerns. The database is a stateful, long-lived store; the API is
a stateless process you restart often as you change code. Keeping them in
separate containers means you can rebuild and restart the API without disturbing
the database, scale them independently, and swap either one out.

### How service names like `db` work

Compose creates a private network where each service is reachable by its **service
name** as a hostname. So inside the API container, the address `db:5432` resolves
to the database container. That is exactly why the connection string uses `db` as
the host:

```
postgresql://postgres:change-me@db:5432/fastapi
                                  ▲
                          the service name, not "localhost"
```

From your **host machine** (outside Docker), the database is instead at
`localhost:${POSTGRES_PORT}`, because the port is published there. This is the
single most common source of "why can't it connect?" confusion — see the
[mistakes section](#15-common-beginner-mistakes).

### Ports

`"127.0.0.1:${API_PORT}:8000"` means: *publish* the container's internal port
`8000` onto your machine at `127.0.0.1:${API_PORT}`. The `127.0.0.1:` prefix binds
it to localhost only, so it isn't exposed to your whole network. Format is
`host:container`.

### Volumes

```yaml
volumes:
  - postgres_data:/var/lib/postgresql/data
```

PostgreSQL writes its data files to `/var/lib/postgresql/data` *inside* the
container. By mapping that path to the named volume `postgres_data`, the data
lives on your host and **survives** the container being recreated. Without a
volume, every `docker compose down` would erase your database.

### What `docker compose down -v` does

`down` removes the containers and network. The `-v` flag *additionally* removes
the named volumes — i.e. it deletes `postgres_data` and therefore **all your
rows**. On the next `up`, Postgres initializes an empty database and
`entrypoint.sh` runs every migration again from zero. Reach for `-v` only when you
*want* a clean slate.

---

## 6. Startup flow

When you run `docker compose up --build`, here is the timeline, step by step.

```
t0   You run: docker compose up --build
       │
t1   The "db" container starts PostgreSQL.
       │  Compose waits for db's healthcheck (pg_isready) to pass,
       │  because api declares: depends_on db (condition: service_healthy)
       ▼
t2   The "api" container starts and runs its CMD: sh /app/entrypoint.sh
       │
t3   entrypoint.sh step 1 — WAIT FOR POSTGRES
       │   It opens a tiny Python loop that tries "SELECT 1" up to 30 times,
       │   sleeping 1s between attempts, until Postgres answers.
       │   (Belt-and-suspenders even though Compose already waited.)
       ▼
t4   entrypoint.sh step 2 — RUN MIGRATIONS
       │   alembic upgrade head
       │   This creates/updates all tables to the latest schema version.
       ▼
t5   entrypoint.sh step 3 — START THE SERVER
       │   exec uvicorn main:app --app-dir src --host 0.0.0.0 --port 8000
       │   "exec" replaces the shell with uvicorn so signals work cleanly.
       ▼
t6   FastAPI is now serving on port 8000 inside the container,
       published to your machine at localhost:${API_PORT}.
       │
t7   The api healthcheck periodically calls http://localhost:8000/health.
       Once it returns 200, the api service is marked "healthy".
```

The key teaching point: **migrations run automatically at boot.** You do not have
to remember to migrate when using Docker — `entrypoint.sh` does it. (When running
locally *without* Docker, you must run them yourself; see section 10.)

Here is `entrypoint.sh` in essence:

```sh
set -e                          # stop on the first error
# 1. loop SELECT 1 until Postgres is reachable (30 tries)
# 2. alembic upgrade head
# 3. exec uvicorn main:app --app-dir src --host 0.0.0.0 --port 8000
```

---

## 7. FastAPI explanation

FastAPI is the framework that turns Python functions into HTTP endpoints.

### What `src/main.py` does

It is intentionally tiny:

```python
from fastapi import FastAPI
from routers import financenotes, ingest, watchlist

app = FastAPI()

@app.get("/health", tags=["health"])
def health():
    return {"status": "ok"}

app.include_router(watchlist.router)
app.include_router(financenotes.router)
app.include_router(ingest.router)
```

- `app = FastAPI()` creates the application object. This `app` is what uvicorn
  runs (`uvicorn main:app`). It also powers the auto-generated `/docs`.
- `@app.get("/health")` registers a function as the handler for `GET /health`.
  When a request hits that URL, FastAPI calls `health()` and turns its return
  value into a JSON response: `{"status": "ok"}`.
- `app.include_router(...)` plugs in each router. A **router** is a group of
  related endpoints defined in its own file, with a shared URL prefix. This keeps
  `main.py` small and lets each feature live in its own module.

### What `/health` is for

It's a trivial endpoint that returns `200 OK`. Monitoring systems (and the Docker
health check here) call it to ask "are you alive?" without touching the database.
It is the simplest possible endpoint and a good first thing to read.

### What `/docs` is

FastAPI reads your route definitions and Pydantic schemas and **generates
interactive API documentation automatically** at `/docs` (Swagger UI) and `/redoc`
(ReDoc). You did not write that page; it is derived from your code. This is one of
FastAPI's biggest conveniences — the docs can never drift from the code because
they *are* the code.

### How a request reaches a route function

1. uvicorn receives the raw HTTP request.
2. FastAPI matches the request's **method + path** (e.g. `POST /watchlist/`) to
   the registered route function.
3. FastAPI resolves that function's **dependencies** (e.g. a database session, a
   parsed/validated request body) and calls the function with them.
4. The function returns a value; FastAPI serializes it (often via a Pydantic
   `response_model`) into a JSON HTTP response.

That third step — dependencies — is the heart of how the database session and
request validation get injected, which the next two sections explain.

---

## 8. Database explanation

### What PostgreSQL is doing here

PostgreSQL is the actual database: a separate server program that stores your rows
durably on disk and answers SQL queries. In this project it runs in the `db`
container. The API never reads files directly — it asks Postgres for data over a
network connection.

### `src/database.py`, line by line

```python
from config import settings

engine = create_engine(settings.sqlalchemy_database_url)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db() -> Generator[Session, None, None]:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
```

- **`engine`** — the low-level object that knows *how* to connect to the database
  (the URL, the connection pool). There is one engine for the whole app. It does
  not open a connection until something actually needs one.
- **`SessionLocal`** — a *factory* that produces `Session` objects. A **session**
  is your workspace for one unit of work: you add/query/update objects through it,
  and it batches those into SQL. `autocommit=False` means changes aren't saved
  until you explicitly `commit()`; `autoflush=False` means it won't auto-send
  pending changes before queries unless you ask.
- **`Base`** — the declarative base class. Every model in `models.py` inherits
  from it. `Base.metadata` collects all the table definitions, which Alembic uses.
- **`get_db`** — a FastAPI **dependency** that provides a session to a request and
  guarantees it gets closed.

### What `yield db` means and why the session closes

`get_db` is a generator. FastAPI's dependency system treats it specially:

1. When a request needs a session, FastAPI runs `get_db` up to the `yield` and
   hands the `db` object to your route function.
2. Your route function runs, using that one session.
3. After the response is produced, FastAPI resumes `get_db` *past* the `yield`,
   so the `finally: db.close()` runs and the connection returns to the pool.

This **one-session-per-request** pattern is important: each request gets a fresh,
isolated session, and you never leak connections, even if the route raises an
error (because `close()` is in a `finally`).

### How route functions use the session

In `deps.py` the session is packaged as a typing alias so routes can request it
cleanly:

```python
db_dependency = Annotated[Session, Depends(get_db)]
```

A route then just writes `db: db_dependency` in its signature and FastAPI injects
a live session. For example, creating a watchlist item:

```python
watchlist_item = WatchlistItem(**watchlist_item_request.model_dump())
db.add(watchlist_item)     # stage the new object in the session
db.commit()                # write it to PostgreSQL
db.refresh(watchlist_item) # reload it (so DB-filled fields like created_at appear)
return watchlist_item
```

`deps.py` also gives you a helper that captures a pattern you'd otherwise repeat
in every "get one" and "update" and "delete" route:

```python
def get_or_404(db, model, item_id, detail="Not found"):
    obj = db.get(model, item_id)       # primary-key lookup
    if obj is None:
        raise HTTPException(status_code=404, detail=detail)
    return obj
```

---

## 9. Models vs. schemas

This is the single most important concept for understanding this codebase, and a
classic point of confusion. There are **two different kinds of classes** that look
similar but do different jobs.

### SQLAlchemy models = database tables

`src/models.py` defines what the **database tables** look like. Each class is a
table; each `Column` is a column.

```python
class WatchlistItem(Base):
    __tablename__ = "watchlist"
    id = Column(Integer, primary_key=True, index=True)
    ticker = Column(String, unique=True, index=True, nullable=False)
    company_name = Column(String, nullable=True)
    notes = Column(Text, nullable=True)
    created_at = Column(DateTime(timezone=True), nullable=False,
                        server_default=func.now())
```

Notice details that encode real rules:

- `ticker` is `unique=True` — the database itself refuses two rows with the same
  ticker. (That's what lets the route translate a clash into HTTP 409.)
- `created_at` uses `server_default=func.now()` — **the database** fills in the
  timestamp, so it's correct even for inserts that don't come through Python.

The `FinanceNote` model adds `tags` (a `JSON` column defaulting to an empty list),
`source_url`, and `external_id` (`unique`, nullable) — the last enabling
idempotent ingestion.

### Pydantic schemas = request/response shapes

`src/schemas.py` defines what the **JSON going in and out** looks like, and
validates it. These are *not* database tables; they never touch SQL. They describe
the API's contract and clean the data.

```python
class WatchlistItemBase(BaseModel):
    ticker: str
    company_name: str | None = None
    notes: str | None = None

    @field_validator("ticker")
    @classmethod
    def clean_ticker(cls, value: str) -> str:
        ticker = value.strip().upper()      # "  aapl " -> "AAPL"
        if not ticker:
            raise ValueError("ticker is required")
        return ticker
```

The schemas come in deliberate variants:

- **`...Base`** — the shared fields and validators.
- **`...Create`** — what a client must send to create something.
- **`...Read`** — what the API sends back (adds DB-generated fields like `id` and
  `created_at`). It sets `model_config = ConfigDict(from_attributes=True)`, which
  lets Pydantic build the response *directly from a SQLAlchemy model object*.
- **`...Ingest`** — like Create but with the optional `external_id` for the bulk
  endpoint.

The `FinanceNote` schemas also show off real-world input cleaning: tags can be
sent as a list *or* a comma-separated string and are normalized to a clean list;
`source_url` must start with `http://` or `https://` or it's rejected.

### Why both are needed

- The **model** is about *storage*: types, constraints, indexes, what the table
  looks like on disk.
- The **schema** is about the *contract and validation*: what callers may send,
  what gets returned, and how messy input is cleaned before it ever reaches the
  database.

Separating them means you can change the API's shape without changing the table,
and vice versa, and you never accidentally expose internal columns or accept
unvalidated junk.

### Following one request all the way through

Let's trace `POST /watchlist/` with body `{"ticker": "aapl", "company_name":
"Apple"}` — from JSON to a row and back.

```
1. HTTP arrives:  POST /watchlist/  body = {"ticker":"aapl","company_name":"Apple"}

2. FastAPI sees the route wants a `schemas.WatchlistItemCreate` body, so it
   parses the JSON into that Pydantic schema. The validator runs:
        "aapl" -> strip + upper -> "AAPL"
   The schema object is now: WatchlistItemCreate(ticker="AAPL",
                                                 company_name="Apple", notes=None)

3. The route function runs (src/routers/watchlist.py):
        watchlist_item = WatchlistItem(**request.model_dump())
   -> a SQLAlchemy model:  WatchlistItem(ticker="AAPL", company_name="Apple")
        db.add(watchlist_item)
        db.commit()           -> SQLAlchemy emits:
                                 INSERT INTO watchlist (ticker, company_name, ...)
                                 VALUES ('AAPL', 'Apple', ...)
                                 Postgres fills created_at via server_default now()
        db.refresh(watchlist_item)   -> reloads id and created_at from the row

4. The route returns the model object. The route declared
   response_model=schemas.WatchlistItemRead, and that schema has
   from_attributes=True, so Pydantic reads the model's attributes and builds:
        {"ticker":"AAPL","company_name":"Apple","notes":null,
         "id":1,"created_at":"2026-06-22T..."}

5. FastAPI sends that JSON back with status 201.
```

If you sent a duplicate `AAPL`, step 3's `commit()` would raise `IntegrityError`
(the unique constraint), the route catches it, rolls back, and raises
`HTTPException(409, "Ticker already exists in watchlist")`.

---

## 10. Alembic migrations

### What migrations are, and why models alone aren't enough

Editing `models.py` changes your **Python description** of a table. It does **not**
change the actual PostgreSQL database — the real `watchlist` table on disk has no
idea you added a column. Something has to issue the `ALTER TABLE` / `CREATE TABLE`
SQL against the live database. That something is **Alembic**, and each change is
recorded as a **migration**: a small, ordered, version-controlled script.

> Mental model: `models.py` is the *blueprint*; migrations are the *construction
> work* that actually builds and remodels the database to match.

### The core commands

- **`alembic upgrade head`** — apply every migration that hasn't run yet, bringing
  the database up to the latest version (`head`). This is what `entrypoint.sh`
  runs on boot and what `make migrate` runs locally.
- **`alembic revision --autogenerate -m "message"`** — look at the difference
  between your models and the current database, and **generate a new migration
  file** capturing it. This is what `make revision m="message"` runs. Always read
  the generated file before trusting it — autogenerate is good but not perfect.
- **`alembic downgrade -1`** — undo the most recent migration (rarely needed in
  development; useful to understand that migrations are reversible).

### `upgrade()` and `downgrade()`

Each migration file has two functions:

- **`upgrade()`** — the changes to apply when moving the schema *forward*.
- **`downgrade()`** — how to *reverse* those changes.

They should be mirror images. For example, the initial migration's `upgrade()`
calls `op.create_table("watchlist", ...)` and its `downgrade()` calls
`op.drop_table("watchlist")`.

### The `alembic_version` table

How does Alembic know which migrations already ran? It keeps a tiny table in your
database called **`alembic_version`** with a single row holding the current
revision id. `upgrade head` compares that id to the chain of migration files and
runs only the missing ones, then updates the row. (You can see this table in
Adminer.)

### How `alembic/env.py` sees your models

```python
import models
...
target_metadata = models.Base.metadata
```

By importing `models` and pointing `target_metadata` at `Base.metadata`, Alembic
knows the full set of tables your code expects, which is what `--autogenerate`
diffs against the live database. The database URL is read from the environment so
the same config works in Docker and locally:

```python
database_url = os.getenv("SQLALCHEMY_DATABASE_URL") or config.get_main_option("sqlalchemy.url")
```

This is why `alembic.ini`'s `sqlalchemy.url` is intentionally blank — the real
value comes from `SQLALCHEMY_DATABASE_URL`.

### This repo's actual migration chain

The migrations form an ordered chain, each pointing back to the previous one via
`down_revision`. Reading them in order is a great mini-history of the schema:

```
b79c8f92502b  create initial tables
                 └ creates "watchlist" and "finance_notes" with their indexes
                        │ down_revision = None  (this is the first migration)
                        ▼
2f4d8c6a9b10  add finance note ingest fields
                 └ adds finance_notes.tags (JSON) and finance_notes.source_url
                        ▼
c3e7f1a2b4d6  enable pgvector extension
                 └ op.execute("CREATE EXTENSION IF NOT EXISTS vector;")
                        ▼
d4a1f0b2c3e5  make created_at timezone-aware, non-null, db-defaulted
                 └ backfills NULLs, then alters both tables' created_at to
                   DateTime(timezone=True) NOT NULL DEFAULT now()
                        ▼
e5b2a1c4d6f7  add external_id and indexes   ◄── current head
                 └ adds finance_notes.external_id (unique) + index on created_at
```

A few teaching points hidden in these files:

- The **`d4a1f0b2c3e5`** migration shows real-world care: before adding a
  `NOT NULL` constraint it runs `UPDATE ... SET created_at = now() WHERE created_at
  IS NULL` to backfill existing rows, and uses
  `postgresql_using="created_at AT TIME ZONE 'UTC'"` to reinterpret old naive
  timestamps as UTC. You can't just slap `NOT NULL` on a column that already has
  nulls.
- The **`c3e7f1a2b4d6`** migration is how `pgvector` is "enabled": it runs
  `CREATE EXTENSION IF NOT EXISTS vector`. That makes the `vector` type *available*
  in Postgres — but note **no table here actually uses a vector column yet**. The
  capability is provisioned ahead of the feature.
- The **`2f4d8c6a9b10`** migration adds `tags` with a temporary
  `server_default='[]'` so existing rows get a valid value, then immediately drops
  the default with `op.alter_column(..., server_default=None)` so the application
  controls it going forward. That's a standard "add a non-null column to an
  existing table" trick.

---

## 11. API endpoints

Below is every endpoint currently implemented. All examples assume the server is
at `http://localhost:8000`.

> Note on the `tag` filter: filtering notes by tag uses a PostgreSQL-specific
> JSONB operator, so it works against the real Postgres database but is **not**
> exercised by the SQLite-based tests.

### `GET /health` — liveness check
- **File:** `src/main.py` · **Table touched:** none
- Returns `{"status": "ok"}`.

```bash
curl http://localhost:8000/health
```

### Watchlist — `src/routers/watchlist.py` (table: `watchlist`)

**`GET /watchlist/`** — list items, newest first, paginated.
- Query params: `limit` (1–200, default 50), `offset` (≥0, default 0).
```bash
curl "http://localhost:8000/watchlist/?limit=10&offset=0"
```

**`GET /watchlist/{id}`** — fetch one item by id (404 if missing).
```bash
curl http://localhost:8000/watchlist/1
```

**`POST /watchlist/`** — create an item. Returns `201`. Duplicate ticker → `409`.
- Body:
```json
{ "ticker": "aapl", "company_name": "Apple", "notes": "core holding" }
```
- Response (`201`):
```json
{ "ticker": "AAPL", "company_name": "Apple", "notes": "core holding",
  "id": 1, "created_at": "2026-06-22T12:00:00+00:00" }
```
```bash
curl -X POST http://localhost:8000/watchlist/ \
  -H "Content-Type: application/json" \
  -d '{"ticker":"aapl","company_name":"Apple"}'
```

**`PUT /watchlist/{id}`** — replace an item's fields (404 if missing, 409 on
ticker clash).
```bash
curl -X PUT http://localhost:8000/watchlist/1 \
  -H "Content-Type: application/json" \
  -d '{"ticker":"AAPL","notes":"trim position"}'
```

**`DELETE /watchlist/{id}`** — delete an item (404 if missing).
```bash
curl -X DELETE http://localhost:8000/watchlist/1
# -> {"message":"Watchlist item deleted successfully"}
```

### Finance notes — `src/routers/financenotes.py` (table: `finance_notes`)

**`GET /financenotes/`** — list notes, newest first, paginated, with optional
filters:
- `ticker` — exact match (input is upper-cased).
- `q` — case-insensitive search across `title` and `content`.
- `tag` — match notes containing this tag (**Postgres-only**).
- `limit` / `offset` — pagination.
```bash
curl "http://localhost:8000/financenotes/?ticker=aapl&q=earnings&limit=20"
```

**`GET /financenotes/{id}`** — fetch one note by id (404 if missing).

**`POST /financenotes/`** — create a note. Returns `201`.
- Body:
```json
{ "ticker": "AAPL", "title": "Q3 earnings beat",
  "content": "Revenue up on iPhone + Services.",
  "tags": ["earnings", "bullish"],
  "source_url": "https://example.com/report" }
```
```bash
curl -X POST http://localhost:8000/financenotes/ \
  -H "Content-Type: application/json" \
  -d '{"ticker":"AAPL","title":"Q3 earnings beat","content":"Revenue up."}'
```

**`PUT /financenotes/{id}`** — replace a note's fields (404 if missing).

**`DELETE /financenotes/{id}`** — delete a note (404 if missing).

### Ingest — `src/routers/ingest.py` (table: `finance_notes`)

**`POST /ingest/finance-notes`** — bulk-create notes idempotently. Returns `200`
with a summary. Covered in detail in the next section.
```bash
curl -X POST http://localhost:8000/ingest/finance-notes \
  -H "Content-Type: application/json" \
  -d '[{"ticker":"AAPL","title":"n1","content":"c1","external_id":"src-1"},
       {"ticker":"MSFT","title":"n2","content":"c2","external_id":"src-2"}]'
# -> {"created":2,"skipped":0,"items":[ ... ]}
```

---

## 12. The ingest endpoint

### What it currently does

`POST /ingest/finance-notes` takes a **list** of notes (not a single one) and
inserts them, returning a summary: how many were `created`, how many `skipped`,
and the created `items`.

Its defining feature is **idempotency via `external_id`**. Here is the logic:

```python
for note in notes:
    if note.external_id:
        already_exists = db.query(FinanceNote).filter(
            FinanceNote.external_id == note.external_id).first()
        if already_exists:
            skipped += 1
            continue

    finance_note = FinanceNote(**note.model_dump())
    db.add(finance_note)
    try:
        db.commit()
    except IntegrityError:   # e.g. a concurrent insert of the same external_id
        db.rollback()
        skipped += 1
        continue
    db.refresh(finance_note)
    created.append(finance_note)
```

Two robustness choices to learn from:

1. **One commit per note**, not one big commit for the whole batch. If a single
   note fails, the others still go through — the batch isn't all-or-nothing.
2. **Defense in depth on uniqueness.** It checks for an existing `external_id`
   first, *and* catches the database's `IntegrityError` in case two requests race
   to insert the same id at the same moment. The unique index on `external_id`
   (from migration `e5b2a1c4d6f7`) is the ultimate guarantee.

### Why it exists

A normal `POST /financenotes/` is for a human creating one note through a UI. The
ingest endpoint is for **bulk, repeatable, machine-driven** loading where the
caller may send the same data more than once (retries, scheduled re-runs,
overlapping batches). The `external_id` is the sender's own stable identifier for
each note; using it as a dedup key means re-sending a batch is safe and produces
no duplicates.

### How an agent could use it later

Imagine an automated agent (the roadmap nicknames this "OpenClaw") that scrapes or
generates finance notes. Each note it produces would carry a deterministic
`external_id` (say, a hash of the source article URL). The agent can then POST its
whole batch to `/ingest/finance-notes` on a schedule without tracking what it
already sent — the backend skips anything it's seen. This decouples the producer
(the agent) from the bookkeeping (the database).

### Normal CRUD vs. machine/agent ingest

| | User CRUD (`POST /financenotes/`) | Machine ingest (`POST /ingest/finance-notes`) |
|---|---|---|
| Input | one note | a list of notes |
| Caller | a human via UI/docs | a script or agent |
| Re-sending | creates a duplicate | skipped (idempotent) |
| Dedup key | none | `external_id` |
| Response | the created note | a `{created, skipped, items}` summary |

---

## 13. Testing explanation

### What pytest is

`pytest` is the test runner. It discovers functions named `test_*`, runs them, and
reports pass/fail. The configuration in `pytest.ini` tells it where the tests are
(`testpaths = tests`) and puts `src/` on the import path (`pythonpath = src`) so a
test can simply `from main import app`.

### How the tests talk to FastAPI (without a real database)

The clever part is in `tests/conftest.py`. It defines a `client` fixture that:

1. Spins up an **in-memory SQLite** database (`create_engine("sqlite://", ...)`)
   that lives only for that one test.
2. Creates all the tables from the models with `Base.metadata.create_all(...)`.
3. **Overrides** the real `get_db` dependency with one that uses this SQLite
   session: `app.dependency_overrides[get_db] = override_get_db`.
4. Wraps the app in FastAPI's `TestClient`, which lets tests make requests like
   `client.get("/health")` *in-process*, with no network and no server running.

This is a beautiful illustration of why dependency injection is useful: because the
database session is injected via `get_db`, the test can swap in a throwaway
database without changing a line of application code.

> Caveat worth understanding: SQLite is *not* Postgres. Features that rely on
> Postgres-specific behavior — the JSONB `tag` filter, certain `created_at`
> server-default nuances — aren't truly exercised by these tests. The tests
> create tables straight from the models with `create_all`, so they also don't
> run the Alembic migrations.

### What the current tests check

In `tests/test_api.py`:

- **`test_health`** — `/health` returns `200` and `{"status": "ok"}`.
- **`test_watchlist_crud`** — the full lifecycle: create (and that `"aapl"` is
  normalized to `"AAPL"`), duplicate → `409`, list, get-by-id, `404` for a missing
  id, update, delete, then `404` again.
- **`test_finance_notes_filter_and_pagination`** — creates three notes, then
  checks filtering by ticker, the `q` text search, and the `limit` pagination.
- **`test_ingest_bulk_and_dedup`** — posts a batch (expects `created=2`), then
  posts the *same* batch again and expects `created=0, skipped=2` — proving
  idempotency.

### How to run them

```bash
make test                              # run everything
pytest                                 # same thing
pytest tests/test_api.py::test_watchlist_crud   # run a single test
pytest -v                              # verbose, show each test name
```

### What a passing test means

It means the endpoints behaved correctly against the in-memory SQLite database for
the scenarios written. It does **not** prove the Postgres-only paths work, nor that
your migrations are correct — those need a real Postgres to verify.

### What tests to add next

- A test for the **`tag` filter** running against a real Postgres (e.g. via a
  test container), since SQLite can't cover it.
- Validation tests: a missing `ticker` → `422`, a bad `source_url` → `422`.
- An ingest test mixing notes **with and without** `external_id` in one batch.
- A test that runs the **Alembic migrations** against a fresh database and asserts
  the resulting schema, so migrations themselves are covered.

---

## 14. Makefile and the dev workflow

The `Makefile` is just a set of named shortcuts. Run `make <target>`:

| Command | What it runs | Use it to… |
|---------|--------------|-----------|
| `make install` | `pip install -r requirements-dev.txt` | install runtime + dev deps locally |
| `make dev` | `uvicorn main:app --app-dir src --reload` | run the API locally with auto-reload |
| `make up` | `docker compose up --build` | build & start the whole Docker stack |
| `make down` | `docker compose down` | stop the stack (keep data) |
| `make logs` | `docker compose logs -f api` | follow the API container's logs |
| `make migrate` | `alembic upgrade head` | apply migrations locally |
| `make revision m="..."` | `alembic revision --autogenerate -m "..."` | generate a new migration |
| `make fmt` | `black src alembic tests` | auto-format the code |
| `make test` | `pytest` | run the test suite |

> `make dev` runs uvicorn **on your host**, not in Docker. For it to reach a
> database, you need a Postgres it can connect to and a matching
> `SQLALCHEMY_DATABASE_URL` (with host `localhost`, not `db`). Many people simply
> use `make up` for everything and reserve `make dev` for when they want
> host-side autoreload against a separately-running database.

### A normal development loop

```
1. Change application code (a router, a schema, etc.).
       │
2. Did you change a MODEL (models.py)?
       ├─ no  → skip to step 3
       └─ yes → generate a migration:
                  make revision m="describe the change"
                then READ the generated file in alembic/versions/
       │
3. Run it:
       make up           # Docker rebuilds, entrypoint applies migrations, serves
       │                 # (or: make migrate && make dev for host-side)
4. Try the endpoint:
       open http://localhost:8000/docs   and click Execute
       (or use curl; or inspect rows in Adminer at :8080)
       │
5. Run the tests:
       make test
       │
6. Format and commit:
       make fmt
       git add -A && git commit -m "..."
```

The one rule beginners forget: **a model change is not done until there's a
migration for it.** Code and database must move together.

---

## 15. Common beginner mistakes

These are the specific traps this stack sets, and how to avoid them.

- **Forgetting to copy `.env.example` to `.env`.** Compose can't substitute
  `${API_PORT}`/`${POSTGRES_PASSWORD}` and the stack won't start (or starts with
  blank values). Always `cp .env.example .env` first.

- **Confusing `localhost` and `db` as the database host.** Inside Docker the
  database is at `db:5432`; from your host machine it's at
  `localhost:${POSTGRES_PORT}`. Using `localhost` in the container's
  `SQLALCHEMY_DATABASE_URL` makes the API try to connect to *itself* and fail.

- **Forgetting migrations.** If you skip `alembic upgrade head` (when running
  locally without Docker), the tables won't exist and every query errors. In
  Docker this is automatic; locally it's on you.

- **Deleting the volume and losing data.** `docker compose down -v` erases
  `postgres_data`. Use plain `down` unless you *want* a clean database.

- **Port already in use.** If `5432`, `8000`, or `8080` is taken (e.g. a local
  Postgres already on `5432`), the stack fails to bind. Change the offending
  `*_PORT` in `.env`.

- **Docker running old code.** If your change doesn't seem to take effect, you
  probably started without rebuilding. Use `docker compose up --build` so the
  image is rebuilt with your latest code.

- **Committing `.env`.** It holds secrets and is gitignored on purpose. Never
  force-add it. Only `.env.example` (with placeholder values) belongs in Git.

- **Changing a model but not creating a migration.** Editing `models.py` does
  nothing to the live database. You must `make revision m="..."` and apply it. The
  app and the database will silently disagree until you do.

- **Expecting SQLAlchemy models to auto-update tables.** SQLAlchemy does *not*
  alter your existing tables to match the models. That's Alembic's job. (The only
  place tables are auto-created from models is the **tests**, via `create_all` on a
  throwaway SQLite DB — not in production.)

- **"It works in `/docs` but the table doesn't exist."** Usually means migrations
  didn't run against the database you're actually hitting. Check the API logs for
  the `alembic upgrade head` step and confirm `SQLALCHEMY_DATABASE_URL` points
  where you think.

- **Import-path confusion from `--app-dir src`.** Because the app runs with
  `--app-dir src`, imports inside `src/` are flat: `from models import ...`, not
  `from src.models import ...`. If you write `from src....` it will break. New
  modules must follow the flat convention, and tests rely on `pythonpath = src` in
  `pytest.ini` for the same reason.

---

## 16. How to read this repo as a learner

A suggested order, with a question to ask yourself at each stop. Reading code with
a question in mind is far more effective than reading top to bottom.

1. **`src/main.py`** — *How does the app get assembled, and what are its pieces?*
   See that it's just `FastAPI()` + a health route + three routers.

2. **`src/routers/watchlist.py`** — *What does one full set of CRUD endpoints look
   like?* This is the simplest, most complete router. Notice the dependencies in
   the function signatures and the `IntegrityError → 409` pattern.

3. **`src/schemas.py`** — *What is the API allowed to receive and return, and how
   is input cleaned?* Watch the `Base`/`Create`/`Read` split and the validators.

4. **`src/models.py`** — *What do the tables actually look like, and what
   constraints does the database enforce?* Compare these columns to the schema
   fields and notice what's different (e.g. `id`, `created_at`).

5. **`src/database.py` + `src/deps.py`** — *Where does the database session come
   from, and how does each request get one safely?* Understand `get_db`'s
   `yield`/`close` and the `get_or_404` helper.

6. **`alembic/versions/*.py` (in chain order)** — *How did the schema get built up
   over time, and how do code changes reach the real database?* Read them oldest to
   newest; they're a narrated history.

7. **`Dockerfile`, `docker-compose.yml`, `entrypoint.sh`** — *How does the whole
   thing start, and how do the services find each other?* Trace the startup
   timeline from section 6.

8. **`tests/conftest.py` + `tests/test_api.py`** — *How is the app tested without a
   real database, and what behavior is guaranteed?* Notice the dependency override.

Then come back to `src/routers/financenotes.py` and `src/routers/ingest.py`, which
will now read easily because you understand every building block they use.

---

## 17. What this repo teaches

By understanding this one small codebase, you've met most of the core ideas of
backend engineering:

- **HTTP APIs** — turning URLs + methods into functions (FastAPI routers).
- **CRUD** — the create/read/update/delete lifecycle of a resource.
- **Validation** — cleaning and rejecting input at the boundary (Pydantic).
- **Database sessions** — one unit of work per request, opened and closed safely.
- **The model/schema split** — separating storage from the API contract.
- **Migrations** — evolving a database's structure safely and reproducibly.
- **Dockerized development** — running an app and its dependencies as a stack.
- **Environment variables & secrets hygiene** — configuration via `.env`, never
  committing secrets.
- **Health checks** — exposing a simple endpoint so infrastructure can monitor the
  app.
- **Idempotency** — designing an endpoint that's safe to call repeatedly.
- **Testing** — verifying behavior fast, in-process, with dependency overrides.
- **Project organization** — config, models, schemas, routers, deps, migrations,
  and tests each in their own clear place.

---

## 18. What is intentionally not included yet

Being honest about the boundaries is part of the lesson.

- **No authentication or authorization.** There is no login, no JWT, no API keys.
  Every endpoint is open. (`bcrypt`, `passlib`, and `python-jose` are present in
  `requirements.txt` as groundwork, but nothing uses them yet.)
- **No frontend.** There's no web/mobile UI — only the JSON API and the
  auto-generated `/docs` page.
- **No production deployment setup.** The Docker stack is for *development*. There's
  no HTTPS, no reverse proxy, no production process manager, no cloud config.
- **No Kubernetes / orchestration.** Single-host Docker Compose only.
- **No microservices.** It's one small service plus a database.
- **No advanced security** beyond repo hygiene (gitignored secrets, localhost-bound
  ports). No rate limiting, no input throttling, no audit logging.
- **No real external finance data.** Nothing fetches live prices or news; you put
  the data in yourself.
- **No semantic search yet.** The `pgvector` extension is enabled, but there is no
  embedding column on any table and no vector-search endpoint. The capability is
  staged, not built.

---

## 19. Future roadmap

Practical next steps, roughly in order of how naturally they follow from what's
here:

- **Richer note querying** — more filters, multi-tag matching, date ranges,
  combined search. (Basic ticker/tag/`q` filtering and pagination already exist.)
- **Better tagging** — a controlled vocabulary or a separate tags table instead of
  a free-form JSON list.
- **Agent / "OpenClaw" ingestion** — build the automated producer that posts
  batches to `/ingest/finance-notes` using deterministic `external_id`s. The
  endpoint is ready for it.
- **Attachments** — let notes carry screenshots or images (charts, filings).
- **Export** — render notes to Markdown or PDF for sharing.
- **External finance data** — integrate a real prices/news API to enrich notes.
- **pgvector semantic search** — add an embedding column to `finance_notes`, store
  vector embeddings of note content, and add a "find similar / search by meaning"
  endpoint. The extension is already enabled, so this is the natural payoff.
- **Authentication** — wire up the already-present `passlib`/`bcrypt`/`python-jose`
  into real login and protected routes.
- **More tests** — Postgres-backed tests for the JSONB tag filter, validation-error
  tests, and tests that run the migrations against a real database.

---

## 20. Quick command reference

```bash
# --- Setup ---
cp .env.example .env            # create your local env file, then edit secrets

# --- Run with Docker (recommended) ---
make up                         # = docker compose up --build  (build + start all)
make down                       # = docker compose down        (stop, keep data)
docker compose down -v          # stop AND delete the DB volume (DESTROYS data)
make logs                       # = docker compose logs -f api  (follow API logs)

# --- Health & docs ---
curl http://localhost:8000/health      # liveness check
# http://localhost:8000/docs           # interactive API docs (Swagger UI)
# http://localhost:8080                # Adminer DB GUI (server: db)

# --- Run locally (host uvicorn, needs a reachable Postgres) ---
make install                    # install runtime + dev dependencies
make migrate                    # apply migrations (alembic upgrade head)
make dev                        # run API with autoreload

# --- Migrations ---
make migrate                    # apply all pending migrations
make revision m="add foo"       # autogenerate a new migration (then READ it)

# --- Tests & formatting ---
make test                       # run the full test suite
pytest tests/test_api.py::test_watchlist_crud   # run a single test
make fmt                        # format with black
```

---

*Happy learning. The best way to internalize this is to run the stack, open
`/docs`, create a watchlist item, and then watch the row appear in Adminer — then
read the four files that made that happen: `main.py` → `watchlist.py` →
`schemas.py` → `models.py`.*
