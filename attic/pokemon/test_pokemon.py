import sys 
sys.path.append("packages/vdb/pokemon")
import pokemon, scrape

def test_scrape():
    args = {}
    slug = "bulbasaur"

    m  = scrape.info(args, slug)

    ls = scrape.all(args)
    pokemon.description(m)

def test_pokemon():

    pokemon.pokemon({}).get("output")

    slug = "ogerpon"
    url = f"https://pokemondb.net/pokedex/{slug}"
    print(scrape.info({}, slug))

    print(scrape.scrape({}, url, "return the url of images, only the url"))
    scrape.scrape({}, url, "return the all the url of the pokemon images , only the urls")