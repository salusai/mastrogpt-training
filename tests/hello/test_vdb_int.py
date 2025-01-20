import os, requests as req
def test_vdb_int():
    vdb = os.environ.get("OPSDEV_HOST") + "/api/my/hello/vdb"
    
    args = {"drop_collection": "test"}
    res = req.post(vdb, json=args).json()
    assert res.get("output").startswith("Start with '*'")
    

    args = {"input": "Hello, world."}
    res = req.post(vdb, json=args).json()
    args = {"input": "Hello again, world."}
    req.post(vdb, json=args).json()
    args = {"input": "We are on earth."}
    req.post(vdb, json=args).json()

    args = {"input": "*world"}
    res = req.post(vdb, json=args).json()
    assert res.get("output").count("world") >= 2
    
    
    args = {"input": "!world"}
    req.post(vdb, json=args).json()

    args = {"input": "*world"}
    res = req.post(vdb, json=args).json()
    assert res.get("output").count("world") == 0
    
    