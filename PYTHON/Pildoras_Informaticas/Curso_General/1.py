class vehiculos():
    
    def __init__ (self,marca,modelo):

        self.__marca=marca
        self.modelo=modelo
        self.enmarcha=False
        self.acelera=False
        self.frena=False

    def arrancar(self):
        self.enmarcha=True
    
    def acelerar(self):
        self.acelera=True
    
    def frenar(self):
        self.frena=True
    
    def estado(self):
        print("Marca: ", self.marca, "\nModelo: ", self.modelo, "\nEn marcha: ", self.enmarcha, "\nAceleración: ", self.acelera,
        "\nFrenado: ", self.frena)

class moto(vehiculos):
    pass

mimoto=moto("porsche","911")

print(mimoto.estado)