from __future__ import annotations

from app.legal.drafting.prompts.base import BASE_SYSTEM_PROMPT


class PromptService:

    def build(
        self,
        template: str,
        facts: str,
        context: str = "",
    ) -> str:

        return "\n\n".join(
            part.strip()
            for part in (
                BASE_SYSTEM_PROMPT,
                template,
                context,
                facts,
            )
            if part.strip()
        )
