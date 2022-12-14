def divide():
    op1=float(input("Introduce el primer número: "))
    op2=float(input("Introduce el segundo número: "))
    try:
        print("La division es " + str(op1/op2))

    except ValueError:
        print("No se admiten caracteres no numéricos")

    except ZeroDivisionError:
        print("No es posible dividir entre cero")
    
    finally:
        print("Final del cálculo")

divide()
