"""enable pgvector extension

Revision ID: c3e7f1a2b4d6
Revises: 2f4d8c6a9b10
Create Date: 2026-06-16

"""

from alembic import op

revision = "c3e7f1a2b4d6"
down_revision = "2f4d8c6a9b10"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.execute("CREATE EXTENSION IF NOT EXISTS vector;")


def downgrade() -> None:
    op.execute("DROP EXTENSION IF EXISTS vector;")
