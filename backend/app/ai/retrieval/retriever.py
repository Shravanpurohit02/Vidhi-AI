from app.ai.chunking.chunker import TextChunker
from app.ai.embeddings.mock import MockEmbeddingProvider
from app.ai.vectorstore.memory import MemoryVectorStore


class Retriever:

    def __init__(self):
        self.chunker = TextChunker()
        self.embedder = MockEmbeddingProvider()
        self.store = MemoryVectorStore()

    def index_document(
        self,
        text: str,
        metadata: dict,
    ):

        chunks = self.chunker.chunk(text)

        for chunk in chunks:

            embedding = self.embedder.embed(chunk)

            self.store.add(
                embedding,
                metadata,
                chunk,
            )

    def retrieve(
        self,
        query: str,
    ):

        embedding = self.embedder.embed(query)

        return self.store.search(embedding)
