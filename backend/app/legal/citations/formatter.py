from __future__ import annotations

from app.legal.citations.styles import CitationStyle


class CitationFormatter:

    def format(
        self,
        citation: str,
        style: CitationStyle = CitationStyle.RAW,
    ) -> str:

        citation = citation.strip()

        return citation


formatter = CitationFormatter()
