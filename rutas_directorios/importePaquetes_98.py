"""Importe dinámico de paquetes"""

#ver la clase 98
from pathlib import Path

path = Path()
paths = [p for p in path.iterdir() if p.is_dir()]

dependencias = {
    "db": "base de datos"
    "api": "esta es la api"
    "graphql": "esto es graphql"
}

def load(p):
    paquete = __import__(str(p).replace("/", "."))
    try:
        paquete.init(**dependencias)
    except:
        print("El paquete no tiene función init")


list(map(load, paths))

"""
En el __init__.py

def init(db, api, **_):
    print(F"soy modulo dos: {db} {api})

    
Ver la clase para probar de nuevo como imortar las dependencias.

"""