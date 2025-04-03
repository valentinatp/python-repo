import requests

def restcountries_fetch(name_country):
    #ingresamos el nombre del pais en la URL
    #agrego parametros a la url de la consulta para que me devuelva los datos necesarios y no sobre carge la consulta a la API
    url_rest_countries = f"https://restcountries.com/v3.1/name/{name_country}?fields=name,capital,population,languages"
    #consultamos la API
    response = requests.get(url_rest_countries)
    #respuesta de la API convertido a formato Json
    data = response.json() #responde una lista
    
    #recorremos los atributos de la respuesta de la API
    #capturo el nombre de la consulta
    for name in data:
        print("-----Nombre oficial del Pais ingresado------")
        print(f"Nombre oficial: {name['name']['official']}")
    #capturo el nombre de la/as capital/es
    for capital_data in data:
        print("-----Capital del Pais ingresado------")
        capital_pais = capital_data['capital']
        for capital in capital_pais:
            print(f"Capital: {capital}")
    #capturo la poblacion
    for poblation in data:
        print("-----Poblacion oficial del Pais ingresado------")
        print(f"Poblacion oficial: {poblation['population']}")
    #capturo el lenguaje
    for lenguaje_data in data:
        print("-----Lenguaje del Pais ingresado------")
        list_languages = lenguaje_data['languages']
        for lenguaje in list_languages.values():
            print(lenguaje)
    return 

pais_ingresado = input("Ingrese el nombre del Pais: ")
restcountries_fetch(pais_ingresado)