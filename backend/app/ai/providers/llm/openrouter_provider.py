from __future__ import annotations

import os
from openai import OpenAI

from app.ai.providers.base.provider import AIProvider
from app.ai.providers.capabilities import Capability


class OpenrouterProvider(AIProvider):

    name="openrouter"

    capabilities={
        Capability.CHAT,
    }

    def __init__(self):

        self.client=OpenAI(
            api_key=os.getenv("OPENROUTER_API_KEY"),
            base_url="https://openrouter.ai/api/v1",
        )

    def health(self):
        return bool(os.getenv("OPENROUTER_API_KEY"))

    def chat(
        self,
        messages,
        model="openai/gpt-oss-120b",
        **kwargs,
    ):
        return self.client.chat.completions.create(
            model=model,
            messages=messages,
            **kwargs,
        )
