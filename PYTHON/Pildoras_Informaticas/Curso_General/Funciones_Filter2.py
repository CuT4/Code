
class Empleado:

    def __init__ (self, nombre, cargo, salario):

        self.nombre=nombre
        self.cargo=cargo
        self.salario=salario

    def __str__(self):
        return "{} que trabaja como {} tiene un salario de {} €".format(self.nombre, self.cargo, self.salario)


tuplaEmpleados=[
(Empleado, "Juan", "Director", 75000),
(Empleado, "Ana", "Presidenta", 100000),
(Empleado, "Pedro", "Administrativo", 47000),
(Empleado, "Xulian", "Botones", 21000),

]


def salarios_altos(empleado):
    if [2 ]>=50000:
        return True
    


for empleado_salario in salarios_altos:
    print(empleado_salario)
