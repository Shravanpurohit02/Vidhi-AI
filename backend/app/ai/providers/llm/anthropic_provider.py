from __future__ import annotations

import os
import anthropic

from app.ai.providers.base.provider import AIProvider
from app.ai.providers.capabilities import Capability


class AnthropicProvider(AIProvider):

    name="anthropic"
    priority=4

    capabilities={
        Capability.CHAT,
    }

    def __init__(self):
        self.client=anthropic.Anthropic(
            api_key=os.getenv("ANTHROPIC_API_KEY"),
        )

    def health(self):
        return bool(os.getenv("ANTHROPIC_API_KEY"))

    def chat(self,messages,model="claude-sonnet-4",**kwargs):
        return self.client.messages.create(
            model=model,
            messages=messages,
            **kwargs,
        )
