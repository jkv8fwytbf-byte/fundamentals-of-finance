"""add external_id and indexes to finance_notes

Adds an optional, unique external_id used for idempotent ingestion, plus an
index on created_at to support newest-first listing.

Revision ID: e5b2a1c4d6f7
Revises: d4a1f0b2c3e5
Create Date: 2026-06-22

"""

import sqlalchemy as sa

from alembic import op

revision = "e5b2a1c4d6f7"
down_revision = "d4a1f0b2c3e5"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column(
        "finance_notes",
        sa.Column("external_id", sa.String(length=255), nullable=True),
    )
    # Unique index; Postgres allows many NULLs, so notes without an external_id
    # are unaffected.
    op.create_index(
        "ix_finance_notes_external_id",
        "finance_notes",
        ["external_id"],
        unique=True,
    )
    op.create_index(
        "ix_finance_notes_created_at",
        "finance_notes",
        ["created_at"],
    )


def downgrade() -> None:
    op.drop_index("ix_finance_notes_created_at", table_name="finance_notes")
    op.drop_index("ix_finance_notes_external_id", table_name="finance_notes")
    op.drop_column("finance_notes", "external_id")
