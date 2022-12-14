def funcion_decoradora(funcion_parametro):

    def funcion_interna(*args, **kwargs):
        print("A continuacion se realizará un cálculo: ")
        funcion_parametro(*args, **kwargs)
        print("Se ha terminado el cálculo")
    return funcion_interna

#tudevice


@funcion_decoradora
def suma(num1, num2, num3):
    print(num1 + num2 +num3)

@funcion_decoradora
def resta(num1, num2):
    print(num1 - num2)

@funcion_decoradora
def potencia(base, exponente):
    print(base**exponente)

suma(12, 32, 30)
resta(300, 21)
potencia(base=2, exponente=2)       