from fastapi import APIRouter, Path, Query
from sqlalchemy import or_
from sqlalchemy.dialects.postgresql import JSONB

import schemas
from deps import PaginationParams, db_dependency, get_or_404
from models import FinanceNote

router = APIRouter(prefix="/financenotes", tags=["financenotes"])


@router.get("/", status_code=200, response_model=list[schemas.FinanceNoteRead])
def read_finance_notes(
    db: db_dependency,
    page: PaginationParams,
    ticker: str | None = Query(default=None, description="Filter by exact ticker"),
    tag: str | None = Query(default=None, description="Filter by a single tag"),
    q: str | None = Query(default=None, description="Search title and content"),
):
    query = db.query(FinanceNote)

    if ticker:
        query = query.filter(FinanceNote.ticker == ticker.strip().upper())

    if q:
        like = f"%{q.strip()}%"
        query = query.filter(
            or_(FinanceNote.title.ilike(like), FinanceNote.content.ilike(like))
        )

    if tag:
        # Cast the JSON column to JSONB so we can use the "contains" (@>)
        # operator. This branch runs on PostgreSQL only.
        query = query.filter(FinanceNote.tags.cast(JSONB).contains([tag.strip()]))

    return (
        query.order_by(FinanceNote.created_at.desc())
        .offset(page.offset)
        .limit(page.limit)
        .all()
    )


@router.get(
    "/{finance_note_id}", status_code=200, response_model=schemas.FinanceNoteRead
)
def read_finance_note_by_id(db: db_dependency, finance_note_id: int = Path(gt=0)):
    return get_or_404(db, FinanceNote, finance_note_id, "Finance note not found")


@router.post("/", status_code=201, response_model=schemas.FinanceNoteRead)
def create_finance_note(
    db: db_dependency, finance_note_request: schemas.FinanceNoteCreate
):
    finance_note = FinanceNote(**finance_note_request.model_dump())
    db.add(finance_note)
    db.commit()
    db.refresh(finance_note)
    return finance_note


@router.put("/{finance_note_id}", response_model=schemas.FinanceNoteRead)
def update_finance_note(
    db: db_dependency,
    finance_note_request: schemas.FinanceNoteCreate,
    finance_note_id: int = Path(gt=0),
):
    finance_note = get_or_404(db, FinanceNote, finance_note_id, "Finance note not found")

    finance_note.ticker = finance_note_request.ticker
    finance_note.title = finance_note_request.title
    finance_note.content = finance_note_request.content
    finance_note.tags = finance_note_request.tags
    finance_note.source_url = finance_note_request.source_url
    db.commit()
    db.refresh(finance_note)
    return finance_note


@router.delete("/{finance_note_id}")
def delete_finance_note(
    db: db_dependency,
    finance_note_id: int = Path(gt=0),
):
    finance_note = get_or_404(db, FinanceNote, finance_note_id, "Finance note not found")
    db.delete(finance_note)
    db.commit()
    return {"message": "Finance note deleted successfully"}
