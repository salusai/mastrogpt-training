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
# Module 2: Assistants

https://www.nuvolaris.io

---

![bg](https://fakeimg.pl/350x200/ff0000,0/000?text=Agenda&retina=1)


---

# Our Goal: build a Chat accessing an Open LLM

- Prerequisites
- Simple UI
- Accessing the LLM

---

![bg](https://fakeimg.pl/350x200/ff0000,0/000?text=Prerequisites&retina=1)

---


```python
username = "demo"
password = "demogpu"
url =  "https://ollama.nuvolaris.io"
auth = (username, password)

from ollama import Client
client = Client(host=url, auth=auth)

msg = {"role":"user","content": "what is the capital of Italy"}
model = "llama3.1:8b"

client.chat(model=model, messages=[msg])
```

```python
g = client.chat(model=model, messages=[msg], stream=True)
for r in g: print(r.message.content, end='')
```