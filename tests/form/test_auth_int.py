import os, requests as req
def test_auth():
    url = os.environ.get("OPSDEV_HOST") + "/api/my/form/auth"
    res = req.get(url).json()
    assert res.get("output") == "auth"
