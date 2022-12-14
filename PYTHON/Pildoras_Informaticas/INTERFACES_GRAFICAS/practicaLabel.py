from tkinter import *

raiz=Tk()
raiz.title("Ventana2")

miframe=Frame(raiz, width=500, height=400)

mi_Imagen=PhotoImage(file="Reyes.png")

miframe.pack()

Label(miframe, image=mi_Imagen).place(x=100, y=200)

#mi_Label=Label(miframe, text="Siuuuu")
#mi_Label.place(x=100, y=200)

#Label(miframe, text="Siuuuu", fg="red", font=(21)).place(x=100, y=200)


raiz.mainloop()

