import packages.postgen.postgen.postgen as postgen
def test_postgen():
    res = postgen.postgen({})
    assert res["output"] == "postgen"
