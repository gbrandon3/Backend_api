import os
import redis

class RedisCache:
    redis_host = os.environ.get('REDISHOST', '')
    redis_port = int(os.environ.get('REDISPORT', 0))
    redis_client = redis.Redis(host=redis_host, port=redis_port)

    def getKey(self, key):
        return str(self.redis_client.get(key).decode('utf-8'))

