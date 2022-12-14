
edad=int(input("Introduce la edad: "))

while edad<12 or edad>100:
    print("Edad incorrecta")
    edad=int(input("Introduce la edad de nuevo: "))

if edad>=12:
    print("edad correcta")


print("Gracias por confiar en nosotros")
print("Tu edad es " + str(edad))
