"""Tupla"""

#es exactamente lo mismo que una lista pero no se pueden modificar
#podemos crear otras tuplas a partir de otras tuplas

numeros =(1, 2, 3) + (4, 5, 6)
print(numeros)
#es decir, que no queremos modificar accidentalmente un listado

#puedo usar tuple para hacer una lista iterable -> 
#si queremos crear una variable y lo definimos como tuple por que todo lo que esta adentro es ITERABLE
punto = tuple([1, 2])
print(punto)

#se puede realizar todas las operaciones de una lista menos appen o pop 
#recuerda que no se pueden modificar.
menosNumeros = numeros[:2]
print(menosNumeros)

primero, segundo, *otros = numeros
print(primero, segundo, otros)

# SI QUEREMOS MODIFICAR UNA TUPLA (AUNQUE NO SE RECOMIENDA)
listaNumeros = list(numeros)
listaNumeros[0] = "Chanchito Feliz"
print(listaNumeros)
#ENTONCES EN ESTE CASO MODIFICAMOS LA LISTA PERO NO LA TUPLA
print(numeros) #me imprime la tupla inicial
