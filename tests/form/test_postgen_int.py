import os, requests as req
def test_postgen():
    url = os.environ.get("OPSDEV_HOST") + "/api/my/form/postgen"
    res = req.get(url).json()
    assert res.get("output") == "postgen"
