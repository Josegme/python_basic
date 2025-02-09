#67 Métodos de Clases

#creamos unas clases con diferentes propiedades y métodos (funciones)
class Perro:
    patas = 4

    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    @classmethod #para hacerlo como método de clase con CLS, es decir CLS = clase = Perro
    def habla(cls): #podemos tomar este método y hacerlo como método de clase
        print("Guau!")

    #creo la FACTORY METHOD
    @classmethod
    def factory(cls):
        return cls("Chanchito Feliz", 4) #cls = Perro (que es la clase)
    

Perro.habla()
perro1 = Perro("Chanchito", 2)
perro2 = Perro("Felipe", 3)
perro3 = Perro.factory()
print(perro3.edad, perro3.nombre)

#Podemos crear un FACTORY METHOD Fabrica de instancias de nuestra clase. En este caso PERRO
