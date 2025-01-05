import os, requests as req
def test_simple():
    url = os.environ.get("OPSDEV_HOST") + "/api/my/simple/simple"
    res = req.get(url).json()
    assert res["output"].startswith("Welcome")
    res = req.post(url, {"input": "What is capital of Italy."}).json()
    assert res["output"].find("Rom") != -1
