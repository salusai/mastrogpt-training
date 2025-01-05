import sys, os
sys.path.append(os.path.abspath("packages/stream/stream"))

import stream

def test_stream():
    res = stream.stream({})
    assert res["output"].startswith("Welcome")
    res = stream.stream({"input": "What is capital of Italy."})
    assert res["output"].find("Rom") != -1
