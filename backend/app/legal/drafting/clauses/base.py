from __future__ import annotations

from dataclasses import dataclass


@dataclass(slots=True)
class BaseClause:
    """
    Represents a reusable legal drafting clause.
    """

    name: str
    content: str
    required: bool = True
