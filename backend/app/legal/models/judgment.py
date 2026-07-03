from dataclasses import dataclass
from datetime import date


@dataclass
class Judgment:
    title: str
    court: str
    citation: str
    decision_date: date | None
    judges: list[str]
    text: str
