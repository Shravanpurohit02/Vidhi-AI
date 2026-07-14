from __future__ import annotations

from app.legal.citations.normalizer import CitationNormalizer


class CitationMatcher:

    def match(
        self,
        citations:list[str],
    )->list[str]:

        seen=set()
        output=[]

        for citation in citations:

            citation=CitationNormalizer.normalize(citation)

            if citation and citation not in seen:
                seen.add(citation)
                output.append(citation)

        return output
