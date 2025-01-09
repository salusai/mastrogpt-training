import os, requests as req
def test_llm():
    url = os.environ.get("OPSDEV_HOST") + "/api/my/hello/llm"
    res = req.get(url).json()
    assert res.get("output") == "llm"
