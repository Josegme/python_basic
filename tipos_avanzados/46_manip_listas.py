"""46 -> Manipulando Listas"""

mascotas = ["Wolfgang", "Pelusa", "Pulga", "Copito"]
print(mascotas[0]) #Cuando quiero acceder a un elemento en determinada posición

#Cuando quiero modificar algún elemento del listado
mascotas[0] = "Bicho" 
print(mascotas)

#si quiero acceder a una sección de la lista
print(mascotas[1:3]) #para seleccionar ciertos elementos dentro de la lista
#por defecto si no coloco alguna posición de izq o der toma por defecto el 0 o el ultimo como limitas de busqueda de elementos
print(mascotas[:3])
print(mascotas[2:]) #desde donde hasta donde 
#Que pasa si solo quiero acceder a elementos pares 
print(mascotas[::2]) #va saltando de dos en dos
print(mascotas[1::2]) 
print(mascotas[1:2:2])

numeros = [20]
print(numeros)
