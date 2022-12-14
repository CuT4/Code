clientes={}
opcion=""

while opcion != 6:

    if opcion==1:

        nif=input("introduce el NIF del cliente: ")
        nombre=input("Introduzca el nombre del cliente: ")
        direccion=input("Introduzca la dirección del cliente: ")
        telefono=input("Introduzca el teléfono del cliente: ")
        correo=input("Introduzca el correo del cliente: ")
        preferente=input("Preferencia (S/N): ")

        cliente={"nombre": nombre, "direccion": direccion, "telefono": telefono, "correo": correo, "preferente": preferente}

        clientes[nif]=cliente

    if opcion==2:
        nif=input("introduce el NIF del cliente: ")

        if nif in clientes:
            del clientes[nif]

        else:
            print("No tenemos clientes con NIF ", nif)
    
    if opcion==3:
        nif=input("introduce el NIF del cliente: ")

        if nif in clientes:
            print("NIF: ", nif)

            for clave, valor in clientes[nif].items():
                print(clave.title() + ": " + valor)

        else:
            print("No tenemos clientes con NIF ", nif)

    if opcion==4:

        for clave, valor in clientes.items():
            print(clave, valor["nombre"])

    if opcion==5:

        for clave, valor in clientes.items():

            if valor["preferente"]:
                print(clave, valor["nombre"])

opcion=int(input("(1)Añadir Cliente \n (2)Eliminar Cliente \n (3)Mostrar cliente \n (4)Todos Los Clientes \n (5)Clientes Preferentes \n (6)Terminar \nElige una opción: "))

            









