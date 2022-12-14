from decimal import*
from pickle import decode_long

"""El numero Phi, o numero áureo, es
un número irracional. Lo cual conlleva
que no podamos interpretarlo con todos sus decimales.
Lo máximo que nos podemos hacercar a Phi es
a una aproximación del mismo, como pasa con
el resto de números irracionales.

Para esta aproximación se ha usado el último término
numérico de la sucesión de Fibonacci calculada por
Óscar Rodriguez Santiago en JavaScript, antes de que
este lenguage interprete los términos de dicha sucesión
como infinitos por ser estos muy grandes
como la variable 'a' y su antecesor como la
variable 'b'.
Dividiendo un término cada vez mayor de la
sucesión de Fibonacci entre el anterior a este
se obtiene una aproximación a Phi.
"""


a=1.3069892237633987e+308
b=8.077637632156222e+307
print(Decimal(a/b))