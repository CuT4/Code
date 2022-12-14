num=int(input("Introduce un número entero: "))
suma=0

while num>0:
    suma=suma+num
    num=int(input("Introduce otro número entero: "))

if num<0:
    print("No se tendrá en cuenta el último número introducido puesto que es negativo")

print("La suma de los números introducidos es: " + str(suma))