import re

listaNombres=["Ma1",
                "Pa1",
                "Ce1",
                "Al1",
                "Ma2",
                "Se1",
                "Ma3"]

for elemento in listaNombres:
    if re.findall("Ma[0-3]", elemento):
        print(elemento)