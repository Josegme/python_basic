"""Polimorfismo"""
from abc import ABC, abstractmethod

class Model(ABC):
    @abstractmethod
    def guardar(self):
        pass

class Usuario(Model):
    def guardar(self):
        print('guaradando en BBDD')

class Sesion(Model): #las sesiones son lo que permite a un Servidor identificar se esta conectando y la peticion
    def guardar(self):
        print('guardando en archivo')

def guardar(entidades):
    for entidad in entidades:
        entidad.guardar()

usuario = Usuario()
sesion = Sesion() 
#entonces estamos teniendo dos clases que implementan el mismo método

guardar([sesion, usuario])