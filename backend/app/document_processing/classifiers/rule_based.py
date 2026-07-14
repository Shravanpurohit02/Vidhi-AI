from __future__ import annotations


class RuleBasedClassifier:

    RULES = {
        "judgment": [
            "judgment",
            "pronounced",
            "appellant",
            "respondent",
        ],
        "order": [
            "ordered",
            "court orders",
            "disposed of",
        ],
        "petition": [
            "petition",
            "petitioner",
        ],
        "written_statement": [
            "written statement",
        ],
        "plaint": [
            "plaint",
        ],
        "affidavit": [
            "affidavit",
            "solemnly affirm",
        ],
        "agreement": [
            "agreement",
            "between the parties",
        ],
        "contract": [
            "contract",
        ],
        "notice": [
            "legal notice",
            "notice",
        ],
        "fir": [
            "first information report",
            "crime no",
            "fir",
        ],
        "charge_sheet": [
            "charge sheet",
            "chargesheet",
        ],
        "bail_application": [
            "bail application",
            "anticipatory bail",
            "regular bail",
        ],
        "appeal": [
            "memorandum of appeal",
            "appeal",
        ],
        "revision": [
            "revision petition",
            "criminal revision",
            "civil revision",
        ],
        "written_arguments": [
            "written arguments",
        ],
    }

    def classify(self, text: str, filename: str | None = None) -> dict:
        sample = text.lower()[:5000]

        for category, keywords in self.RULES.items():
            if any(keyword in sample for keyword in keywords):
                return {
                    "category": category,
                    "confidence": 0.80,
                }

        return {
            "category": "unknown",
            "confidence": 0.0,
        }
