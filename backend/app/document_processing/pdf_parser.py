from __future__ import annotations

from pathlib import Path

from pypdf import PdfReader


class PDFParser:
    """Production PDF parser."""

    @staticmethod
    def parse(path: str | Path) -> dict:
        path = Path(path)

        reader = PdfReader(str(path))

        pages = []
        full_text = []

        for index, page in enumerate(reader.pages, start=1):
            text = page.extract_text() or ""

            pages.append(
                {
                    "page": index,
                    "text": text,
                    "characters": len(text),
                }
            )

            full_text.append(text)

        return {
            "file": str(path),
            "page_count": len(reader.pages),
            "pages": pages,
            "text": "\n\n".join(full_text).strip(),
            "metadata": dict(reader.metadata or {}),
        }
