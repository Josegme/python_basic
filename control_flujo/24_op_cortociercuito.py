"""Operadores de Cortocircuito"""

#Declaro las variables
gas = False
encendido = True
edad = 18

if gas and encendido and edad > 17:
    print("Puedes Avanzar")
else:
    print("Si Gas es False - > toda la operacion es Falsa")

#Evalua de izq a derecha ------> si el primero es falso ya no evalua el resto
#de esta manera ahorramos memoria y ejecutamos mas rápido
