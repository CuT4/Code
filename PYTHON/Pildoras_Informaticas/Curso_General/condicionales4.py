print("Programa de becas año 2021")

distancia_escuela=int(input("Introduce la distancia a la escuela en kilómetros: "))
print(distancia_escuela)
numero_de_hermnanos=int(input("Introduce el número de hermanos del solicitante: "))
print(numero_de_hermnanos)
salario_familiar=int(input("Introduce salario familiar anual bruto: "))
print(salario_familiar)

if distancia_escuela>40 and numero_de_hermnanos>2 or salario_familiar<40000:
    print("Tienes derecho a beca")

else:
    print("No tienes derecho a beca")
