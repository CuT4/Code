print("Tu cuenta de ahorros cuneta con\nun rendimiento anual de un 8%")

cantidad=float(input("Introduce la cantidad a depositar: "))

rendimiento=1+(8/100)

a1=cantidad*rendimiento
a2=a1*rendimiento
a3=a2*rendimiento
a4=a3*rendimiento
a5=a4*rendimiento
a6=a5*rendimiento
a7=a6*rendimiento
a8=a7*rendimiento
a9=a8*rendimiento
a10=a9*rendimiento

print("En un año tendrás: " + str(a1) + "€")
print("En dos años tendrás: " + str(a2) + "€")
print("En tres años tendrás: " + str(a3) + "€")
print("En cuatro años tendrás: " + str(a4) + "€")
print("En cinco años tendrás: " + str(a5) + "€")
print("En seis años tendrás: " + str(a6) + "€")
print("En siete años tendrás: " + str(a7) + "€")
print("En ocho años tendrás: " + str(a8) + "€")
print("En nueve años tendrás: " + str(a9) + "€")
print("En 10 años tendrás: " + str(a10) + "€")
