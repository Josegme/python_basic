"""Excepciones Personalizadas"""

class MiError(Exception):
    "Esta clase es para representar un Error"

    def __init__(self, mensaje, codigo):
        self.mensaje = mensaje
        self.codigo = codigo

    def __str__(self):
        return f"{self.mensaje} - codigo: {self.codigo}"

        

def division(n = 0):
    if n == 0:
        raise MiError("No se puede dividir por cero", 805)
    return 5/n
#puedo buscar las excepciones en python errors and exceptions 

try:
    division() 
except MiError as e:
    print(e)

#puede ser que necesitemos agregar mayor información lógica cuando estamos ejecutando nuestro programa
#creamos un def 