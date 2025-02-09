#66 Propiedades de clases e instancias

class Perro:
    patas = 4
    def __init__(self, nombre, edad): 
        self.nombre = nombre
        self.edad = edad
#para crear propiedades dentro de una clase utilizamos SELF.NombreDeLaPropiedad


    def habla(self):
        print(f"{self.nombre} dice: GUAU!")


print(Perro.patas)

#puede cambiar a patas haciendo
Perro.patas = 3
mi_perro = Perro("Frodo", 5)
mi_perro.patas = 5
mi_perro2 = Perro("Felipe", 1)
print(Perro.patas)
print(mi_perro.patas)
print(mi_perro2.patas)