"""lista de Comprensión"""

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
nombres = [usuario for usuario in usuarios if usuario[1] > 2]

print(nombres)
#podemos modificar lista, filtrar y hacer nuevas listas.



valor = [usuario[1] for usuario in usuarios]
print(valor)