#rutas -> Path.py
"""
from pathlib import Path
#para windows usar r"C:ARchivos de Programa\Minecraft"
Path(r"C:Archivos de Programas\Minecraft")
#para linux o mac se importa diferente
Path("/usr/bin") #ruta absoluta
Path() 
Path.home()
Path("one/__init__.py") #ruta relativa AP/one/__init__.py
"""

path = Path("hola-mundo/mi-archivo.py")
path.is_file()
path.is_dir()
path.exists()
#ademas tenemos accesos a propiedades
print(
    path.name,
    path.stem,
    path.suffix,
    path.parent,
    path.absolute()
)
#otros métodos para trabajar
p = path.with_name("chanchito.py")
print(p)
p = path.with_suffix(".bat")
print(p)
p = path.with_stem("feliz")
print(p)
