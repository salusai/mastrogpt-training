import os, requests as req
MODEL="llama3.1:8b"
def llm(args):
  host = args.get("OLLAMA_HOST", os.getenv("OLLAMA_HOST"))
  auth = args.get("OLLAMA_TOKEN", os.getenv("AUTH"))
  url =  f"https://{auth}@{host}/api/generate"
  msg = { "model": MODEL, "prompt": args.get("input", "Hello."), "stream": False }
  res = req.post(url, json=msg).json()
  return { "output": res.get("response") }
