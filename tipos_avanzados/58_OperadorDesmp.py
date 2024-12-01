"""Operador De Desempaquetamiento"""

lista1 = [1, 2, 3, 4]
    #Si pasamos esta lista a print(lista) nos va a imprimir un listad
    #print(lista)
    #pero si yo quiero que imprimir esta lista pasandole con el valor de su propia posicion print(1, 2, 3, 4)
    #cada uno como argumento de cada alemento de la lista
#print(1, 2, 3, 4)
#print(*lista)
    #para que sirve esto?
    #con el operador de desmpaquetamiento * tambien podemos trabajar en una función
#def n(n1, n2, n3): 
    #si tenemos esos tres argumentos en una lista -> lo que podemos hacer es 
    #llamar a la funcion n le pasamos la lista y le agregamos el operador *

#podemos tambien combinar listas
lista2 = [5, 6]

combinada =["Hola", *lista1, "Mundo", *lista2]
print(combinada)

punto1 = {"x": 19, "y": "hola"}
punto2 = {"y": 15}

nuevoPunto = {**punto1, **punto2}
print(nuevoPunto)
#se imprime asi -> 
#['Hola', 1, 2, 3, 4, 'Mundo', 5, 6]
#{'x': 19, 'y': 15} ->las propiedades son asignadas de Izquierda a Derecha- si no encuentra pasa a la siguiente
nuevoPunto2 = {**punto1, "lala": "Hola Mundo", **punto2, "z": "Hola"}
print(nuevoPunto2) 
#{'x': 19, 'y': 15, 'lala': 'Hola Mundo', 'z': 'Hola'} 
#vemos que primero imprime las listas con las propiedades asignadas
#y luego las propiedades que agregamos dentro de la variable donde llamamos con el print
