import sys, os 
sys.path.append("packages/hello/cache")

import redis
import cache

def test_cache():    
    res = cache.cache({})
    assert res.get("output") == "no op specified"
    res = cache.cache({"op": "set", "key": "hello", "value": "world"})
    assert res.get("output") == "OK"
    res = cache.cache({"op": "get", "key": "hello"})
    assert res.get("output") == "world"
