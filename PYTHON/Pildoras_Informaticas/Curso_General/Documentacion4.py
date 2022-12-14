import doctest
import math


def raiz_cuadrada(lista_numeros):

    """
    La funcion deveuelve una lista con la 
    raíz cuadrada de los elementos numéricos 
    pasados por lista a su parámetros
    
    '>>>lista=[]'
    '>>>for i in [4, 9, 16]:'
    ...     lista.append(i)
    '>>>rai_cuadrada(lista)'
    [2, 3, 4]
    """

    return [math.sqrt(n) for n in lista_numeros]


#doctest.testmod()

#print(raiz_cuadrada([9,16,64]))