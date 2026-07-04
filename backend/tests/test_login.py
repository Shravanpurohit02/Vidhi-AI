from fastapi.testclient import TestClient

from app.main import app


def test_login_endpoint_exists():
    with TestClient(app) as client:
        response = client.post(
            "/auth/login",
            json={
                "email": "dummy@example.com",
                "password": "dummy",
            },
        )

    assert response.status_code in (200, 401)
