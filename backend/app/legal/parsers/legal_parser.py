from pathlib import Path

from app.legal.citations.extractor import CitationExtractor


class LegalParser:

    def __init__(self):
        self.extractor = CitationExtractor()

    def parse(self, path: str):

        text = Path(path).read_text(
            encoding="utf-8",
            errors="ignore",
        )

        return {
            "text": text,
            "citations": self.extractor.extract(text),
            "length": len(text),
        }
