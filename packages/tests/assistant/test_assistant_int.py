import os, requests as req
def test_assistant():
    url = os.environ.get("OPSDEV_HOST") + "/api/my/assistant/assistant"
    res = req.get(url).json()
    assert res.get("output") == "assistant"
