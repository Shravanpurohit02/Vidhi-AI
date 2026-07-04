from pathlib import Path

from app.legal.knowledge.corpus.corpus_manager import CorpusManager


def test_corpus_manager():

    Path("tmp_corpus").mkdir(exist_ok=True)

    Path(
        "tmp_corpus/sample.txt"
    ).write_text(
        "Article 21 protects life."
    )

    manager = CorpusManager()

    result = manager.ingest_directory(
        "tmp_corpus"
    )

    stats = manager.statistics(
        "tmp_corpus"
    )

    assert result["documents"] == 1
    assert stats["documents"] == 1
