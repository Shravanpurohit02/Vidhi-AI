from fastapi.testclient import TestClient

from app.main import app


def test_workflow_dashboard():

    with TestClient(app) as client:

        response = client.get("/workflow/dashboard")

    assert response.status_code == 200

    body = response.json()

    assert "analytics" in body
    assert "pending_tasks" in body
    assert "upcoming_hearings" in body
    assert "generated_at" in body

    assert isinstance(body["pending_tasks"], int)
    assert isinstance(body["upcoming_hearings"], int)
