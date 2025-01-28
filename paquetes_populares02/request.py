"""
API REST
es el formato mas comun con el cual podemos trabajar en internet 
para poder obtener datos en una app u obtener datos. Por ejemplo si queremos guardar
datos desde nuestra app para no guardar a todo en nuestra app.
por ej si tenemos https://api.holamundo.io/users/
esto va a tener una lista de usuarios
es una capa con la que vamos a iteractuar API= appication programming interface
Re -> represetational
S -> state -> 
T -> transfer
podemos utilizar para los tipos de datos que necesitemos o queramos representar en estados
"""
#si queremos interactuar con la URL vamos a interactuar con diferentes "VERBOS"
#GET -> se utiliza para listar "leer"
#POST -> para crear un usuario
#PUT / PATCH (reemplazar o reemplazar) -> se utiliza para reemplazar algo. 
#DELETE -> para eliminar
#para acceder a los endpoint voy a acceder con los "VERBOS" y de esa manera manipulo el endpoint
#por ejemplo vamos JSONtypicode -> JSONPLACEHOLDER -> Resources 
#vamos a acceder al de user -> la URL es el endpoint con el recursos que vamos a utilizar o acceder
import requests

#url = "https://jsonplaceholder.typicode.com/users"

#r = requests.get(url, timeout=10)
#print(
#   r.status_code,
#   r.text,
#)
#r = r.json()

#for user in r:
   # print(user["name"]) #podemos obtener asi un listado o un usuario en particular.


#url = "https://jsonplaceholder.typicode.com/users/1"
#r = requests.get(url, timeout=10)
#print(r.json())

url = "https://jsonplaceholder.typicode.com/users/1"
user = {
    "name": "Chanchito Felizs"
}
r = requests.post(url, timeout=10, data=user)
print(r.status_code)

#lo mismo para put y patch
#hay que seguir la conveción
#200=listar 201=crear 204=actualizar o eliminar.