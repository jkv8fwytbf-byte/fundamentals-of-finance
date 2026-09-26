from fastapi import FastAPI

from routers import financenotes, ingest, watchlist

app = FastAPI()


@app.get("/health", tags=["health"])
def health():
    return {"status": "ok"}


app.include_router(watchlist.router)
app.include_router(financenotes.router)
app.include_router(ingest.router)
