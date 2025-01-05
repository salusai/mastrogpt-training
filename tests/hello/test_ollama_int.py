import os, requests as req
def test_ollama():
    url = os.environ.get("OPSDEV_HOST") + "/api/my/hello/ollama"
    res = req.get(url).json()
    assert res.get("output") == "ollama"
