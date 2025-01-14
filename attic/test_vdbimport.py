#%load_ext autoreload
#%autoreload 2
import sys, os
sys.path.append("packages/vdbimport/vdbimport")
import vdbimport

args = {
    "LINKEDIN_USERNAME": os.getenv("LINKEDIN_USERNAME"),
    "LINKEDIN_PASSWORD": os.getenv("LINKEDIN_PASSWORD"),
    "profile": "msciab"
}

def test_linkedin(args):
    name = args.get("profile")
    api = vdbimport.linkedin(args)
    assert len(texts) > 0
    texts = vdbimport.recent_posts(api, name)
    sents = vdbimport.sentencer(texts)
    assert len(sents) >= len(texts)

def test_scrape(args):
    
    data, text_size, emb_size = vdbimport.scrape(args)
    
    assert len(data) > 0
    assert len(text_size) > 0
    assert len(emb_size) > 0
    
def test_import():
    name = args.get("profile")
    pymilvus.drop_collection(name)
    assert len(pymilvus.list_collections()) == 0
    
    data, text_size, emb_size = vdbimport.scrape(args)
    vdbimport.connect(args)  
    vdbimport.create_collection(name, emb_size, text_size)
    
    assert name in pymilvus.list_collections() 

    Collection(name).insert(data)
    
    coll = Collection(name)
    coll.load()

    res =  coll.query(expr="", output_fields=["*"], limit=1000)  
    
    assert len(res) == len(data)
    
  