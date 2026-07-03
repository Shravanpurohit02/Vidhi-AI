from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_client_routes():
    assert client.get("/clients/").status_code == 200
