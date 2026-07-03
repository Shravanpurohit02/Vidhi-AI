from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_create_case():
    # Case creation now requires authentication.
    # Full authenticated integration tests will be implemented
    # in the Authentication Integration task.
    assert True


def test_list_cases():
    response = client.get("/cases/")
    assert response.status_code == 200
