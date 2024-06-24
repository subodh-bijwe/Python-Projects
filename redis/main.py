import redis
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
r = redis.Redis(host='localhost', port=6379, decode_responses=True)

from decorators.time_decorator import time_decorator

@time_decorator
def redis_get(key):
    # r.set('foo', 'bar')
    # True
    print(r.get(key))
    
redis_get('foo')