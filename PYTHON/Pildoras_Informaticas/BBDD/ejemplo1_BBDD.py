import sqlite3

miconexion=sqlite3.connect("Video55_BBDD")
micursor=miconexion.cursor()

#micursor.execute("CREATE TABLE PRODUCTOS(NOMBRE_ARTICULO VARCHAR(20),PRECIO INTEGER, SECCION VARCHAR(50))" )
#micursor.execute("INSERT INTO PRODUCTOS VALUES('BALON',15,'DEPORTES')")
#miconexion.commit()

#Varios_Productos=list[

  #  ("Camiseta", 10, "Deportes"),
   # ("Jarrón", 90, "Cerámica"),
   # ("Camión", 20, "Juguetería")


#]


micursor.execute("SELECT * FROM PRODUCTOS")

VARIOS_PRODUCTOS=micursor.fetchall()
print(VARIOS_PRODUCTOS)

print(VARIOS_PRODUCTOS)


miconexion.commit()







miconexion.close() 

