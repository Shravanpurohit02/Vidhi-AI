from __future__ import annotations

import string

from app.legal.templates.templates import TEMPLATES


class TemplateValidator:
    """
    Validates drafting templates before they are rendered.
    """

    REQUIRED_FIELDS = {
        "facts",
        "relief",
    }

    def exists(
        self,
        template: str,
    ) -> bool:
        return template in TEMPLATES

    def placeholders(
        self,
        template: str,
    ) -> set[str]:

        formatter = string.Formatter()

        return {
            field_name
            for _, field_name, _, _ in formatter.parse(TEMPLATES[template])
            if field_name
        }

    def validate(
        self,
        template: str,
    ) -> None:

        if not self.exists(template):
            raise ValueError(f"Unknown template '{template}'.")

        placeholders = self.placeholders(template)

        missing = self.REQUIRED_FIELDS - placeholders

        if missing:
            raise ValueError(
                f"Template '{template}' is missing placeholders: "
                f"{', '.join(sorted(missing))}"
            )

        unknown = placeholders - self.REQUIRED_FIELDS

        if unknown:
            raise ValueError(
                f"Template '{template}' contains unknown placeholders: "
                f"{', '.join(sorted(unknown))}"
            )


validator = TemplateValidator()
