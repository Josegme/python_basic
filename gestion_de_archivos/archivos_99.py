
from pathlib import Path
from time import ctime

archivo = Path("gestion_de_archivos/archivos/archivo-prueba.txt")
#archivo.exists()
#archivo.rename()
#archivo.unlink()

#print(archivo.stat()) #para ver estadisticas o info de la metadata del archivo

print("Acceso", ctime(archivo.stat().st_atime)) #timesTamp -> fecha (unix) pero se utiliza un modulo ctime
print("Creación", ctime(archivo.stat().st_ctime))
print("modificación", ctime(archivo.stat().st_mtime))