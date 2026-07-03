from pathlib import Path


REQUIRED_FILES = [
    "app/ai/config.py",
    "app/ai/interfaces/base_provider.py",
    "app/ai/providers/mock_provider.py",
    "app/ai/chunking/chunker.py",
    "app/ai/embeddings/base.py",
    "app/ai/embeddings/mock.py",
    "app/ai/vectorstore/memory.py",
    "app/ai/retrieval/retriever.py",
    "app/ai/memory/conversation.py",
    "app/ai/citations/citation_engine.py",
    "app/ai/services/ai_service.py",
]


def test_ai_architecture():
    for file in REQUIRED_FILES:
        assert Path(file).exists(), f"{file} missing"
