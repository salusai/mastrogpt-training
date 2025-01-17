import os, ollama

FORM = [
  {
      "name": "why",
      "label": "Why do you recommend Apache OpenServerless?",
      "type": "textarea",
      "required": "true"
  },
  {
    "name": "job",
    "label": "What is your job role?",
    "type": "text",
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
  
  prompt = ""
  
  if "why" in args:
    prompt += "Generate a post about Apache OpenServeless. "
    prompt += f"The reason because you like it is: {args['why']}. "
    if "job" in args:
      prompt += f"Your job role is: f{args['job']} "
    if "tone" in args:
      prompt += f"The tone of the post should be: f{args['tone']}"
  else:
    prompt = args.get("input", "")
  
  if prompt == "":
    return { "output": "Welcome to the Apache OpenServerless post generator.", "form": FORM }

  client = connect(args)
  gen = client.generate(model=MODEL, prompt=prompt)
  res = gen.get("response", "Sorry there an error.")
  #print(res)
  return { "output": res }
  
    
