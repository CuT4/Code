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
    minombre2.set("")
    miapellido2.set("")
    miid2.set("")
    midireccion2.set("")
    mipasword2.set("")
    comentario2.delete(1.0, END)



def crear():
    miConexion=sqlite3.connect("Usuarios")
    miCursor=miConexion.cursor()

    miCursor.execute("INSERT INTO DATOS_USUARIO VALUES(NULL,'" + minombre2.get() +
    "','" + mipasword2.get() +
    "','" + miapellido2.get() +
    "','" + midireccion2.get() +
    "','"+ comentario2.get("1.0", END) + "')")
    
    miConexion.commit()
    messagebox.showinfo("BBDD", "Registro insertado con éxito")



def leer():
    miConexion=sqlite3.connect("Usuarios")
    miCursor=miConexion.cursor()

    miCursor.execute("SELECT * FROM DATOS_USUARIO WHERE ID=" + miid2.get())
    el_usuario=miCursor.fetchall()

    for usuario in el_usuario:

        miid2.set(usuario[0])
        minombre2.set(usuario[1])
        mipasword2.set(usuario[2])
        miapellido2.set(usuario[3])
        midireccion2.set(usuario[4])
        comentario2.insert(1.0, usuario[5])

    miConexion.commit()



def actualizar():
    miConexion=sqlite3.connect("Usuarios")
    miCursor=miConexion.cursor()

    miCursor.execute("UPDATE DATOS_USUARIO SET NOMBRE='" + minombre2.get() + 
    "', PASWORD='" + mipasword2.get() + 
    "', APELLIDO='" + miapellido2.get() +
    "', DIRECCION='" + midireccion2.get() +
    "', COMENTARIO='" + comentario2.get(1.0, END) +
    "' WHERE ID=" + miid2.get())

    miConexion.commit()
    messagebox.showinfo("BBDD", "Registro actualizado con éxito")



def eliminar():
    miConexion=sqlite3.connect("Usuarios")
    miCursor=miConexion.cursor()

    miCursor.execute("DELETE FROM DATOS_USUARIO WHERE ID=" + miid2.get())
    miConexion.commit()
    messagebox.showinfo("BBDD", "Registro borrado con éxito")




#---------- ROOT -----------------------------------------

root=Tk()
root.title("APP-1")
root.geometry("650x650")

miFrame=Frame(root)
miFrame.pack()


#--------   COLUMNA   1  LABEL(S) -------------------------------------

id=Label(miFrame, text="Id: ")
id.grid(row=0, column=0, padx=10, pady=5)

nombreLabel=Label(miFrame, text="Nombre: ")
nombreLabel.grid(row=1, column=0, padx=10, pady=5)

PasswordLabel=Label(miFrame, text="Password: ")
PasswordLabel.grid(row=2, column=0, padx=10, pady=5)

apellidoLabel=Label(miFrame, text="Apellido: ")
apellidoLabel.grid(row=3, column=0, padx=10, pady=5)

direccionLabel=Label(miFrame, text="Direccion")
direccionLabel.grid(row=4, column=0, padx=10, pady=5)

COMENTARIO_Label=Label(miFrame, text="Comentario: ")
COMENTARIO_Label.grid(row=5, column=0, padx=10, pady=5)

#--------  STRINGVAR (S) -------------------------------------

miid2=StringVar()
minombre2=StringVar()
midireccion2=StringVar()
mipasword2=StringVar()
miapellido2=StringVar()

#--------  COLUMNA   2  ENTRY(S) -------------------------------------

id2=Entry(miFrame, textvariable=miid2)
id2.grid(row=0, column=2)

nombre2=Entry(miFrame, textvariable=minombre2)
nombre2.grid(row=1, column=2)

pasword2=Entry(miFrame, textvariable=mipasword2)
pasword2.grid(row=2, column=2)
pasword2.config(show="*")

apellido2=Entry(miFrame, textvariable=miapellido2)
apellido2.grid(row=3, column=2)

direccion2=Entry(miFrame, textvariable=midireccion2)
direccion2.grid(row=4, column=2)

comentario2=Text(miFrame, width=32, height=5)
comentario2.grid(row=5, column=2)
barra_scroll=Scrollbar(miFrame, command=comentario2.yview)
barra_scroll.grid(row=5, column=3, sticky="nsew")
comentario2.config(yscrollcommand=barra_scroll.set)

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