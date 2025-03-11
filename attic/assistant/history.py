import redis
import uuid
import openai
import json
import os
from urllib.parse import urlparse, urlunparse

ROLE = "You are an helpful assistant."
MODEL = "llama3.1:8b"

class History:
  cache = None
  queue = None
  client = None

  # connect to redis and setup a queue with expiry date of one day
  def __init__(self, args):
    prefix = args.get("REDIS_PREFIX", os.getenv("REDIS_PREFIX"))
    redis_url = args.get("REDIS_URL", os.getenv("REDIS_URL"))
    self.cache = redis.from_url(redis_url)
    self.queue = args.get("state")
    
    if self.queue is None:
      self.queue = prefix+"assistant:"+str(uuid.uuid4())
      self.cache.expire(self.queue, 86400)
      self.prompt("system", ROLE)
    
    base_url = None
    api_key = None
      
    host = args.get("OLLAMA_HOST", os.getenv("OLLAMA_HOST"))
    api_key = args.get("AUTH", os.getenv("AUTH"))
    base_url = f"https://{api_key}@{host}/v1"
    
    self.client = openai.OpenAI(
      base_url = base_url,
      api_key = api_key,
    )

  # push in redis an entry  - assumes redis and quue has been initialized
  def prompt(self, role, content):
      entry = { "role": role, "content": content }
      self.cache.rpush(self.queue, json.dumps(entry))
      
  def messages(self):
    content = [ json.loads(item.decode('UTF-8')) for item in self.cache.lrange(self.queue, 0, -1)]
    return content
  
  def state(self):
    return self.queue

  # chat with the llm
  # return the answr from the llm
  def chat(self, text):
    self.prompt("user", text)
    res = self.client.chat.completions.create(
      model=MODEL,
      messages= self.messages(),
    )
    message = res.choices[0].message.content
    self.prompt("assistant", message)
    return message
  