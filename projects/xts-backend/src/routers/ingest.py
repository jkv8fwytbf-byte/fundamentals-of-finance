from fastapi import APIRouter
from sqlalchemy.exc import IntegrityError

import schemas
from deps import db_dependency
from models import FinanceNote

router = APIRouter(prefix="/ingest", tags=["ingest"])


@router.post("/finance-notes", response_model=schemas.IngestResult)
def ingest_finance_notes(
    db: db_dependency,
    notes: list[schemas.FinanceNoteIngest],
):
    """Bulk-ingest finance notes from an external source/agent.

    Each item with an ``external_id`` is idempotent: if a note with that id
    already exists it is skipped, so re-sending the same batch is safe.
    Items are committed one at a time so a single failure doesn't abort the
    whole batch.
    """
    created: list[FinanceNote] = []
    skipped = 0

    for note in notes:
        if note.external_id:
            already_exists = (
                db.query(FinanceNote)
                .filter(FinanceNote.external_id == note.external_id)
                .first()
            )
            if already_exists:
                skipped += 1
                continue

        finance_note = FinanceNote(**note.model_dump())
        db.add(finance_note)
        try:
            db.commit()
        except IntegrityError:
            # e.g. a concurrent insert of the same external_id
            db.rollback()
            skipped += 1
            continue

        db.refresh(finance_note)
        created.append(finance_note)

    return schemas.IngestResult(
        created=len(created), skipped=skipped, items=created
    )
