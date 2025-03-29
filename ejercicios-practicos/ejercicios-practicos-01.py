
'''
#01.- Conversión de metros a centímetros
    Escribe un programa que pida al usuario un número en metros y lo convierta a centímetros.
    Ejemplo:
    Entrada: Introduce la longitud en metros: 2
    Salida: La longitud en centímetros es: 200 cm
'''
print("Bienvenido a Calculadora de Transformación Metros a Centimetros")
#Solicitamos el dato en metros
print("Introduce la longitud en metros:")
#Capturamos el dato
numero_metro = int(input())
#Calculamos la conversion
conversion_centimetros = numero_metro * 100
#Imprimimos el resultado
print(f"La longitud en centímetros es: {conversion_centimetros} cm")

'''
#02.- Edad en el futuro
    Crea un programa que pida el nombre del usuario y su edad. Luego, calcula cuántos años tendrá en 10 años.
    Ejemplo:
    Entrada:
    Introduce tu nombre: Ana
    Introduce tu edad: 25
    Salida:
    Hola Ana, en 10 años tendrás 35 años.
'''
print("Bienvenido, acá podrás calcular cuantos años tendrás en 10 años más.")
#Solicitamos el nombre
print("Introduce tu nombre: ")
#Capturamos el valor del dato
nombre = input()
#Solicitamos la edad
print("Introduce tu edad: ")
#Capturamos el valor del dato
edad = int(input())
#Calculamos la edad
calculo_edad_futura = edad +  10
#Imprimimos el resultado
print(f"Hola {nombre}, en 10 años tendrás {calculo_edad_futura} años.")

'''
#03.- Área de un rectángulo
    Pide al usuario que introduzca la base y la altura de un rectángulo, y muestra el área calculada.
    Ejemplo:
    Entrada:
    Base: 5
    Altura: 3
    Salida:
    El área del rectángulo es: 15
''' 
print("Bienvenido, acá podrás calcular el área de un Rectángulo.")
#Solicitamos el valor de la base
base = int(input("Ingresa la Base: "))
#Solicitamos el valor de la altura
altura = int(input("Ingresa la Altura: "))
#Calculamos el área del rectángulo
calculo_area = base * altura
#Imprimimos el resultado
print(f"El área de un rectángulo es: {calculo_area}.")
'''
#04.- Calculadora simple
    Pide al usuario dos números y muestra la suma, resta, multiplicación y división de esos números.
    Ejemplo:
    Entrada:
    Primer número: 8
    Segundo número: 4
    Salida:
    Suma: 12
    Resta: 4
    Multiplicación: 32
    División: 2
'''
print("Bienvenido a la Calculadora.")
#Solicitamos el primer numero
primer_numero = int(input("Ingresa el primer número: "))
#Solicitamos el segundo numero
segundo_numero = int(input("Ingresa el segundo número: "))
#Calculamos la suma
calculo_suma = primer_numero + segundo_numero
#Calculamos la resta
calculo_resta = primer_numero - segundo_numero
#Calculamos la multiplicacion
calculo_multiplicacion = primer_numero * segundo_numero
#Calculamos la division
calculo_division = int(primer_numero / segundo_numero)
#Imprimimos el resultado
print(f"El resultado del calculo de la suma es: {calculo_suma}")
print(f"El resultado del calculo de la resta es: {calculo_resta}")
print(f"El resultado del calculo de la multiplicación es: {calculo_multiplicacion}")
print(f"El resultado del calculo de la división es: {calculo_division}")

'''
#05.- Cálculo del IVA
    Pide al usuario el precio de un producto y calcula el precio final con un IVA del 19%.
    Ejemplo:
    Entrada:
    Introduce el precio del producto: 100
    Salida:
    El precio final con IVA es: $119
'''
print("Bienvenido a la Calculadora de IVA.")
#Solicitamos el valor del producto
valor_producto = int(input("Ingresa el precio del producto: "))
#Estimamos el valor del IVA
valor_iva = float(0.19)
#Calculamos el valor del IVA del producto
calculo_iva_producto = valor_producto * valor_iva
#Sumamos el valor del IVA al valor del producto
valor_total_producto = int(valor_producto + calculo_iva_producto)
#Imprimimos el resultado
print(f"El precio final con IVA es: ${valor_total_producto}")
'''
#06.- Promedio de tres números
    Solicita tres números al usuario y muestra su promedio.
    Ejemplo:
    Entrada:
    Número 1: 5
    Número 2: 7
    Número 3: 10
    Salida:
    El promedio es: 7.33
'''
print("Bienvenido a la Calculadora de promedios.")
#Solicitamos la primera nota
primera_nota = int(input("Ingresa el primer nota: "))
#Solicitamos la segunda nota
segunda_nota = int(input("Ingresa el segundo nota: "))
#Solicitamos la tercerna nota
tercera_nota = int(input("Ingresa el tercer nota: "))
#Calculamos la suma de las 3 notas
suma_nota = primera_nota + segunda_nota + tercera_nota
#Calculamos el promedio de las 3 notas
calculo_promedio = float((suma_nota / 3))
#Formateamos el valor del promedio para que solo se muestre con 2 decimales.
#       ':.2f' indica que debe mostrar un float con 2 decimales y cualquier parte entera.
#       Al método '.format()' se le agrega la variable que contiene el resultado a redondear.
redondeo_promedio = "{:.2f}".format(calculo_promedio)
#Imprimimos el resultado
print(f"El promedio final de las tres notas es: {redondeo_promedio}")
'''
#07.- Tiempo en segundos
    Pide al usuario una cantidad de horas, minutos y segundos, y calcula el tiempo total en segundos.
    Ejemplo:
    Entrada:
    Horas: 1
    Minutos: 15
    Segundos: 30
    Salida:
    El tiempo total es: 4530 segundos
'''
print("Bienvenido a la Calculadora de Segundos.")
#Solicitamos la hora
hora = int(input("Ingresa una cantidad de horas: "))
#Solicitamos los minutos
minuto = int(input("Ingresa una cantidad de minutos: "))
#Solicitamos los segundos
segundo = int(input("Ingresa una cantidad de segundos: "))
#Transformamos las horas a segundos
#   Para calcular de horas a segundos se debe múltiplicar
#   la cantidad de horas * 60 (transforma a minutos) * 60 (transforma a segundos)
#   otra opcion en un solo paso: cantidad de horas * 3600 (60 minutos * 60 segundos) 
calculo_segundos_hora = hora * 60 * 60
#Transformamos los minutos a segundos
calculo_segundos_minuto = minuto * 60
#Calculamos el Total de segundos
calculo_total_segundos = int(calculo_segundos_hora + calculo_segundos_minuto + segundo)
#Imprimimos el resultado
print(f"El tiempo total en segundos es: {calculo_total_segundos}.")