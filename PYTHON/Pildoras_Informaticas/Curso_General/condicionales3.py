
salario_presidente=int(input("Introduce salario presidente: "))
print("Salario presidente: " + str(salario_presidente))

salario_director=int(input("Introduce salario director: "))
print("Salario director: " + str(salario_director))

salario_jefe_area=int(input("Introduce salario jefe de area: "))
print("Salario jefe de area: " + str(salario_jefe_area))

salario_administrativo=int(input("Introduce salario administrativo: "))
print("Salario administrativo: " + str(salario_administrativo))

if salario_administrativo<salario_jefe_area<salario_director<salario_presidente:
    print("Todo correcto")
else:
    print("Algo va mal en esta empresa")

