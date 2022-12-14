nombreUS=input("Introduzca su nombre: ")
passwordUS=input("Introduzca su contraseña para posteriormente iniciar sesión: ")

print("Procederemos a iniciar sesion...")

nom=input("Introduzca su nombre, por favor: ")
con=input("Introduzca su contraseña, por favor: ")

if nom + con == nombreUS + passwordUS:
    print("Los datos introducidos son corrcetos")

else:
    print("Los datos introducidos no son correctos")