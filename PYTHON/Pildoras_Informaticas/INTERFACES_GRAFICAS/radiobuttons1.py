from tkinter import *

root=Tk()


varOption=IntVar()


def imprimir():
    #print(varOption.get())

    if varOption.get()==1:
        etiqueta.config(text="Has elegido masculino")
    
    else:
        etiqueta.config(text="Has elegido femenino")



Label(root, text="Género").pack()

Radiobutton(root, text="Masculino", variable=varOption, value=1, command=imprimir).pack()
Radiobutton(root, text="Femenino", variable=varOption, value=2, command=imprimir ).pack()


etiqueta=Label()
etiqueta.pack()






root.mainloop()