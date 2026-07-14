from __future__ import annotations

class TaskClassifier:

    MAP={
        "research":"research",
        "draft":"drafting",
        "agreement":"drafting",
        "petition":"drafting",
        "judgment":"reasoning",
        "case":"research",
        "evidence":"evidence",
        "ocr":"ocr",
    }

    def classify(self,query:str)->str:

        q=query.lower()

        for k,v in self.MAP.items():
            if k in q:
                return v

        return "general"
