diccionario={"plátano":1.35, "manzana":0.80, "pera":0.85, "naranja":0.70}

fruta_deseada=input("¿Qué fruta quieres comprar? ")
kilos=float(input("¿Cuántos kg quieres? "))

if fruta_deseada in diccionario:
    print(kilos, " de ", fruta_deseada, " valen ", str(diccionario[fruta_deseada]*kilos), " € ")
else:
    print("No tenemos ese producto")

