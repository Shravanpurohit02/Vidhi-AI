from __future__ import annotations

from datetime import datetime

from pydantic import BaseModel


class ChainOfCustodyEntry(BaseModel):
    timestamp: datetime
    actor: str
    action: str
    notes: str = ""
