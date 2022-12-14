def encriptar(texto):
    textoFinal=""
    for letra in texto:
        ascii=ord(letra)
        ascii+=3
        textoFinal+=chr(ascii)

    return textoFinal


def desEncriptar(texto):
    textoFinal=""
    for letra in texto:
        ascii=ord(letra)
        ascii-=3
        textoFinal+=chr(ascii)

    return textoFinal


def encriptarArchivo(rutaArchivo):
    archivo=open(rutaArchivo, "r")
    texto=archivo.read()
    archivo.close()
    textoencriptado=encriptar(texto)

    archivo=open(rutaArchivo, "w")
    archivo.write(textoencriptado)
    archivo.close()
    print("El archivo se encriptó correctamente")


def desEncriptarArchivo(rutaArchivo):
    archivo=open(rutaArchivo, "r")
    texto=archivo.read()
    archivo.close()
    textoDesEncriptado=desEncriptar(texto)

    archivo=open(rutaArchivo, "w")
    archivo.write(textoDesEncriptado)
    archivo.close()
    print("El archivo se desencriptó correctamente")


EoD=input("Escribe 'E' para  encriptar o escribe 'D' para desencriptar: ")
rutaArchivo=input("Introduce la ruta del archivo: ")

if EoD=="E":
    encriptarArchivo(rutaArchivo)

if EoD=="D":
    desEncriptarArchivo(rutaArchivo)



