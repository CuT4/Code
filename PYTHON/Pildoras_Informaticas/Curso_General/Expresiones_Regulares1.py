import re

cadena="Vamos a aprender expresiones regulares"

TextoBuscar="aprender"

if re.search(TextoBuscar, cadena) is not None:

    print("He encontrado el texto")

else:
    print("No he encontrado el texto")