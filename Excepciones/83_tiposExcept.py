"""Tipos de Excepciones"""
"""
try:  
    n1 = int(input("Ingresa el primer número: "))
except Exception as e:
    print(type(e))
#si coloco un string entonces devuelve <class 'ValueError'> que es el tipo de error 
#tambien pueden surgir otro tipo de errores -> <class 'NameError'>
"""

try:  
    n1 = int(input("Ingresa el primer número: "))
    jlkjrjoje  #este es un ejemplo de error y vamos a manejar con otro except
except ValueError as e:
    print("Ingrese un valor que corresponda.")
except NameError as e:
    print("Ocurrio un error! ")