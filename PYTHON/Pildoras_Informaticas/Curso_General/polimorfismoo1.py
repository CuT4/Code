class coche():
    
    def desplazamiento(self):
        print("Me desplazo con cuatro ruedas")

class moto():

    def desplazamiento(self):
        print("Me deslpazo con dos ruedas")

class camion():

    def desplazamiento(self):
        print("Me desplazo con seis ruedas")


def desplazamientoV(vehiculo):
    vehiculo.desplazamiento()

mivehiculo=camion()
desplazamientoV(mivehiculo)