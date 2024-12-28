#--kind python:default
#--web true
#--param OLLAMA_HOST $OLLAMA_HOST
#--param OLLAMA_USERNAME $OLLAMA_USERNAME
#--param OLLAMA_PASSWORD $OLLAMA_PASSWORD
#--param MILVUS_HOST $MILVUS_HOST
#--param MILVUS_PORT $MILVUS_PORT
#--param MILVUS_TOKEN $MILVUS_TOKEN

import vdbquery
def main(args):
  return {"body": vdbquery.vdbquery(args)}
