def area_circulo(radio):

    pi=3.141592


    circunferencia=2*pi*(radio)

    area=pi*(radio**2)

    print("La circunferencia del circulo es ", str(circunferencia))
    print("El area del circulo es", str(area))

def volumen_cilindro(radio, altura):

    pi=3.141592

    circunferencia=2*pi*(radio)

    area=pi*(radio**2)

    volumen=pi*(radio**2)*altura

    print("El volumen del cilindro es ", str(volumen))


print(area_circulo(5))

print(volumen_cilindro(5, 10))

    



