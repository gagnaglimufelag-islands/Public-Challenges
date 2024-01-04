import re
import base64
import pickle

from cachelib import MemcachedCache as CachelibMemcachedCache
from flask_caching.backends.base import BaseCache

_test_memcached_key = re.compile(r"[^\x00-\x21\xff]{1,250}$").match


class FastCache(BaseCache, CachelibMemcachedCache):
    def __init__(self, servers=None, default_timeout=300, key_prefix=None):
        BaseCache.__init__(self, default_timeout=default_timeout)
        CachelibMemcachedCache.__init__(
            self,
            servers=servers,
            default_timeout=default_timeout,
            key_prefix=key_prefix,
        )

    @classmethod
    def factory(cls, app, config, args, kwargs):
        args.append(config["CACHE_MEMCACHED_SERVERS"])
        kwargs.update(dict(key_prefix=config["CACHE_KEY_PREFIX"]))
        return cls(*args, **kwargs)

    def set(self, key, value, timeout=None):
        value = base64.b64encode(pickle.dumps(value))
        return super().set(key, value, timeout=timeout)

    def get(self, key):
        value = super().get(key)
        if value:
            return pickle.loads(base64.b64decode(super().get(key)))
        return None

    def delete_many(self, *keys):
        new_keys = []
        for key in keys:
            key = self._normalize_key(key)
            if _test_memcached_key(key):
                new_keys.append(key)
        return self._client.delete_multi(new_keys)

    def inc(self, key, delta=1):
        key = self._normalize_key(key)
        return self._client.incr(key, delta)

    def dec(self, key, delta=1):
        key = self._normalize_key(key)
        return self._client.decr(key, delta)
