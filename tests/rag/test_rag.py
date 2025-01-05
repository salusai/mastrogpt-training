import sys 
sys.path.append("packages/rag/rag")
import rag

def test_rag():
    res = rag.rag({})
    assert res["output"] == "rag"
