from __future__ import annotations

import importlib.util

from app.evidence.storage.storage_provider import StorageProvider


class AzureBlobStorageProvider(StorageProvider):

    @property
    def name(self):
        return "azure"

    def save(self, source, destination):
        raise NotImplementedError

    def delete(self, path):
        raise NotImplementedError

    def exists(self, path):
        return importlib.util.find_spec("azure.storage.blob") is not None
