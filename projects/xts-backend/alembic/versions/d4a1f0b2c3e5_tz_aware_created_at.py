"""make created_at timezone-aware, non-null, db-defaulted

Changes both tables' created_at columns:
  - type DateTime -> DateTime(timezone=True), interpreting existing naive
    values as UTC (the app always wrote UTC)
  - NOT NULL with a server_default of now(), so the database fills it in

Revision ID: d4a1f0b2c3e5
Revises: c3e7f1a2b4d6
Create Date: 2026-06-22

"""

import sqlalchemy as sa

from alembic import op

revision = "d4a1f0b2c3e5"
down_revision = "c3e7f1a2b4d6"
branch_labels = None
depends_on = None

TABLES = ("watchlist", "finance_notes")


def upgrade() -> None:
    for table in TABLES:
        # Backfill any NULLs so the NOT NULL constraint can be applied.
        op.execute(f"UPDATE {table} SET created_at = now() WHERE created_at IS NULL")
        op.alter_column(
            table,
            "created_at",
            existing_type=sa.DateTime(),
            type_=sa.DateTime(timezone=True),
            existing_nullable=True,
            nullable=False,
            server_default=sa.text("now()"),
            postgresql_using="created_at AT TIME ZONE 'UTC'",
        )


def downgrade() -> None:
    for table in TABLES:
        op.alter_column(
            table,
            "created_at",
            existing_type=sa.DateTime(timezone=True),
            type_=sa.DateTime(),
            existing_nullable=False,
            nullable=True,
            server_default=None,
        )
