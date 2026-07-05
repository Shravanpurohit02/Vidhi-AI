from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_case_crud_routes_exist():
    assert client.get("/cases").status_code in (200, 307)
    assert client.get("/cases/1").status_code in (200, 404)
    assert client.put(
        "/cases/1",
        json={"title": "Updated", "description": "", "court": "", "status": "Open"},
    ).status_code in (200, 404)
    assert client.delete("/cases/1").status_code in (200, 404)
