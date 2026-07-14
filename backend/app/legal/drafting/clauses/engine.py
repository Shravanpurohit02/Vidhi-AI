from __future__ import annotations

from app.legal.drafting.clauses.registry import registry


class ClauseEngine:

    def build(
        self,
        clause_names: list[str],
        **context,
    ) -> str:

        sections: list[str] = []

        for name in clause_names:

            if not registry.exists(name):
                continue

            clause = registry.get(name)

            try:
                text = clause.content.format(**context)
            except KeyError:
                text = clause.content

            if text.strip():
                sections.append(text.strip())

        return "\n\n".join(sections)


engine = ClauseEngine()
