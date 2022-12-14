import math

def calcula_raiz(num1):

    if num1<0:
        raise ValueError ("No hay raices cuadradas de numeros negativos")
    else:
        return math.sqrt(num1)

op1=int(input("Introduce un numero: "))
try:
    print(calcula_raiz(op1))
except ValueError as ErrorNumeroNegativo:
    print(ErrorNumeroNegativo)
    


print("Finalizado")