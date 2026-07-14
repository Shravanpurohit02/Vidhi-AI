from __future__ import annotations


class VectorStoreService:
    """
    Canonical vector store interface.
    """

    def add(self, *args, **kwargs):
        raise NotImplementedError

    def search(self, *args, **kwargs):
        raise NotImplementedError

    def retrieve(self, *args, **kwargs):
        return self.search(*args, **kwargs)

    def delete(self, *args, **kwargs):
        raise NotImplementedError

    def health(self):
        return True
