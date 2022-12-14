from decimal import*
import os

# getcontext().prec=10000
k=0
r=0
potencias=Decimal(1)
anterior=0
while True:
    r+=Decimal((4/(8*k+1)-2/(8*k+4)-1/(8*k+5)-1/(8*k+6)))/potencias
    k+=1
    potencias*=16
    os.system("cls")
    print(r)
    