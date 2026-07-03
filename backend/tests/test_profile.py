from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_profile_requires_authentication():
    response = client.get("/profile/me")

    assert response.status_code == 401
