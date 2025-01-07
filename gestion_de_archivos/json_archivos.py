"""JSON archivos"""

import json
from pathlib import Path

#escribir json 
"""
productos= [
    {"id": 1, "name": "Surfboard"},
    {"id": 2, "name": "Bicicleta"},
    {"id": 3, "name": "Skate"},
]

data = json.dumps(productos)
Path("gestion_de_archivos/archivos/productos.json").write_text(data)
"""

#leer json
data = Path("gestion_de_archivos/archivos/productos.json").read_text()
productos = json.loads(data)
print(productos)

#modificar json
productos[0]["name"] = "Chanchito Feliz"
Path("gestion_de_archivos/archivos/productos.json").write_text(json.dumps(productos))
