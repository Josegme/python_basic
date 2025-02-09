from io import open
#escritura
texto = "Hola Mundo!"

#archivo = open("gestion_de_archivo/archivos/hola-mundo.txt", "w")
#archivo.write(texto)
#archivo.close()
#modo con el cual vamos a abrir el archivo w=write

#lectura
#archivo = open("gestion_de_archivo/archivos/hola-mundo.txt", "r")
#texto = archivo.read()
#archivo.close()
#print(texto)

#archivo = open("gestion_de_archivo/archivos/hola-mundo.txt", "r")
#texto = archivo.readlines()
#archivo.close()
#print(texto)

#with open("gestion_de_archivos/archivos/hola-mundo.txt", "r") as archivo:
    #todo identado luego para escribir el código
    #__enter__ se ejecuta cuando hayamos abierto el archivo
    #__exit__ se ejecuta cuando termina de ejecutar todo el bloque y se cierra
    #print(archivo.readlines())
    #for linea in archivo: 
        #print(linea)

#con método de SEEK podemos utilizar a parte de WITH

#agregar - lectura - escritura

with open("gestion_de_archivos/archivos/archivo-prueba.txt", "r+") as archivo:
    texto = archivo.readline()
    archivo.seek(0)
    texto[0] = "Chanchito Feliz"
    archivo.writelines(texto)

#r+ solo reemplaza lo que indicado
