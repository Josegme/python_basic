"""Propiedades y Métodos Privados"""

class Perro:
    def __init__(self, nombre, edad):
        self.__nombre = nombre
        self.edad = edad
#cuando creamos una propiedad es como cuando le damos el nombre a un perro
#nunca le vamos a cambiar mas el nombre del perro una vez asignada
#entonces para que eso suceda tenemos que crear a NOMBRE como PROPIEDAD PRIVADA
#para lograr esto vamos a presionar SHIFT+CTROL+P
#elegimos >rename symbol y coloco los __nombre para que sea privado y nadie pueda modificar.

    def habla(self):
        print(f"{self.__nombre} dice: Guau!")

    @classmethod
    def factory(cls):
        return cls("Chanchito feliz", 4) 
    
perro1 = Perro.factory()
perro1.habla()

#__dic__ es un diccionario que nos permite acceder a las propiedades que tiene una instancia de un objeto
print(perro1.__dict__)