from fastapi import APIRouter, HTTPException, Path
from sqlalchemy.exc import IntegrityError

import schemas
from deps import PaginationParams, db_dependency, get_or_404
from models import WatchlistItem

router = APIRouter(prefix="/watchlist", tags=["watchlist"])


@router.get("/", status_code=200, response_model=list[schemas.WatchlistItemRead])
def read_watchlist(db: db_dependency, page: PaginationParams):
    return (
        db.query(WatchlistItem)
        .order_by(WatchlistItem.created_at.desc())
        .offset(page.offset)
        .limit(page.limit)
        .all()
    )


@router.get(
    "/{watchlist_item_id}",
    status_code=200,
    response_model=schemas.WatchlistItemRead,
)
def read_watchlist_item_by_id(db: db_dependency, watchlist_item_id: int = Path(gt=0)):
    return get_or_404(db, WatchlistItem, watchlist_item_id, "Watchlist item not found")


@router.post("/", status_code=201, response_model=schemas.WatchlistItemRead)
def create_watchlist_item(
    db: db_dependency,
    watchlist_item_request: schemas.WatchlistItemCreate,
):
    watchlist_item = WatchlistItem(**watchlist_item_request.model_dump())
    db.add(watchlist_item)

    try:
        db.commit()
    except IntegrityError as exc:
        db.rollback()
        raise HTTPException(
            status_code=409,
            detail="Ticker already exists in watchlist",
        ) from exc

    db.refresh(watchlist_item)
    return watchlist_item


@router.put("/{watchlist_item_id}", response_model=schemas.WatchlistItemRead)
def update_watchlist_item(
    db: db_dependency,
    watchlist_item_request: schemas.WatchlistItemCreate,
    watchlist_item_id: int = Path(gt=0),
):
    watchlist_item = get_or_404(
        db, WatchlistItem, watchlist_item_id, "Watchlist item not found"
    )

    watchlist_item.ticker = watchlist_item_request.ticker
    watchlist_item.company_name = watchlist_item_request.company_name
    watchlist_item.notes = watchlist_item_request.notes

    try:
        db.commit()
    except IntegrityError as exc:
        db.rollback()
        raise HTTPException(
            status_code=409,
            detail="Ticker already exists in watchlist",
        ) from exc

    db.refresh(watchlist_item)
    return watchlist_item


@router.delete("/{watchlist_item_id}")
def delete_watchlist_item(
    db: db_dependency,
    watchlist_item_id: int = Path(gt=0),
):
    watchlist_item = get_or_404(
        db, WatchlistItem, watchlist_item_id, "Watchlist item not found"
    )
    db.delete(watchlist_item)
    db.commit()
    return {"message": "Watchlist item deleted successfully"}
