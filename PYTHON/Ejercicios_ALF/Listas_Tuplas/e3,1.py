lista_asignatuiras=["Matemáticas", "Física", "Química", "Historia", "Lengua"]

for asignatura in lista_asignatuiras:
    p=input("¿Que nota has sacado en "+ str(asignatura +" ?"))

    for respuesta in p:
        print("Has sacado un " + str(p) + " en " + str(asignatura))



