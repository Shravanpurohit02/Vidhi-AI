from __future__ import annotations

from app.document_processing.embeddings.bootstrap import build_registry


def health() -> dict:

    registry = build_registry()

    status = {}

    for name in registry.all():
        provider = registry.get(name)
        status[name] = provider.is_available()

    return status
