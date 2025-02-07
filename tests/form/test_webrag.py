import sys 
sys.path.append("packages/form/webrag")
import webrag

def test_webrag():
    res = webrag.webrag({})
    assert res["output"] == "webrag"
