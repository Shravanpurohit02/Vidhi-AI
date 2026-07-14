from __future__ import annotations

from abc import ABC, abstractmethod

from app.ai.providers.http.client import HTTPClient


class HTTPProvider(ABC):

    def __init__(self):
        self.http = HTTPClient()

    @abstractmethod
    async def health(self):
        ...

    @abstractmethod
    async def chat(self,*args,**kwargs):
        ...
