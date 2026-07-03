from fastapi.testclient import TestClient

from app.main import app
from app.legal.entities.entity_extractor import LegalEntityExtractor

client = TestClient(app)


def test_entity_extraction():

    result = LegalEntityExtractor().extract(
        "Article 21 and Section 420 of Indian Penal Code Act"
    )

    assert "Article 21" in result["articles"]
    assert "Section 420" in result["sections"]


def test_research_endpoint():

    response = client.post(
        "/research/",
        json={
            "question": "Explain Article 21."
        },
    )

    assert response.status_code == 200

    body = response.json()

    assert "answer" in body
    assert "entities" in body
