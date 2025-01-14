import os
import pymilvus
import ollama

EMB_MODEL = "mxbai-embed-large"

LlmClient = None

def llm(args):
  global LlmClient
  if LlmClient is None:
    host = args.get("OLLAMA_HOST", os.environ.get("OLLAMA_HOST"))
    username = args.get("OLLAMA_USERNAME", os.environ.get("OLLAMA_USERNAME"))
    password = args.get("OLLAMA_PASSWORD", os.environ.get("OLLAMA_PASSWORD"))
    auth = (username, password)
    #print(host, auth)
    LlmClient = ollama.Client(host, auth=auth)
  return LlmClient

def linkedin(args):
    from linkedin_api import Linkedin
    username = args.get("LINKEDIN_USERNAME", os.getenv("LINKEDIN_USERNAME"))
    password = args.get("LINKEDIN_PASSWORD", os.getenv("LINKEDIN_PASSWORD"))
    api = Linkedin(username, password)
    return api

def recent_posts(api, profile):
    posts = api.get_profile_posts(profile)
    texts = []
    for post in posts:
        text = post['commentary']['text']['text']
        texts.append(text)
        print(text)
    return texts
    
def sentencer(texts):
  from spacy.lang.en import English # updated
  nlp = English()
  nlp.add_pipe('sentencizer')
  sents = []
  for text in texts:
    #text = texts[0]
    doc = nlp(text)
    # append the full text
    sents.append(text)
    for sent in doc.sents:
      print(sent.text)
      sents.append(sent.text)
  return sents

def embedder(llm, sentences):
  res = []
  text_size = 0
  emb_size = 0
  for text in sentences:
    print(text)
    out = llm.embed(input=text, model=EMB_MODEL)
    embedding = out.embeddings[0]
    id_pk = hash(text) & 0x7FFFFFFFFFFFFFFF
    res.append({"id": id_pk, "text": text, "embedding": embedding })
    text_size = max(text_size, len(text.encode('utf-8')))
    emb_size = max(emb_size, len(embedding))
  return (res, text_size, emb_size)

def scrape(args):
    name = args.get("profile")
    api = linkedin(args)
    texts = recent_posts(api, name)
    sents = sentencer(texts)
    return embedder(llm(args), sents)

  
def connect(args):
    uri = args.get("MILVUS_HOST", os.getenv("MILVUS_HOST", "./test.db"))
    token = args.get("MILVUS_TOKEN", os.getenv("MILVUS_TOKEN", ""))    
    db_name = args.get("MILVUS_DB_NAME", os.getenv("MILVUS_DB_NAME"))
    pymilvus.connections.connect(uri=uri, token=token, db_name=db_name)
 
def create_collection(name, emb_size, text_size):   
  from pymilvus import FieldSchema, CollectionSchema, DataType, Collection
  pk_field = FieldSchema(name="id", dtype=DataType.INT64, is_primary=True)
  emb_field = FieldSchema(name="embedding",dtype=DataType.FLOAT_VECTOR,dim=emb_size)
  text_field = FieldSchema(name="text", dtype=DataType.VARCHAR, max_length=text_size)
  schema = CollectionSchema(fields=[pk_field, emb_field, text_field])
  coll = Collection(name, schema=schema)

  # Define index parameters     
  index_params = {
    "index_type": "IVF_FLAT",       # Index type (e.g., IVF_FLAT, IVF_SQ8, HNSW)
    "metric_type": "L2",           # Distance metric (L2, IP, COSINE)
    "params": {"nlist": 128}       # Number of clusters for IVF-based indices
  }

  # Create the index
  coll.create_index(field_name="embedding", index_params=index_params)

        
def vdbimport(args):
    name = args.get("profile")
    data, text_size, emb_size = scrape(args)
    connect(args)  
    create_collection(name, emb_size, text_size)
    output = Collection(name).insert(data)
    return { "output": output }
