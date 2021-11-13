import redis
import os


def redis_init():
    r = redis.Redis(
        host=os.environ.get('REDIS_HOST'),
        port=os.environ.get('REDIS_PORT'),
        password=os.environ.get('REDIS_PASSWORD')
    )
    if not r.get('counter'):
        r.set('counter', '0')
    return r
