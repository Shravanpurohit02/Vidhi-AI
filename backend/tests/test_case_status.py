from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_status_filter_endpoint_exists():
    response = client.get("/cases/status/Draft")
    assert response.status_code == 200
