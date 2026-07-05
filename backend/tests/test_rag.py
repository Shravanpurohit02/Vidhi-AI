from app.ai.retrieval.retriever import Retriever


def test_chunking():

    r = Retriever()

    chunks = r.chunker.chunk("A" * 5000)

    assert len(chunks) > 1


def test_index():

    r = Retriever()

    r.index_document(
        "This is a legal document.",
        {
            "case": 1,
        },
    )

    assert len(r.store.items) > 0


def test_retrieve():

    r = Retriever()

    r.index_document(
        "Article 21 guarantees right to life.",
        {},
    )

    results = r.retrieve("Article 21")

    assert len(results) > 0
