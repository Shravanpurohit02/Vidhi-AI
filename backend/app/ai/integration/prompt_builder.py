from __future__ import annotations


class PromptBuilder:

    def build(
        self,
        system_prompt: str,
        context: str,
        user_prompt: str,
    ) -> str:

        return "\n\n".join(
            part.strip()
            for part in (
                system_prompt,
                context,
                user_prompt,
            )
            if part.strip()
        )
