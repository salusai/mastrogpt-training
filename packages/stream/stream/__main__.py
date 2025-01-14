#--kind python:default
#--web true
#--param OLLAMA_HOST $OLLAMA_HOST
#--param OLLAMA_TOKEN $OLLAMA_TOKEN

import stream
def main(args):
  return {"body": stream.stream(args)}
