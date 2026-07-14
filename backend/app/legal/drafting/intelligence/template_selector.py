from __future__ import annotations

class TemplateSelector:

    MAP={
        "bail":"bail_application",
        "appeal":"appeal",
        "writ":"writ_petition",
        "contract":"agreement",
        "notice":"legal_notice",
        "affidavit":"affidavit",
    }

    def select(self,query:str)->str:

        q=query.lower()

        for key,value in self.MAP.items():
            if key in q:
                return value

        return "general"
