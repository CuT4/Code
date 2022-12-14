import pickle

class persona():

     def __init__(self, nombre, genero, edad):
         self.nombre=nombre
         self.genero=genero
         self.edad=edad
         print("Se ha creado una persona nueva que se llama ", self.nombre)


def __str__(self):
    return "{} {} {}".format(self.nombre, self.genero, self.edad)


class lista_personas():
    personas=[]

    def __init__(self):
        listadepersonas=open("Fichero_externo_personas", "ab+")
        listadepersonas.seek(0)
        
        try:
            self.personas=pickle.load(listadepersonas)
            print("Se cargaron {} del fichero externo".format(len(self.personas)))

        except:
            print("Fichero vacío")

        finally:
            listadepersonas.close()
            del(listadepersonas)

    def agregar_personas(self,p):
        self.personas.append()

    def mostar_personas(self):
        for p in self.personas:
            print(p)

    def guardarpersonasenficheroexterno(self):
        listadepersonas=open("Fichero_externo", "wb")
        pickle.dump(self.personas, listadepersonas)
        listadepersonas.close()
        del(listadepersonas)

    def mostarinfoficheroexterno(self):
        print("El fichero externo contiene: ")
        
        for p in self.personas:
            print(p)


miLista=lista_personas()
Persona=persona("Sandra", "F", "19")
miLista.agregar_personas(Persona)
miLista.mostarinfoficheroexterno()






