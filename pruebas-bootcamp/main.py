def main():
  addmultiplenumbers()
  multiplymultiplenumbers()
  isiteven()
  isitaninteger()
#Las funciones de calculo deben ir fuera de la función main()
#Debe sumar N cantidad de numeros de una lista.
def addmultiplenumbers(*num):
    list_numbers = num
    add_numbers = 0
    for i in list_numbers:
        list_on_list = i
        for x in list_on_list:
            add_numbers += x
    return add_numbers
   # return print(add_numbers)

#Debe multiplicar N cantidad de numeros de una lista.
def multiplymultiplenumbers(*num):
    list_numbers = num
    multiply_numbers = 1
    for x in list_numbers:
        list_on_list_multiply = x
        for i in list_on_list_multiply:
            multiply_numbers *= i
    return multiply_numbers
    #return print(multiply_numbers)
#Validar si el número es Par y Entero
def isiteven(num):
    if num%2 == 0 and isinstance(num,int):
        isParInt = True 
    else:
        isParInt = False
    return isParInt
    #return print(isParInt)

#Validar si el número Entero
def isitaninteger(num):
    isInteger = False
    if isinstance(num, int) or type(num) == int or num == int(num):
        isInteger = True
    else:
        isInteger = False
    return isInteger
    #return print(isInteger)

#addmultiplenumbers([5,7,9])
#multiplymultiplenumbers([2,2,2,10])
#isiteven(6.5)
#isitaninteger(6.5)

if __name__=="__main__":
    main()