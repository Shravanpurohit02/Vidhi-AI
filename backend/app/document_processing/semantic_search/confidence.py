from __future__ import annotations

class ConfidenceScorer:

    @staticmethod
    def label(score:float)->str:
        if score>=0.90:
            return "very_high"
        if score>=0.75:
            return "high"
        if score>=0.55:
            return "medium"
        if score>=0.35:
            return "low"
        return "very_low"
