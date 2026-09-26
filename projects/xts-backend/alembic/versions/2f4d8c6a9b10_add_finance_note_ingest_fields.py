"""add finance note ingest fields

Revision ID: 2f4d8c6a9b10
Revises: b79c8f92502b
Create Date: 2026-06-15 00:00:00.000000

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision: str = "2f4d8c6a9b10"
down_revision: Union[str, Sequence[str], None] = "b79c8f92502b"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.add_column(
        "finance_notes",
        sa.Column(
            "tags",
            sa.JSON(),
            nullable=False,
            server_default=sa.text("'[]'::json"),
        ),
    )
    op.add_column("finance_notes", sa.Column("source_url", sa.String(), nullable=True))
    op.alter_column("finance_notes", "tags", server_default=None)


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_column("finance_notes", "source_url")
    op.drop_column("finance_notes", "tags")
