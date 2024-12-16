import os, ollama

FORM = [
  {
    "name": "form",
    "label": "What is your job role?",
    "type": "text",
    "required": "true"
  },
  {
      "name": "why",
      "label": "Why do you recommend Apache OpenServerless?",
      "type": "textarea",
      "required": "true"
  },
  {
      "name": "tone",
      "label": "What tone should the post have?",
      "type": "text",
      "required": "true"
  }
]

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

def postgen(args):
  inp = args.get("input", "")
  if inp == "":
    return { "form": FORM }
  client = connect(args)
  gen = client.generate(model=MODEL, prompt=inp)
  res = gen.get("response", "Sorry there an error.")
  #print(res)
  return { "output": res }
  
    
