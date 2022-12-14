#!/usr/bin/python

class coche():
    def __init__(self):

        self.__largochasis=250
        self.__anchochasis=120
        self.__ruedas=4
        self.__enmarcha=False
    
    def arrancar(self,arrancamos):
        self.__enmarcha=arrancamos

        if(self.__enmarcha):
            return "El coche está en marcha"

        else:
            return "El coche está parado"

    def estado(self):
        print("El coche tiene ", self.__ruedas, " ruedas. Un ancho de ", self.__anchochasis,"y un largo de ", self.__largochasis)


micoche=coche()
print(micoche.arrancar(True))
micoche.estado

print("-------------segundo objeto a continuación--------------------")

micoche2=coche()
print(micoche2.arrancar(False))
micoche2.ruedas=2
micoche2.estado

