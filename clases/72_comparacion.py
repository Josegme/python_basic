"""Comparando objetos"""

class Coordenadas:
    def __init__(self, lat, lon):
        self.lat = lat
        self.lon = lon
    
    def __eq__(self, otro):
        return self.lat == otro.lat and self.lon == otro.lon
    
    def __ne__(self, otro):
        return self.lat != otro.lat and self.lon != otro.lon

    def __lt__(self, otro):
        return (self.lat + self.lon) < (otro.lat + otro.lon)
    
    def __le__(self, otro):
        return self.lat + self.lon <= otro.lat + otro.lon


#para pasar una nueva instancia vamos a tener que pasarle un valor de Lan y lon a nuestra clase
coords = Coordenadas(45, 27)
coords2 = Coordenadas(45, 27)
#queremos saber si esas dods coordenadas son iguales
#rint(coords == coords2) #imprime False
#como hago para quenos devuelva true ya que son las mismas coordenadas entonces def __eq__
#print(coords != coords2) 
#imprime True para == y False para != lo que es correcto ya que coords==coords2
print(coords <= coords2)
