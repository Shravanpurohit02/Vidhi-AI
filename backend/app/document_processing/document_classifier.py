from __future__ import annotations

from pathlib import Path

from app.document_processing.classifiers.rule_based import RuleBasedClassifier


class DocumentClassifier:

    def __init__(self):
        self.rule_classifier = RuleBasedClassifier()

    def classify(self, text: str, filename: str | None = None) -> dict:
        result = self.rule_classifier.classify(text, filename)

        return {
            "category": result["category"],
            "confidence": result["confidence"],
            "method": "rule_based",
        }

    def classify_file(self, path: str | Path, text: str) -> dict:
        path = Path(path)
        return self.classify(text=text, filename=path.name)
