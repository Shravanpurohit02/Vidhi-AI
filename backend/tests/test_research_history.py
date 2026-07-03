from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_research_history():

    client.post(
        "/research/",
        json={
            "question": "Explain Article 21."
        },
    )

    response = client.get("/research/history")

    assert response.status_code == 200

    assert isinstance(response.json(), list)


def test_clear_history():

    response = client.delete("/research/history")

    assert response.status_code == 200

    assert response.json()["status"] == "cleared"
