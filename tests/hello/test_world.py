import sys 
sys.path.append("packages/hello/world")
import world

def test_world():
    res = world.world({})
    assert res["output"] == "world"
