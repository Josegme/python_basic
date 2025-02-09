""""Archivos ZIP : comprimidos"""""

from pathlib import Path
from zipfile import ZipFile
"""
with ZipFile("gestion_de_archivos/comprimidos.zip", "w") as zip:
    #estamos en python_basic
    for path in Path().rglob("*.*"): #para que incluya todos los archivos dentro de la carpeta
        print(path)
        if str(path) != "gestion_de_archivos/comprimidos.zip":
            zip.write(path)
"""

with ZipFile("archivos/comprimidos.zip", "w") as zip:
    print(zip.namelist())
    info = zip.getinfo("archivos/comprimidos.zip")
    print(
        info.file_size,
        info.compress_size
    )
zip.extractall("archivos/descomprimidos")