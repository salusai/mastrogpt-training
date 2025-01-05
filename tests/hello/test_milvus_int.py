import os, requests as req
def test_milvus():
    url = os.environ.get("OPSDEV_HOST") + "/api/my/hello/milvus"
    res = req.get(url).json()
    assert res.get("output") == "milvus"
