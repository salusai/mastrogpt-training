import os, requests as req
def test_querydoc():
    url = os.environ.get("OPSDEV_HOST") + "/api/my/querydoc/querydoc"
    res = req.get(url).json()
    assert res.get("output") == "querydoc"
