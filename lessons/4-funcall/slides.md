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
# Module 3: Function Calling

https://www.nuvolaris.io

---

![bg](https://fakeimg.pl/350x200/ff0000,0/000?text=Agenda&retina=1)


# Setup

```python
username = "demo"
password = "demogpu"
url =  "https://ollama.nuvolaris.io"
auth = (username, password)

from ollama import Client
client = Client(host=url, auth=auth)

msg = {"role":"user","content": "What is the capital of Italy?"}
model = "llama3.1:8b"

client.chat(model=model, messages=[msg])
```

```python

import ollama

msg = {"role":"user","content": "What is the theory of relativity?"}
g = client.chat(model=model, messages=[msg], stream=True)
for r in g: print(r.message.content, end='')
```

```python
import ollama

github_star_count = {
  'type': 'function',
  'function': {
    'name': 'github_star_count',
    'description': 'Get the star count of a GitHub project, returns -1 if the repo does not exist',
    'parameters': {
      'type': 'object',
      'properties': {
        'owner': {
          'type': 'string',
          'description': 'The project owner or organization"',
        },
        'repo': {
          'type': 'string',
          'description': 'The name of the project repository"',
        },
      },
      'required': ['owner', 'repo'],
    },
  },
}

msg = {'role': 'user', 'content': 'How meany stars has the OpenServerless project in the Apache Organization'}

res = ollama.chat(model='llama3.1:8b', messages=[msg], tools=[github_star_count])


print(res['message']['tool_calls'])
```