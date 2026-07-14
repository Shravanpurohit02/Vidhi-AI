from __future__ import annotations
from app.document_processing.embeddings.openai_provider import OpenAIProvider


class AzureOpenAIProvider(OpenAIProvider):
    @property
    def name(self):
        return "azure_openai"
