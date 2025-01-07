"""Create table"""
import sqlite3

con = sqlite3.connect("sqlite/app.db")
cursor = con.cursor() #objeto que funciona como intermediario para poder enviar consultas
cursor.execute(
    """
    CREATE TABLE if not exists usuarios
    (id INTEGER primary key, nombre VARCHAR(50));

    """
)
con.commit()
con.close()
