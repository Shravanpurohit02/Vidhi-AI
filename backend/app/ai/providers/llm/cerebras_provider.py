from __future__ import annotations

import os
from openai import OpenAI

from app.ai.providers.base.provider import AIProvider
from app.ai.providers.capabilities import Capability


class CerebrasProvider(AIProvider):

    name="cerebras"

    capabilities={
        Capability.CHAT,
    }

    def __init__(self):

        self.client=OpenAI(
            api_key=os.getenv("CEREBRAS_API_KEY"),
            base_url="https://api.cerebras.ai/v1",
        )

    def health(self):
        return bool(os.getenv("CEREBRAS_API_KEY"))

    def chat(
        self,
        messages,
        model="llama-4-scout-17b-16e-instruct",
        **kwargs,
    ):
        return self.client.chat.completions.create(
            model=model,
            messages=messages,
            **kwargs,
        )
