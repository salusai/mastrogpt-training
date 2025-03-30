import os, requests as req

class Chat:
    def __init__(self, args, model):
        host = args.get("OLLAMA_HOST", os.getenv("OLLAMA_HOST"))
        auth = args.get("AUTH", os.getenv("AUTH"))
        self.url = f"https://{auth}@{host}"
        self.model = model

    def ask(self, prompt):
        #  preparing a request
        msg = { "model": self.model, "prompt": prompt, "stream": False}
        url = f"{self.url}/api/generate"  
        res = req.post(url, json=msg).json()
        return res.get("response", "error")
    

