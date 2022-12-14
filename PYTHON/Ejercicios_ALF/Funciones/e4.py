def impuestos(cantidad, impuesto=21):

    return cantidad + cantidad*impuesto/100


print(impuestos(100000, 31))