from __future__ import annotations

from typing import Any

from app.ai.integration.provider_router import provider_router


class AIService:
    """
    Multi-turn conversation manager.
    """

    def __init__(self):
        self._history: list[dict[str, str]] = []

    def clear(self) -> None:
        self._history.clear()

    def history(self) -> list[dict[str, str]]:
        return list(self._history)

    def ask(
        self,
        prompt: str,
        system_prompt: str | None = None,
        provider: str | None = None,
        **kwargs: Any,
    ) -> str:

        self._history.append(
            {
                "role": "user",
                "content": prompt,
            }
        )

        ai = provider_router.provider(
            preferred=provider,
        )

        if hasattr(ai, "chat"):

            answer = ai.chat(
                messages=self._history,
                temperature=kwargs.get("temperature", 0.2),
                top_p=kwargs.get("top_p", 1.0),
                max_tokens=kwargs.get("max_tokens"),
            )

        else:

            answer = ai.generate(
                prompt=prompt,
                system_prompt=system_prompt,
                **kwargs,
            )

        self._history.append(
            {
                "role": "assistant",
                "content": answer,
            }
        )

        return answer


conversation_service = AIService()
