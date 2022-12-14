
numero1=int(input("Introduce un número: "))
numero2=int(input("Introduce un número mayor que " + str(numero1) + ":"))

while numero2>numero1:
    numero1=numero2
    numero2=int(input("Introduce un número mayor que " + str(numero1) + ":"))

print("Número 2 no es mayor que " + str(numero1) + ":")


