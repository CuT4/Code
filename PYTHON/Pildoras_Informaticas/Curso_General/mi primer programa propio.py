
email_cliente=input("Introduce tu direcciónn de correo electrónico: ")

for i in email_cliente:

    if i=="@" or i==".":
        arrobas=email_cliente.count("@")
        puntos=email_cliente.count(".")

if arrobas>=2:
    print("No puedes poner más de dos arrobas en el correo")

if arrobas==1:
    print("El número de arrobas es correcto")

print("El número de puntos del email es: " + str(puntos)) 

