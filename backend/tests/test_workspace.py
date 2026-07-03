from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_workspace_routes():

    assert client.get("/workspace/hearings").status_code == 200
    assert client.get("/workspace/tasks").status_code == 200
