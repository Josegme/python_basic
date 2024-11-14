"""Ordenando Listas"""
numeros = [2, 4, 1, 45, 75, 22]

#para ordenar Listas utilizamos Método SORT

#numeros.sort()
#print(numeros) me imprime de manera ASC

#si quiero ordenar de manera ordenada o en reversa REVERSE
#numeros.sort(reverse=True)
#print(numeros)

#SORTED devuelve una Nueva lista..es decir que no afecta la lista anterior
numeros2 = sorted(numeros)
print(numeros) #cuando llamamos numeros esta lista no se efecta
print(numeros2) #va a crear una nueva lista ordenada con lo elementos de la lista anterior

numeros2 = sorted(numeros, reverse=True)
print(numeros) #cuando llamamos numeros esta lista no se efecta
print(numeros2)

#que pasa cuando tenemos un lista mas compleja
usuarios = [
        [4, "Juan"], 
        [1, "Felipe"],  
        [5, "Pulga"]    
        ]
usuarios.sort() 
print(usuarios)

#Si tenemos un listado con listado [] o con tuplas ()
#sort va ordenar siempre que el indice este primero
#si quiero que orden tengo que pasar una función ORDENA

usuarios = [
        ["Juan", 1], 
        ["Felipe", 8],  
        ["Pulga", 5] 
        ]
def ordena(elemento):
    return elemento[1]

usuarios.sort(key=ordena) #tambien le puedo pasar reverse=True
print(usuarios)