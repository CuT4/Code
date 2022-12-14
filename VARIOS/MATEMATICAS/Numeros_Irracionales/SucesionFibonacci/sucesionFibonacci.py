anterior=1
siguiente=1
lista=[1,1]
for i in range(20):
    a=anterior+siguiente
    lista.append(a)
    anterior=siguiente
    siguiente=a
print(lista)