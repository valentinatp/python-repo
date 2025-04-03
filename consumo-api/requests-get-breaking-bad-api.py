import requests

def breakingbad_fetch():
    #ingresamos la url de la API
    url_breaking_bad = "https://api.breakingbadquotes.xyz/v1/quotes"
    #obtenemos la informacion de la API
    response = requests.get(url_breaking_bad)
    #transformamos la informacion de la API a Json
    data = response.json()
    #recorremos la informacion de la API
    for sentence in data:
        #capturamos la frase y autor
        sentence
    #agreamos el valor de la frase a una variable
    frase = sentence['quote']
    #agreamos el valor del autor a una variable
    autor = sentence['author']
    #imprimimos la frase y el autor
    print(f"Frase: {frase}")
    print(f"Autor: {autor}")
    return 

breakingbad_fetch()