diccionario={'Matemáticas': 6, 'Física': 4, 'Química': 5}
total_creditos=0

for asiganatura, creditos in diccionario.items():

    print(asiganatura, " tiene ", creditos, " créditos")

    total_creditos+=creditos

print("En total hay ", str(total_creditos), " créditos")  