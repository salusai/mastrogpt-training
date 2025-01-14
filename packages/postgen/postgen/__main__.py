#--kind python:default
#--web true
#--param OLLAMA_HOST $OLLAMA_HOST
#--param OLLAMA_TOKEN $AUTH
import postgen
def main(args):
  #print(args)
  return {"body": postgen.postgen(args)}
