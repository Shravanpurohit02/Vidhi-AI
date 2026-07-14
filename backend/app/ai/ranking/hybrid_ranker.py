from __future__ import annotations


class HybridRanker:
    """
    Combines lexical and semantic search results into a single ranked list.

    Backward compatible:
    - Results without scores are still accepted.
    - Duplicate documents are removed.
    - Higher combined score ranks first.
    """

    DEFAULT_LEXICAL_SCORE = 0.50
    DEFAULT_SEMANTIC_SCORE = 0.50

    def _combined_score(
        self,
        result: dict,
    ) -> float:

        lexical = float(
            result.get(
                "lexical_score",
                self.DEFAULT_LEXICAL_SCORE,
            )
        )

        semantic = float(
            result.get(
                "semantic_score",
                self.DEFAULT_SEMANTIC_SCORE,
            )
        )

        return (lexical + semantic) / 2.0

    def combine(
        self,
        lexical: list[dict],
        semantic: list[dict],
    ) -> list[dict]:

        merged: dict[str, dict] = {}

        for result in lexical + semantic:

            key = (
                result.get("id")
                or result.get("document_id")
                or result.get("text")
                or str(id(result))
            )

            score = self._combined_score(result)

            existing = merged.get(key)

            if existing is None:
                result["hybrid_score"] = score
                merged[key] = result
                continue

            if score > existing.get(
                "hybrid_score",
                0.0,
            ):
                result["hybrid_score"] = score
                merged[key] = result

        return sorted(
            merged.values(),
            key=lambda item: item.get(
                "hybrid_score",
                0.0,
            ),
            reverse=True,
        )
