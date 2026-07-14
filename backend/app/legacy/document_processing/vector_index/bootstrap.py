from __future__ import annotations

from app.document_processing.vector_index.registry import VectorIndexRegistry

from app.document_processing.vector_index.sqlite_provider import SQLiteProvider
from app.document_processing.vector_index.faiss_provider import FAISSProvider
from app.document_processing.vector_index.chromadb_provider import ChromaDBProvider
from app.document_processing.vector_index.qdrant_provider import QdrantProvider
from app.document_processing.vector_index.lancedb_provider import LanceDBProvider
from app.document_processing.vector_index.milvus_provider import MilvusProvider
from app.document_processing.vector_index.pgvector_provider import PGVectorProvider
from app.document_processing.vector_index.weaviate_provider import WeaviateProvider
from app.document_processing.vector_index.pinecone_provider import PineconeProvider
from app.document_processing.vector_index.elasticsearch_provider import (
    ElasticsearchProvider,
)
from app.document_processing.vector_index.opensearch_provider import OpenSearchProvider


def build_registry():
    registry = VectorIndexRegistry()

    for provider in (
        SQLiteProvider(),
        FAISSProvider(),
        ChromaDBProvider(),
        QdrantProvider(),
        LanceDBProvider(),
        MilvusProvider(),
        PGVectorProvider(),
        WeaviateProvider(),
        PineconeProvider(),
        ElasticsearchProvider(),
        OpenSearchProvider(),
    ):
        registry.register(provider)

    return registry
