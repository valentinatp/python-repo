'''
Hoja para realizar los ejercicios practicos
'''
'''
Ejercicios python
Consejo: Revisar el concepto de split, cuidado con el tipo de datos a trabajar si es entero o
string.
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
