from __future__ import annotations

from app.document_processing.classifiers.ai_classifier import AIClassifier
from app.document_processing.classifiers.rule_based import RuleBasedClassifier


class EnsembleClassifier:

    def __init__(self):
        self.rule = RuleBasedClassifier()
        self.ai = AIClassifier()

    def classify(self, text: str, filename: str | None = None) -> dict:

        rule_result = self.rule.classify(text, filename)
        ai_result = self.ai.classify(text)

        if ai_result["confidence"] > rule_result["confidence"]:
            ai_result["method"] = "ai"
            return ai_result

        rule_result["method"] = "rule_based"
        return rule_result
