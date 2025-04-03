import requests

#Obtenermos informacion de API
def pokeapi_fetch(name):
    url_poke_api = "https://pokeapi.co/api/v2/pokemon/"
    response = requests.get(url_poke_api + name)
    response_json = response.json()
    
    print("----- Nombre de Pokemon escogido -------")
    nombre_pokemon = response_json["name"]
    print(f"Nombre: {nombre_pokemon}")

    print("----- Tipo de Pokemon escogido -------")
    for type in response_json['types']:
        print(f"Tipo: {type['type']['name']}")
    
    print("----- Habilidades de Pokemon escogido -------")
    for ability in response_json['abilities']:
        print(f"Habilidades: {ability['ability']['name']}")

    return

nombre_pokemon_ingresado = input("Ingrese el nombre de un pokemon: ")
pokeapi_fetch(nombre_pokemon_ingresado)