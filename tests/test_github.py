import packages.github.github.github as github
def test_github():
    res = github.github({})
    assert res["output"] == "github"
