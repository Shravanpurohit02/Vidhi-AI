from __future__ import annotations


class AIClassifier:
    """
    AI-powered document classifier.

    Future providers:
      - OpenAI
      - Gemini
      - Claude
      - Ollama
      - Local models
    """

    def classify(self, text: str) -> dict:
        return {
            "category": "unknown",
            "confidence": 0.0,
            "provider": None,
            "reason": "AI classifier not configured.",
        }
