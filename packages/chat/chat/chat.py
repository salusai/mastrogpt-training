import os, ollama

MODEL = "llama3.1:8b"
client = None

def connect(args):
  global client
  if client is None:
    host = f"https://{args.get("OLLAMA_HOST", os.environ.get("OLLAMA_HOST"))}"
    token = args.get("OLLAMA_TOKEN", os.environ.get("AUTH"))
    auth = (token.split(":")[0], token.split(":")[1])
    client = ollama.Client(host, auth=auth)
  return client

def chat(args):
  text = args.get("input", "")
  model = args.get("model", MODEL)
  if text == "":
    return { "output": f"Welcome to {model}" }
  client = connect(args)
  gen = client.generate(model=model, prompt=text)
  res = gen.get("response", "Sorry there an error.")
  #print(res)
  return { "output": res }
