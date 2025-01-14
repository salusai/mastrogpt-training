import os, requests as req
def test_vdbquery():
    url = os.environ.get("OPSDEV_HOST") + "/api/my/vdbquery/vdbquery"
    res = req.get(url).json()
    assert res.get("output") == "vdbquery"
