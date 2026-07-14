from __future__ import annotations


class DraftCitationService:

    def append(
        self,
        draft: str,
        citations: str,
    ) -> str:

        if not citations:
            return draft

        return draft + "\n\nReferenced Material\n" + citations
