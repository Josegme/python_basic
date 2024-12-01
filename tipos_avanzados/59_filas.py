"""59 Filas se rigen por FIFO - Firts in/Firts out"""

#Si tenemos personas que llegan a hacer una fila 
#primero se coloca una persona, atras se coloca otra persona y asi hasta que se haga una fila de 4 personas
#es decir que en esta fila tenemos 4 elementos y en una fila se caracteriza por que se cumple 
#con FIFO -> el primero en entrar es el primero en salir (por que el que esta primero le atienden primero por ejemplo)
lista =[1, 2, 3, 4] #el problema viene cuando la lista tiene muchos datos por ejemplo 100000000
#entonces vamos a trabajar de con una COLECCIÓN "deque" (diquiu)
from collections import deque

fila = deque([1, 2])
#puedo agregar elementos a la lista de fila con fila.append()
#fila.append(3)
#fila.append(4)
#fila.append(5)
print(fila)
#si quiero eliminar elementos -> debo comenzar con la izquierda. 
fila.popleft()
#agrego otro popleft()
fila.popleft() #deberia imprimir "fila vacia"
print(fila)
#luego voy a ir eliminando con popleft los elementos de la lista veamos 

if not fila: #lista vacia seria falsy
    print("fila vacia")