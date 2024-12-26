"""Herencia Multiple"""

class Animal:
    def comer(self):
        print("comiendo")

    def pasear(self):
        print("paseando animales")

class Perro: #en este caso perro no está heredando nada
    def pasear(self):
        print("paseando al perro")


class Chanchito(Perro, Animal): #hereda los métodos que le voy agregando
    def programar(self):
        print("programando")

chanchito = Chanchito()
chanchito.pasear() #imprime "paseando al perro" aplicando la Herencia de derecha a izquierda
#es decir que toma los metodos en el orden que le colocamos dentro de ()
#TENEMOS QUE SEGUIR LA REGLA DE METODO QUE SE ENCUENTRE DUPLICADO HAY QUE ELIMNAR Y LO METODOS NO SE REPITAN
