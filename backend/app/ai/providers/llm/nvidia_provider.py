from __future__ import annotations

import os

from openai import OpenAI

from app.ai.providers.base.provider import AIProvider
from app.ai.providers.capabilities import Capability


class NVIDIAProvider(AIProvider):

    name = "nvidia"

    priority = 1

    capabilities = {
        Capability.CHAT,
        Capability.EMBEDDING,
    }

    def __init__(self):

        self.client = OpenAI(
            api_key=os.getenv("NVIDIA_API_KEY"),
            base_url="https://integrate.api.nvidia.com/v1",
        )

    def health(self) -> bool:
        return bool(os.getenv("NVIDIA_API_KEY"))

    def chat(
        self,
        messages,
        model="meta/llama-3.3-70b-instruct",
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
        model="nvidia/nv-embedqa-e5-v5",
    ):
        return self.client.embeddings.create(
            model=model,
            input=text,
        )
