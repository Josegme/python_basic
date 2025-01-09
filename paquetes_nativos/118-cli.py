import os
from pathlib import Path
import sys

#print(sys.argv) #esto me abre la ventana de cmd
#python3 paquetes-nativos/118-cli.py

def cli(args):
    if len(args) == 1:   
        print("no se pasaron argumentos")
        return 
    if len(args) != 3:
        print("se necesitan dos argumentos")
        return
    origen = args[1]
    o = Path(origen)
    if not o.exists():
        print("Origen no existe")
        return
    
    destino = args[2]
    d = Path(destino)
    if d.exists():
        print("el destino no puede existir")
        return
    
    os.rename(str(origen), str(destino))
    print("Archivo renombrasdo con exito")



cli(sys.argv)
"""

"""