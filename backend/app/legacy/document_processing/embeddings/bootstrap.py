from __future__ import annotations

from app.document_processing.embeddings.registry import EmbeddingRegistry

from app.document_processing.embeddings.mock_provider import MockProvider
from app.document_processing.embeddings.ollama_provider import OllamaProvider
from app.document_processing.embeddings.openai_provider import OpenAIProvider
from app.document_processing.embeddings.openrouter_provider import OpenRouterProvider
from app.document_processing.embeddings.gemini_provider import GeminiProvider
from app.document_processing.embeddings.huggingface_provider import HuggingFaceProvider
from app.document_processing.embeddings.sentence_transformers_provider import (
    SentenceTransformersProvider,
)
from app.document_processing.embeddings.cohere_provider import CohereProvider
from app.document_processing.embeddings.jina_provider import JinaProvider
from app.document_processing.embeddings.voyage_provider import VoyageProvider
from app.document_processing.embeddings.mistral_provider import (
    MistralEmbeddingProvider,
)
from app.document_processing.embeddings.cerebras_provider import CerebrasProvider
from app.document_processing.embeddings.together_provider import TogetherProvider
from app.document_processing.embeddings.fireworks_provider import FireworksProvider
from app.document_processing.embeddings.deepinfra_provider import DeepInfraProvider
from app.document_processing.embeddings.azure_openai_provider import (
    AzureOpenAIProvider,
)
from app.document_processing.embeddings.aws_bedrock_provider import (
    AWSBedrockProvider,
)
from app.document_processing.embeddings.nvidia_provider import NVIDIAProvider


def build_registry() -> EmbeddingRegistry:
    registry = EmbeddingRegistry()

    providers = [
        MockProvider(),
        OllamaProvider(),
        HuggingFaceProvider(),
        SentenceTransformersProvider(),
        OpenAIProvider(),
        OpenRouterProvider(),
        GeminiProvider(),
        CohereProvider(),
        JinaProvider(),
        VoyageProvider(),
        MistralEmbeddingProvider(),
        CerebrasProvider(),
        TogetherProvider(),
        FireworksProvider(),
        DeepInfraProvider(),
        AzureOpenAIProvider(),
        AWSBedrockProvider(),
        NVIDIAProvider(),
    ]

    for provider in providers:
        registry.register(provider)

    return registry
