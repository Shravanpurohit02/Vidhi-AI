from __future__ import annotations

import os

from groq import Groq

from app.ai.providers.base.provider import AIProvider
from app.ai.providers.capabilities import Capability


class GroqProvider(AIProvider):

    name="groq"
    priority=5

    capabilities={
        Capability.CHAT,
    }

    def __init__(self):
        self.client=Groq(
            api_key=os.getenv("GROQ_API_KEY"),
        )

    def health(self):
        return bool(os.getenv("GROQ_API_KEY"))

    def chat(
        self,
        messages,
        model="llama-3.3-70b-versatile",
        **kwargs,
    ):
        return self.client.chat.completions.create(
            model=model,
            messages=messages,
            **kwargs,
        )
