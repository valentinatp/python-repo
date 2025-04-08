import requests
def consultar_api_fetch(endpoint):
    url_consultada = "https://ftx.us/api"
    response = requests.get(url_consultada + endpoint)
    print(response)
    # for i in response:
    #     print(i)
    # if response[200] == "200":
    #     print("La solicitud ha tenido exito.")
    return
endpoint_ingresado = input("Ingresa el endpoint para consultar: ")
print(f"Consultando Endopoint ingresado... ... ...")
consultar_api_fetch(endpoint_ingresado)