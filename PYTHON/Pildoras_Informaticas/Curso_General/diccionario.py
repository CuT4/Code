midiccionario={"Alemania":"Berlín", "Esapaña":"madrid", "Francia":"Milan"}
print(midiccionario)
#Cuando le escribo el nuevo valor para la clave "Francia", se sobreescribe
midiccionario["Francia"]="París"
print(midiccionario)
#para eliminar usar el método DEL
del midiccionario["Alemania"]
print(midiccionario)
#los diccionarios pueden tener texto y número
mitupla=["españa","reino unido", "alemania"]
diccionario={mitupla[0]:"madrid",mitupla[1]:"londres",mitupla[2]:"berlín"} 
print(diccionario)

