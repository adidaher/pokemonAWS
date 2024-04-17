import requests
import random
import json

url = "https://pokeapi.co/api/v2/pokemon?limit=50"

def fetch_Pokemons():
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data.get('results')
    else:
        print("Error:", response.status_code)
        return None


def generate_pokemons():
    try:
        pokemonList = fetch_Pokemons()
        if pokemonList:
            list_size = len(pokemonList)
            random_number = random.randint(0, list_size-1)
            if load_from_json(pokemonList[random_number].get('name')):
                print("Pokemon already exists in JSON file.")
                return pokemonList[random_number]
            else:
                save_to_json(pokemonList[random_number])
                print("Pokemon added to JSON file.")
                return pokemonList[random_number]
    except Exception as err:
        print("Error:", err)
        return None

def load_from_json(pokemon_name):
    try:
        with open('pokemon_data.json', 'r') as json_file:
            pokemons = json.load(json_file)
            print("Loaded pokemons:", pokemons)
            if pokemons:
                return pokemon_name in pokemons
            else:
                return False
    except FileNotFoundError:
        return False
    except json.decoder.JSONDecodeError:
        print("JSON file is empty or not valid.")
        return False


def save_to_json(pokemon_data):
    print("saving ", pokemon_data)
    try:
        with open('pokemon_data.json', 'r') as json_file:
            existing_data = json.load(json_file)
    except FileNotFoundError:
        existing_data = {}
    except json.decoder.JSONDecodeError:
        existing_data = {}

    existing_data[pokemon_data['name']] = {
        'url': pokemon_data['url']
    }
    with open('pokemon_data.json', 'w') as json_file:
        json.dump(existing_data, json_file, indent=4)


def main():
    ans = input('Ask for pokemon? ')
    if ans =='yes':
        pokemon = generate_pokemons()
        if pokemon:
            print(pokemon)
        else:
            print("Failed to fetch pokemon.")
    else:
        print("Greeting")


main()


