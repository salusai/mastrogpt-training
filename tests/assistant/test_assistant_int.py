import os, requests as req
def test_assistant():
    url = os.environ.get("OPSDEV_HOST") + "/api/my/assistant/assistant"
    res = req.get(url).json()
    assert res.get("output").startswith("Welcome")
    inp = "I tell you the country and you tell me the capital."
    res = req.post(url, json={"input": inp, "state": res.get("state")}).json()
    assert res.get("output") != ""
    inp = "Italy"
    res = req.post(url, json={"input": inp, "state": res.get("state")}).json()
    assert res.get("output").find("Rom")
    
    
