from __future__ import annotations
from app.document_processing.embeddings.openai_provider import OpenAIProvider


class NVIDIAProvider(OpenAIProvider):
    @property
    def name(self):
        return "nvidia"
