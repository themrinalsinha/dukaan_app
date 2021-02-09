from typing import List

from django.conf import settings
from redis import Redis


class RedisStore:
    def __init__(self, url=None) -> None:
        self.connection_url = url or settings.REDIS_CONNECTION_STRING
        self.connection = Redis.from_url(self.connection_url)

    def add_to_cart(self, key: str, value: str) -> int:
        return self.connection.rpush(key, value)

    def get_cart(self, key, remove=False) -> List:
        values = self.connection.lrange(key, 0, -1)
        if remove:
            self.connection.delete(key)
        return values

    def remove_from_cart(self, key: str, value: int, count: int=1) -> None:
        return self.connection.lrem(key, count, value)
