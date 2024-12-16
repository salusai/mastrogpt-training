import packages.postgen.postgen.postgen as postgen
def test_postgen():
    res = postgen.postgen({})
    assert "form" in res
    res = postgen.postgen({"input": "What is the capital of Italy?"})
    output = res.get("output")
    assert output
    assert output.find("Roma") != -1
    