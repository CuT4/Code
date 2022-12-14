#Si el número es par: dividir entre 2
#Si el número es impar: multiplicar por 3 y sumar 1
import keyboard
import time
n=float(input("Introduce tu número: "))
print(n)
while True:
    if(n%2)==0:
        n=n/2
        print(n)
        time.sleep(0.3)
        
    else:
        n=(n*3)+1
        print(n)
        time.sleep(0.3)

    if keyboard.is_pressed("q"):
        break

#Inevitablemente la secuencia acabará en un bucle: 4,2,1, 4,2,1, 4,2,1...