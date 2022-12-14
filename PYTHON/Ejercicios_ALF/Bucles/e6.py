n=int(input("Introduce un numero entero: "))

asterisco1="*"

for i in range(n):
    for i in range(i+1):
        print("*", end="")
    print("")
    
