datos={}
continuar=True

while continuar:
    clave=input("¿Que tipo de datos quieres guardar? ")
    valor=input(clave + ": ")

    datos[clave]=valor

    continuar=input("¿Desear continuar añadiendo datos? si/no: ")=="si"

print(datos)