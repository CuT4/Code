from tkinter import*

raiz=Tk()
raiz.title("Culo de mono calculador")

miframe=Frame(raiz)



operacion=""


resultado=0

#------------------PANTALLA----------------------

numeroPantalla=StringVar()


pantalla=Entry(miframe, textvariable=numeroPantalla)
pantalla.grid(row=1, column=1, padx=10, pady=10, columnspan=4)
pantalla.config(background="black", fg="green", justify="right")

#---------------PUSA TECLADO-----------


def numeroPulsado(num):

    global operacion
    if operacion!="":
        numeroPantalla.set(num)
        operacion=""
    
    else:
        numeroPantalla.set(numeroPantalla.get() + num)

#------------DEF SUMA-----------
def suma(num):
    
    global operacion

    global resultado

    resultado+=int(num) #resultado=resultado + int(num)

    operacion="suma"

    numeroPantalla.set(resultado)


#------------DEF RESULTADO---------

def el_resultado():

    global resultado

    numeroPantalla.set(resultado+int(numeroPantalla.get()))
    
    resultado=0

#---------------FILA 1-----------

boton7=Button(miframe, text="7", width=3, command=lambda:numeroPulsado("7"))
boton8=Button(miframe, text="8", width=3, command=lambda:numeroPulsado("8"))
boton9=Button(miframe, text="9", width=3, command=lambda:numeroPulsado("9"))
D=Button(miframe, text="/", width=3)

boton7.grid(row=2, column=1)
boton8.grid(row=2, column=2)
boton9.grid(row=2, column=3)
D.grid(row=2, column=4)


#---------------FILA 2-----------

boton4=Button(miframe, text="4", width=3, command=lambda:numeroPulsado("4"))
boton5=Button(miframe, text="5", width=3, command=lambda:numeroPulsado("5"))
boton6=Button(miframe, text="6", width=3, command=lambda:numeroPulsado("6"))
mult=Button(miframe, text="x", width=3)

boton4.grid(row=3, column=1)
boton5.grid(row=3, column=2)
boton6.grid(row=3, column=3)
mult.grid(row=3, column=4)


#---------------FILA 3-----------

boton1=Button(miframe, text="1", width=3, command=lambda:numeroPulsado("1"))
boton2=Button(miframe, text="2", width=3, command=lambda:numeroPulsado("2"))
boton3=Button(miframe, text="3", width=3, command=lambda:numeroPulsado("3"))
boton_restar=Button(miframe, text="-", width=3)


boton1.grid(row=4, column=1)
boton5.grid(row=4, column=2)
boton6.grid(row=4, column=3)
boton_restar.grid(row=4, column=4 )

#---------------FILA 4-----------

boton0=Button(miframe, text="0", width=3, command=lambda:numeroPulsado("0"))
boton_coma=Button(miframe, text=",", width=3, command=lambda:numeroPulsado(","))
boton_igual=Button(miframe, text="=", width=3, command=lambda:el_resultado())
boton_suma=Button(miframe, text="+", width=3, command=lambda:suma(numeroPantalla.get()))


boton0.grid(row=5, column=1)
boton_coma.grid(row=5, column=2)
boton_igual.grid(row=5, column=3)
boton_suma.grid(row=5, column=4 )



raiz.mainloop()