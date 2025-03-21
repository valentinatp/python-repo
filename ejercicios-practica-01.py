print("Bienvenido a la Calculadora de Segundos.")
hora = int(input("Ingresa una cantidad de horas: "))
minuto = int(input("Ingresa una cantidad de minutos: "))
segundo = int(input("Ingresa una cantidad de segundos: "))
#Para calcular de horas a segundos se debe múltiplicar
# la cantidad de horas * 60 (transforma a minutos) * 60 (transforma a segundos)
# otra opcion en un solo paso: cantidad de horas * 3600 (60 minutos * 60 segundos) 
calculo_segundos_hora = hora * 60 * 60
#Para calcular minutos a segundos
calculo_segundos_minuto = minuto * 60
#Total de segundos
calculo_total_segundos = int(calculo_segundos_hora + calculo_segundos_minuto + segundo)
print(f"El tiempo total en segundos es: {calculo_total_segundos}.")

