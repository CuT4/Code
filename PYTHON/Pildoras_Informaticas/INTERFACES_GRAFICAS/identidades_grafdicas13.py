from tkinter import*
from tkinter import filedialog

root=Tk()


def abre_fichero():
    fichero=filedialog.askopenfilename(title="Abrir", initialdir="C:", filetypes=(("Ficheros de excel", "*.xlsl",
    ("Ficjeros de texto", "*txt"), ("Todos los ficheros", "*.*"))))
    print(fichero)

Button(root, text="Abrir fichero", command=abre_fichero).pack()









root.mainloop()
    