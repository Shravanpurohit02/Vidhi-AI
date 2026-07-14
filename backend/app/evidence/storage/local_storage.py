from __future__ import annotations

import os
import shutil

from app.evidence.storage.storage_provider import StorageProvider


class LocalStorageProvider(StorageProvider):

    @property
    def name(self) -> str:
        return "local"

    def save(self, source: str, destination: str) -> str:
        os.makedirs(os.path.dirname(destination), exist_ok=True)
        shutil.copy2(source, destination)
        return destination

    def delete(self, path: str) -> None:
        if os.path.exists(path):
            os.remove(path)

    def exists(self, path: str) -> bool:
        return os.path.exists(path)
