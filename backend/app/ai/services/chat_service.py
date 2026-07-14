from __future__ import annotations

from typing import Any

from app.ai.integration.provider_router import provider_router


class AIService:
    """
    Unified chat interface for every AI provider.
    """

    def chat(
        self,
        prompt: str,
        system_prompt: str | None = None,
        provider: str | None = None,
        **kwargs: Any,
    ) -> str:

        ai = provider_router.provider(
            preferred=provider,
        )

        return ai.generate(
            prompt=prompt,
            system_prompt=system_prompt,
            **kwargs,
        )

    async def stream(
        self,
        prompt: str,
        system_prompt: str | None = None,
        provider: str | None = None,
        **kwargs: Any,
    ):

        ai = provider_router.provider(
            capability="streaming",
            preferred=provider,
        )

        async for chunk in ai.stream(
            prompt=prompt,
            system_prompt=system_prompt,
            **kwargs,
        ):
            yield chunk

    def json(
        self,
        prompt: str,
        system_prompt: str | None = None,
        provider: str | None = None,
    ) -> str:

        ai = provider_router.provider(
            capability="json_mode",
            preferred=provider,
        )

        if hasattr(ai, "generate_json"):
            return ai.generate_json(
                prompt=prompt,
                system_prompt=system_prompt,
            )

        return ai.generate(
            prompt=prompt,
            system_prompt=system_prompt,
        )

    def usage(
        self,
        provider: str | None = None,
    ) -> dict[str, int]:

        try:
            ai = provider_router.provider(
                preferred=provider,
            )
        except Exception:
            return {
                "prompt_tokens": 0,
                "completion_tokens": 0,
                "total_tokens": 0,
            }

        if hasattr(ai, "usage"):
            return ai.usage()

        return {
            "prompt_tokens": 0,
            "completion_tokens": 0,
            "total_tokens": 0,
        }


chat_service = AIService()
