import packages.simple.simple.simple as simple
def test_simple():
    res = simple.simple({})
    assert res["output"].startswith("Welcome")
    res = simple.simple({"input": "What is capital of Italy."})
    assert res["output"].find("Rom") != -1
