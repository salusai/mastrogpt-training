#--kind python:default
#--web true
#--kind python:default
#--param OLLAMA_HOST $OLLAMA_HOST
#--param OLLAMA_USERNAME $OLLAMA_USERNAME
#--param OLLAMA_PASSWORD $OLLAMA_PASSWORD
#--param MILVUS_HOST $MILVUS_HOST
#--param MILVUS_PORT $MILVUS_PORT
#--param MILVUS_TOKEN $MILVUS_TOKEN

import vdbimport
def main(args):
  return {"body": vdbimport.vdbimport(args)}
