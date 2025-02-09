"""Else y Finally"""
"""
try:  
    n1 = int(input("Ingresa el primer número: "))
except Exception as e:
    print("Ocurrio un error!")
else:
    print("No ocurrio ningún error")
"""

try:  
    n1 = int(input("Ingresa el primer número: "))
except Exception as e:
    print("Ocurrio un error!")
finally:
    print("Se ejecuta siempre!")
