"""Diccionarios"""

#UNO DE LOS TIPOS DE DATOS MAS UTILIZADOS JUNTO CON LAS LISTAS
#son una colección de datos agrupados con clave: valor
#muy utilizado para BD

punto = {"x": 25, 
         "y": 50
         } #solo acepta string como LLAVE: cualquier tipo

print(punto)
#si queremos acceder a alguno de los valores de la llave
print(punto["x"])
print(punto["y"])

#podemos agregar mas LLAVES al diccionario
punto["z"] = 45
print(punto)

#que pasa si quiero acceder a una llave que no existe
#print(punto, punto["lala"]) #me va a dar un error por que lala no existe en mi diccionario

#podemos preguntar si lala se encuentra en nuestro diccionario
if "lala" in punto:
    print("encontre lala", punto["lala"])
else: 
    print("no existe lala en el diccionario.")

print(punto.get("x")) 
print(punto.get("lala")) #devuelve NONE
print(punto.get("lala", "no existe")) #puedo poner que devuelva algo por defecto cuando no existe el valor
print(punto.get("lala", 0)) #le paso ese valor como segundo argumento

#si quiero eliminar alguna llave con su valor
del punto["x"]
print(punto)

del (punto["y"])
print(punto)

#vamos a agregar la llave x
punto["x"] = 25

for valor in punto:
    print(valor) #trae solo la llave

for valor in punto:
    print(valor, punto[valor]) #trae la llave valor

#otra forma de acceder al diccionario
for valor in punto.items():
    print(valor) #esto me devuelve los elementos dentro del diccionario en forma de tuplas 

#para desempaquetar los elementos dentro del diccionario
for llave, valor in punto.items():
    print(llave, valor) 

#estas son todas las formas de acceder a los diccionarios.
#cuando trabajamos con BD tenemos siempre que trabajar con el id
usuarios = [
    {"id": 1, "nombre": "Chanchito" },
    {"id": 2, "nombre": "Feliz" },
    {"id": 3, "nombre": "Nicolas" },
    {"id": 4, "nombre": "Felipe" },
]
#si queremos acceder a los nombres tenemos que iterar en usuarios
for usuario in usuarios:
    print(usuario["nombre"])