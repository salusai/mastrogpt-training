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

https://www.nuvolaris.io

---

![bg](https://fakeimg.pl/350x200/ff0000,0/000?text=Agenda&retina=1)



---

%cd ../training/lessons/3-rag

```python
import ollama
from pathlib import Path
doc = Path("alice.txt").read_text()
model = "mxbai-embed-large"
r = ollama.embeddings(model=model, prompt=doc)
```

---

```python
from pymilvus import MilvusClient
client = MilvusClient("milvus_demo.db")
client.create_collection(collection_name="demo", dimension=768)


docs = [
    "Artificial intelligence was founded as an academic discipline in 1956.",
    "Alan Turing was the first person to conduct substantial research in AI.",
    "Born in Maida Vale, London, Turing was raised in southern England.",
]

```

