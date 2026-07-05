from app.ai.index.index_manager import IndexManager
from app.ai.search.hybrid_search import HybridSearch


def test_hybrid_search():

    manager = IndexManager()

    manager.index(
        "Article 21 protects life and liberty.",
        {
            "source": "constitution",
        },
    )

    manager.index(
        "Section 420 concerns cheating.",
        {
            "source": "IPC",
        },
    )

    results = HybridSearch().search("Article 21")

    assert len(results) >= 1


def test_embedding_cache():

    manager = IndexManager()

    manager.index(
        "Cache Test",
        {},
    )

    assert manager.cache.get("Cache Test") is not None
