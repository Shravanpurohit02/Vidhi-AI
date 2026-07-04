from pathlib import Path

from pypdf import PdfReader

from app.legal.citations.extractor import CitationExtractor


class LegalParser:

    def __init__(self):
        self.extractor = CitationExtractor()

    def _read_text(self, path: Path) -> str:
        return path.read_text(
            encoding="utf-8",
            errors="ignore",
        )

    def _read_pdf(self, path: Path) -> str:
        reader = PdfReader(str(path))
        parts = []

        for page in reader.pages:
            parts.append(page.extract_text() or "")

        return "\n".join(parts)

    def _read_docx(self, path: Path) -> str:
        try:
            from docx import Document
        except ImportError as exc:
            raise RuntimeError(
                "DOCX parsing requires the optional "
                "'python-docx' package."
            ) from exc

        document = Document(str(path))

        return "\n".join(
            paragraph.text
            for paragraph in document.paragraphs
        )

    def parse(self, path: str):
        path = Path(path)

        suffix = path.suffix.lower()

        if suffix in {".txt", ".md"}:
            text = self._read_text(path)

        elif suffix == ".pdf":
            text = self._read_pdf(path)

        elif suffix == ".docx":
            text = self._read_docx(path)

        else:
            raise ValueError(
                f"Unsupported file type: {suffix}"
            )

        return {
            "text": text,
            "citations": self.extractor.extract(text),
            "length": len(text),
        }
