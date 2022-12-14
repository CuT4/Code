"""
Este programa calcula tu indice de masa corporal
"""

peso=float(input("Introduce tu peso en kilogramos: "))
altura=float(input("Introduce tu altura en metros: "))

imc=peso*altura/2

print("Tu indice de masa corporal es: ", str(imc))