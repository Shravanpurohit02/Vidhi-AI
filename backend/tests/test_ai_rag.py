from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_document_ingestion():

    response = client.post(
        "/ai/ingest",
        json={
            "text": "Article 21 guarantees protection of life and personal liberty.",
            "metadata": {
                "source": "Constitution"
            }
        },
    )

    assert response.status_code == 200


def test_chat_after_ingestion():

    response = client.post(
        "/ai/chat",
        json={
            "message": "What does Article 21 provide?"
        },
    )

    assert response.status_code == 200

    body = response.json()

    assert "answer" in body
