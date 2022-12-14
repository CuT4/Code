#nif;nombre;email;teléfono;descuento

clientes={}



opcion=""

while opcion!=3:

    continuar=input("¿Quieres añadir un cliente? (S/N): ")

    if continuar=="S":

        nif=input("Introduce tu NIF: ")
        nombre=input("Introduce tu nombre: ")
        email=input("Introduce tu email: ")
        telefono=input("Introduce tu número de descuento: ")

        cliente={"nombre":nombre, "email":email, "telefono":telefono}
        clientes[nif]=cliente

    else:
        break

for clave, valor in clientes.items():
    print(clientes[nif], clave, valor["nombre"])
    
    






