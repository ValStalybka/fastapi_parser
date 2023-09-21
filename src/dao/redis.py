from redis import Redis

from src.config import Settings


redis_cache = Redis(
    host=Settings().redis.host,
    port=Settings().redis.port,
    db=Settings().redis.db,
)
