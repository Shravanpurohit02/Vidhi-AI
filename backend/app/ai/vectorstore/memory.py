class MemoryVectorStore:

    def __init__(self):
        self.items = []

    def add(
        self,
        embedding,
        metadata,
        text,
    ):
        self.items.append(
            {
                "embedding": embedding,
                "metadata": metadata,
                "text": text,
            }
        )

    def search(
        self,
        embedding,
        top_k=5,
    ):
        return self.items[:top_k]
