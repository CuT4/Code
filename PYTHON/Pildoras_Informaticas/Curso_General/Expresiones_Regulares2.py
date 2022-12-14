import re

lista_Nombres=["https://algo.com",
                "http://algo.es",
                "https://algo.com"]

for nombre in lista_Nombres:
    if re.findall(".com", nombre):
        print(nombre)