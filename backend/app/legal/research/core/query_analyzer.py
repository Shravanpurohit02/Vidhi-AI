from __future__ import annotations

class QueryAnalyzer:

    def analyze(self, query:str)->dict:

        return {
            "original":query,
            "normalized":" ".join(query.lower().split()),
            "keywords":[
                x for x in query.lower().split()
                if len(x)>2
            ],
        }
