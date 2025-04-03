import requests

def jsonplaceholder_post():
    url_jsonplaceholder_api = "https://jsonplaceholder.typicode.com/users"
    #solicitamos los datos de ingreso
    user_id = 1
    id_user = 101
    nombre = input("Ingresa tu nombre: ")
    correo = input("Ingresa tu correo: ")
    direccion = input("Ingresa tu direccion: ")
    usuario = {
            'userId' : user_id, 
            'id' : id_user, 
            'name' : nombre, 
            'email' : correo, 
            'address' : direccion 
        }
    #agregamos el usuario en el servidor
    post_usuario = requests.post(url_jsonplaceholder_api, json = usuario)
    print(post_usuario)
    return post_usuario

def jsonplaceholder_fetch():
    url_jsonplaceholder_api = "https://jsonplaceholder.typicode.com/users"
    response = requests.get(url_jsonplaceholder_api)
    response_json = response.json()
    print(response)
    print(response_json)
    return


jsonplaceholder_post()
jsonplaceholder_fetch()
