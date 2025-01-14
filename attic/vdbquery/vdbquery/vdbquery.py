import os, ollama, pymilvus
from pymilvus import connections, utility, Collection

EMB_MODEL = "mxbai-embed-large"
  
llm_client = None

def llm(args):
  global llm_client
  if llm_client is None:
    host = args.get("OLLAMA_HOST", os.environ.get("OLLAMA_HOST"))
    username = args.get("OLLAMA_USERNAME", os.environ.get("OLLAMA_USERNAME"))
    password = args.get("OLLAMA_PASSWORD", os.environ.get("OLLAMA_PASSWORD"))
    auth = (username, password)
    #print(host, auth)
    llm_client = ollama.Client(host, auth=auth)
  return llm_client

def connect(args):
    uri = args.get("MILVUS_HOST", os.getenv("MILVUS_HOST", "./test.db"))
    token = args.get("MILVUS_TOKEN", os.getenv("MILVUS_TOKEN", ""))    
    db_name = args.get("MILVUS_DB_NAME", os.getenv("MILVUS_DB_NAME"))
    pymilvus.connections.connect(uri=uri, token=token, db_name=db_name)

def embed(llm, text):
  emb = llm.embed(input=text, model=EMB_MODEL)
  return emb.embeddings[0]
  
def vdbquery(args):
  name = args.get("profile")
  connect(args)
  llm = llm(args)
  
  coll = Collection(name)
  text = args.get("input")
  emb = embed(llm, text)
  res = coll.search(
    data=[emb],
    anns_field="embedding",
    param={"metric_type": "L2"},
    output_fields=["text"],
    limit=100,
  )
  for e in res[0]:
    print(e.entity.text)
  res.done
  return { "output": "vdbquery"}
