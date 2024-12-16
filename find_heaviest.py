import requests

def fetch_planet_data():
    url = "https://api.le-systeme-solaire.net/rest/bodies/"
    response = requests.get(url)
    planets = response.json()['bodies']
    return planets

def find_heaviest_planet(planets):
    max_mass = 0
    max_planet = {}
    try:
        for planet in planets:
            if planet['isPlanet']:
                planet_mass = planet['mass']['massValue']
                if planet_mass > max_mass:
                    max_mass = planet_mass
                    max_planet[planet['name']] = planet_mass

    except TypeError:
        print(" ")
    max_key = max(max_planet, key = max_planet.get)
    print(f"{max_key} is the heaviest planet with a mass of {max_planet[max_key]}.")


    # print(f"The planet with the most mass is {name}, with a mass of {max_mass}.")

planets = fetch_planet_data()
find_heaviest_planet(planets)
