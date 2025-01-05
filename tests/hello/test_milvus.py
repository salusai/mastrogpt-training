import sys 
sys.path.append("packages/hello/milvus")
import milvus

def test_milvus():
    res = milvus.milvus({})
    assert res["output"] == "milvus"
