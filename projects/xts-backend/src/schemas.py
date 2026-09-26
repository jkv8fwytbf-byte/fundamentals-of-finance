from datetime import datetime

from pydantic import BaseModel, ConfigDict, Field, field_validator


class WatchlistItemBase(BaseModel):
    ticker: str
    company_name: str | None = None
    notes: str | None = None

    @field_validator("ticker")
    @classmethod
    def clean_ticker(cls, value: str) -> str:
        ticker = value.strip().upper()
        if not ticker:
            raise ValueError("ticker is required")
        return ticker

    @field_validator("company_name", "notes", mode="before")
    @classmethod
    def clean_optional_text(cls, value: str | None) -> str | None:
        if value is None:
            return None

        text = value.strip()
        return text or None


class WatchlistItemCreate(WatchlistItemBase):
    pass


class WatchlistItemRead(WatchlistItemBase):
    id: int
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)


class FinanceNoteBase(BaseModel):
    ticker: str
    title: str
    content: str
    tags: list[str] = Field(default_factory=list)
    source_url: str | None = None

    @field_validator("ticker")
    @classmethod
    def clean_ticker(cls, value: str) -> str:
        ticker = value.strip().upper()
        if not ticker:
            raise ValueError("ticker is required")
        return ticker

    @field_validator("title", "content")
    @classmethod
    def clean_required_text(cls, value: str) -> str:
        text = value.strip()
        if not text:
            raise ValueError("field is required")
        return text

    @field_validator("tags", mode="before")
    @classmethod
    def clean_tags(cls, value: list[str] | str | None) -> list[str]:
        if value is None:
            return []

        if isinstance(value, str):
            value = value.split(",")

        return [tag.strip() for tag in value if tag and tag.strip()]

    @field_validator("source_url", mode="before")
    @classmethod
    def clean_source_url(cls, value: str | None) -> str | None:
        if value is None:
            return None

        source_url = value.strip()
        if not source_url:
            return None

        if not source_url.startswith(("http://", "https://")):
            raise ValueError("source_url must start with http:// or https://")

        return source_url


class FinanceNoteCreate(FinanceNoteBase):
    pass


class FinanceNoteIngest(FinanceNoteBase):
    # Optional stable id from the calling source/agent. When present, ingestion
    # is idempotent: a note with the same external_id is skipped.
    external_id: str | None = None

    @field_validator("external_id", mode="before")
    @classmethod
    def clean_external_id(cls, value: str | None) -> str | None:
        if value is None:
            return None
        text = str(value).strip()
        return text or None


class FinanceNoteRead(FinanceNoteBase):
    id: int
    external_id: str | None = None
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)


class IngestResult(BaseModel):
    """Summary returned by the bulk ingest endpoint."""

    created: int
    skipped: int
    items: list[FinanceNoteRead]
