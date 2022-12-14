import re

nombre1="Jara Lopez"
nombre2="378322368236789"
nombre3="a78732687326883"

if re.match("\d", nombre2 ):
    print("hemos")
else:
    print("No hemos")
#-----------------------------------------------------------------------------
nombre1="Jara Lopez"
nombre2="378322368236789"
nombre3="a78732687326883"

if re.search("Lopez", nombre1 ):
    print("hemos")
else:
    print("No hemos")

