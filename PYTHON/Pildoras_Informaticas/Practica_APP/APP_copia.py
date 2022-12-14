#Se importan las librerías
from tkinter import *
from tkinter import Tk
from tkinter import messagebox
import sqlite3




#--------------- FUNCIONES-----------------------------

def conectarBBDD():
    try:
        miConexion=sqlite3.connect("Usuarios")
        miCursor=miConexion.cursor()

        miCursor.execute('''
            CREATE TABLE DATOS_USUARIO (
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            NOMBRE VARCHAR(30),
            PASWORD VARCHAR(50),
            APELLIDO VARCHAR (30),
            DIRECCION VARCHAR(50),
            COMENTARIO VARCHAR (100))
        ''')
    
        messagebox.showinfo("BBDD", "Base de datos creada con éxito")

    except:
        messagebox.showwarning("ERROR:", "Base de datos ya creada")



def salir_app():

    valor=messagebox.askquestion("Salir", "¿Deseas salir de la aplicación?")

    if valor=="yes":
        root.destroy()



def borrar_campos():
    nombreStringVar.set("")
    apellidoStringVar.set("")
    idStringVar.set("")
    direccionStringVar.set("")
    passwordStringVar.set("")
    comentarioText.delete(1.0, END)



def crear():
    miConexion=sqlite3.connect("Usuarios")
    miCursor=miConexion.cursor()

    miCursor.execute("INSERT INTO DATOS_USUARIO VALUES(NULL,'" + nombreStringVar.get() +
    "','" + passwordStringVar.get() +
    "','" + apellidoStringVar.get() +
    "','" + direccionStringVar.get() +
    "','"+ comentarioText.get("1.0", END) + "')")
    
    miConexion.commit()
    messagebox.showinfo("BBDD", "Registro insertado con éxito")



def leer():
    miConexion=sqlite3.connect("Usuarios")
    miCursor=miConexion.cursor()

    miCursor.execute("SELECT * FROM DATOS_USUARIO WHERE ID=" + idStringVar.get())
    el_usuario=miCursor.fetchall()

    for usuario in el_usuario:

        idStringVar.set(usuario[0])
        nombreStringVar.set(usuario[1])
        passwordStringVar.set(usuario[2])
        apellidoStringVar.set(usuario[3])
        direccionStringVar.set(usuario[4])
        comentarioText.insert(1.0, usuario[5])

    miConexion.commit()



def actualizar():
    miConexion=sqlite3.connect("Usuarios")
    miCursor=miConexion.cursor()

    miCursor.execute("UPDATE DATOS_USUARIO SET NOMBRE='" + nombreStringVar.get() + 
    "', PASWORD='" + passwordStringVar.get() + 
    "', APELLIDO='" + apellidoStringVar.get() +
    "', DIRECCION='" + direccionStringVar.get() +
    "', COMENTARIO='" + comentarioText.get(1.0, END) +
    "' WHERE ID=" + idStringVar.get())

    miConexion.commit()
    messagebox.showinfo("BBDD", "Registro actualizado con éxito")



def eliminar():
    miConexion=sqlite3.connect("Usuarios")
    miCursor=miConexion.cursor()

    miCursor.execute("DELETE FROM DATOS_USUARIO WHERE ID=" + idStringVar.get())
    miConexion.commit()
    messagebox.showinfo("BBDD", "Registro borrado con éxito")




#---------- ROOT -----------------------------------------

root=Tk()
root.title("APP-1")
root.geometry("650x650")
frameBody=Frame(root)
frameBody.pack()

"""
-Crea la raíz, la base sobre la que montaremos el resto de la aplicación
-Nombra la aplicación
-Asigna la medida de la app
-Crea un frame que pertenece a 'root'
-Hace falta utilizar .pack() con los frames
"""
#--------   COLUMNA   1  LABEL(S) -------------------------------------
id=Label(frameBody, text="Id: ")
id.grid(row=0, column=0, padx=10, pady=5)

nombreLabel=Label(frameBody, text="Nombre: ")
nombreLabel.grid(row=1, column=0, padx=10, pady=5)

passwordLabel=Label(frameBody, text="Password: ")
passwordLabel.grid(row=2, column=0, padx=10, pady=5)

apellidoLabel=Label(frameBody, text="Apellido: ")
apellidoLabel.grid(row=3, column=0, padx=10, pady=5)

direccionLabel=Label(frameBody, text="Direccion")
direccionLabel.grid(row=4, column=0, padx=10, pady=5)

comentarioLabel=Label(frameBody, text="Comentario: ")
comentarioLabel.grid(row=5, column=0, padx=10, pady=5)

"""
-Primera columna con sus respectivos 'label' bien posicionados
gracias a utilizas .grid(), como se puede ver, están en la misma
columna (0) y van desde la fila 1 a la 5.
"""
#--------  STRINGVAR (S) ---------------------------------------------

idStringVar=StringVar()
nombreStringVar=StringVar()
direccionStringVar=StringVar()
passwordStringVar=StringVar()
apellidoStringVar=StringVar()

"""
Declaración de todos los StringVar().
StringVar() es un objeto que se encarga de almacenar el valor del
string, en este caso se encarga de el valor de los entry a continuación.
"""

#--------  COLUMNA   2  ENTRY(S) -------------------------------------

idEntry=Entry(frameBody, textvariable=idStringVar)
idEntry.grid(row=0, column=2)

nombreEntry=Entry(frameBody, textvariable=nombreStringVar)
nombreEntry.grid(row=1, column=2)

passwordEntry=Entry(frameBody, textvariable=passwordStringVar)
passwordEntry.grid(row=2, column=2)
passwordEntry.config(show="*")

apellidoEntry=Entry(frameBody, textvariable=apellidoStringVar)
apellidoEntry.grid(row=3, column=2)

direccionEntry=Entry(frameBody, textvariable=direccionStringVar)
direccionEntry.grid(row=4, column=2)

comentarioText=Text(frameBody, width=32, height=5)
comentarioText.grid(row=5, column=2)
"""
Los parámetros que reciben estos Entry() son:
el frame al que pertenecen, y dónde se va a almacenar el
valor introducido en esos entry. El comentario no se correcponde
con ningún objeto StringVar() por ser este un Text() y no un Entry()

Se asignan sus respectivas posiciones.
"""
barraScroll=Scrollbar(frameBody, command=comentarioText.yview)
barraScroll.grid(row=5, column=3, sticky="nsew")
"""
-Crea una ScrollBar para poder desplazarse por el contenido del
cuadro de texto.
-Scrollbar() recibe dos parámetros: el frame contenedor y la opción,
en este caso 'command', el cual permite asociar la scrollBar a un cuadro
de texto e indicar el eje en el que queremos hacer scroll.
-Se posiciona la ScrollBar paralela y a la derecha del cuadro de texto,
el parámetro 'sticky=nsew' es para su posición también (north, south, east, west)
"""
comentarioText.config(yscrollcommand=barraScroll.set)
"""
En esta última línea se determina que la propiedad de scroll (en el eje y)
del objeto 'comentarioText' se asigna al objeto 'barrraScroll'.
"""
#------------ BARRA DE MENUS --------------------------------------------

barra_menu=Menu(root)
root.config(menu=barra_menu, width=300, height=300)

BBDD=Menu(barra_menu, tearoff=0)
BBDD.add_command(label="Crear BBDD", command=conectarBBDD)
BBDD.add_command(label="Salir", command=salir_app)

BORRAR_MENU=Menu(barra_menu, tearoff=0)
BORRAR_MENU.add_command(label="Borrar Campos", command=borrar_campos)

CRUD_MENU=Menu(barra_menu, tearoff=0)
CRUD_MENU.add_command(label="Insertar", command=crear)
CRUD_MENU.add_command(label="Leer", command=leer)
CRUD_MENU.add_command(label="Actualizar", command=actualizar)
CRUD_MENU.add_command(label="Borrar Registro", command=eliminar)

AYUDA_MENU=Menu(barra_menu, tearoff=0)
AYUDA_MENU.add_command(label="Licencia")
AYUDA_MENU.add_command(label="A cerca de...")


barra_menu.add_cascade(label="BBDD", menu=BBDD)
barra_menu.add_cascade(label="Borrar Campos", menu=BORRAR_MENU, command=borrar_campos)
barra_menu.add_cascade(label="CRUD", menu=CRUD_MENU)
barra_menu.add_cascade(label="Ayuda", menu=AYUDA_MENU)

#----------BOTONES DE ABAJO---------------

miFrame2=Frame(root)
miFrame2.pack()

botonConnect=Button(miFrame2, text="Insertar", command=crear)
botonConnect.grid(row=1, column=0, pady=10, padx=10)

botonLeer=Button(miFrame2, text="Leer", command=leer)
botonLeer.grid(row=1, column=1, pady=10, padx=10)

botonUpdate=Button(miFrame2, text="Actualizar", command=actualizar)
botonUpdate.grid(row=1, column=2, pady=10, padx=10)

botonDelete=Button(miFrame2, text="Borrar Campos", command=borrar_campos)
botonDelete.grid(row=1, column=3, pady=10, padx=10)


root.mainloop()



























root.mainloop()