from __future__ import annotations


class DocumentRouter:
    """Routes classified documents to downstream processing pipelines."""

    ROUTES = {
        "judgment": "legal_research",
        "order": "legal_research",
        "petition": "drafting",
        "written_statement": "drafting",
        "plaint": "drafting",
        "affidavit": "drafting",
        "agreement": "contract_analysis",
        "contract": "contract_analysis",
        "notice": "drafting",
        "fir": "criminal_analysis",
        "charge_sheet": "criminal_analysis",
        "bail_application": "criminal_analysis",
        "appeal": "appellate_analysis",
        "revision": "appellate_analysis",
        "written_arguments": "drafting",
        "unknown": "manual_review",
    }

    @classmethod
    def route(cls, category: str) -> str:
        return cls.ROUTES.get(category, "manual_review")
