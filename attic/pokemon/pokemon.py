import scrape
import json

USAGE = """USAGE:
*<sub>         list pokemon with substring
@<pokemon>     grab the pokemon
"""

all_pokemon = None


def description(m):
    abilities = ", ".join(m['abilities'])
    return f"""The pokemon {m['name']} 
has a height of {m['height']} meters
and a weight of {m['weight']} kg
and the following abilities: {abilities}.
"""

def pokemon(args):
    global all_pokemon
    if all_pokemon is None:
        all_pokemon = scrape.all(args)
    
    res = {}
    inp = args.get("input", "")
    out = USAGE
    if inp.startswith("*"):
        pref = inp[1:].lower()
        out = f"Pokemon starting with '{pref}':\n"
        for key in all_pokemon.keys():
            #print(key)
            if key.lower().startswith(pref):
                out += f"{key}\n"
    elif inp.startswith("@"):
        name = inp[1:] 
        slug = all_pokemon.get(name)
        if slug:
            try:
                m = json.loads(scrape.info(args, slug))
                img = m['image']
                print(img)
                res['html'] = f'<img src="{img}">'
                out = description(m)
            except Exception as e:
                out = str(e)
        else:
            out = f"{name} not found"
    else:
        out = USAGE

    res['output'] = out
    return res
