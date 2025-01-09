import os
import redis
def cache(args):
  
  rd = redis.from_url(args.get("REDIS_URL", os.getenv("REDIS_URL")))
  prefix = args.get("REDIS_PREFIX", os.getenv("REDIS_PREFIX"))
  
  op = args.get("op", "no-op")
  key = f"{prefix}/{args.get("key", "no-key")}"
  value = args.get("value", "no-value")
  res = "no op specified"
  
  if op == "get":
    res = rd.get(key).decode("UTF-8")
  elif op == "set":
    res = "OK" if rd.set(key, value) else "ERR"
  return { "output": res }
