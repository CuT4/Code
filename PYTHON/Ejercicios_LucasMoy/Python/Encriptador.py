#archivo=open("texto.txt", "a")
#archivo.write("prueba de guardado en el archivo")
#archivo.close()

"""Creamos la funcion encriptar, ya que es un encriptador,
y va a servir para enciptar archivos, para ello nos ayudamos
de la función "ord()" para pasar a valor numérico cualquier
caracter según la tabla ASCII.
"""
def encriptar(texto):

    textoFinal=""
    for letra in texto:
        ASCII=ord(letra)
        ASCII+=4
        textoFinal+=chr(ASCII)
    
    return textoFinal

"""El textoFinal hace referencia al texto resultante de la función,
por cada letra en el texto, "ord(letra)" pasa los caracteres al
número correspondiente en la tabla ASCII, le sumamos el número que
queramos para así que se guarde como otro caracter de la tabla ASCII
que no es el que hemos escrito anteriormente. Con la función "chr()",
pasamos el número de la tabla ASCII a un caracter legible, pero que
es aquel que corresponda con otro caracter de la tabla que esté a
una distancia igual a la cantidad de que le hemos sumado con "ord()". 
"""


def desencriptar(texto):


    textoFinal=""


    for letra in texto:
        ASCII=ord(letra)
        ASCII-=4
        textoFinal+=chr(ASCII)
    return textoFinal

"""Esta función es parecida a la enterior pero, en lugar de
sumar una cantidad después de haber aplicado la función
"ord()" para los caracteres que hayamos escrito se correspondan con 
aquella distancia sumada, en esta función debemos restar la 
cantidadantes aplicada para que así vuelva el texto a ser el que nosotros
hemos escrito.
"""


def encriptarArchivo(rutaArchivo):

    archivo= open(texto, "r")
    texto=archivo.read()
    textoEncriptado=encriptar(texto)
    archivo.close()
    


    archivo=open(texto, "w")
    archivo.write(textoEncriptado)
    archivo.close()

    print("El archivo se encriptó correctamente")

"""Esta función se encarga de seleccionar la ruta
del archivo a encriptar en cuestión. Primero abre el archivo
en modo lectura, luego lo lee, y lo cierra. El texto se guarda
en la variable "textoEncriptado" que utiliza la anterior función
"encriptar()". Vuelve a abrir el archivo, pero esta vez en modo
de escritura para escribir en él lo que se ha conseguido con
"textoEncriptado". Se cierra el archivo, ahora ya encriptado
"""

def desencriptarArchivo(rutaArchivo):

    archivo= open(texto, "r")
    texto=archivo.read()
    textoDesEncriptado=desencriptar(texto)
    archivo.close()
    


    archivo=open(texto, "w")
    archivo.write(textoDesEncriptado)
    archivo.close()

    print("El archivo se ha desencriptado correctamente")

"""Esta función es parecida a la anterior pero hace lo
opuesto a ella. Abre el archivo en modo lectura, lo lee, y lo cierra.
Guarda en la variable "textoDesEncriptado" el texto en los caracteres
introducidos originalmente gracias a utilizar la función "desencriptar()"
Abre de nuevo el archivo, esta vez en modo de escritura para sobreescribir
los caracteres encriptados con los caracteres originales.Cierra el archivo.
"""


EoD=input("Escribe 'E' para  encriptar o escribe 'D' para desencriptar: ")
rutaArchivo=input("Introduce la ruta del archivo: ")

if EoD=="E":
    encriptarArchivo(rutaArchivo)

if EoD=="D":
    desencriptarArchivo(rutaArchivo)

"""Estas últimas líneas de código preguntan al usuario si quiere
encriptar o desencriptar algún archivo. Si responde "E" encripta un archivo
llamando a la función "encriptarArchivo()", y si responde "D" desencripta
un archivo llamando a la función "desencriptarArchivo()".
"""




