import sys 
sys.path.append("packages/form/postgen")
import postgen

def test_postgen():
    res = postgen.postgen({})
    assert res["output"] == "postgen"
