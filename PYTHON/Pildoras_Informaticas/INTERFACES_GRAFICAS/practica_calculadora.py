from tkinter import*

raiz=Tk()







#------------------PANTALLA----------------------

pantalla=Entry(raiz)
pantalla.pack()
pantalla.grid(row=1, column=1, padx=10, pady=10, columnspan=4)
pantalla.config(background="black", fg="green", justify="right")

#---------------FILA 1-----------

boton7=Button(raiz, text="7", width=3)
boton8=Button(raiz, text="8", width=3)
boton9=Button(raiz, text="9", width=3)
D=Button(raiz, text="/", width=3)

boton7.grid(row=2, column=1)
boton8.grid(row=2, column=2)
boton9.grid(row=2, column=3)
D.grid(row=2, column=4)


#---------------FILA 2-----------

boton4=Button(raiz, text="4", width=3)
boton5=Button(raiz, text="5", width=3)
boton6=Button(raiz, text="6", width=3)
mult=Button(raiz, text="x", width=3)

boton4.grid(row=3, column=1)
boton5.grid(row=3, column=2)
boton6.grid(row=3, column=3)
mult.grid(row=3, column=4)


#---------------FILA 3-----------

boton1=Button(raiz, text="1", width=3)
boton2=Button(raiz, text="2", width=3)
boton3=Button(raiz, text="3", width=3)
boton_restar=Button(raiz, text="-", width=3)


boton1.grid(row=4, column=1)
boton5.grid(row=4, column=2)
boton6.grid(row=4, column=3)
boton_restar.grid(row=4, column=4 )

#---------------FILA 4-----------

boton0=Button(raiz, text="0", width=3)
boton_coma=Button(raiz, text=",", width=3)
boton_igual=Button(raiz, text="=", width=3)
boton_suma=Button(raiz, text="+", width=3)


boton0.grid(row=5, column=1)
boton_coma.grid(row=5, column=2)
boton_igual.grid(row=5, column=3)
boton_suma.grid(row=5, column=4 )



raiz.mainloop()