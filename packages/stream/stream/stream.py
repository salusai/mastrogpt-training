import os, ollama

MODEL = "llama3.1:8b"
client = None

def connect(args):
  global client
  if client is None:
    host = args.get("OLLAMA_HOST", os.environ.get("OLLAMA_HOST"))
    username = args.get("OLLAMA_USERNAME", os.environ.get("OLLAMA_USERNAME"))
    password = args.get("OLLAMA_PASSWORD", os.environ.get("OLLAMA_PASSWORD"))
    auth = (username, password)
    #print(host, auth)
    client = ollama.Client(host, auth=auth)
  return client

def stream(args):
  text = args.get("input", "")
  model = args.get("model", MODEL)
  if text == "":
    return { "output": f"Welcome to {model}" }
  client = connect(args)
  
  gen = client.generate(model=model, prompt=text, stream=True)
  res = ""
  for chunk in gen:
    print(chunk)
    if "response" in chunk:
      res += chunk["response"]
  return { "output": res }
