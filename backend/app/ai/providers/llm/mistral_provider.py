from __future__ import annotations

import os
from openai import OpenAI

from app.ai.providers.base.provider import AIProvider
from app.ai.providers.capabilities import Capability


class MistralProvider(AIProvider):

    name="mistral"

    capabilities={
        Capability.CHAT,
    }

    def __init__(self):

        self.client=OpenAI(
            api_key=os.getenv("MISTRAL_API_KEY"),
            base_url="https://api.mistral.ai/v1",
        )

    def health(self):
        return bool(os.getenv("MISTRAL_API_KEY"))

    def chat(
        self,
        messages,
        model="mistral-large-latest",
        **kwargs,
    ):
        return self.client.chat.completions.create(
            model=model,
            messages=messages,
            **kwargs,
        )
