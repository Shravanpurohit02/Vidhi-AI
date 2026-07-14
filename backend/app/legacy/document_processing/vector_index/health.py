from __future__ import annotations

from app.document_processing.vector_index.bootstrap import build_registry


def health():
    registry = build_registry()
    return {name: registry.get(name).is_available() for name in registry.all()}
