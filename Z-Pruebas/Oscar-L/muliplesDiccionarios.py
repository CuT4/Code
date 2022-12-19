#Importo la librería random para poner notas aleatorias a los usuarios/alumnos
import random

#Creo el array 'alumnos' (se pueden poner cuantos se deseen)
alumnos=["OSCAR", "MARIA DEL CARMEN","ANTONIO", "MARIA", "MANUEL", "CARMEN", "JOSE", "ANA MARIA", "FRANCISCO", "MARIA PILAR", "DAVID",	"LAURA", "PILAR"]
#Creo el array 'materias' (se pueden poner cuantas se deseen)
materias=["matemáticas", "FQ", "EF", "plástica", "historia", "geografía", "castellano", "TIC", "Cuci", "biología"]
nombre={}
max=len(materias)
#La función 'crear(name)' recibe un nombre y con él completa el valor 'Nombre' en un diccionario
def crear(name):
    #Itetrará tantas veces como alumnos haya
    #El nombre es la primera clave-valor
    nombre["Nombre: "]=name
    for i in range(len(alumnos)):
        """
        Procuro que no se busquen asignaturas con posiciones mayores a la máxima del array 'materias'.
        Ya que sino se añadirían valores vacíos o nulos al diccionario
        """
        if i>=max:
            pass
        #De no haber ningún inconvceniente a la hora de iterar, se añaden valores al diccionario
        else:
            """
            Las materias se ordenan en clave-valor según sus posiciones en el array 
            (la clave de cada una se obtiene tras acceder a su posición en el array a cada vuelta de bucle)
            El valor (o nota) de cada clave (o materia) en este diccionario es aleatorio.
            """
            nombre[materias[i]]=random.randint(0, 10)
    #La función crear devuelve un diccionario con el nombre del usuario, sus asignaturas y sus respectivas notas
    return nombre

#todos() será una función que imprima por consola y escriba en un documento de texto los diccionarios obtenidos
def todos():
    #Abro un archivo especificando su ruta, indico 'a+' para que pueda leer y escribir en ese documento
    with open('/home/zinedine/Desktop/Code/Z-Pruebas/Oscar-L/text.txt', "a+") as f: #Escoger la ruta dependiendo del PC
        #Para cada alumno hace lo siguiente
        for i in range(len(alumnos)):
            #Hago uso de la función crear para, precisamente, crear un diccioonario para cada usuario
            creado=crear(alumnos[i])
            print(creado)
            f.write(str(creado))
            #Escribir este salto de línea evita que todo quede junto
            f.write("\n")
        #Estos saltos de línea están fuera del bucle para que, una vez escritos todos los usuarios de una tanta, se deje margen con el siguiente
        f.write("\n")
        f.write("\n")
        #Cierro la conexión con el archivo
        f.close()
todos()
print("\n")
print("En caso de que no funcione: especifica correctamente la ruta en la función 'todos() '")



