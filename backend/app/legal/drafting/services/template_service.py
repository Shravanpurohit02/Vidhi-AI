from __future__ import annotations


class TemplateService:

    def render(
        self,
        template: str,
        variables: dict,
    ) -> str:

        return template.format(**variables)
