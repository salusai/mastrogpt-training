import sys
sys.path.append("packages/hello/vdb")
import vdb

def test_vdb():
    vdb.vdb_init({"drop_collection": vdb.COLLECTION})
    args = {}
    db = vdb.vdb_init({})
    res = vdb.vdb({})
    assert res.get("output", "").startswith("Start with '*'")
    inp = "This is a test."
    assert vdb.vdb({"input": inp}).get("output", "").startswith("OK:")
    inp = "I want to verify if it works."
    assert vdb.vdb({"input": inp}).get("output", "").startswith("OK:")
    inp = "More text to search."
    assert vdb.vdb({"input": inp}).get("output", "").startswith("OK:")
    inp = "This is another test."
    assert vdb.vdb({"input": inp}).get("output", "").startswith("OK:")
    
    inp = "*"
    assert vdb.vdb({"input": inp}).get("output") == 'Please specify a not empty search string.'
    inp = "!"
    assert vdb.vdb({"input": inp}).get("output") == 'Please specify a not empty delete substring.'
     
    inp = "*test"
    assert vdb.vdb({"input": inp}).get("output").count("test") == 2
    
    inp = "*works"
    assert vdb.vdb({"input": inp}).get("output").count('works') == 1
    
    inp = "*missing"
    assert vdb.vdb({"input": inp}).get("output").count("missing") == 0
    
    inp = "!test"
    out = vdb.vdb({"input": inp}).get("output")
    assert out.find("Deleted: 2")!=-1
      

    inp = "*works"
    assert vdb.vdb({"input": inp}).get("output").count("works") == 1
    
    inp = "*test"
    assert vdb.vdb({"input": inp}).get("output").count("test") == 0
