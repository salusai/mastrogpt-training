import sys 
sys.path.append("packages/hello/redis")
import redis

def test_redis():
    res = redis.redis({})
    assert res["output"] == "redis"
