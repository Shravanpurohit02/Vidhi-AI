from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_workflow_dashboard():

    response = client.get("/workflow/dashboard")

    assert response.status_code == 200

    body = response.json()

    assert "analytics" in body
    assert "pending_tasks" in body
    assert "upcoming_hearings" in body
