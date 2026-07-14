from __future__ import annotations

class IntentClassifier:

    def classify(self,query:str)->str:

        q=query.lower()

        if "judgment" in q or "case" in q:
            return "precedent"

        if "section" in q or "act" in q:
            return "statute"

        if "draft" in q:
            return "drafting"

        return "general"
