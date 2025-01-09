import sys 
sys.path.append("packages/hello/llm")
import llm

def test_llm():
    msg = {"input": "what is the capital of italy"}
    res = llm.llm(msg)
    assert  res.get("output").find("Rom") != -1
