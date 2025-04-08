import requests

def rick_morty_fetch():
    url_rickmorty_api = "https://rickandmortyapi.com/api/character"
    response = requests.get(url_rickmorty_api)
    data = response.json()
    print(type(data))
    
    # for page in data["info"]["pages"]:
    #     print(page)
    #print(data["info"][next])
    for id_personaje in data["results"]:
       print(id_personaje["id"])

    for personaje in data["results"]:
        print(personaje["name"])
        
    return

ingreso_usuario = input("Quieres ver mas? (s/n): ")
print(f"Respuesta usuario: {ingreso_usuario}")
rick_morty_fetch()