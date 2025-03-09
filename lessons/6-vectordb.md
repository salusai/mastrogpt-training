---
marp: true
theme: gaia
_class: lead
paginate: true
backgroundColor: #fff
backgroundImage: url('https://marp.app/assets/hero-background.jpg')
color: 266089
html: true

---
![bg left:50% 70%](assets/nuvolaris-logo.png)

### Developing Open LLM applications with

<center>
<img width="100%"src="assets/openserverless-logo.png">
</center>

## Lesson 6

## Vector Database

---
![bg left:50% 80%](assets/mastrogpt.png)

## Vector Database


- Vector Database

- Embedding

- Importing PDF

---

![bg](https://fakeimg.pl/700x400/ff0000,0/0A6BAC?retina=1&text=Vector+Database)

---

# Access Milvus

```python
import os
from pymilvus import MilvusClient

uri = f"http://{os.getenv("MILVUS_HOST")}"
token = os.getenv("MILVUS_TOKEN")
db_name =  os.getenv("MILVUS_DB_NAME")
client = MilvusClient(uri=uri, token=token, db_name=db_name)
```

---

# Create Schema

- Parameters
```
COLLECTION = "test" 
DIMENSION=1024
from pymilvus import DataType
````

- Define Schema
```
schema = client.create_schema()
schema.add_field(field_name="id", datatype=DataType.INT64, is_primary=True, auto_id=True)
schema.add_field(field_name="text", datatype=DataType.VARCHAR, max_length=DIMENSION)
schema.add_field(field_name="embeddings", datatype=DataType.FLOAT_VECTOR, dim=DIMENSION)
```

---

# Create Index and Collection

- Define Index
```
index_params = client.prepare_index_params()
index_params.add_index("embeddings", index_type="AUTOINDEX", metric_type="IP")
```

- Create Collection with Index and Schema

```
client.create_collection(
     collection_name=collection, 
     schema=schema, index_params=index_params)
```

---

# Insert

```
text = "Hello World"
vec = [float(i) for i in range(0,DIMENSION)] # DO NOT DO THIS! Just a sample
client.insert(COLLECTION, {"text":text, "embeddings": vec})
```

# Retrieve

```
qit = client.query_iterator(collection_name=COLLECTION, batchSize=2, output_fields=["text"])
res = qit.next()
print(res[0].get("text"))
```

---

![bg](https://fakeimg.pl/700x400/ff0000,0/0A6BAC?retina=1&text=Embedding)

---

# Embedding

- Use an embedding model
```
MODEL="mxbai-embed-large:latest"
DIMENSION=1024
```

- Invoke the embeeding API
```
inp = "Hello World"
url = f"https://{os.getenv("AUTH")}@{os.getenv("OLLAMA_HOST")}/api/embeddings"
msg = { "model": MODEL, "prompt": inp, "stream": False }
res = req.post(url, json=msg).json()
out = res.get('embedding', [])
```
---

# VectorDB with embedding

```

```

---

![bg](https://fakeimg.pl/700x400/ff0000,0/0A6BAC?retina=1&text=PDF+Import)

---