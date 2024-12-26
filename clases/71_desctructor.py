"""Desctructor"""
#método mágico que se ejecuta cuando eliminamos un objeto de la memoria
class Perro:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def __del__(self):
        print(f"Chau Perro 8( {self.nombre}")

    def __str__(self):
        return f"Clase Perro: {self.nombre}"
    
    def habla(self):
        print(f"{self.nombre} dice: GUAU!" )

perro = Perro("Chanchito", 7)
del perro