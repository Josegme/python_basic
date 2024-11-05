"""XARGS"""

def suma(a, b):
    print(a + b)

suma(2, 5) 
#cada vez que necesite sumar voy a tener que incorporar un parametro más
#de esa manera cuando agregue un valor al argumento pueda ejecutar
#por ejemplo si quiero sumar un número mas deberia agregar c
""" def suma(a, b, c)
    print(a + b + c)
    
suma(2, 5, 7)"""

#para que sepamos que son muchos elementos
def sumaXargs(*numeros): #le paso un nombre en plural y le coloco * para que tome todos los numeros
    resultado = 0 #como numeros es un iterable vamos a necesistar un contador 
    for numero in numeros: #para que itere y sume todos los numeros que le pase al argumento
        resultado += numero #muestra el resultado
    print(resultado) #imprime el resultado
#para imprimer el for el prin debe estar debajo del for identado correctamente
#si esta mal identado se puede crear un bucle infinito y dar error

sumaXargs(2, 5, 7)
sumaXargs(2, 5)
sumaXargs(2, 8, 45, 32)
