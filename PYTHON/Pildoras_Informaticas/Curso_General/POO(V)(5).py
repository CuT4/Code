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
            chequeo=self.__chequeo_interno()


        if(self.__enmarcha and chequeo):
            return "El coche está en marcha"
        
        elif(self.__enmarcha and chequeo==False):
            return "Algo esta mal"

        else:
            return "El coche está parado"

    def estado(self):
        print("El coche tiene ", self.__ruedas, " ruedas. Un ancho de ", self.__anchochasis,"y un largo de ", self.__largochasis)

    def __chequeo_interno(self):
        print("Realizando chequeo interno")
        self.gasolina="ok"
        self.aceite="ok"
        self.puertas="ok"

        if(self.gasolina=="ok" and self.aceite=="ok" and self.puertas=="ok"):
            
            return True

        else:
            
            return False


micoche=coche()
print(micoche.arrancar(True))
micoche.estado()

print("-------------segundo objeto a continuación--------------------")

micoche2=coche()
print(micoche2.arrancar(False))
micoche2.estado()