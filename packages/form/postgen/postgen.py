USAGE = """I will generate a post on Apache OpenServerless post for you! 
Tell me 'post' and I will ask for the required informations."""

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

import os, requests as req
def chat(args, inp):
  host = args.get("OLLAMA_HOST", os.getenv("OLLAMA_HOST"))
  auth = args.get("AUTH", os.getenv("AUTH"))
  url = f"https://{auth}@{host}/api/generate"
  msg = { "model": MODEL, "prompt": inp, "stream": False}
  res = req.post(url, json=msg).json()
  return  res.get("response", "error")
 

def postgen(args):
  print(args)

  res = {}
  inp = args.get("input", "")
  out = USAGE

  print("TYPE", type(inp))

  if type(inp) is dict and "form" in inp:
      data = inp["form"]
      inp = f"""Generate a post promoting Apache OpenServerless.
Your job role is {data['job']}.
The reason because you are Apache OpenServerless is {data['why']}.
The tone of the post should be {data['tone']}.
"""
      out = chat(args, inp)
      for field in data.keys():
        print(data[field])

  elif inp == "post":
    out = "please fill the form"
    res['form'] = FORM
  elif inp != "":
    out = chat(args, inp)

  res['output'] = out
  return res



