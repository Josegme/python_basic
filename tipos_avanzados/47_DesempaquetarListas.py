"""Desempaquetar Listas"""

numeros = [1, 2, 3, 4, 5, 6, 7, 8] #si quisieramos obtener los num de esta lista y quiero utiliarlos como variables

#en el primero de los caso deberia asignar cada posición a una variable
#primero = numeros[0]
#segundo = numeros[1]
#tercero = numeros[2]
#pero esto no es buena práctica

#primero, segundo, tercero = numeros
#de esta manera asigno a nombre el orden que corresponde a las variables en la lista
#print(primero, segundo, tercero)
#ahora puede ser que yo quiera obtener un solo valor de la lista
#entonces debo escribir de la siguiente manera
#primero, *otros = numeros
#print(primero, otros)

#que pasa cuando tenemos un listado que tiene infinitos elementos
#primero, segundo, *otros = numeros
#print(primero, segundo)
primero, segundo, *otros, ultimo = numeros
print(segundo, otros, ultimo)
primero, segundo, *otros, penu = numeros
print(segundo, penu, otros)
