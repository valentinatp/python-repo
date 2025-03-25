'''
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
#Calculamos el valor 
porcentaje_descuento = int(input("Ingresa el porcentaje de descuento: "))
#Calculamos el valor del porcentaje sobre el valor del producto
calculo_valor_porcentaje = int(precio_producto * (porcentaje_descuento /100))
#Calculamos el valor final del producto
valor_final_producto = int(precio_producto - calculo_valor_porcentaje)
#Imprimimos el resultado del valor final del producto
print(f"El precio final con descuento es: ${valor_final_producto}.")