class vehiculos():

    def __init__ (self,marca,modelo):

        self.marca=marca
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

class furgoneta(vehiculos):
    def carga(self,cargar):
        self.cargado=cargar
        if (self.cargado):
            return "La furgoneta está cargada"
        else:
            return "La furgoneta no está cargada"

class moto(vehiculos):
    hcaballito=""
    def caballito(self):
        self.hcaballito=print("Voy haciendo el caballito")

        def estado(self):
            print("Marca: ", self.marca, "\nModelo: ", self.modelo, "\nEn marcha: ", self.enmarcha, "\nAceleración: ", self.acelera,
        "\nFrenado: ", self.frena, "\n", self.hcaballito)

class VEelectricos():
    def __init__ (self, marca, modelo):
        super().__init__(marca, modelo)
        self.autonomia=100 + "km"

    
    def cargarEnergia(self):
        self.cargando=True

    

mimoto=moto("porsche", "911")

mimoto.caballito()

mimoto.estado()


mifurgoneta=furgoneta("Renault", "Kangoo")
mifurgoneta.arrancar
mifurgoneta.estado
print(mifurgoneta.carga(True))



class biciElectrica(moto,VEelectricos):
    pass

mibici=biciElectrica("Honda", "BMX")
mibici.caballito()
mibici.estado




    

