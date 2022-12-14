class Persona():

    def __init__ (self, nombre, edad, residencia):
        
        self.nombre=nombre
        self.edad=edad
        self.residencia=residencia
    
    def descripcion(self):
        print("Nombre: ", self.nombre, "\nEdad: ", self.edad, "\nReside en: ", self.residencia)

class empleado(Persona):
    def __init__(self, salario, antigüedad, nombre_empleado, edad_empleado, residencia_empleado):

        super().__init__(nombre_empleado, edad_empleado, residencia_empleado)

        self.salario=salario
        self.antigüedad=antigüedad
    
    def descripcion(self):
        super().descripcion
        print("Su salario es: ", self.salario, "\nSu edad es: ", self.edad)


Antonio=Persona("Antonio", 55, "Madrid")

Antonio.descripcion()

isinstance(Antonio, empleado)
print(isinstance(Antonio,empleado))





