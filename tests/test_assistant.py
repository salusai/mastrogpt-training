import sys, os
sys.path.append(os.path.abspath("packages/assistant/assistant"))
import chat
import assistant

args = {
    "REDIS_URL": "redis://localhost:6379",
    "REDIS_PREFIX": "prefix",
    "OLLAMA_HOST": os.getenv("OLLAMA_HOST"),
    "OLLAMA_USERNAME": os.getenv("OLLAMA_USERNAME"),
    "OLLAMA_PASSWORD": os.getenv("OLLAMA_PASSWORD"),
}

def test_chat():
    
    ch = chat.Chat(args)
    assert ch.state() != ""
    assert ch.messages()[0]["role"] == "system"
    
    ch.prompt("user", "Please tell me the capital city the country I ask for.")
    assert ch.messages()[1]["role"] == "user"
    
    message = ch.chat("The country is Italy.")
    assert message.find("Rom") != -1
    
def test_assistant():
    res = assistant.assistant(args)
    assert res["state"] != ""
    assert res["output"].startswith("Welcome")
    args["state"] = res["state"]
    args["input"] = "Please tell me the capital city the country I ask for."
    res = assistant.assistant(args)
    args["input"] = "The country is Italy."
    res = assistant.assistant(args)
    assert res["output"].find("Rom") != -1
