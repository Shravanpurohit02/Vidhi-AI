from app.legal.citations.extractor import CitationExtractor
from app.legal.knowledge.knowledge_base import KnowledgeBase


def test_citation_extraction():

    text = """
    AIR 1978 SC 597

    (1978) 1 SCC 248
    """

    citations = CitationExtractor().extract(text)

    assert len(citations) == 2


def test_ingestion():

    kb = KnowledgeBase()

    parsed = kb.ingest_file(
        "legal_corpus/sample_judgment.txt",
        {
            "source": "sample",
        },
    )

    assert parsed["length"] > 0

    assert len(parsed["citations"]) == 2
