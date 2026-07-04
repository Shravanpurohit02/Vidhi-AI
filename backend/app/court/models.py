from dataclasses import dataclass, field


@dataclass
class CourtCase:
    source: str

    cnr: str = ""
    title: str = ""
    case_number: str = ""
    case_type: str = ""
    year: str = ""

    court: str = ""
    state: str = ""
    district: str = ""

    status: str = ""
    next_hearing: str = ""

    parties: list[str] = field(default_factory=list)
    advocates: list[str] = field(default_factory=list)

    orders: list[dict] = field(default_factory=list)
    judgments: list[dict] = field(default_factory=list)
