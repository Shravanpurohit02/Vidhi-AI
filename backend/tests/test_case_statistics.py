from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_case_statistics_endpoint():
    response = client.get("/cases/statistics")

    assert response.status_code == 200

    body = response.json()

    assert "total" in body
    assert "draft" in body
    assert "open" in body
    assert "closed" in body
