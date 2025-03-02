import bucket
import vision

USAGE = """
Usage:
  *<substring>      list files with <subtring> in path
  !<prefix>         remove files starting with <prefix>
  @<substring>      decode files with this <substring>
  ?                 this message
"""

def store(args):
  res = {}
  out = USAGE
  inp = args.get("input", "")
  buc = bucket.Bucket(args)

  if inp.startswith("*"):
    ls = buc.find(inp[1:])
    out = "Found:\n"
    for item in ls:
      out += f"- {item}\n"
  elif inp.startswith("!"):
    count = buc.remove(inp[1:])
    out = f"Removed {count} files"

  elif inp.startswith("@"):
    ls = buc.find(inp[1:])
    if len(ls) > 0:
      key = ls[0]
      out = f"Looking at {key}, I see:\n"
      img = buc.read_b64(key)
      vis = vision.Vision(args)
      out += vis.decode(img)
      url = buc.url(key, 3600)
      res['html'] = f"<img src='{url}'>"
      print(url)
    else:
      out = f"Not found '*{inp[1:]}*'"

  res['output'] = out
  return res

    
