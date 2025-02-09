"""Anulación de Método o metthod override"""

#cuando tomamos un método que hayamos heredado y decidimos reemplazarlo para cambiar la funcionalidad
class Ave:
    def vuela(self):
        print("vuela ave")

class Pato(Ave): #hereda de Ave
    def vuela(self):
        super().vuela()
        print("vuela pato")

pato = Pato()
pato.vuela() 
#vemos que devuelve "vuela pato" y ¿por que?
#por que vomo definimos vuela en la subclase esta reemplaza al método 
#de la clase Ave por el método de la subclase (pato es subclase)

#si utilizamos super().classpadre o podemos hacer tambien con el constructuor
