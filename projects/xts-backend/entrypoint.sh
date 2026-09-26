#!/bin/sh
# Startup sequence for the API container:
#   1. wait until Postgres is reachable
#   2. apply Alembic migrations
#   3. hand off to uvicorn
set -e

echo "Waiting for Postgres to be reachable..."
python - <<'PY'
import os
import time

from sqlalchemy import create_engine, text

engine = create_engine(os.environ["SQLALCHEMY_DATABASE_URL"])
for attempt in range(1, 31):
    try:
        with engine.connect() as conn:
            conn.execute(text("SELECT 1"))
        print("Postgres is reachable.")
        break
    except Exception as exc:
        print(f"  attempt {attempt}/30: not ready ({exc.__class__.__name__}), retrying in 1s")
        time.sleep(1)
else:
    raise SystemExit("Postgres did not become reachable in time")
PY

echo "Running database migrations..."
alembic upgrade head

echo "Starting API..."
exec uvicorn main:app --app-dir src --host 0.0.0.0 --port 8000
