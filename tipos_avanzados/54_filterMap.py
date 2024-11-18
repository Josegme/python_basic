"""Filter y Map"""
#Esto es por si nos topamos con un manejo de listas con Filter o Map
#también pueden operar ambas a la vez

usuarios = [
        ["Chanchito", 4], 
        ["Felipe", 1],  
        ["Pulga", 5] 
]
#del listado de Usuarios que tenemos solo queremos el NOMBRE
#entonces solo queremos los nombres de las listas

#nombres = []
#for usuario in usuarios:
#  nombres.append(usuario[0])
#print(nombres)

#map
#variable = [expresion[item que quiero hacer la lista] for item in items]
#nombres = [usuario[0] for usuario in usuarios]
#Filter
# si yo quiero filtrar datos de esa lista
#nombres = [usuario for usuario in usuarios if usuario[1] > 2]

#print(nombres)
#podemos modificar lista, filtrar y hacer nuevas listas.

"""para hacer Filter o Map"""
#nombre = list(map(lambda usuario: usuario[0], usuarios))


#filter recibe una funcion LAMDAsi evalua en True devuelve el elemento
menosUsuarios = list(filter(lambda usuario: usuario[1]> 2, usuarios))
print(menosUsuarios)