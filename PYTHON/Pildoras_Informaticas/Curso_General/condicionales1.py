print("Notas finales de examenes")
nota_alumno=input("Introduce tu nota media: ")

def evaluación(nota):

    if nota>5:
        print("Felicidades has aprobado!")
    if nota<5:
        print("Lo sentimos, has suspendido")

print(evaluación(int(nota_alumno)))