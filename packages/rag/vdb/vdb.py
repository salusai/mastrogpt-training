import embed

import pymilvus
from pymilvus import MilvusClient, FieldSchema, CollectionSchema, DataType, Collection

COLLECTION="test"
# dimension produced by the embed model
DIMENSION=1024

def vdb_init(args):
    # connect to db
    uri = args.get("MILVUS_HOST", os.getenv("MILVUS_HOST"))
    token = args.get("MILVUS_TOKEN", os.getenv("MILVUS_TOKEN"))    
    db_name = args.get("MILVUS_DB_NAME", os.getenv("MILVUS_DB_NAME"))
    db = MilvusClient(uri=uri, token=token, db_name=db_name)
    
    # create test collection if not existed
    if not COLLECTION in  db.list_collections():
      fields = [
        FieldSchema(name="id", dtype=DataType.INT64, is_primary=True, auto_id=True),  # Primary key
        FieldSchema(name="vector", dtype=DataType.FLOAT_VECTOR, dim=DIMENSION),  # Vector field
        FieldSchema(name="text", dtype=DataType.VARCHAR, max_length=DIMENSION)  # Metadata field
      ]
      schema = CollectionSchema(fields=fields, description="test collection")
      db.create_collection(collection_name=COLLECTION, dimension=DIMENSION, schema=schema)
      
    return db

def vdb(args):
  llm = embed.url(args)
  db = vdb_init(args)
  
  out = f"Start with '!' to text in collection {COLLECTION}.\nJust type text to perform full text search."
  inp = args.get('input', "")

  if inp.startswith("!"):
    inp = inp[1:]
    vec = embed.embed(url, inp)
    data = [{ "vector": vec, "text": inp }]
    r = db.insert(collection_name=COLLECTION, data=data)
    out = f"OK: {r}" if r.get('insert_count', 0) == 1 else f"ERROR: {r}"
  else:
    
  milvus(args)
  collection = Collection("upload")

  return { "output": "vdb" }

