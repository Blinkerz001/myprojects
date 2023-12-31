from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
url = 'https://pokemondb.net/pokedex/all'
request = Request(
    url,
    headers = {'User-Agent':'Mozilla/5.0'} 
    )
page = urlopen(request)
page_content_bytes = page.read()
page_html = page_content_bytes.decode("utf-8")

soup = BeautifulSoup(page_html, "html.parser")

rows = soup.find_all("table", id="pokedex")[0].find_all("tbody")[0].find_all("tr")
for pokemon in rows[0:5]:
    pokemon_data = pokemon.find_all("td")
    id = pokemon_data[0]['data-sort-value']
    pic = pokemon_data[0].find_all("img", class_= "img-fixed icon-pkmn")[0]['src']

    name = pokemon_data[1].find_all("a")[0].getText()
    if pokemon_data[1].find_all("small"):
        name = pokemon_data[1].find_all("a")[0].getText()+" - "+ pokemon_data[1].find_all("small")[0].getText()
    name_link = pokemon_data[1].find_all("a")[0]["href"]
    types = []
    for pokemon_type in pokemon_data[2].find_all("a"):
        types.append(pokemon_type.getText())
    total = pokemon_data[3].getText()
    hp = pokemon_data[4].getText()
    atk = pokemon_data[5].getText()
    defense = pokemon_data[6].getText()
    sp_atk = pokemon_data[7].getText()
    sp_defense = pokemon_data[8].getText()
    speed = pokemon_data[9].getText()
    
    