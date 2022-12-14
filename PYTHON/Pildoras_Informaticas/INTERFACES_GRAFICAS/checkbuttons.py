from tkinter import*

root=Tk()
root.title("CheckButtons")

#foto=PhotoImage(file="avion.png")
#Label(root, image=foto).pack()


playa=IntVar()
montagna=IntVar()
rural=IntVar()

def opciones_Viaje():
    opcion_escogida=""

    if playa.get()==1:
        opcion_escogida+=" playa"
    
    if montagna.get()==1:
        opcion_escogida+=" montaña"

    if rural.get()==1:
        opcion_escogida+=" rural"

    
    texto_final.config(text=opcion_escogida)


frame=Frame(root)
frame.pack()

Label(frame, text="Elige tu destino: ", width=50, pady=50).pack()


Checkbutton(frame, text="Playa", variable=playa, onvalue=1, offvalue=0, command=opciones_Viaje).pack()
Checkbutton(frame, text="Montaña", variable=montagna, onvalue=1, offvalue=0, command=opciones_Viaje).pack()
Checkbutton(frame, text="Rural", variable=rural, onvalue=1, offvalue=0, command=opciones_Viaje).pack()


texto_final=Label(frame)
texto_final.pack()



root.mainloop()