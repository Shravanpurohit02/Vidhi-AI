from __future__ import annotations

from functools import wraps

from app.ai.cache.cache_manager import CacheManager

_cache=CacheManager()

def cached(ttl:int=3600):

    def wrapper(fn):

        @wraps(fn)
        def inner(*args,**kwargs):

            key=str((fn.__name__,args,sorted(kwargs.items())))

            value=_cache.get(key)

            if value is not None:
                return value

            value=fn(*args,**kwargs)

            _cache.set(
                key,
                value,
                ttl,
            )

            return value

        return inner

    return wrapper
