meses = {1:'enero', 2:'febrero', 3:'marzo', 4:'abril', 5:'mayo', 6:'junio', 7:'julio', 8:'agosto', 9:'septiembre', 10:'octubre', 11:'noviembre', 12:'diciembre'}

fecha_nacimineto=input("Introduce en formato dd/mm/aaaa tu fecha de nacimeinto: ")

fecha_nacimineto=fecha_nacimineto.split("/")

print("Has nacido el día ", fecha_nacimineto[0], " de ", meses[int(fecha_nacimineto[1])], " del año ", fecha_nacimineto[2])
