"""
Óscar, esto es una 'calculadora' capcaz de hacer las siguientes operaciones:
-Sumar: Se le sumarán al primer número todos los números siguientes.
-Restar: Le resta al primer número que le pases todos los siguientes.
-Multiplicar: Se multiplicará el primer número por todos los siguientes.
-Dividir: El primer número será dividido entre los siguientes.

INSTRUCCIONES: 
1.  No importa si vas a sumar, restar, multiplicar o dividir: Introduce el primer número y siempre
    los siguientes separados por espacios (esto simplifica la promgramación)

2. Lee bien qué es lo que te dice por la terminal.

NOTA: Se pueden usar números positivos, negativos, enteros y decimales (en forma de fraccion no son válidos)
    Recuerda que si estás usando la función de restar, por ejemplo, 123-34 = 123-(-34) = 123+34;
    Por lo tanto al sumar es lo mismo: 73-56 = 73+(-56) = 73-56
    (Esto ya es más de matemáticas, concretamente de 1ºESO)

RETO: Te reto a que comentes este código, es decir, que expliques que hace cada línea simplificando lo 
    máximo posible pero que se entienda. Si hay algo que no conozcas búscalo en internet primero, estas pueden
    ser cosas como '.pop()' o '.split()'. Debes comentar las funciones y los condicionales.
    No te rayes si no te sale a la primera, es normal, comentar código ageno requiere leerlo varias veces además
    de entender que es lo que hace y cómo lo hace.
    (Diría que para un desarroyador master de python este ejercicio tiene dificultad inferior a 1/10)
    Son condicionales y funciones básicamente, cosas que ya conoces bien, tú puedes hacerlo Óscar.
"""


#---------COLORES---------------------------------------------------------------------------------------------------
"""
Este apartado es meramente estético. Sirve para poder imprimir mensages de colores.
No es necesario para que el programa funcione. TE LO PUEDES SALTAR
"""
class bcolors:
    OK = '\033[92m' #GREEN
    WARNING = '\033[93m' #YELLOW
    FAIL = '\033[91m' #RED
    RESET = '\033[0m' #RESET COLOR

#---------SELECCIÓN INICIAL---------------------------------------------------------------------------------------------------
inicial=input("Sumar (s), Restar (r), Multiplicar (m), Dividir (d): ")

#---------FUNCIONES---------------------------------------------------------------------------------------------------
def pasarArray(string):
    arrayString=string.split()
    arrayNumber=[]
    for i in arrayString:
        arrayNumber.append(float(i))
    return arrayNumber

#---------FUNCIONES OPERADORES---------------------------------------------------------------------------------------------------
def sumar(n):
    print(n)
    resultado=n[0]
    n.pop(0)
    for i in n:
        resultado+=i
    return resultado

def restar(n):#Funciona
    print(n)
    resultado=n[0]
    n.pop(0)
    for i in n:
        resultado-=i
    return resultado

def multiplicar(n):#Funciona
    print(n)
    resultado=n[0]
    n.pop(0)
    for i in n:
        resultado*=i
    return resultado

def dividir(n):#Funciona
    print(n)
    resultado=n[0]
    n.pop(0)
    for i in n:
        resultado/=i
    return resultado

#---------CONDICIONES---------------------------------------------------------------------------------------------------
if inicial.lower()=="s":
    terminos=input("(Separados por espacios) Introduce los números a sumar: ")
    numeros=pasarArray(terminos)
    print(bcolors.OK , "Resultado:" , sumar(numeros) , bcolors.RESET)#Se puede hacer un print normal (Está así por los colores)

elif inicial.lower()=="r":
    terminos=input("(Separados por espacios) Al primer número se le restarán los siguientes: ")
    numeros=pasarArray(terminos)
    print(bcolors.OK ,"Resultado:" , restar(numeros) , bcolors.RESET)#Se puede hacer un print normal (Está así por los colores)

elif inicial.lower()=="m":
    terminos=input("(Separados por espacios) Se multiplicarán los siguientes números: ")
    numeros=pasarArray(terminos)
    print(bcolors.OK ,"Resultado:" , multiplicar(numeros) , bcolors.RESET)#Se puede hacer un print normal (Está así por los colores)

elif inicial.lower()=="d":
    try:
        terminos=input("(Separados por espacios) El primer número será dividido entre los siguientes: ")
        numeros=pasarArray(terminos)
        print(bcolors.OK ,"Resultado:" , dividir(numeros) , bcolors.RESET)#Se puede hacer un print normal (Está así por los colores)

    except:
        print(bcolors.FAIL , "Lo siento, no se puede dividir entre cero" , bcolors.RESET)#Se puede hacer un print normal (Está así por los colores)
        print(ZeroDivisionError)

else:
    print(bcolors.WARNING , "---Opción no válida---" , bcolors.RESET)#Se puede hacer un print normal (Está así por los colores)
        
