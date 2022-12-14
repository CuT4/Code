correoUS=input("Introduce tu correo electrónico: ")

if "@" in correoUS:
    pass

else:
    print("La direccion de correo no es correcta")


print(correoUS[:correoUS.find("@")] + "@ceu.es")

