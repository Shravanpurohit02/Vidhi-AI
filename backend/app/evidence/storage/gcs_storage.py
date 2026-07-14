from __future__ import annotations

import importlib.util

from app.evidence.storage.storage_provider import StorageProvider


class GCSStorageProvider(StorageProvider):

    @property
    def name(self):
        return "gcs"

    def save(self, source, destination):
        raise NotImplementedError

    def delete(self, path):
        raise NotImplementedError

    def exists(self, path):
        return importlib.util.find_spec("google.cloud.storage") is not None
