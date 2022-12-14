contador=0
email_cliente=input("Introduce tu correco: ")

for i in email_cliente:

    if (i=="@" or i=="."):

        contador=contador+1
        
if contador==2:
    print("El email es correcto")
else:
    print("El email es incorrecto")
    
