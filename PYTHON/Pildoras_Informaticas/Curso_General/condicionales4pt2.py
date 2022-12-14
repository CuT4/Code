print("Asignaturas optativas año 2021")
print("Inglés-Francés-Cultura_Clásica")
asignatura=input("Introduce la asignaturas que has de escoger para el curso que viene: ")
option=asignatura.lower()
if option in("inglés","francés","cultura clásica"):
    print("Asignatura escogida:" + option)
else:
    print("La asignatura escogida no está disponible.")
