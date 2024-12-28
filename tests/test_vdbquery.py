#%load_ext autoreload
#%autoreload 2
import sys, os
sys.path.append("packages/vdbquery/vdbquery")
import vdbquery

args = {
    "profile": "msciab",
    "input": "List the topics covered in the posts."
}

def test_query():
    name = args.get("profile")
    vdbquery.connect(args)
    
    res = Collection(name).query(expr="", output_fields=["*"], limit=1000)
    assert len(res) > 0
    
def test_search():
    pass
    

def test_vdbquery():
    name = args.get("profile")
    text = args.get("input")
    llm = vdbquery.llm(args)
    res = vdbquery.vdbquery({})
    assert res["output"] == "vdbquery"
