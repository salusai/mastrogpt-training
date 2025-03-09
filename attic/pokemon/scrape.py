import json, requests as req, chat
from bs4 import BeautifulSoup

POKEDEX = "https://pokemondb.net/pokedex"

def scrape(args, url, prompt):
  html = req.get(url).text
  ch = chat.Chat(args)
  html = req.get(url).text
  ch.add(f"""user:
I have the following html:
```
{html}
```
{prompt}
""")
  return ch.complete()

def info(args, name):
  url = f"{POKEDEX}/{name}"
  html = req.get(url).text
  ch = chat.Chat(args)
  ch.add(f"""user:
I have the following html:
```
{html}
```
Answer in this JSON format:
```
{{
  "name": <name>,
  "image": <image>,
  "height": <height>,
  "weight" : <weight>,
  "abilties": <abilities>
}}
```
where:
<name> is the pokemon name,
<height> is the pokemon height, provide only one numeric value in meters,
<weight> is the pokemon weight, provide only one numeric value in kg,
<image> is the url of the second image to the site img.pokemondb.net,
<abilities> is an array of abilities names.
Do not provide any comment or explanation.
""")
  return ch.complete()

def all(args):
    url = f"{POKEDEX}/all"
    html = req.get(url).text
    soup = BeautifulSoup(html, 'html.parser')
    anchors = soup.find_all('a', class_='ent-name')
    ls = []
    res = {}
    for anchor in anchors: 
      id = anchor['href'].split("/")[-1]
      res[anchor.text] = id
    return res
