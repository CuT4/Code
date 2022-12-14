edad=input("Introduce edad: ")

while (edad.isdigit()==False):
    print("Por favor, introduce un número")
    edad=input("Introduce edad: ")

if(int(edad)<18):
    print("No puede pasar")

else:
    print("Puede pasar")


