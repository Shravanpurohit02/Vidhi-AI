from __future__ import annotations

import importlib.util

from app.evidence.storage.storage_provider import StorageProvider


class S3StorageProvider(StorageProvider):

    @property
    def name(self):
        return "s3"

    def save(self, source, destination):
        raise NotImplementedError

    def delete(self, path):
        raise NotImplementedError

    def exists(self, path):
        return importlib.util.find_spec("boto3") is not None
