import os, requests as req
def test_vdb():
    llm = os.environ.get("OPSDEV_HOST") + "/api/my/hello/vdb"
    args = {"drop_collection": "test"}
    res = req.post(llm, json=args).json()
    
    assert res.get("output").startswith("Start with '*'")
    
    
    args = {"input": "This is a test."}
    res = req.post(llm, json=args).json()
    
    
    args = {"input": "This is another test."}
    req.post(llm, json=args).json()
    
    args = {"input": "Checking if it works."}
    req.post(llm, json=args).json()

    args = {"input": "*test"}
    res = req.post(llm, json=args).json()
    assert res.get("output").count("test") == 2
    
    
    args = {"input": "!test"}
    req.post(llm, json=args).json()

    args = {"input": "*test"}
    res = req.post(llm, json=args).json()
    assert res.get("output").count("test") == 0
    
    