from __future__ import annotations


class ConfidenceEngine:
    """
    Calculates a normalized confidence score for research results.

    Weights:
        Retrieval quality : 40%
        Reranker quality  : 30%
        Citation coverage : 20%
        Context coverage  : 10%
    """

    RETRIEVAL_WEIGHT = 0.40
    RERANK_WEIGHT = 0.30
    CITATION_WEIGHT = 0.20
    CONTEXT_WEIGHT = 0.10

    @staticmethod
    def _clamp(value: float) -> float:
        return max(0.0, min(1.0, value))

    def calculate(
        self,
        retrieval_score: float,
        rerank_score: float,
        citation_count: int,
        context_count: int,
    ) -> float:

        retrieval = self._clamp(retrieval_score)

        rerank = self._clamp(rerank_score)

        citation = self._clamp(citation_count / 10.0)

        context = self._clamp(context_count / 10.0)

        score = (
            retrieval * self.RETRIEVAL_WEIGHT
            + rerank * self.RERANK_WEIGHT
            + citation * self.CITATION_WEIGHT
            + context * self.CONTEXT_WEIGHT
        )

        return round(
            self._clamp(score),
            3,
        )
