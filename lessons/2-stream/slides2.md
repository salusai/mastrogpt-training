
# Our Goal: build a Chat accessing an Open LLM

- Prerequisites
- Simple UI
- Accessing the LLM
- TODO

---

![bg](https://fakeimg.pl/350x200/ff0000,0/000?text=Prerequisites&retina=1)

---

# We will primarily use **Python**

- However the UI are in JavaScript 
- We use also Nodejs to download the rest

## Start installing NodeJS

## https://nodejs.org/en/download/

- Many options, pick your favorite
- update to 22 if you have already node

--- 

# Check the prerequisites

- Convention:  `$` means `type this at the terminal`
- All the lines withot `$` menas `check this example`
- `#YMMV` means the actual output can be different 

```bash
$ node -v
v22.11.0 # or greater
```
- ensure you have **at least** v22, please

---
# Test


```bash
export OPSDEV_APIHOST=https://pinocchio.nuvolaris.dev
export URL=$OPSDEV_APIHOST/api/my
export URL=$OPSDEV_APIHOST/api/my

http $URL/mastrogpt/index

http $URL/mastrogpt/demo
http $URL/mastrogpt/demo input=chess
http $URL/mastrogpt/demo input=code
http $URL/mastrogpt/demo input=form
```

---

# Check ollama is running

```python
username = "demo"
password = "demogpu"
url =  "https://ollama.nuvolaris.io"
auth = (username, password)
import requests as req
req.get(url, auth=auth).text
```

---

# Simple request

!ollama pull llama3.1:8b
!ollama ls

- Select the `model`
- Set streaming to false (*important*)
- Make the request

```python
genurl = f"{url}/api/generate"
data = {}
data["model"] = "llama3.1:8b"
data["stream"] = False
data["prompt"] = "what is the capital of Italy"
req.post(genurl, auth=auth, json=data).json()
```

---

# Streaming

- Long request
```python
genurl = f"{url}/api/generate"
data = {}
data["model"] = "llama3.1:8b"
data["stream"] = True
data["prompt"] = "what is the theory of relativity"

r = req.post(genurl, auth=auth, json=data, stream=True)
g = r.iter_lines()
```

---
# Steam Answer

- one by one

```python
# repeat this
next(g)
```

- repeat until is done

```
for line in g: print(line)
```



