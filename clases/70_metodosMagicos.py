"""Métodos Mágicos"""

class Perro:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def __str__(self):
        return f"clase Perro: {self.nombre}"

    def habla(self):
        print(f"{self.nombre} dice: GUAU!")

#se van a ejecutar sin que le estemos llamando directamente

perro = Perro("chanchito", 7)
print(perro)
#podemos tomar una nueva variable y crear 
texto = str(perro)
print(texto)

#los principales métodos mágicos podemos ir a google 
#magic methods python
#a guide to python magic methods 