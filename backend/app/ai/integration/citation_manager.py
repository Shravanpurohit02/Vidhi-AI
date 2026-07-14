from __future__ import annotations


class CitationManager:

    def format(self, citations: list[dict]) -> str:

        if not citations:
            return ""

        lines = []

        for citation in citations:
            lines.append(
                f"- {citation.get('document_id','')} : {citation.get('chunk_id','')}"
            )

        return "\n".join(lines)
