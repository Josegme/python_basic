"""Loops Anidados"""

for j in range(5): #este es el aouter for/loop
    for k in range(3): #este es el inner for/loop
        print(f"{j}, {k}")

#el código se ejecuta de arriba hacia abajo
#entonces se ejecuta el primer for j=0 y sigue por el siguiente for k=0
#entonces en la linea 3- 0, 0
#tener en cuenta que ingresa al primer for, pero luego deber iterar completamente en el segundo for
#por lo tanto primero cuando entra por primera vez en el for imprime 0
#y luego itera 3 veces (de 0 a 2) en el segundo for -> 0,0 - 0,1 - 0,2 -
#y asi sucesivamente.

#Se Recomienda utilizar el For Anidado solo cuando tenemos que
#solucionar un problema determinado. Pero no se recomienda que sea la primera solución
#sobre todo cuando se analizan millones de datos.


