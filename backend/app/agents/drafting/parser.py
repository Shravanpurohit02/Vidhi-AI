from dataclasses import dataclass

from app.legal.templates.templates import TEMPLATES


@dataclass(slots=True)
class DraftRequest:

    template: str
    facts: str
    relief: str = ""


class DraftRequestParser:

    DEFAULT_TEMPLATE = "legal_notice"

    def parse(
        self,
        query: str,
    ) -> DraftRequest:

        q = query.lower()

        template = self.DEFAULT_TEMPLATE

        for name in TEMPLATES:
            if name.lower() in q:
                template = name
                break

        facts = query.strip()

        relief = ""

        marker = "relief:"

        if marker in q:
            idx = q.index(marker)
            relief = query[idx + len(marker) :].strip()
            facts = query[:idx].strip()

        return DraftRequest(
            template=template,
            facts=facts,
            relief=relief,
        )
