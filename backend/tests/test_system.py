from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_metrics_endpoint():
    response = client.get("/system/metrics")
    assert response.status_code == 200
    assert isinstance(response.json(), dict)


def test_audit_endpoint():
    response = client.get("/system/audit")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
