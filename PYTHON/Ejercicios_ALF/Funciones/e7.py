def al_cuadrado(*nums):

    lista=[]

    for i in nums:
        
        lista.append(i**2)

    return lista

print(al_cuadrado(8, 9, 10))
print(al_cuadrado(2, 14, 7))
