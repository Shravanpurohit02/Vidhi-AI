from __future__ import annotations

import os

from huggingface_hub import InferenceClient

from app.ai.providers.base.provider import AIProvider
from app.ai.providers.capabilities import Capability


class HuggingFaceProvider(AIProvider):

    name="huggingface"

    capabilities={
        Capability.EMBEDDING,
        Capability.RERANK,
        Capability.VISION,
    }

    def __init__(self):

        self.client=InferenceClient(
            api_key=os.getenv("HUGGINGFACE_API_KEY"),
        )

    def health(self):
        return bool(os.getenv("HUGGINGFACE_API_KEY"))
