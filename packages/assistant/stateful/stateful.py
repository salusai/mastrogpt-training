import chat
import history

def stateful(args):
  
  hi = history.History(args)
  ch = chat.Chat(args)
  
  inp = args.get("input", "")
  out = f"Hello from {chat.MODEL}"
  res = {}
  
  if inp != "":
    hi.load(ch)
    msg = f"user:{inp}"
    ch.add(msg)
    hi.save(msg)
    print(ch.messages)
    out = ch.complete()
    hi.save(f"assistant:{out}")
    res['state'] = hi.id()

  res['output'] = out
  return res
