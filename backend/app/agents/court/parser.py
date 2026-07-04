import re
from dataclasses import dataclass


@dataclass
class CourtIntent:
    intent: str
    cnr: str | None = None
    case_number: str | None = None
    case_type: str | None = None
    year: str | None = None


class CourtIntentParser:

    CNR_PATTERN = re.compile(r"\b[A-Z]{4}\d{12}\b", re.IGNORECASE)

    CASE_PATTERN = re.compile(
        r"([A-Za-z()./-]+)\s+(\d+)\s*/\s*(\d{4})",
        re.IGNORECASE,
    )

    def parse(self, query: str) -> CourtIntent:

        cnr = self.CNR_PATTERN.search(query)

        if cnr:
            return CourtIntent(
                intent="search_by_cnr",
                cnr=cnr.group(0).upper(),
            )

        case = self.CASE_PATTERN.search(query)

        if case:
            return CourtIntent(
                intent="search_by_case",
                case_type=case.group(1),
                case_number=case.group(2),
                year=case.group(3),
            )

        if "import" in query.lower():
            return CourtIntent(intent="import_case")

        return CourtIntent(intent="unknown")
