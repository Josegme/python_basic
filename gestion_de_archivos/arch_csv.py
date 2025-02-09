#Trabajar con archivos CSV

import csv 
import os
"""
#escribir e indicar la ruta del archivo
with open("gestion_de_archivos/archivo.csv", "w") as archivo:
    writer = csv.writer(archivo)
    writer.writerow(["twid_id", "user_id", "text"])
    writer.writerow([1000, 1, "este es un twit"])
    writer.writerow([1001, 2, "otro twit"])
    """
"""
with open("gestion_de_archivos/archivo.csv") as archivo:
    reader = csv.reader(archivo)
    print((list(reader)))
    for linea in reader:
        print(linea)
"""

with open("archivos/archivo.csv") as r, open("archivos/archivo_temp.csv", "w") as w:
    reader = csv.reader(r)
    writer = csv.writer(w)
    for linea in reader: 
        if linea[0] == "1000":
            writer.writerw([1000, 1, "texto modificado"])
        else:
            writer.writerow(linea)
    os.remove("archivos/archivo.csv")
    os.rename("archivos/archivo_temp.csv", "archivos/achivo.csv" )


