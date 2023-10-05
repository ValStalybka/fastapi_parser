import functools
import json
from typing import Callable
from typing import Union

from bson import json_util

from src.infrastructure.dao.redis import redis_cache


def cache_result(name: Union[str, Callable]) -> Callable:
    """decorator for caching with redis, takes 1 argument:
    name: str - name of key stored in redis"""

    def inner(func):
        @functools.wraps(func)
        def wrap(*args, **kwargs):
            if (cache := redis_cache.get(name)) is not None:
                return json.loads(cache, object_hook=json_util.object_hook)

            else:
                data = func(*args, **kwargs)
                json_data = json.dumps(data, default=json_util.default)
                redis_cache.set(name=name, value=json_data, ex=1000)
                return data

        return wrap

    return inner
