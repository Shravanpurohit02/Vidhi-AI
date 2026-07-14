from __future__ import annotations

import re


class CitationValidator:

    SCC = re.compile(r"\(\d{4}\)\s*\d+\s*SCC\s*\d+")
    AIR = re.compile(r"AIR\s*\d{4}\s*[A-Za-z]+\s*\d+")

    def valid(
        self,
        citation: str,
    ) -> bool:

        citation = citation.strip()

        return bool(self.SCC.fullmatch(citation) or self.AIR.fullmatch(citation))

    def validate(
        self,
        citations: list[str],
    ) -> list[str]:

        return [citation for citation in citations if self.valid(citation)]


validator = CitationValidator()
