from app.ai.index.index_manager import IndexManager
from app.ai.search.hybrid_search import HybridSearch


def test_index_and_search():

    manager = IndexManager()

    manager.index(
        "Article 21 protects life.",
        {
            "source":"constitution"
        },
    )

    results = HybridSearch().search(
        "Article 21"
    )

    assert len(results) >= 1
