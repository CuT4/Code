print("Le pediremos dos números para dividir el primero entre el segundo.")

n1=int(input("INtroduzca su primer numero, por favor: "))
n2=int(input("Introduzca se segundo número si es tan amable: "))

try:
    if n1/n2 !=1:
        print(str(n1) + " entre " + str(n2) + " da como resultado " + str(n1/n2))
    
   
except:
    print("No se puede dividir entre cero")


