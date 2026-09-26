def test_health(client):
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_watchlist_crud(client):
    # create (ticker is normalized to upper-case)
    response = client.post(
        "/watchlist/", json={"ticker": "aapl", "company_name": "Apple"}
    )
    assert response.status_code == 201
    item = response.json()
    assert item["ticker"] == "AAPL"
    item_id = item["id"]

    # duplicate ticker -> 409
    assert client.post("/watchlist/", json={"ticker": "AAPL"}).status_code == 409

    # list
    listed = client.get("/watchlist/")
    assert listed.status_code == 200
    assert len(listed.json()) == 1

    # get by id / 404
    assert client.get(f"/watchlist/{item_id}").status_code == 200
    assert client.get("/watchlist/999999").status_code == 404

    # update
    updated = client.put(
        f"/watchlist/{item_id}", json={"ticker": "AAPL", "notes": "buy"}
    )
    assert updated.status_code == 200
    assert updated.json()["notes"] == "buy"

    # delete -> gone
    assert client.delete(f"/watchlist/{item_id}").status_code == 200
    assert client.get(f"/watchlist/{item_id}").status_code == 404


def test_finance_notes_filter_and_pagination(client):
    client.post(
        "/financenotes/",
        json={"ticker": "AAPL", "title": "Earnings beat", "content": "iPhone sales"},
    )
    client.post(
        "/financenotes/",
        json={"ticker": "MSFT", "title": "Azure growth", "content": "Cloud revenue up"},
    )
    client.post(
        "/financenotes/",
        json={"ticker": "AAPL", "title": "Services", "content": "Margins improving"},
    )

    # filter by ticker (input is normalized to upper-case)
    by_ticker = client.get("/financenotes/", params={"ticker": "aapl"})
    assert by_ticker.status_code == 200
    assert len(by_ticker.json()) == 2

    # full-text-ish search across title + content
    search = client.get("/financenotes/", params={"q": "azure"})
    assert len(search.json()) == 1

    # pagination
    assert len(client.get("/financenotes/", params={"limit": 1}).json()) == 1


def test_ingest_bulk_and_dedup(client):
    payload = [
        {"ticker": "AAPL", "title": "n1", "content": "c1", "external_id": "src-1"},
        {"ticker": "AAPL", "title": "n2", "content": "c2", "external_id": "src-2"},
    ]

    first = client.post("/ingest/finance-notes", json=payload)
    assert first.status_code == 200
    assert first.json()["created"] == 2
    assert first.json()["skipped"] == 0

    # re-sending the same external_ids is idempotent
    second = client.post("/ingest/finance-notes", json=payload).json()
    assert second["created"] == 0
    assert second["skipped"] == 2
