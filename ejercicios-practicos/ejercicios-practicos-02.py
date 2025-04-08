'''
1. Conversión de kilogramos a gramos 
Escribe un programa que pida al usuario un número en kilogramos y lo convierta a 
gramos. 
Ejemplo: 
Entrada: Introduce el peso en kilogramos: 3 
Salida: El peso en gramos es: 3000 g 
'''
print("Bienvenido a la Calculadora convertidora de Kilos a Gramos.")
#Solicitamos al usuario ingresar una cantidad de Kilos
#Le asignamos el tipo de dato Float para aceptar kilos fraccionados
kilogramos = float(input("Introduce el peso en Kilogramos: "))
#Convertimos el peso en Kilos a Gramos
calculoGramosKilo = int(kilogramos * 1000)
#Imprimimos el resultado
print(f"El peso en gramos es: {calculoGramosKilo}g.")
'''''
2. Edad en el pasado 
Crea un programa que pida el nombre del usuario y su edad. Luego, calcula cuántos 
años tenía hace 5 años. 
Ejemplo: 
Entrada: 
Introduce tu nombre: Luis 
Introduce tu edad: 30 
Salida: 
Hola Luis, hace 5 años tenías 25 años. 
'''
print("Bienvenido a la Calculadora de Edad en el pasado.")
#Solicitamos que el usuario ingrese su Nombre
nombre = str(input("Introduce tu nombre: "))
#Solicitamos que el usuario ingrese su edad
edad = int(input("Introduce tu edad: "))
#Calculamos la edad que tenia el usuario hace 5 años atrás
calcularEdad = edad - 5
#Imprimimos el resultado
print(f"Hola {nombre}, hace 5 años tenías {calcularEdad} años.")
'''''
3. Área de un triángulo 
Pide al usuario la base y la altura de un triángulo, y muestra su área. 
Ejemplo: 
Entrada: 
Base: 6 
Altura: 4 
Salida: 
El área del triángulo es: 12 
'''
print("Bienvenido a la Calculadora de Area de un Triangulo.")
#Solicitamos al usuario que ingrese la Base del Triangulo
baseTriangulo = int(input("Ingresa el valor de la Base del triangulo: "))
#Solicitamos al usuario que ingrese la Altura del Triangulo
alturaTriangulo = int(input("Ingresa el valor de la Altura del triangulo: "))
#Realizamos la formula para calcular el area de un triangulo (base*altura)
calculoDeAreaTriangulo = int(baseTriangulo * alturaTriangulo / 2)
#Imprimimos el resultado
print(f"El area del triangulo es: {calculoDeAreaTriangulo}.")
'''''
4. Operaciones con dos números 
Pide al usuario dos números y muestra el módulo (resto de la división) y la potencia del 
primer número elevado al segundo. 
Ejemplo: 
Entrada: 
Primer número: 10 
Segundo número: 3 
Salida: 
Módulo: 1 
Potencia: 1000 
'''
print("Bienvenido a la Calculadora.")
#Solicitamos al usuario que ingrese el primer numero
primer_numero = int(input("Ingresa el primer numero: "))
#Solicitamos al usuario que ingrese el segundo numero
segundo_numero = int(input("Ingresa el segundo numero: "))
#Calculamos el Modulo/Resto de la division
calculo_modulo = primer_numero % segundo_numero
#Calculamos la potencia del primer numero elevado al segundo
calculo_potencia = primer_numero ** segundo_numero
#Imprimimos el resultado del Modulo
print(f"El Modulo es: {calculo_modulo}")
#Imprimimos el resultado de la Potencia
print(f"La Potencia es: {calculo_potencia}.")
'''''
5. Cálculo del descuento 
Pide al usuario el precio de un producto y un porcentaje de descuento. Calcula el precio 
final aplicando el descuento. 
Ejemplo: 
 Entrada: 
 Precio original: 200 
 Descuento: 15 
 Salida: 
 El precio final con descuento es: $170 
 '''
print("Bienvenido a la Calculadora.")
#Solicitamos al usuario que ingrese el precio original del producto
precio_producto = int(input("Ingresa el precio del producto: "))
#Solicitamos al usuario que ingrese el porcentaje de descuento
porcentaje_descuento = int(input("Ingresa el porcentaje de descuento: "))
#Calculamos el valor del porcentaje sobre el valor del producto
calculo_valor_porcentaje = int(precio_producto * (porcentaje_descuento /100))
#Calculamos el valor final del producto
valor_final_producto = int(precio_producto - calculo_valor_porcentaje)
#Imprimimos el resultado del valor final del producto
print(f"El precio final con descuento es: ${valor_final_producto}.")
'''''
 
6. Promedio de cuatro números 
 Solicita cuatro números al usuario y muestra su promedio. 
 Ejemplo: 
 Entrada: 
 Número 1: 4 
 Número 2: 6 
 Número 3: 8 
 Número 4: 10 
 Salida: 
 El promedio es: 7.0 
 '''
print("Bienvenido a la Calculadora.")
#Solicitamos al usuario que ingrese el primer numero
primer_numero = float(input("Ingresa el primer numero: "))
#Solicitamos al usuario que ingrese el segundo numero
segundo_numero = float(input("Ingresa el segundo numero: "))
#Solicitamos al usuario que ingrese el tercero numero
tercer_numero = float(input("Ingresa el tercer numero: "))
#Solicitamos al usuario que ingrese el cuarto numero
cuarto_numero = float(input("Ingresa el cuarto numero: "))
#Calculamos el promedio sumando los numeros y dividiendo el resultado por la cantidad de numeros ingresados
calculo_promedio = float((primer_numero + segundo_numero + tercer_numero + cuarto_numero) / 4)
#Imprimimos el resultado del promedio de los numeros ingresados
print(f"El promedio es: {calculo_promedio}")
'''''
7. Tiempo en minutos 
 Pide al usuario una cantidad de días, horas y minutos, y calcula el tiempo total en 
minutos. 
 Ejemplo: 
 Entrada: 
 Días: 1 
 Horas: 2 
 Minutos: 30 
 Salida: 
 El tiempo total es: 1650 minutos / son 1590 minutos.
 '''
print("Bienvenido a la Calculadora de minutos.")
#Solicitar al usuario que ingrese una cantidad de dias
dias = int(input("Ingrese una cantidad de dias: "))
#Solicitar al usuario que ingrese una cantidad de horas
horas = int(input("Ingresa una cantidad de horas: "))
#Solicitar al usuario que ingrese una cantidad de minutos
minutos = int(input("Ingrese una cantidad de minutos: "))
#Calcular tiempo total en minutos con los valores ingresados
#Transformar los dias en horas, luego transformar las horas en minutos
dias_en_minutos = (dias * 24) * 60 
#print(f"Dias en minutos: {dias_en_minutos}")
#Transformar las horas en minutos
horas_en_minutos = horas * 60
#print(f"Horas en minutos: {horas_en_minutos}")
#print(f"Cantidad de minutos: {minutos}")
#Calcular la suma de la cantidad de minutos totales
total_de_minutos = dias_en_minutos + horas_en_minutos + minutos
#Imprimimos el resultado del total de minutos.
print(f"El tiempo total es: {total_de_minutos}.")
'''''
8. Número al revés 
 Pide al usuario un número de tres dígitos y muéstralo al revés. 
 Ejemplo: 
 Entrada: 123 
 Salida: 321 
 '''
print("Bienvenido.")
#Solicitar al usuario que ingrese un numero de 3 digitos
numero_ingresado = str(input("Ingrese un numero de 3 digitos: "))
#Invertir los numeros
#Utilizare el metodo de 'corte' [inicio:fin] que sirve para invertir cadenas
#Este metodo funciona indicando una posicion de 'Inicio'=0 y una posicion de 'Fin'=N
#Para este caso utilizare el metodo de corte indicando el final con '-1' para invertir la cadena.
numero_invertido = numero_ingresado [::-1]
#Imprimir el numero final
print(numero_invertido)
'''
9. Suma de los dígitos de un número 
 Solicita al usuario un número de tres cifras y muestra la suma de sus dígitos. 
 Ejemplo: 
 Entrada: 527 
 Salida: La suma de los dígitos es: 14 
 '''
print("Bienvenido.")
#Solicitar al usuario que ingrese un numero de 3 digitos
numero_ingresado = str(input("Ingrese un numero de 3 digitos: "))
#print(type(numero_ingresado)) - valido el tipo de dato ingresado
#Separar los digitos del numero ingresado
primer_digito = int(numero_ingresado[0])
segundo_digito = int(numero_ingresado[1])
tercer_digito = int(numero_ingresado[2])
#Calcular la suma de los numeros 
calculo_suma = primer_digito + segundo_digito + tercer_digito
#Imprimir el resultado con el total de la suma
print(f"La suma de los digitos es: {calculo_suma}")
''' 
10. Conversión de millas a kilómetros 
 Pide al usuario una distancia en millas y conviértela a kilómetros (1 milla = 1.609 km). 
 Ejemplo: 
 Entrada: 5 
 Salida: La distancia en kilómetros es: 8.045 km 
 '''
print("Bienvenido.")
#Solicitar al usuario que ingrese una distancia en millas
millas_ingresadas = int(input("Ingrese una distacia en millas: "))
#Convertimos las millas en kilometros
kilometros = millas_ingresadas * 1609
#Imprimimos el resultado de la conversion
print(f"La distancia en kilometros es: {kilometros}km.")
'''
11. Cálculo de la hipotenusa 
 Pide al usuario la longitud de los dos catetos de un triángulo rectángulo y calcula la 
hipotenusa. 
 Ejemplo: 
 Entrada: 
 Cateto 1: 3 
 Cateto 2: 4 
 Salida: La hipotenusa es: 5.0 
 '''
#Import de libreria matematica
import math
print("Bienvenido.")
#Solicitar al usuario que ingrese los catetos de un triangulo rectangulo
#Solicitamos al usuario que ingrese el primer cateto
primer_cateto = float(input("Ingresa el primer cateto: "))
#Solicitamos al usuario que ingrese el segundo cateto
segundo_cateto = float(input("Ingresa el segundo cateto: "))
#Calculamos el valor de la hipotenusa
#Incorporamos la libreria 'math', para utilizar la funcion '.sqrt' para calcular la Raiz Cuadrada del resultado
calculo_hipotenusa = math.sqrt((primer_cateto ** 2) + (segundo_cateto ** 2))
#Verificamos le valor de la sumaa
print(calculo_hipotenusa)
'''
12. Cantidad de billetes 
 Pide al usuario una cantidad de dinero en dólares y calcula cuántos billetes de 100, 50, 
20, 10, 5 y 1 se necesitan para formar esa cantidad. 
 Ejemplo: 
 Entrada: 186 
 Salida: 
 1 billete de 100 
 1 billete de 50 
 1 billete de 20 
 1 billete de 10 
 1 billete de 5 
 1 billete de 1 
 '''
print("Bienvenido.")
#Solicitar al usuario que ingrese la cantidad de dinero.
dinero_ingresado = int(input("Ingrese la cantidad de dinero a consultar: "))
#Calcular cuantos billetes de 100 contiene el monto.
calculo_billete_cien = dinero_ingresado / 100
print(f"{int(calculo_billete_cien)} billete de 100.")
dinero_actualizado = dinero_ingresado - (int(calculo_billete_cien) * 100) 
#print(int(dinero_actualizado))
#Calcular cuantos billetes de 50 contiene el monto.
calculo_billete_cincuenta = dinero_actualizado / 50
print(f"{int(calculo_billete_cincuenta)} billete de 50.")
dinero_actualizado = dinero_actualizado - 50 
#Calcular cuantos billetes de 20 contiene el monto.
calculo_billete_veinte = dinero_actualizado / 20
print(f"{int(calculo_billete_veinte)} billete de 20.")
dinero_actualizado = dinero_actualizado - 20 
#Calcular cuantos billetes de 10 contiene el monto.
calculo_billete_diez = dinero_actualizado / 10
print(f"{int(calculo_billete_diez)} billete de 10.")
dinero_actualizado = dinero_actualizado - 10 
#Calcular cuantos billetes de 5 contiene el monto.
calculo_billete_cinco = dinero_actualizado / 5
print(f"{int(calculo_billete_cinco)} billete de 5.")
dinero_actualizado = dinero_actualizado - 5
#Calcular cuantos billetes de 1 contiene el monto.
calculo_billete_uno = dinero_actualizado / 1
print(f"{int(calculo_billete_uno)} billete de 1.")
'''''
13. Número par o impar 
 Pide al usuario un número y determina si es par o impar. 
 Ejemplo: 
 Entrada: 7 
 Salida: El número es impar. 
 '''
print("Bienvenido.")
#solicitamos al usuario que ingrese un numero para validar si es par o impar
numero_ingresado = int(input("Ingrese un numero: "))
#creamos la condicion para validar si es Par o Impar
if ( numero_ingresado % 2 == 0 ):
    print(f"El numero ingresado {numero_ingresado} es Par.")
else:
    print(f"El numero ingresado {numero_ingresado} es Impar.")
'''''
14. Cálculo del perímetro de un círculo 
 Pide al usuario el radio de un círculo y calcula su perímetro (P = 2πr). 
 Ejemplo: 
 Entrada: 
 Radio: 5 
 Salida: 
 El perímetro del círculo es: 31.42 
'''
print("Bienvenido.")
#solicitamos que ingrese el radio de un circulo.
radio = int(input("Ingrese el Radio del circulo: "))
calculo_perimetro_circulo = (2 * 3.14) * (radio)
redondeo_perimetro = "{:.2f}".format(calculo_perimetro_circulo)
print(float(redondeo_perimetro))
'''''
15. Conversión de temperatura 
 Pide al usuario una temperatura en grados Celsius y conviértela a Fahrenheit. (F = C × 
9/5 + 32) 
 Ejemplo: 
 Entrada: 
 Temperatura en °C: 25 
Salida: 
La temperatura en Fahrenheit es: 77°F
'''
print("Bienvenido.")
#solicitamos la usuario ingresar los grados en celsius
grados_celsius = float(input("Ingrese los grados Celsius: "))
#Calculamos la formula de transformacion
calculo_fahrenheit = (grados_celsius * (9/5)) + 32
print(f"La temperatura en Fahrenheit es: {calculo_fahrenheit}°F.")