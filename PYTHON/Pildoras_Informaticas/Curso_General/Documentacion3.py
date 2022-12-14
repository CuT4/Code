import doctest

def compruebamail(mailUS):
    """
    La funcion compruebamail() evalua un mail, si contiene una arroba es correcto.
    Si contiene más de una arroba es in correcto. Si la arroba está al final es incorrecto.

    >>>compruebamail('juancastelo@gmail.com')
    True

    >>>compruebamail('juan@@castelo.comgmail')
    False

    """

    arroba=mailUS.count("@")

    if (arroba!=1 or mailUS.rfind("@")==(len(mailUS)-1) or mailUS.rfind("@")==0):
        return False
        print("False")
    else:
        return True
        print("True")

compruebamail("paco@@paco.com")