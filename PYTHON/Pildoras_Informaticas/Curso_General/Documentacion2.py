import doctest

def area_triangulo(base, altura):
    """Esta funcion calcula el area de un trinagulo multiplicando su base por su altura dividido entre dos
    
    >>> area_triangulo(3,6)
    9.0

    """
    return (base*altura)/2

doctest.testmod()










