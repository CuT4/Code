import sqlite3

miconexion=sqlite3.connect("GetsionProductos(2)")

miCursor=miconexion.cursor()






miconexion.commit()
miconexion.close()