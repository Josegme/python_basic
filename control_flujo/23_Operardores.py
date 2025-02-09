"""Operadores Lógicos"""

#AND - OR - NOT

#Si tenemos dos variables
gas = False
encendido = True
edad = 16

if not gas and encendido and edad >18: 
    print("Puedes Cocinar ")
else:
    print("No puedes cocinar")
#si ambos son True envia el msj

if gas and (encendido or edad > 18):
    print("Puedes cocinar-pero debes controlar")
#si uno de los dos es TRUE - Envia el msj


#Como quedaria esto con Operador Ternario
if gas and (encendido or edad > 17):
    print("puedes avanzar")

#utilizando el NOT
if not gas and (encendido or edad > 17):
    print("Como not gas (F) y 'Encendido es False' pero es a mayor a 17 es True")
    print("puedes avanzar")