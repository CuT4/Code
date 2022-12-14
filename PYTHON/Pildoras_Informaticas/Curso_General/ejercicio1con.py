#Crea un programa que pida dos números por teclado. El programa tendrá una función llamada 
#DevuelveMax” encargada de devolver el número más alto de los dos introducidos.

print("Vas a introducir dos números")

n1=int(input("Introduce un número: "))
n2=int(input("Introduce otro número: "))

def DevuelveMax(num1,num2):
    if n1<n2:
        print(n1,"Es menor que ",n2)
    elif n1>n2:
        print(n1,"Es mayor que",n2)
    else:
        print("son iguales")

DevuelveMax(n1,n2)
