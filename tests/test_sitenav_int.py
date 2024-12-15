import os, requests as req
def test_sitenav():
    url = os.environ.get("OPSDEV_HOST") + "/api/my/sitenav/sitenav"
    res = req.get(url).json()
    assert res.get("output") == "sitenav"
