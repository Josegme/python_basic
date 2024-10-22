"""Números - Funciones (Funciones Nativas)"""
import math 

print(round(1.3)) #nos devuelve el número entero mas cercado del decimal "reodondea"
print(round(1.9)) #2 en este caso

print(abs(-77)) #nos devuelve el valor absoluto

#Importante: Python no tiene muchas funciones nativas para realizar calculos
#pero si tenemos MODULO de manera nativa que podemos traer e importar para realizar operaciones
"""import math : es el modulo que vamos a importar para poder trabajar (math.py) ya viene escrito en Py"""

print(math.ceil(1.1)) #ceil redondea hacia arriba
print(math.floor(1.99999)) #floor redondea hacia abajo

print(math.isnan(23)) #me indica si el valor que le paso es o no un número (boolean)
#print(math.isnan("23")) 
print(math.pow(10, 3)) #para elevar un número a una potencia..da 1000
print(math.sqrt(9)) #para devolver la raiz cuadrada

#si queremos encontrar todas las funciones 
#NAVEGADOR -> MATH PYTHON Y ESTUDIAR LA INFO


