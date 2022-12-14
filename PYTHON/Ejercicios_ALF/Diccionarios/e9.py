"""
Escribir un programa que gestione las facturas pendientes de cobro de una empresa. 
Las facturas se almacenarán en un diccionario donde la clave de cada factura será 
el número de factura y el valor el coste de la factura. 
El programa debe preguntar al usuario si quiere añadir una nueva factura, pagar una existente o terminar. 
Si desea añadir una nueva factura se preguntará por el número de factura y su coste y se añadirá al diccionario. 
Si se desea pagar una factura se preguntará por el número de factura y se eliminará del diccionario. 
Después de cada operación el programa debe mostrar por pantalla la cantidad cobrada hasta el momento y la cantidad pendiente de cobro.


"""



from select import select


diccionario={}

n_factura=()
valor=()
continuar=True

while continuar:

    n_factura=input("Introduce el número de la factura: ")
    valor=int(input("Introduce el valor del cobro: "))

    diccionario[n_factura]=valor

    continuar=input("¿Desea añadir más facturas? ")=="si"

p=input("¿Desea pagar alguna factura existente? ")

if p=="si":
    print(diccionario)
    seleccion=int(input("¿Que factura quieres pagar?"))

diccionario.get(seleccion)

cantidad_a_pagar=print("Tienes que pagar "+ str(seleccion)+ "€")

cantidad_pagada=int(input("Introduce la cantidad a pagar: "))

if cantidad_pagada==diccionario.get(seleccion):
    diccionario.pop(seleccion)
    print("Tu deuda está saldada")

else:
    print("La cantidad no es suficiente")




