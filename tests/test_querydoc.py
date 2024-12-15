import packages.querydoc.querydoc.querydoc as querydoc
def test_querydoc():
    res = querydoc.querydoc({})
    assert res["output"] == "querydoc"
