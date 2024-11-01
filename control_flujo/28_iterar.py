"""Trabajamos con Iterables cuando dentro del RAGNGE(iterable) existe un 
elemento con el cual podamos iterar"""

buscar = 10

for numero in range(5):
    print(numero)
    if numero == buscar:
        print("Encontrado el ", buscar)
        break
else:
    print("No encontre el número buscado.")

#Lo que debemos entender es que dentro del RANGE(iterables)
#en Python existen muchos iterables: LISTAS - TUPLAS - STRINGS etc

for char in "Ultimate Python": #esamos iterando un string
    print(char)
