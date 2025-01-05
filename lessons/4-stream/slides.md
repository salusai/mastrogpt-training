---
marp: true
theme: gaia
_class: lead
paginate: true
backgroundColor: #fff
backgroundImage: url('https://marp.app/assets/hero-background.jpg')
html: true
---

![bg left:40% 80%](./logo-full-transparent.png)

## Developing Open LLM applications with Apache OpenServerless 
# Module 3: RAG

https://milvus.io/docs/it/build_RAG_with_milvus_and_ollama.md

https://www.nuvolaris.io

---

![bg](https://fakeimg.pl/350x200/ff0000,0/000?text=Agenda&retina=1)


---

%cd ../training/lessons/3-rag
!pwd
!ls

```python
username = "demo"
password = "demogpu"
url =  "https://ollama.nuvolaris.io"
auth = (username, password)

model = "mxbai-embed-large"
from ollama import Client
client = Client(host=url, auth=auth)
r = client.embed(model=model, input="Hello world")
emb_size = len(r.embeddings[0])
```

```python
from pymilvus import MilvusClient
client = MilvusClient("alice.db")
client.create_collection(collection_name="alice", dimension=emb_size)

```

```python
from spacy.lang.en import English # updated
from pathlib import Path

nlp = English()
nlp.add_pipe('sentencizer')

#sentences = [sent.text.strip() for sent in doc.sents]


doc = nlp(Path("alice.txt").read_text())
embs = []
for sent in doc.sents:
    text = sent.text.strip()
    print(text)
    r = ollama.embed(model=model, input=text)
    embs.append(r)
    print(r)
```

---


