from types import coroutine


correo_electronico=input("Introduce tu correo electrónico: ")

arroba=correo_electronico.count("@")

if(arroba!=1 or correo_electronico.rfind("@")==(len(correo_electronico)-1) or correo_electronico.find("@")==0):
    print("Mail incorrecto")
else:
    print("Mail correcto")



            

