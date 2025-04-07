import json
import vdb
import chat

USAGE = """
Prefixes:
`=<model>`        change the model
`@<collection>`   change the collection
`#<size>`         change the size of the query
`*<query>`        run a vector search
`?`               show usage
Params:
"""

def search(args, collection, limit, text): 
  print("search:", text, "in", collection, "limit", limit)
  db = vdb.VectorDB(args, collection)
  res = db.vector_search(text, limit=limit)
  prompt = ""
  for (w, txt) in res:
    prompt += txt + "\n"
    #print(txt)
  return prompt 

def query(args):
  state = {}
  try: state = json.loads(args.get("state", "{}"))
  except: pass
  print(state)
  model = state.get("model", "llama3.1:8b")
  limit = int(state.get("limit", "30"))
  collection = args.get("collection", "linkedin")

  inp = args.get("input", "")
  out = ""
  prompt = ""
  if inp.startswith("#"):
    try: limit = int(inp[1:])
    except: pass
  elif inp.startswith("@"):
    collection = inp[1:]
  elif inp.startswith("="):
    model = inp[1:]
  elif inp.startswith("*"):
    out = search(args, collection, limit, inp[1:])
  elif not inp in  ["?", ""]:
    info = search(args, collection, limit, inp)
    prompt = f"{inp}.\nUse the following informations:\n{info} "
    out = chat.Chat(args, model).ask(prompt)

  if out == "":
    out = f"{USAGE}model={model}\ncollection={collection}\nlimit={limit}"

  state["model"] = model
  state["limit"] = str(limit)
  state["collection"] = collection
  return { "output": out, "state": json.dumps(state) }
