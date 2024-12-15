import packages.imgen.imgen.imgen as imgen
def test_imgen():
    res = imgen.imgen({})
    assert res["output"] == "imgen"
