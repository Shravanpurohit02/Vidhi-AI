from __future__ import annotations

class ClauseRecommender:

    CLAUSES={
        "agreement":[
            "Definitions",
            "Obligations",
            "Termination",
            "Jurisdiction",
        ],
        "legal_notice":[
            "Facts",
            "Cause of Action",
            "Demand",
        ],
        "bail_application":[
            "Facts",
            "Grounds",
            "Prayer",
        ],
        "appeal":[
            "Facts",
            "Grounds",
            "Reliefs",
        ],
    }

    def recommend(self,template:str):

        return self.CLAUSES.get(
            template,
            [],
        )
