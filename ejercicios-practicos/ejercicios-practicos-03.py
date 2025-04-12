'''
Ejercicios python
Consejo: Revisar el concepto de split, cuidado con el tipo de datos a trabajar si es entero o
string.
1. Generar una lista de números
Pide al usuario un número n y usa un bucle while para generar una lista de los números del 1
al n.
Ejemplo:
Entrada: n = 5
Salida: [1, 2, 3, 4, 5]
'''
#solicitamos al usuario la cantidad de numeros a imprimir x consola.
cantidad_numeros_ingresados = int(input("Ingrese la cantidad de numero a imprimir: "))
#creamos la lista nueva
lista_numeros = []
#utilizamos bucle While para generar la lista de numeros
contador = 1
while contador <= cantidad_numeros_ingresados:
    lista_numeros.append(contador)
    contador += 1
print(lista_numeros)
'''''
2. Sumar elementos de una lista
Crea un programa que use un bucle for para sumar todos los números de una lista
proporcionada por el usuario.
Ejemplo:
Entrada: [3, 5, 7, 2]
Salida: La suma de los elementos es: 17
'''
print("Bienvenido.")
#solicitamos al usuario ingresar una lista de numeros
cantidad_numeros_ingresados = int(input("Ingrese la cantidad de numeros que ingresara: "))
#creamos la lista con los numeros ingresados
lista_numeros = []
#creamos el contador para activar el while
contador = 1
#creamos una variable que almacenara los numeros a sumar dentro del for
suma_numeros_lista = 0
#inicializamos el ciclo While para agregar numeros a la lista
while contador <= cantidad_numeros_ingresados:
    #solicitamos los numeros a sumar
    numero_ingresado = int(input("Ingrese un numero: "))
    #agregamos los numeros a la lista creada previamente
    lista_numeros.append(numero_ingresado)
    #aumentamos le contador para controlar el bucle While
    contador += 1
#verificamos que se agregen los numeros correctamente a la lista
print(lista_numeros)
#inicializamos un ciclo For para recorrer la lista
for i in lista_numeros:
    #capturamos los numeros de la lista y los sumamos
    suma_numeros_lista += i    
#imprimimos la suma de todos los numeros
print(suma_numeros_lista)
'''''
3. Filtrar números pares
Solicita una lista de números al usuario y usa un bucle for para agregar solo los números
pares a una nueva lista.
Ejemplo:
Entrada: [1, 2, 3, 4, 5, 6]
Salida: [2, 4, 6]
'''
print("Bienvenido.")
#solicitamos al usuario ingresar una lista de numeros
cantidad_numeros_ingresados = int(input("Ingrese la cantidad de numeros que ingresara: "))
#creamos la lista con los numeros ingresados
lista_numeros = []
#creamos la lista para almacenar los numeros pares
lista_numeros_pares = []
#creamos el contador para activar el while
contador = 1
#inicializamos el ciclo While para agregar numeros a la lista
while contador <= cantidad_numeros_ingresados:
    #solicitamos los numeros a sumar
    numero_ingresado = int(input("Ingrese un numero: "))
    #agregamos los numeros a la lista creada previamente
    lista_numeros.append(numero_ingresado)
    #aumentamos le contador para controlar el bucle While
    contador += 1
#verificamos que se agregen los numeros correctamente a la lista
print(lista_numeros)
#inicializamos un ciclo For para recorrer la lista
for i in lista_numeros:
    #capturamos los numeros de la lista y los sumamos
    if ( i % 2 == 0 ):
        lista_numeros_pares.append(i)    
#imprimimos la suma de todos los numeros
print(lista_numeros_pares)
'''''
4. Cálculo del promedio y evaluación
Escribe un programa que permita al usuario ingresar números (notas) hasta que escriba la
palabra "fin". El programa debe calcular el promedio de las notas ingresadas. Usa un bucle
while para obtener las notas y una condicional para determinar si el promedio indica que el
usuario aprobó o reprobó.
Condiciones:
Si el promedio es mayor o igual a 4.0, el usuario aprueba.
Si es menor a 4.0, el usuario reprueba.
Ejemplo:
Entrada: 5, 3, 4, fin
Salida:
El promedio es: 4.0
¡Aprobaste!
Entrada: 2, 3, fin
Salida:
El promedio es: 2.5
Reprobaste
'''
print("Bienvenido.")
#Condicionar el ingreso de notas.
#Si el usuario no ingresa la palabra 'fin' el programa debe continuar solicitando el ingreso de un valor.
contador = 1
lista_de_notas = []
#iniciamos el ciclo con 'contador' en 1, para no detener el programa.
while contador != 0:
    #Solicitar al usuario que ingrese una nota
    nota_ingresada = input('Ingrese una nota: ')
    if nota_ingresada != " " or nota_ingresada >= 0:
        #condicionamos el ingreso de los valores.
        if nota_ingresada == 'fin':
            contador = 0
        else:
            #agregamos los valores a la lista 'lista_de_notas'.
            lista_de_notas.append(nota_ingresada)
            #aumentamos el contador para seguir solicitando los valores.
            contador + 1    
    else:
        print('Ingrese una nota valida.')
#inicializamos el contador en 1 para recorrer las notas de la lista.
contador_nota = 0
#inicializamos la variable 'suma_nota' en 0 para poder sumar cada nota ingresada a la lista.
suma_nota = 0
#recorremos la lista con los valores.
for nota in lista_de_notas:
    suma_nota += float(nota)
while contador_nota < len(lista_de_notas):
    promedio = suma_nota / len(lista_de_notas)
    contador_nota += 1
print(promedio) 
#Condicionamos el promedio calculado
if promedio >= 4:
    print(f"El promedio es: {promedio}")
    print('Aprobaste')
else:
    print(f"El promedio es: {promedio}")
    print('Reprobaste')
