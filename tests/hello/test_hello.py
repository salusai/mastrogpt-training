import sys 
sys.path.append("packages/hello/hello")
import hello

def test_hello():
    res = hello.hello({})
    assert res["output"] == "hello"
