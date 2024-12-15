import os, requests as req
def test_imgen():
    url = os.environ.get("OPSDEV_HOST") + "/api/my/imgen/imgen"
    res = req.get(url).json()
    assert res.get("output") == "imgen"
