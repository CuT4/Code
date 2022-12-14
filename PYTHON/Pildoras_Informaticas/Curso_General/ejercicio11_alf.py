print("Bienvenido a tu banco de confianza.\nEl inetrés de tu cuenta de ahorros es del 4%")

dinero_cliente=int(input("Introduce la cantidad de dienro a depositar: "))

interés=4/100

ano1=float(dinero_cliente+(interés*dinero_cliente))
ano2=float(interés*ano1)
ano3=float(interés*ano2)

print("La cantidad tras un año será: ", ano1)
print("La cantidad tras dos años será: ", ano2)
print("La cantidad tras tres años será: ", ano3)

