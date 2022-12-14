import pickle

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


coche1=vehiculos( "Ferrari", "350")
coche2=vehiculos( "Lambo", "250")
coche3=vehiculos( "Rolls", "150")

coches=[coche1, coche2, coche3]

fichero=open("los_coches", "wb")

pickle.dump(coches, fichero)
fichero.close()




apertura_fichero=open("los_coches", "rb")
mis_coches=pickle.load(apertura_fichero)

apertura_fichero.close()


for c in mis_coches:
    print(c.estado())

