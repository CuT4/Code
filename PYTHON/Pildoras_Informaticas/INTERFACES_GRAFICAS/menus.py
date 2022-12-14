from tkinter import*
from tkinter import messagebox

root=Tk()

def infoAdicional():
    messagebox.showinfo("Procesador de Oscar", "Procesador textos")

def estado_licencia():
    messagebox.showwarning("Licencia", "Producto bajo licencia")

def salida():
    #valor=messagebox.askquestion("Salir", "¿Desea salir de la aplicación?")
    valor=messagebox.askokcancel("Salir", "¿Desea salir de la aplicación?")

    if valor==True:
        root.destroy()

def cerrar_documento():
    valor=messagebox.askretrycancel("Reintentar", "Editor abierto")
    if valor==False:
        root.destroy()
    

barra_menu=Menu(root)
root.config(menu=barra_menu, width=300, height=300)

archivo_menu=Menu(barra_menu, tearoff=0)
archivo_menu.add_command(label="Nuevo")
archivo_menu.add_command(label="Guardar")
archivo_menu.add_command(label="Guardar como")
archivo_menu.add_separator()
archivo_menu.add_command(label="Cerrar", command=cerrar_documento)
archivo_menu.add_command(label="Salir", command=salida)

archivo_edit=Menu(barra_menu, tearoff=0)
archivo_edit.add_command(label="Copiar")
archivo_edit.add_command(label="Pegar")
archivo_edit.add_command(label="Cortar")

archivo_tools=Menu(barra_menu, tearoff=0)

archivo_help=Menu(barra_menu, tearoff=0)
archivo_help.add_command(label="licencia", command=estado_licencia)
archivo_help.add_command(label="Acerca de...", command=infoAdicional)

barra_menu.add_cascade(label="Archivo", menu=archivo_menu)

barra_menu.add_cascade(label="Edicion", menu=archivo_edit)

barra_menu.add_cascade(label="Herramientas", menu=archivo_tools)

barra_menu.add_cascade(label="Ayuda", menu=archivo_help)



root.mainloop()