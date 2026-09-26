"""create initial tables

Revision ID: b79c8f92502b
Revises:
Create Date: 2026-06-15

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

revision: str = "b79c8f92502b"
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "watchlist",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("ticker", sa.String(), nullable=False),
        sa.Column("company_name", sa.String(), nullable=True),
        sa.Column("notes", sa.Text(), nullable=True),
        sa.Column("created_at", sa.DateTime(), nullable=True),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(op.f("ix_watchlist_id"), "watchlist", ["id"], unique=False)
    op.create_index(op.f("ix_watchlist_ticker"), "watchlist", ["ticker"], unique=True)

    op.create_table(
        "finance_notes",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("ticker", sa.String(), nullable=False),
        sa.Column("title", sa.String(), nullable=False),
        sa.Column("content", sa.Text(), nullable=False),
        sa.Column("created_at", sa.DateTime(), nullable=True),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(op.f("ix_finance_notes_id"), "finance_notes", ["id"], unique=False)
    op.create_index(
        op.f("ix_finance_notes_ticker"), "finance_notes", ["ticker"], unique=False
    )


def downgrade() -> None:
    op.drop_index(op.f("ix_finance_notes_ticker"), table_name="finance_notes")
    op.drop_index(op.f("ix_finance_notes_id"), table_name="finance_notes")
    op.drop_table("finance_notes")

    op.drop_index(op.f("ix_watchlist_ticker"), table_name="watchlist")
    op.drop_index(op.f("ix_watchlist_id"), table_name="watchlist")
    op.drop_table("watchlist")
