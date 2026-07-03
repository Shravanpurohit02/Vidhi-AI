from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_search_endpoint_exists():
    response = client.get("/cases/search?q=test")
    assert response.status_code in (200, 401)
