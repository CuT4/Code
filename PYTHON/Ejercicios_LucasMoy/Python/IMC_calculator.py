#Calculadora de IMC= peso/ altura**2

# <19:Delgado
# Entre 20 y 25: Normal
# Entre 26 y 30: Sobrepeso
# Más de 30: Obesidad




peso=float(input("¿Cuál es tu peso en kg? "))
altura=float(input("¿Cuál es tu altura en metros? "))

imc=peso/altura**2

if imc<20:
    print("Estás delgado")
if imc>=20 and imc<=25:
    print("Estás bien")
if imc>=26 and imc<=30:
    print("Estás gorso")
if imc>30:
    print("Estás obeso")
