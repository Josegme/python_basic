#65 Constructor y Propiedades

#el constructor es una funcion que vamos a definir dentro de la clase
#esta se va a definir siempre siempre cuando creamos una instancia

class Perro:
    def __init__(self, nombre, edad): #SELF se utiliza para referenciar las instancias de las clases
        self.nombre = nombre #una propiedad es una varible que se encuentra asociada a una clase
        self.edad = edad

    def habla(self):
        print(f"{self.nombre} dice: Guau!") #para acceder a la propiedad

mi_perro = Perro("Perrito", 1)
mi_perro.habla()
