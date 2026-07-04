from fastapi.testclient import TestClient

from app.main import app


def test_reasoning():

    with TestClient(app) as client:

        response = client.post(
            "/reasoning/analyze",
            json={
                "text": """
Article 21 protects life.

(1978) 1 SCC 248

AIR 1978 SC 597
"""
            },
        )

    assert response.status_code == 200

    body = response.json()

    assert "answer" in body
    assert "reasoning" in body
    assert "citations" in body
    assert "provider" in body
    assert "processing_time" in body
    assert "generated_at" in body


def test_citation_graph():

    from app.legal.graphs.citation_graph import CitationGraph

    graph = CitationGraph()

    graph.add_document(
        "doc1",
        [
            "(1978) 1 SCC 248",
        ],
    )

    assert len(graph.neighbours("doc1")) == 1
