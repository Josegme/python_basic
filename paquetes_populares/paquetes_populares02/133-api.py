"""
    cuando estamos trabajando con una API nos otorga un USUARIO o CONTRASEÑA
    y al API nos entrega una KEY o API KEY esta necesariamente hay que agregar a
    todas las peticiones que hagamos (GET, PUT, PATH etc) 
    y van a tener que tener en todas sus cabeceras la API KEY
"""
url = "https://jsonplaceholder.typicode.com/user/2"
apikey = "123456"
headers = {
    "Aurhorization": f"Bearer {apikey}"
}
#en el 95% de los casos vamos a tener que tener la API en la cabezera 
#depende de las API 

r= requests.delete(url, timeout=10, headers=headers)
print(r)

