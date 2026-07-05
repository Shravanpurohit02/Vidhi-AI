from pathlib import Path

REQUIRED_FILES = [
    "app/legal/models/judgment.py",
    "app/legal/citations/extractor.py",
    "app/legal/parsers/legal_parser.py",
    "app/legal/knowledge/knowledge_base.py",
    "app/legal/entities/entity_extractor.py",
    "app/legal/search/semantic_search.py",
    "app/legal/research/research_service.py",
    "app/legal/ranking/ranker.py",
    "app/legal/history/history.py",
    "app/legal/session/session.py",
    "app/api/v1/research.py",
]


def test_legal_architecture():
    for file in REQUIRED_FILES:
        assert Path(file).exists(), f"{file} missing"
