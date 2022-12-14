import funciones_matematicas


class Areas:
    def areacuadrado(lado):

        """Calcula el area de un cuadrado elevando al cuadrado el lado que se le pasa por parámetro)"""

        return "El área del cuadrado es " + str(lado*lado)


    def areatriangulo(base,altura):
        return "El área del triangulo es " + str ((base*altura)/2)


print(Areas.areacuadrado(8))

print(Areas.areatriangulo(30,40))



