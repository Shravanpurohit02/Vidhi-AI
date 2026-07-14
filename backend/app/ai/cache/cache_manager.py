from __future__ import annotations

import time

class CacheManager:

    def __init__(self):
        self.store={}

    def get(self,key):

        item=self.store.get(key)

        if item is None:
            return None

        value,expires=item

        if expires and expires<time.time():
            self.store.pop(key,None)
            return None

        return value

    def set(
        self,
        key,
        value,
        ttl:int=3600,
    ):

        self.store[key]=(
            value,
            time.time()+ttl if ttl else None,
        )

    def delete(self,key):
        self.store.pop(key,None)

    def clear(self):
        self.store.clear()
