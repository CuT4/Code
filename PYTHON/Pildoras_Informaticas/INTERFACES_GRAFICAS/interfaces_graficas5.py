from tkinter import *

raiz=Tk()
raiz.title("Ventana123")

frame=Frame(raiz, width=1200, height=600)
frame.pack()

minombre=StringVar()

cuadronombre=Entry(frame, textvariable=minombre)
cuadronombre.grid(row=0, column=1)

cuadroapellido=Entry(frame)
cuadroapellido.grid(row=1, column=1)

cuadrodireccion=Entry(frame )
cuadrodireccion.grid(row=2, column=1)

texto_comentario=Text(frame, width=16, height=5)
texto_comentario.grid(row=4, column=1, pady=10, padx=10)

barra_scroll=Scrollbar(frame, command=texto_comentario.yview)
barra_scroll.grid(row=4, column=2, sticky="nsew")

texto_comentario.config(yscrollcommand=barra_scroll.set)

nombre=Label(frame, text="Nombre: ")
nombre.grid(row=0, column=0, sticky="e", pady=10)

apellido=Label(frame, text="Apellidos: ")
apellido.grid(row=1, column=0, sticky="e", pady=10)

direccion=Label(frame, text="Direccion: ")
direccion.grid(row=2, column=0, sticky="e", pady=10)

cuadrocontraseña=Entry(frame)
cuadrocontraseña.grid(row=3, column=1)

contraseña=Label(frame, text="Introduce tu contraseña: " )
contraseña.grid(row=3, column=0, sticky="e", pady=10)

comentarios_label=Label(frame, text="Comentarios" )
comentarios_label.grid(row=4, column=0, sticky="e", pady=10)

def codigo_boton():
    minombre.set("Carlos Luis")


boton=Button(raiz, text="Esto es un boton", command=codigo_boton)
boton.pack()







raiz.mainloop()