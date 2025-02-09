#Directorios

from pathlib import Path

path = Path("rutas")
#path.exists()
#path.mkdir()
#path.rmdir()
#path.rename("chanchito-feliz")

#print(path.iterdir)

for p in path.iterdir():
    print(p)

#si quiero volver a la carpeta anterior cd..
#me puedo mover segun las rutas que requiera moviendome entre los directorios
