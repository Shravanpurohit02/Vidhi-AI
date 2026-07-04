from pathlib import Path

import pytest

from app.legal.parsers.legal_parser import LegalParser


def test_parse_text_file():
    Path("tmp_parser.txt").write_text(
        "Article 21 protects life.",
        encoding="utf-8",
    )

    parsed = LegalParser().parse("tmp_parser.txt")

    assert parsed["length"] > 0
    assert "Article 21" in parsed["text"]


def test_parse_markdown_file():
    Path("tmp_parser.md").write_text(
        "# Heading\n\nArticle 21 protects life.",
        encoding="utf-8",
    )

    parsed = LegalParser().parse("tmp_parser.md")

    assert parsed["length"] > 0


def test_unsupported_extension():
    Path("tmp_parser.xyz").write_text(
        "dummy",
        encoding="utf-8",
    )

    with pytest.raises(ValueError):
        LegalParser().parse("tmp_parser.xyz")
