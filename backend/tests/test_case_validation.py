from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_get_nonexistent_case():
    response = client.get("/cases/999999")
    assert response.status_code == 404


def test_update_nonexistent_case():
    response = client.put(
        "/cases/999999",
        json={
            "title": "Updated",
            "description": "Updated",
            "court": "High Court",
            "status": "Open",
        },
    )
    assert response.status_code == 404


def test_delete_nonexistent_case():
    response = client.delete("/cases/999999")
    assert response.status_code == 404


def test_search_without_query():
    response = client.get("/cases/search")
    assert response.status_code == 422


def test_statistics_response_schema():
    response = client.get("/cases/statistics")

    assert response.status_code == 200

    body = response.json()

    assert isinstance(body["total"], int)
    assert isinstance(body["draft"], int)
    assert isinstance(body["open"], int)
    assert isinstance(body["closed"], int)
