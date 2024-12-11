
import requests as req
import json
url =  "https://ollama.nuvolaris.io"
username = "demo"
password = "demogpu"
auth = (username, password)

genurl = f"{url}/api/generate"
data = {}
data["model"] = "llama3.1:8b"
data["stream"] = True
data["prompt"] = "What is the theory of relativity?"

r = req.post(genurl, auth=auth, json=data, stream=True)
g = r.iter_lines()

out = ""
for chunk in g:
    d = json.loads(chunk)
    res = d.get("response", "")
    out += res
    print(res, end="")
    

