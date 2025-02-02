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

## Lesson 2

# An LLM chat with streaming

---
![bg left:50% 80%](assets/mastrogpt.png)

### Agenda

- Accessing the LLM

- Managing Secrets

- Streaming an answer

- Streaming with the LLM


---

![bg](https://fakeimg.pl/700x400/ff0000,0/0A6BAC?retina=1&text=Accessing+the+LLM)


---
# Getting credentials

- Credentials are available in the environment:
  - `OLLAMA_HOST` is the url
  - `AUTH` are the credentials
    - **for the dev environment only!**
- Enter the CLI: `ops ai cli`
- Checking you have the credentials:

```python
import os
os.getenv("OLLAMA_HOST")
os.getenv("AUTH")
```

---

# Accessing Ollama

```python
args = {}
host = args.get("OLLAMA_HOST", os.getenv("OLLAMA_HOST"))
auth = args.get("AUTH", os.getenv("AUTH"))
base = f"https://{auth}@{host}/"
```

## Test it!

```
!curl {base}
```
`Ollama is Running`

---

# Talking with a model in Ollama

```python
# using llama 3.1 8 Billions
MODEL = "llama3.1:8b"
inp = "Who are you?"
# preparing a request
msg = { "model": MODEL, "prompt": inp, "stream": False}
url = f"{base}/api/generate"
# making a request
import requests as req
res = req.post(url, json=msg).json()
out = res.get('response', 'error')
print(out)
```

---

# Putting all togegether in an action

Checking the code:
```
!code packages/chat/simple.py
```

# Deploying the action

Low level commands (it can be simpler!)
```bash
!ops package create chat
!ops action create chat/simple packages/chat/simple.py \
     --web=true --param AUTH {auth} --param OLLAMA_HOST {host}
```

---

![bg](https://fakeimg.pl/700x400/ff0000,0/0A6BAC?retina=1&text=Managing+Secrets)

---

![bg](https://fakeimg.pl/700x400/ff0000,0/0A6BAC?retina=1&text=Streaming+an+Answer)


---

![bg](https://fakeimg.pl/700x400/ff0000,0/0A6BAC?retina=1&text=Streaming+an+Answer)

---

![bg](https://fakeimg.pl/700x400/ff0000,0/0A6BAC?retina=1&text=Streaming+the+LLM)


---

![bg](https://fakeimg.pl/350x200/ff0000,0/0A6BAC?retina=1&text=What+is+Next?)

---

# Lesson 3 - Form

Support for form, display and advanced rendering

## More lessons
- Lesson 4: Building an Assistant
- Lesson 5: Vision Support
- Lesson 6: VectorDB
- Lesson 7: Bulding a RAG
