import os, requests as req
def test_hello():
    url = os.environ.get("OPSDEV_HOST") + "/api/my/hello/hello"
    res = req.get(url).json()
    assert res.get("output") == "hello"
