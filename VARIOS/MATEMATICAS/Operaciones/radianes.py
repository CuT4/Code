#Para pasar de ángulos a radianes tenemos que multiplicar por (π/180)
#Para pasar de radianes a grados hay que multiplicar por (180/π)
import math

def angleRadian(array):
    newArray=[]
    for i in range(len(array)):
        newArray.append(i*(math.pi/180))
    return newArray

def radianAngle(array):
    newArray=[]
    for i in range(len(array)):
        newArray.append(i*(180/math.pi))
    return newArray

"""
To complete this code I'll need to make it 
compatible with fractions, the input must be
capable of reading '/' as a fraction and 'pi'
as 'math.pi'
"""


