from tkinter import *
from tkinter import filedialog


root=Tk()

def abreFichero():
    fichero=filedialog.askopenfilename(title="Abrir", initialdir="documents")
    print("Abrir fichero")


Button(root, text="Abrir fichero", command=abreFichero).pack()




root.mainloop()

