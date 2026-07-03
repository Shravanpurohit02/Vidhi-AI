from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_document_search_route():
    response = client.get("/documents/search?q=test")
    assert response.status_code == 200


def test_case_documents_route():
    response = client.get("/documents/case/1")
    assert response.status_code == 200


def test_delete_missing_document():
    response = client.delete("/documents/999999")
    assert response.status_code == 404
