from __future__ import annotations

from app.legal.drafting.clauses.base import BaseClause


class ClauseRegistry:

    def __init__(self):
        self._clauses: dict[str, BaseClause] = {}

    def register(
        self,
        clause: BaseClause,
    ) -> None:
        self._clauses[clause.name] = clause

    def get(
        self,
        name: str,
    ) -> BaseClause:
        return self._clauses[name]

    def exists(
        self,
        name: str,
    ) -> bool:
        return name in self._clauses

    def names(self) -> list[str]:
        return sorted(self._clauses.keys())

    def all(self) -> list[BaseClause]:
        return list(self._clauses.values())


registry = ClauseRegistry()
