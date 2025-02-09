""" Loop FOR tienen diferente usos
Cumple multiples funciones:
1 - Para Iterar una lista de Elementos: Si tenemos un listado de Usuarios
cada usuario tiene su nombre y apellido-> si necesistamos el nombre completo
debemos crear de manera virtual el campo "nombre Completo"
2 - Para Buscar elemento - Operaciones Matemáticas ---etc
"""
#range crea una secuencia de numeros ..en este caso hasta 4 o sea itera de 0 a 4 (5 veces)
#entonces número va a tener el valor 0, 1, 2, 3 , 4. 
for numero in range(5): 
    print(numero, numero* 'Hola Mundo') 

print('')

"""for desde in range(9):
    print('Imprime en un rango de 0 a 8 (es decir, hasta n-1)')
    print(desde)"""

#27 for else -> Supongamos que vamos a buscar un número dentro del rango
#una vez que encuentro el número "elemento que estoy buscando dentro del rango"
#deberia cortar el bucle, por que sino el bucle va a recorrer todo el rango
#ejemplo2 
buscar = 3
for numero in range(5):
    print(numero) #para ver cuantas veces itera nuestro bucle hasta encontrar el número buscado
    if numero == buscar:
        print("encontrado", buscar)
        break #para detener el bucle

#Puede ser que estemos buscando un elemento que este fuera del rango
# y además si no encuentra por lo tanto no se va a cortar en el BREAK
#Veamos otro ejemplo
buscar1 = 10
for numero in range(7):
    print(numero)
    if numero == buscar1:
        print("Encontrado", buscar1)
        break
else:
    print("No se encontro el elemento buscado")
#es decir que estamos ejecutando un FOR ELSE
