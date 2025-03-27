#Calcular la suma entre dos numeros e imprimir el resultado.
#Solicitar al usuario que ingrese el primer número.
primer_numero = float(input("Ingrese el primer numero: "))
#Solicitar al usuario que ingrese el segundo número.
segundo_numero = float(input("Ingrese el segundo numero: "))
#Preguntar al usuario que calculo quiere realizar con los numeros ingresados.
# 1: Suma
# 2: Resta
# 3: Multiplicacion
# 4: Division
# 5: Modulo
print("Escoje el calculo a realizar.")
print(f"Opciones de calculo: 1: Suma, 2: Resta, 3: Multiplicacion, 4: Division, 5: Modulo")
calculo_elegido = int(input("Ingrese el numero de la operacion a realizar: "))
print(f"Eleccion de usuario: {calculo_elegido}.")
if calculo_elegido == 1:
    #Calcular la suma entre ambos números.
    calculo_suma = primer_numero + segundo_numero
    #Imprimir el resultado de la suma entre ambos números.
    print(f"El resultado de la suma de ambos numeros es: {calculo_suma}")
elif calculo_elegido == 2:
    #Calcular la resta entre ambos numeros.
    calculo_resta = primer_numero - segundo_numero
    #Imprimir el resultado de la resta entre ambos números.
    print(f"El resultado de la resta de ambos numeros es: {calculo_resta}")
elif calculo_elegido == 3:
    #Calcular la multiplicacion entre ambos numeros.
    calculo_multiplicacion = primer_numero * segundo_numero
    #Imprimir el resultado de la multiplicacion entre ambos números.
    print(f"El resultado de la multiplicacion de ambos numeros es: {calculo_multiplicacion}")
elif calculo_elegido == 4:
    #Calcular la division entre ambos numeros.
    calculo_division = primer_numero / segundo_numero
    #Imprimir el resultado de la division entre ambos números.
    print(f"El resultado de la division de ambos numeros es: {calculo_division}")
elif calculo_elegido == 5:
    #Calcular el modulo de ambos numeros.
    calculo_modulo = primer_numero % segundo_numero
    #Imprimir el resultado de la modulo entre ambos números.
    print(f"El resultado del modulo de ambos numeros es: {calculo_modulo}")
else:
    print("Ingrese un numero valido entre 1 a 5.")



