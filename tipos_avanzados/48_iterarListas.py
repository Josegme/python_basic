"""Iterar Listas"""

#todas las listas son iterables 
mascotas = ["Pelusa", "Pulga", "Felipe", "Chanchito Feliz"]
#for para iterar los elementos de nuestra lista

for mascota in enumerate(mascotas): #funcion ENUMERATE con argumento mascotas 
    print(mascota)

    #esto me va a devolver tuplas/listado de tuplas
    #(0, 'Pelusta')
    #(1, 'Pulga')
    #(2, 'Felipe')
    #(3, 'Chanchito Feliz')

for indice, mascota in enumerate(mascotas): #funcion ENUMERATE con argumento mascotas 
    print(indice, mascota) #si le paso una posición INDICE