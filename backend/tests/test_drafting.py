from fastapi.testclient import TestClient

from app.main import app


def test_generate_notice():

    with TestClient(app) as client:

        response = client.post(
            "/drafting/generate",
            json={
                "template": "legal_notice",
                "facts": "Client was not paid for services rendered.",
                "relief": "Recovery of outstanding dues.",
            },
        )

    assert response.status_code == 200

    data = response.json()

    assert "document" in data
    assert "template" in data
    assert "provider" in data
    assert "processing_time" in data
    assert "word_count" in data
    assert data["template"] == "legal_notice"
    assert data["word_count"] > 0


def test_invalid_template():

    with TestClient(app) as client:

        response = client.post(
            "/drafting/generate",
            json={
                "template": "unknown",
                "facts": "Test facts",
            },
        )

    assert response.status_code == 400
