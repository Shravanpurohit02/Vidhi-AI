from __future__ import annotations

class CourtExtractor:

    COURTS=[
        "supreme court",
        "high court",
        "district court",
        "sessions court",
        "tribunal",
    ]

    def extract(self,text:str)->str:

        lower=text.lower()

        for court in self.COURTS:
            if court in lower:
                return court.title()

        return ""
