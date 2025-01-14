import os, requests as req
def test_vdbimport():
    url = os.environ.get("OPSDEV_HOST") + "/api/my/vdbimport/vdbimport"
    res = req.get(url).json()
    assert res.get("output") == "vdbimport"
