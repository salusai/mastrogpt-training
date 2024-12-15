import packages.sitenav.sitenav.sitenav as sitenav
def test_sitenav():
    res = sitenav.sitenav({})
    assert res["output"] == "sitenav"
