from dataclasses import dataclass, field
from datetime import datetime


@dataclass
class ResearchSession:
    id: str
    created_at: datetime
    queries: list[str] = field(default_factory=list)

    def add_query(self, query: str):
        self.queries.append(query)
