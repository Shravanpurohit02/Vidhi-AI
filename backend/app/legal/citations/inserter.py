from __future__ import annotations

from app.legal.citations.formatter import formatter


class CitationInserter:

    def insert(
        self,
        document: str,
        citations: list[str],
    ) -> str:

        if not citations:
            return document

        lines = [
            "",
            "",
            "Authorities:",
        ]

        for number, citation in enumerate(citations, start=1):
            lines.append(f"{number}. {formatter.format(citation)}")

        return document + "\n".join(lines)


inserter = CitationInserter()
