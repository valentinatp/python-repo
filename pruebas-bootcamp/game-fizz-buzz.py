#El programa debe imprimir 1000 números, si el número es divisible por 3 y 5 debe imprimir 'Fizzbuzz', si el número es divisible por 5 debe imprimir 'Buzz', si el número es divisible por 3 debe imprimir 'Fizz'.
#============================================================#
#Crear una variable que genere el rango limite de juego, le sumamos (+1) porque la funcion Range resta -1 al numero final.
limite_juego = int(input("Ingrese un numero para establecer un limite en el juego: "))+1
#Recorremos la lista de numeros
for i in range(1,limite_juego):
    #Evaluamos si el numero es divisible por 3 y 5
    if i%3 == 0 and i%5 == 0:
        #Imprimimos el valor de Fizzbuzz para reemplazar el numero
        print('Fizzbuzz')
    #Evaluamos si el numero es divisible por 5
    elif i%5 == 0:
        #Imprimimos el valor de Buzz para reemplazar el numero
        print('Buzz')
    #Evaluamos si el numero es divisible por 3
    elif i%3 == 0:
        #Imprimimos el valor de Fizz para reemplazar el numero
        print('Fizz')
    #Si el numero evaluado no coincide con ninguna condicion, se imprime el valor del numero
    else:
        print(i)