"""Pila - > LIFO"""
#por ejemplo el historial de Navegación -> el ejemplo cuando estamos por comprar algo pero nos arrepentimos y
#vamos para atras. 
pila = []
pila.append(1)
pila.append(2)
pila.append(3)
print(pila)
ultimoElemento = pila.pop()
print(ultimoElemento)
print(pila)
#para trabajar con PILA tengo que trabajar con la LISTA pero
#con la lógica de pila y para ellos solo utilizamos .append y .pop
print(pila[-1])
pila.pop()
pila.pop()

if not pila:
    print("Pila vacia")