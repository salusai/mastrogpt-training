import os, requests as req
def test_llm():
    url = os.environ.get("OPSDEV_HOST") + "/api/my/hello/llm"
    msg = {"input": "what is the capital of italy"}
    res = req.post(url, json=msg).json()
    assert res.get("output").find("Rom") != -1
