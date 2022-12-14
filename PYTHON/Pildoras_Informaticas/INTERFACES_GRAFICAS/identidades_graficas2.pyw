from tkinter import *

raíz=Tk()

raíz.title("Ventana1")

#raíz.resizable(1,0)

raíz.iconbitmap("algo.ico")

#raíz.geometry("650x350")

raíz.config(background="blue")
raíz.config(bd=25) #bd es el ancho del borde
raíz.config(relief="sunken") #es el tipo de borde







miframe=Frame()
miframe.pack()
#miframe.pack(fill="both", expand=True)
miframe.config(background="red")
miframe.config(width="650",height="350")
miframe.config(bd=35) #bd es el borde
miframe.config(relief="groove")
miframe.config(cursor="pirate")


raíz.mainloop()