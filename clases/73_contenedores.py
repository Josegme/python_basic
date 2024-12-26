"""Contenedores"""

class Producto:
    def __init__(self, nombre, precio): #constructor de producto
        self.nombre = nombre
        self.precio = precio
    
    def __str__(self): #metodo str para devolver un string con datos del producto
        return f"Producto: {self.nombre} - precio: {self.precio}"

class Categoria:
    productos = [] #necesitamos la prodpiedad que contenga los productos que agregamos  a la lista

    def __init__(self, nombre, productos): #constructor de productos en categorias
        self.nombre = nombre
        self.productos = productos

    def agregar(self, producto): #metodo para agregar prodcutos 
        self.productos.append(producto)

    def imprimir(self):
        for producto in self.productos:
            print(producto)

    def imprimir(self):
        for producto in self.productos:
            print(producto)


kayak = Producto("Kayak", 1000)
bicicleta = Producto("bicileta", 750)
surfboard = Producto("Surfboard", 500)
deportes = Categoria("Deportes", [kayak, bicicleta])
deportes.agregar(surfboard)
deportes.imprimir()
#podemos almacenar objetos dentro de objetos 
