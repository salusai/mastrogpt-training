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
        
        self.messages = []
        self.add(ROLE)
        
        #TODO:E4.1 add a sock field 
        # conect to the streamer using STREAM_HOST and STREAM_PORT
        #END TODO
        
    def add(self, msg):
        [role, content] = msg.split(":", maxsplit=1)
        self.messages.append({
                "role": role,
                "content": content,
        })
    
    def complete(self):
        #TODO:E4.2 change the code to implement the steaming
        res = self.client.chat.completions.create(
            model=MODEL,
            messages=self.messages,
        )
        out = "error"
        if len(res.choices) >0:
            out = res.choices[0].message.content
            self.add(f"assistant:{out}")
        return out
        #END TODO
    
