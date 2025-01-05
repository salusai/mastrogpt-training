import cache
import store

def rag(args):

  collection = store.setup(args)
  if collection is None: 
    return { "form": [
        { "type": "text", "label": "Collection", "name": "collection" }
      ]
    }
    
  msg = store.upload(args, collection)
  if msg is not None: 
    return { "output": msg }
  
  data = store.query(args, collection)  
  if data is None: 
    return { "output": chat.process(args, data) }
  
  