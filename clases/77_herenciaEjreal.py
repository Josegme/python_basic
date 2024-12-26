"""Ejemplo Real - Herencia"""

#cuando hacemos BD tenemos Leer - Crear - Actualizar - Eliminar los datos de los usuarios
#ya teniendo nuestras 4 acciones de CRUD
#vamos a tener que crear nuestros métodos 

class Model():
    tabla = False
    
    def __init__(self): 
        if not self.tabla: #tenemos un constructor que va a controlar que hayamos definido una propiedad -> Tabla
            print("Error, tienes que definir una tabla")

    def guardar(self): 
        print(f"Guardando {self.tabla} en BBDD") #método que guarda recursos en nuesra BBDD

    @classmethod
    def buscar_por_id(sefl, _id):
        print(f"buscando por ir {_id}")

class Usuario(Model):
    tabla = "Usuario"

usuario = Usuario()

usuario.guardar()
Usuario.buscar_por_id(123)
