import sys 
sys.path.append("packages/assistant/assistant")
import assistant

def test_assistant():
    res = assistant.assistant({})
    assert res["output"] == "assistant"
