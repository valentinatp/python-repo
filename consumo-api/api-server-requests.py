import requests
def consultar_api_fetch(endpoint):
    url_consultada = "https://jsonplaceholder.typicode.com/"
    response = requests.get(url_consultada + endpoint);
    print(response);
    if response.status_code == 200:
        print("-- La solicitud ha tenido exito --")
    elif response.status_code == 300:
        print("-- Redirección en proceso --")
    elif response.status_code == 404:
        print("-- Solicitud incorrecta --")
    elif response.status_code == 500:
        print("-- Error de conexión con el Servidor --")
    return
endpoint_ingresado = input("Ingresa el endpoint para consultar: ")
print(f"Consultando Endopoint ingresado... ... ...")
consultar_api_fetch(endpoint_ingresado)