from app.ai.embeddings.embedding_selector import selector

# Compatibility aliases
ProviderSelector = selector
Selector = selector
selector = selector

__all__ = [
    "ProviderSelector",
    "Selector",
    "selector",
]
