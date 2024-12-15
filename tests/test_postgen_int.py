import os, requests as req
def test_postgen():
    url = os.environ.get("OPSDEV_HOST") + "/api/my/postgen/postgen"
    res = req.get(url).json()
    assert res.get("output") == "postgen"
