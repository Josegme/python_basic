"""todos los gestores son bastante similares - SQLITE ya viene incluido en python"""

import sqlite3
#para conectarnos a una bd
con = sqlite3.connect("sqlite/app.db") #se conecta o se crea el db
#siempre cerrar la conexión siempre
con.close()

