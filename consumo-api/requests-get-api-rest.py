import requests

numero_ingresado = input("Ingresa un número: ")
respuesta = requests.get(f"http://numbersapi.com/{numero_ingresado}?json")
trivia = respuesta.json()

print(trivia)