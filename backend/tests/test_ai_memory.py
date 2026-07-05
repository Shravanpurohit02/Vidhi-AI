from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_memory_clear():

    response = client.delete("/ai/memory")

    assert response.status_code == 200

    assert response.json()["status"] == "cleared"


def test_chat_contains_citations():

    client.post(
        "/ai/ingest",
        json={
            "text": "Article 21 protects life and personal liberty.",
            "metadata": {
                "source": "Constitution of India",
                "article": "21",
            },
        },
    )

    response = client.post(
        "/ai/chat",
        json={"message": "Explain Article 21."},
    )

    body = response.json()

    assert "answer" in body
    assert "citations" in body
