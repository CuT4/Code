
def suma(num1, num2):
	return num1+num2

def resta(num1, num2):
	return num1-num2

def multiplica(num1, num2):
	return num1*num2

def divide(num1,num2):
    try:
		return num1/num2
	except ZeroDivisionError:
		print("No es posible dividir entre cero")

while True:

	try:
		op1=(int(input("Introduce el primer numero: ")))
		op2=(int(input("Introduce el segundo numero: ")))

		break;	

	except ValueError:
		print("Los valores introducvidos no son correctos")	


operacion=input("Introduce la operacion a realizar (suma,resta,multiplica,divide): ")

if operacion=="suma":
	print(suma(op1,op2))

elif operacion=="resta":
	print(resta(op1,op2))

elif operacion=="multiplica":
	print(multiplica(op1,op2))

elif operacion=="divide":
	print(divide(op1,op2))

else:
	print ("Operacion contemplada")


print("Operacion ejecutada. Continuacion de ejecocion del programa ")