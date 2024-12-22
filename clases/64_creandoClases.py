#64 Creando Clases

#para crear una clase utilizamos CLASS -> Pascal Case o Upper Camel Case
#luedo de crear la clase Perro debo agregar todas las variables asociadas a esa clase
#Cuando creamos una funcion dentro de una clase deja de ser una función y se convierte en un MËTODO
#y lo primero que tenemos que escribir dentro es el parametro SELF

class Perro:
    def habla(self): #todas las funciones asociadas a una clase se llaman MÉTODOS
        print("Guau!")

#Perro() #para invoncar la clase llamo directamente a la clase Class()
#debemos asignar a una variable ese objeto
mi_perro = Perro()
print(type(mi_perro))
#imprime -> <class '__main__.Perro'> _main_ se llama modulo de la clase Perro

mi_perro.habla() #habla es el método que nosotros creamos 

#podemos verificar si este objeto es una instancia de alguna clase
print(isinstance(mi_perro, Perro))

