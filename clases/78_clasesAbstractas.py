"""Clases Abstractas"""
from abc import ABC, abstractmethod  # Importamos lo necesario

class Model(ABC):
    def __init__(self): 
        if not hasattr(self, 'tabla') or not self.tabla:  # Validamos la propiedad `tabla`
            raise AttributeError("Error, tienes que definir una tabla")

    @property
    @abstractmethod
    def tabla(self):
        pass

    @abstractmethod
    def guardar(self): 
        pass

    @classmethod
    def buscar_por_id(cls, _id):
        print(f"Buscando en la tabla {cls.tabla} por ID {_id}")

class Usuario(Model):
    @property
    def tabla(self):
        return "Usuario"

    def guardar(self):
        print(f"Guardando en la tabla {self.tabla} en BBDD")

# Ejemplo de uso
usuario = Usuario()  # Creamos una instancia de Usuario
usuario.guardar()  # Llamamos al método guardar
Usuario.buscar_por_id(123)  # Llamamos al método de clase

"""
Error en la declaración del constructor __init__ en Model:
El constructor intenta verificar self.tabla, pero en Python las propiedades decoradas con @property no se inicializan automáticamente. Al ser abstracta, tabla no está definida en la clase base, lo que lleva a un problema de referencia.

Indentación incorrecta en el método guardar:
El método guardar no está correctamente indentado, por lo que está anidado dentro del método tabla, lo cual no es correcto.

Creación de instancia de una clase abstracta:
No puedes instanciar una clase abstracta como Model. Es necesario definir todas las propiedades y métodos abstractos en una subclase antes de poder instanciarla.

Falta de implementación del método abstracto guardar en la subclase Usuario:
La subclase Usuario hereda de Model, pero no implementa el método abstracto guardar, lo cual es obligatorio.
"""