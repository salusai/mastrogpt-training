import sys 
sys.path.append("packages/hello/llm")
import llm

def test_llm():
    res = llm.llm({})
    assert res["output"] == "llm"
