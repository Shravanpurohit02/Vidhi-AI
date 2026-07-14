from __future__ import annotations


class HallucinationGuard:

    def review(
        self,
        response: str,
        citations: list[dict],
    ) -> dict:

        return {
            "approved": bool(response.strip()),
            "citation_count": len(citations),
            "response": response,
        }
