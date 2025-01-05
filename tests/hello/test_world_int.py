import os, requests as req
def test_world():
    url = os.environ.get("OPSDEV_HOST") + "/api/my/hello/world"
    res = req.get(url).json()
    assert res.get("output") == "world"
