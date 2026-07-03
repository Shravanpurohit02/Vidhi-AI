from fastapi.testclient import TestClient

from app.auth.security import create_access_token
from app.main import app

client = TestClient(app)


def test_protected_route_without_token():
    response = client.get("/profile/me")
    assert response.status_code == 401


def test_protected_route_with_invalid_token():
    response = client.get(
        "/profile/me",
        headers={
            "Authorization": "Bearer invalid_token"
        },
    )

    assert response.status_code == 401


def test_create_valid_token():
    token = create_access_token(
        {"sub": "shravan@example.com"}
    )

    assert isinstance(token, str)
    assert len(token) > 20
