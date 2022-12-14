payaso=112
munheca=75

cobran=0.3

numero_payasos=input("Introduce el número de payasos vendidos: " )
numero_munhecas=input("Introduce le numero de muñecas vendidas: ")

peso_payasos=payaso*(int(numero_payasos))
peso_munhecas=munheca*(int(numero_munhecas))

costeTotal=(peso_munhecas+peso_payasos)*cobran
print(costeTotal)