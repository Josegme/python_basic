"""KWARGS: Key Words Arguments"""

def get_products(**datos): #dos ** para empaquetar todos los parametros 
    print(datos)

#pasamos todos los argumentos a nuestra función
#pero cuando estoy utilizando una kwargs tengo que indicar el nombre del parametro
get_products(id="id", 
             name="iPhone", 
             desc="Esto es un iPhone")  #puedo pasar la cantidad de argumentos que quiera

#esto me devuelve un diccionario -> {'id': 'id'}

#Ahora -> que pasa si quiero acceder a los argumentos desde mi función
#
def get_products1(**celu):
    print(celu["id1"], celu["name1"], celu["parametro"]) #para acceder directamente a los valores que quiero [""]

get_products1(id1="id", 
              name1="Iphone1", 
              desc="Esto es otro telefono",
              parametro="esto es un argumento")
