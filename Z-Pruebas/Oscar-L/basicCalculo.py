pregunta=input("Sumar (s), Restar (r), Multiplicar (m), Dividir (d): ")


if pregunta.lower()=="s":
    n1=float(input("Introduce el primer número a sumar: "))
    n2=float(input("Introduce el segundo número a sumar: "))
    print("Resultado: ", n1+n2)

if pregunta.lower()=="r":
    n1=float(input("Introduce el primer número a restar: "))
    n2=float(input("Introduce el segundo número a restar: "))
    print("Resultado: ", n1-n2)
if pregunta.lower()=="m":
    n1=float(input("Introduce el primer número a multiplicar: "))
    n2=float(input("Introduce el segundo número a multiplicar: "))
    print("Resultado: ", n1*n2)
if pregunta.lower()=="d":
    n1=float(input("Introduce el dividendo: "))
    n2=float(input("Introduce el divisor: "))
    if n2==0:
        print("---No se puede dividir entre cero---")
    else:
        print("Resultado: ", n1/n2)