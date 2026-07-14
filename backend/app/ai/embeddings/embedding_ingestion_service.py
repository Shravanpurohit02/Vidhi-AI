from app.ai.embeddings.embedding_selector import selector

class EmbeddingIngestionService:
    """
    Backward-compatible wrapper.
    """
    def __init__(self, provider=None):
        self.provider = selector.select(provider) if provider else selector.select()

    def embed(self, text):
        return self.provider.create(text)

    def create_embedding(self, text):
        return self.embed(text)

    def create_embeddings(self, texts):
        return [self.embed(t) for t in texts]
