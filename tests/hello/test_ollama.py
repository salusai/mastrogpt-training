import sys 
sys.path.append("packages/hello/ollama")
import ollama

def test_ollama():
    res = ollama.ollama({})
    assert res["output"] == "ollama"
