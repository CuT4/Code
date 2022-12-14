barra_pan=3.49

n_barras_caducadas=int(input("Introduce el número de barras\nque no son del día: "))

print("Las barras que no son del día tienen un 60\npor ciento de descuento")
print("Vamos a aplicar su descuento para " + str(n_barras_caducadas) +" barras de ayer")

op=((n_barras_caducadas*barra_pan)*(1-0.6))

print("Finalmente usted tendrá que pagar "+ str(op) + "€")