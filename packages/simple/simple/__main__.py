#--kind python:default
#--web true
#--param OLLAMA_HOST $OLLAMA_HOST
#--param OLLAMA_USERNAME $OLLAMA_USERNAME
#--param OLLAMA_PASSWORD $OLLAMA_PASSWORD

import simple
def main(args):
  return {"body": simple.simple(args)}
