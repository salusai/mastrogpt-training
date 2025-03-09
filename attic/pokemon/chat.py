import os
import openai

MODEL = "llama3.1:8b"
ROLE = "system:You are an helpful assistant."

class Chat:
    def __init__(self, args):
        
        host = args.get("OLLAMA_HOST", os.getenv("OLLAMA_HOST"))
        api_key = args.get("AUTH", os.getenv("AUTH"))
        base_url = f"https://{api_key}@{host}/v1"
        
        self.client = openai.OpenAI(
            base_url = base_url,
            api_key = api_key,
        )
        
        model = args.get("model", MODEL)
        role = args. get("role", ROLE)
        self.messages = []
        self.model = model
        self.add(role)
        
    def add(self, msg):
        [role, content] = msg.split(":", maxsplit=1)
        self.messages.append({
                "role": role,
                "content": content,
        })
        return msg
    
    def complete(self):
        out = ""
        try:
            res = self.client.chat.completions.create(
                model=self.model,
                messages=self.messages,
                stream=True
            )
            for item in res:
                delta = item.choices[0].delta.content
                #print(delta, end='')
                out += delta
            self.add(f"assistant:{out}")
        except Exception as e:
            out = str(e)
        return out

    def last(self):
        return self.messages[-1]['content']

    def pop(self):
        if len(self.messages) > 0:
            self.messages.pop()
            return True
        return False

