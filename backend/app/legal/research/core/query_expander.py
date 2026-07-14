from __future__ import annotations

class QueryExpander:

    SYNONYMS={
        "ipc":["indian penal code"],
        "crpc":["criminal procedure code"],
        "cpc":["code of civil procedure"],
        "constitution":["constitutional"],
        "article":["art"],
        "section":["sec"],
    }

    def expand(self,query:str)->str:

        q=query.lower()

        for word,alts in self.SYNONYMS.items():
            if word in q:
                q+=" "+" ".join(alts)

        return q
