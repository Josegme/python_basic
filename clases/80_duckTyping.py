"""Duck Typing"""

class Usuario():
    def guardar(self):
        print('guaradando en BBDD')

class Sesion(): #las sesiones son lo que permite a un Servidor identificar se esta conectando y la peticion
    def guardar(self):
        print('guardando en archivo')

def guardar(entidades): #el for va funcionar perfectamente salvo que llame al método de guardar
    for entidad in entidades:
        entidad.guardar()

usuario = Usuario()
sesion = Sesion() 
#entonces estamos teniendo dos clases que implementan el mismo método

guardar([sesion, usuario])