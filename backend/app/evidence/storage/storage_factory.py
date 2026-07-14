from __future__ import annotations

from typing import TypeAlias

from app.evidence.storage.azure_blob_storage import AzureBlobStorageProvider
from app.evidence.storage.gcs_storage import GCSStorageProvider
from app.evidence.storage.local_storage import LocalStorageProvider
from app.evidence.storage.s3_storage import S3StorageProvider
from app.evidence.storage.storage_provider import StorageProvider

ProviderClass: TypeAlias = (
    type[LocalStorageProvider]
    | type[S3StorageProvider]
    | type[AzureBlobStorageProvider]
    | type[GCSStorageProvider]
)


class StorageFactory:

    _providers: dict[str, ProviderClass] = {
        "local": LocalStorageProvider,
        "s3": S3StorageProvider,
        "azure": AzureBlobStorageProvider,
        "gcs": GCSStorageProvider,
    }

    @classmethod
    def create(
        cls,
        provider: str = "local",
    ) -> StorageProvider:
        return cls._providers[provider]()
