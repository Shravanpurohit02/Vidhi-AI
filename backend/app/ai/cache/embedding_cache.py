import hashlib


class EmbeddingCache:

    def __init__(self):
        self.cache = {}

    def _key(self, text: str):
        return hashlib.sha256(
            text.encode("utf-8")
        ).hexdigest()

    def get(self, text: str):
        return self.cache.get(self._key(text))

    def put(self, text: str, embedding):
        self.cache[self._key(text)] = embedding
