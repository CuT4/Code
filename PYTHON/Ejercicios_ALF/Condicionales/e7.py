from turtle import delay


renta=int(input("Introduce tu renta anual: "))

delay(100)

print("procederemos a calcular tu tipo de impositivo...")

delay(1000)


if renta<=10000:
    print("Tienes que pagar un 5%")


if renta>10000 and renta<=20000:
    print("Tienes que pagar un 15%")


if renta>20000 and renta<=35000:
    print("Tienes que pagar un 20%")


if renta>35000 and renta<=60000:
    print("Tienes que pagar un 30%")


if renta>60000:
    print("Tienes que pagar un 45%")

