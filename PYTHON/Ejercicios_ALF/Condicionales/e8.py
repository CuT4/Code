puntuacion_empleado=float(input("Introduce la puntuacion que has obtenido este año: "))

if puntuacion_empleado<0.4:
    print("Tu salario es de 2400€")

if puntuacion_empleado==0.4:
    print("Tu salario es de " + str(2400*1.4))

if puntuacion_empleado==0.6:
    print("Tu salario es de " + str(2400*1.6))

if puntuacion_empleado==1.0:
    print("Tu salario es de " + str(2400*2))


if puntuacion_empleado>1.00000000000000000000001:
    print("La puntuacion es sobre uno. La puntuacion dada es incorrceta.")
