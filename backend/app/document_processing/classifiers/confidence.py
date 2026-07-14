from __future__ import annotations


class ConfidenceScorer:
    """Utility for normalizing classifier confidence scores."""

    @staticmethod
    def normalize(score: float) -> float:
        score = max(0.0, min(1.0, score))
        return round(score, 4)

    @staticmethod
    def level(score: float) -> str:
        score = ConfidenceScorer.normalize(score)

        if score >= 0.90:
            return "very_high"
        if score >= 0.75:
            return "high"
        if score >= 0.50:
            return "medium"
        if score >= 0.25:
            return "low"
        return "very_low"
