import os
import openai
import socket

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
        
        self.messages = []
        self.add(ROLE)
        
        self.sock = None
        sock = args.get("STREAM_HOST")
        port = int(args.get("STREAM_PORT", "0"))
        if sock and port > 0:
            self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.connect((sock, port))
        

    def add(self, msg):
        [role, content] = msg.split(":", maxsplit=1)
        self.messages.append({
                "role": role,
                "content": content,
        })
    
    def complete(self):
        if self.sock:
            res = self.client.chat.completions.create(
                model=MODEL,
                messages=self.messages,
                stream = True,
            )
            out = "error"
        else:
            res = self.client.chat.completions.create(
                model=MODEL,
                messages=self.messages,
            )
            out = "error"
            if len(res.choices) >0:
                out = res.choices[0].message.content
                self.add(f"assistant:{out}")
        return out
