import math
import os
from decimal import*
getcontext().prec=100
e=0

for i in range(1000):
    e+=Decimal(1/math.factorial(i))
    os.system("cls")
    print(e)
        
    
