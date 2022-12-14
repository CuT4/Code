contrasenhaUS=input("Crea tu contraseña para posteriormente inciniar secion: ")

password_Beggin=input("Introduce tu contraseña: ")


while password_Beggin!=contrasenhaUS:
    password_Beggin=input("Introduce tu contraseña: ")

if password_Beggin==contrasenhaUS:
    print("La contraseña es correcta")