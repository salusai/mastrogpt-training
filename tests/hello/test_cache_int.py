import os, requests as req

def test_cache():
    url = os.getenv("OPSDEV_HOST") + "/api/my/hello/cache"
    res = req.get(url).json()
    assert res.get("output") == "no op specified"
    res = req.post(url, json={"op": "set", "key": "hello", "value": "world"}).json()
    assert res.get("output") == "OK"
    res = req.post(url, {"op": "get", "key": "hello"}).json()
    assert res.get("output") == "world"

