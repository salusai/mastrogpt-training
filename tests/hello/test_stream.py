import sys 
sys.path.append("packages/hello/stream")
import stream

def test_stream():
    res = stream.stream({})
    assert res["output"] == "stream"
