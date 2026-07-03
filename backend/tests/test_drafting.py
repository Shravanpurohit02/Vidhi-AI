from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_generate_notice():

    response = client.post(
        "/drafting/generate",
        json={
            "template": "legal_notice",
            "facts": "Client was not paid for services rendered.",
            "relief": "Recovery of outstanding dues.",
        },
    )

    assert response.status_code == 200


def test_invalid_template():

    response = client.post(
        "/drafting/generate",
        json={
            "template": "unknown",
            "facts": "Test",
        },
    )

    assert response.status_code == 400
