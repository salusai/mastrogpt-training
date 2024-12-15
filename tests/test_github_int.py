import os, requests as req
def test_github():
    url = os.environ.get("OPSDEV_HOST") + "/api/my/github/github"
    res = req.get(url).json()
    assert res.get("output") == "github"
