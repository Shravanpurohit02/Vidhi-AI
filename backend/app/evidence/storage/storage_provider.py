from __future__ import annotations

from abc import ABC, abstractmethod


class StorageProvider(ABC):

    @property
    @abstractmethod
    def name(self) -> str: ...

    @abstractmethod
    def save(
        self,
        source: str,
        destination: str,
    ) -> str: ...

    @abstractmethod
    def delete(
        self,
        path: str,
    ) -> None: ...

    @abstractmethod
    def exists(
        self,
        path: str,
    ) -> bool: ...
