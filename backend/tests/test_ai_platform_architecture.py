from pathlib import Path

REQUIRED_FILES = [
    "app/ai/storage/vector_store.py",
    "app/ai/cache/embedding_cache.py",
    "app/ai/bm25/bm25.py",
    "app/ai/ranking/hybrid_ranker.py",
    "app/ai/search/hybrid_search.py",
    "app/ai/index/index_manager.py",
    "app/legal/reasoning/summarizer.py",
    "app/legal/reasoning/reasoning_service.py",
    "app/legal/precedents/precedent_extractor.py",
    "app/legal/graphs/citation_graph.py",
    "app/legal/explainability/explainer.py",
    "app/api/v1/reasoning.py",
]


def test_ai_platform_architecture():
    for file in REQUIRED_FILES:
        assert Path(file).exists(), f"{file} missing"
