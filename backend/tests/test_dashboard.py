from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_dashboard_summary():

    response = client.get("/dashboard/summary")

    assert response.status_code == 200

    body = response.json()

    assert "cases" in body
    assert "documents" in body
    assert "clients" in body
    assert "hearings" in body
    assert "tasks" in body
