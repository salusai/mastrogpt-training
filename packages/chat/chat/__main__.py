#--kind python:default
#--web true
#--param OLLAMA_HOST $OLLAMA_HOST
#--param OLLAMA_USERNAME $OLLAMA_USERNAME
#--param OLLAMA_PASSWORD $OLLAMA_PASSWORD

import chat
def main(args):
  return {"body": chat.chat(args)}
