from __future__ import annotations

class _Selector:
    def select(self, *args, **kwargs):
        try:
            from app.ai.providers.embeddings.huggingface_provider import HuggingFaceEmbeddingProvider
            return HuggingFaceEmbeddingProvider()
        except Exception:
            class _Fallback:
                def create(self, text: str):
                    raise RuntimeError(
                        "No embedding provider is available. Configure an embedding provider first."
                    )
            return _Fallback()

selector = _Selector()
