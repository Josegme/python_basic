"""Expresion LAMBDA"""

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

usuarios.sort(key=lambda el: el[1]) #tambien le puedo pasar reverse=True
print(usuarios)

#estar haciendo funciones anonimas todo el tiempo es mala practica
#pero Si voy a USAR la función una ÚNICA vez -> si puedo utilizar esa función anónima
