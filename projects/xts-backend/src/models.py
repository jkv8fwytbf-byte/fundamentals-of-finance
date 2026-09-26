from sqlalchemy import JSON, Column, DateTime, Integer, String, Text, func

from database import Base


class WatchlistItem(Base):
    __tablename__ = "watchlist"

    id = Column(Integer, primary_key=True, index=True)
    ticker = Column(String, unique=True, index=True, nullable=False)
    company_name = Column(String, nullable=True)
    notes = Column(Text, nullable=True)
    # timezone-aware, filled in by the database (server_default) so the value is
    # correct even for inserts that don't go through the ORM.
    created_at = Column(
        DateTime(timezone=True), nullable=False, server_default=func.now()
    )


class FinanceNote(Base):
    __tablename__ = "finance_notes"

    id = Column(Integer, primary_key=True, index=True)
    ticker = Column(String, index=True, nullable=False)
    title = Column(String, nullable=False)
    content = Column(Text, nullable=False)
    tags = Column(JSON, default=list, nullable=False)
    source_url = Column(String, nullable=True)
    # Stable id supplied by an external source/agent; lets ingestion be
    # idempotent (re-sending the same external_id is skipped).
    external_id = Column(String(255), unique=True, index=True, nullable=True)
    created_at = Column(
        DateTime(timezone=True), index=True, nullable=False, server_default=func.now()
    )
