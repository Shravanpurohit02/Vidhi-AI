from __future__ import annotations

import os
import time
from collections.abc import AsyncIterator
from typing import Any, cast

from openai import OpenAI

from app.ai.interfaces.base_provider import BaseAIProvider


class OpenAICompatibleProvider(BaseAIProvider):

    def __init__(
        self,
        name: str,
        api_key_env: str,
        base_url_env: str,
        model_env: str,
        default_base_url: str,
        default_model: str,
    ):
        self._name = name
        self.api_key = os.getenv(api_key_env, "")
        self.base_url = os.getenv(base_url_env, default_base_url)
        self._model = os.getenv(model_env, default_model)
        self._last_usage: dict[str, int] = {
            "prompt_tokens": 0,
            "completion_tokens": 0,
            "total_tokens": 0,
        }

    @property
    def name(self) -> str:
        return self._name

    @property
    def model(self) -> str:
        return self._model

    def health(self) -> bool:
        return bool(self.api_key)

    def _client(self) -> OpenAI:
        if not self.api_key:
            raise RuntimeError(f"{self._name} API key not configured.")

        return OpenAI(
            api_key=self.api_key,
            base_url=self.base_url,
            timeout=float(os.getenv("REQUEST_TIMEOUT", "60")),
        )

    def _messages(
        self,
        prompt: str,
        system_prompt: str | None,
    ) -> list[dict[str, str]]:
        messages: list[dict[str, str]] = []

        if system_prompt:
            messages.append(
                {
                    "role": "system",
                    "content": system_prompt,
                }
            )

        messages.append(
            {
                "role": "user",
                "content": prompt,
            }
        )

        return messages

    def chat(
        self,
        messages: list[dict[str, str]],
        **kwargs: Any,
    ) -> str:

        retries = int(os.getenv("MAX_PROVIDER_RETRIES", "3"))

        for attempt in range(retries):

            try:

                response = self._client().chat.completions.create(
                    model=kwargs.get("model", self.model),
                    messages=cast(Any, messages),
                    temperature=kwargs.get("temperature", 0.2),
                    top_p=kwargs.get("top_p", 1.0),
                    max_tokens=kwargs.get("max_tokens"),
                )

                usage = getattr(response, "usage", None)

                if usage:
                    self._last_usage = {
                        "prompt_tokens": getattr(usage, "prompt_tokens", 0),
                        "completion_tokens": getattr(usage, "completion_tokens", 0),
                        "total_tokens": getattr(usage, "total_tokens", 0),
                    }

                return response.choices[0].message.content or ""

            except Exception:

                if attempt == retries - 1:
                    raise

                time.sleep(2**attempt)

        raise RuntimeError("Unreachable")

    def generate(
        self,
        prompt: str,
        system_prompt: str | None = None,
        **kwargs: Any,
    ) -> str:

        retries = int(os.getenv("MAX_PROVIDER_RETRIES", "3"))

        for attempt in range(retries):

            try:

                response = self._client().chat.completions.create(
                    model=kwargs.get("model", self.model),
                    messages=cast(Any, self._messages(prompt, system_prompt)),
                    temperature=kwargs.get("temperature", 0.2),
                    max_tokens=kwargs.get("max_tokens"),
                    top_p=kwargs.get("top_p", 1.0),
                )

                usage = getattr(response, "usage", None)

                if usage:
                    self._last_usage = {
                        "prompt_tokens": getattr(usage, "prompt_tokens", 0),
                        "completion_tokens": getattr(usage, "completion_tokens", 0),
                        "total_tokens": getattr(usage, "total_tokens", 0),
                    }

                return response.choices[0].message.content or ""

            except Exception:

                if attempt == retries - 1:
                    raise

                time.sleep(2**attempt)

        raise RuntimeError("Unreachable")

    async def stream(
        self,
        prompt: str,
        system_prompt: str | None = None,
        **kwargs: Any,
    ) -> AsyncIterator[str]:

        stream = self._client().chat.completions.create(
            model=kwargs.get("model", self.model),
            messages=cast(Any, self._messages(prompt, system_prompt)),
            temperature=kwargs.get("temperature", 0.2),
            max_tokens=kwargs.get("max_tokens"),
            top_p=kwargs.get("top_p", 1.0),
            stream=True,
        )

        for chunk in cast(Any, stream):
            delta = chunk.choices[0].delta.content
            if delta:
                yield delta

    def embed(
        self,
        text: str,
        model: str | None = None,
    ) -> list[float]:

        client = self._client()

        response = client.embeddings.create(
            model=model or self.model,
            input=text,
        )

        return response.data[0].embedding

    def generate_json(
        self,
        prompt: str,
        system_prompt: str | None = None,
        **kwargs: Any,
    ) -> str:

        response = self._client().chat.completions.create(
            model=kwargs.get("model", self.model),
            messages=cast(Any, self._messages(prompt, system_prompt)),
            response_format=cast(Any, {"type": "json_object"}),
            temperature=0,
        )

        return response.choices[0].message.content or ""

    def usage(self) -> dict[str, int]:
        """
        Returns token usage from the last completed request.
        """
        return dict(self._last_usage)
