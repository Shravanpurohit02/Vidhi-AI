from __future__ import annotations

class OutcomeClassifier:

    LABELS={
        "dismissed":"dismissed",
        "allowed":"allowed",
        "partly allowed":"partly_allowed",
        "convicted":"convicted",
        "acquitted":"acquitted",
        "granted":"granted",
        "rejected":"rejected",
    }

    def classify(self,text:str)->str:

        lower=text.lower()

        for key,value in self.LABELS.items():
            if key in lower:
                return value

        return "unknown"
