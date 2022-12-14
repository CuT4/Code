frase=input("Introduzca un frase, por favor: ")
letra=input("Introduzca una letra: ")
contador=0

for i in frase:
    if i==letra:
        contador+=1

print("La frase tiene " + str(contador) + " veces la letra " + letra)

    