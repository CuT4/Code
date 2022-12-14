diccionario={'Euro':'€', 'Dollar':'$', 'Yen':'¥'}

pregunta=input("Introduce un divisa: ")

print(diccionario.get(pregunta.title(), "La divisa no está"))