from app.legal.drafting.clauses.base import BaseClause
from app.legal.drafting.clauses.registry import registry


def load_default_clauses() -> None:

    clauses = [
        BaseClause(
            name="heading",
            content="LEGAL DOCUMENT",
        ),
        BaseClause(
            name="facts",
            content="{facts}",
        ),
        BaseClause(
            name="relief",
            content="{relief}",
            required=False,
        ),
        BaseClause(
            name="signature",
            content="Place:\nDate:\n\nSignature",
        ),
    ]

    for clause in clauses:
        if not registry.exists(clause.name):
            registry.register(clause)
