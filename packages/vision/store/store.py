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
      out = f"Looking at {ls[0]}, I see:\n"
      vis = vision.Vision(args)
      img = buc.read_b64(ls[0])
      out += vis.decode(img)
    else:
      out = f"Not found '*{inp[1:]}*'"


  return {"output": out}

    
