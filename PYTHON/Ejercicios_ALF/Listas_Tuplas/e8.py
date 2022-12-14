


palabra=input("Introduce una palíndromo: ")
reverse_palabra=palabra

palabra=list(palabra)
reverse_palabra=list(reverse_palabra)

reverse_palabra.reverse()

if palabra==reverse_palabra:
    print("Tu palabra es un palíndromo")

else:
    print("La palabra introducida no es un palíndromo")

