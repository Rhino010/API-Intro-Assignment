import requests


def fetch_pokemon_data(pokemon_name):
    counter = 0
    weight = 0
    for name in pokemon_name:
        counter += 1
        print("")
        pokemon_url = f"https://pokeapi.co/api/v2/pokemon/{name}"
        response = requests.get(pokemon_url)
        poke_data = response.json()
        print(f"Name: {name.capitalize()}")
        weight += poke_data['weight']
        for stat in poke_data['abilities']:
            print(f"-- Ability: {stat['ability']['name']}")
    print(f"\n**Average weight of all pokemon from list: {calculate_average_weight(weight, counter)} lbs**")

def calculate_average_weight(total_weight, counter):
    average_weight = total_weight / counter
    return average_weight

pokemon_names = ["pikachu", "bulbasaur", "charmander"]

fetch_pokemon_data(pokemon_names)