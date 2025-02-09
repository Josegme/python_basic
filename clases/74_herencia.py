"""Herencia"""
class Animal:
    def comer(self):
        print("comiendo")

class Perro(Animal): 
    def pasear(self):
        print("paseando")


class Chanchito(Perro):
    def programar(self):
        print("programando")

#el primer problema que tenemos que es que en la implementacion de los contructoes
#tenemos dos con el mismo nombre en diferentes clases -> COMER
#y si tenemos que cambiar en alguna de las clases, debemos cambiar en todas y cada una
#lo cual podriamos tener o generar muchos errores 
#para poder solucionar esto creamos una primera clase general
#y le pasamos el constructor comer a cada una de las clases
#agrego entre (class) la clase que voy asignar a todos las clases dentro de sus contructore

chanchito = Chanchito()
chanchito. #va a tomar todos los métodos y propiedades que haya hererado 
#se recomienda no hacer mas de dos veces
#Herencia multinivel
