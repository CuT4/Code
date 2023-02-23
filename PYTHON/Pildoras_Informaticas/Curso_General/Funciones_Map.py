class Empleado:
    
    def __init__ (self, nombre, cargo, salario):

        self.nombre=nombre
        self.cargo=cargo
        self.salario=salario

    def __str__(self):
        return "{} que trabaja como {} tiene un salario de {} €".format(self.nombre, self.cargo, self.salario)


tuplaEmpleados=[
(Empleado, "Juan", "Director", 6700),
(Empleado, "Ana", "Presidenta", 10000),
(Empleado, "Pedro", "Administrativo", 4700),
(Empleado, "Xulian", "Botones", 2100)

]


def calculo_comision(empleado):

    if empleado.salario<=3000:
        empleado.salario=empleado.salario*1.03
    return empleado

listaEmpleados=map(calculo_comision, tuplaEmpleados)

for empleado in listaEmpleados:
    print(empleado)



