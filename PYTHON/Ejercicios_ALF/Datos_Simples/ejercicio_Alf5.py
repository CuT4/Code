"""Escribir un programa que pregunte al usuario
por el número de horas trabajadas y el coste por hora.
Después debe mostrar por pantalla la paga que le corresponde.
"""

horas_trabajo=int(input("Introduce el número de horas trabajadas: "))
cobro_hora=int(input("Introduce a cuánto se paga la hora de trabajo: "))

salario=horas_trabajo*cobro_hora

print("Te correcponde un salario de " + str(salario))