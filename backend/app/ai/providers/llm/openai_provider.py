from __future__ import annotations

import os

from openai import OpenAI

from app.ai.providers.base.provider import AIProvider
from app.ai.providers.capabilities import Capability


class OpenAIProvider(AIProvider):

    name = "openai"

    priority = 2

    capabilities = {
        Capability.CHAT,
        Capability.EMBEDDING,
    }

    def __init__(self):

        self.client = OpenAI(
            api_key=os.getenv("OPENAI_API_KEY"),
        )

    def health(self) -> bool:
        return bool(os.getenv("OPENAI_API_KEY"))

    def chat(
        self,
        messages,
        model="gpt-5",
        **kwargs,
    ):
        return self.client.chat.completions.create(
            model=model,
            messages=messages,
            **kwargs,
        )

    def embed(
        self,
        text,
        model="text-embedding-3-large",
    ):
        return self.client.embeddings.create(
            model=model,
            input=text,
        )
