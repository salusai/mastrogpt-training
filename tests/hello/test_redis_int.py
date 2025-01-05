import os, requests as req
def test_redis():
    url = os.environ.get("OPSDEV_HOST") + "/api/my/hello/redis"
    res = req.get(url).json()
    assert res.get("output") == "redis"
