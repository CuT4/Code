for i in range(5,50,2):
    print(f"valor de la variable {i}")

valido=False

email=input("Introduce tu email: ")

for i in range(len(email)):
    if email[i]=="@":
        valido=True
if valido:
    print("email correcto")
else:
    print("email incorrecto")
