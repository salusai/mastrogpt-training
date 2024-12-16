import os, requests as req
def test_postgen():
    url = os.environ.get("OPSDEV_HOST") + "/api/my/postgen/postgen"
    res = req.get(url).json()
    assert "form" in res
    args = {"input": "What is the capital of Italy?"}
    res = req.post(url, json=args).json()
    assert res.get("output").find("Rom") != -1
