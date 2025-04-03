#Importamos la biblioteca 'Requests'
import requests
#definimos la funcion para consultar la API
def cheep_fetch():
    #(3.Conexion a la API)
    url_consulta = requests.get(f"https://3bda700d-ebe7-421a-bbc1-20cb9289f0cc-00-c4yvkdzp1nlg.janeway.replit.dev/get_cheeps")
    respuesta = url_consulta.json()
    print(respuesta)
    return respuesta

#definimos la funcion para enviar un comentario
#(4.Procesa objetos a la API)
def cheep_post():
    url_cheep = "https://3bda700d-ebe7-421a-bbc1-20cb9289f0cc-00-c4yvkdzp1nlg.janeway.replit.dev/send_cheep"
    #mensaje en duro
    #mensaje_enviado = {'message':'cheep cheep valentina toledo!'}
    #mensaje_dinamico (1.Entrada de texto)
    ingreso_texto_mensaje = str(input("Ingresa un mensaje para postear en Cheep: "))
    mensaje_enviado = {'message':ingreso_texto_mensaje}
    posteo_mensaje = requests.post(url_cheep, json = mensaje_enviado)
    #(2.Salida de texto)
    print(posteo_mensaje.text)
    return posteo_mensaje

#definimos la funcion main para invocar las funciones
def main():
    #Invocacmos a la funcion para consultar API
    cheep_fetch()
    #Invocacmos a la funcion para postear en la API
    cheep_post()

#definimos el boilerplate para controlar la ejecucion del codigo
if __name__=="__main__":
    main()