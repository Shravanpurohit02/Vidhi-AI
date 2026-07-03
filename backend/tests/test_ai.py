from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_ai_chat():

    response = client.post(
        "/ai/chat",
        json={
            "message": "What is Article 21?"
        },
    )

    assert response.status_code == 200

    body = response.json()

    assert "answer" in body
