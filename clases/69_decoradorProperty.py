"""Decorador Property"""

#esto es de apuntes de las clases del profe
"""
class Perro:
    def __init__(self, nombre):
        self.nombre = nombre
    
    @property #solo se utiliza con los getter - que es un método que nos devuelve un valor
    def nombre(self):
        return self.__nombre
    
    @nombre.setter    
    def nombre(self, nombre): 
        print("pasando por setter") #setter setea un valor
        if nombre.strip():
            self.__nombre = nombre
        return

perro = Perro("Choclo")
print(perro.nombre)
    
    """
class Perro:
    def __init__(self, nombre):
        # Usa el setter para inicializar el atributo correctamente
        self.nombre = nombre

    @property
    def nombre(self):
        # Getter: devuelve el valor del atributo privado
        return self.__nombre

    @nombre.setter
    def nombre(self, nombre):
        print("Pasando por setter")
        if nombre.strip():  # Validar que el nombre no esté vacío
            self.__nombre = nombre
        else:
            raise ValueError("El nombre no puede estar vacío o solo contener espacios.")

# Ejemplo de uso
try:
    perro = Perro("Choclo")  # Pasa por el setter al inicializar
    print(perro.nombre)  # Usa el getter
    perro.nombre = "Rex"  # Cambia el nombre usando el setter
    print(perro.nombre)  # Usa el getter
    perro.nombre = "  "  # Esto lanzará un ValueError
except ValueError as e:
    print(e)
    
#volver a revisar este tema