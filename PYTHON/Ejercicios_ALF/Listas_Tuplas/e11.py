a=(1,2,3)
b=(-1,-3,4)

resultado=0

for i in range(len(a)):
    resultado+=a[i]*b[i]

print("El resultado de "+ str(a) + " por " + str(b) +" es " + str(resultado))