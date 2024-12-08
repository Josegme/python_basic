from pprint import pprint 
#1 Eliminar los espacioes en Blanco de un string
    #creo un string
string = "Hola mundo este es mi String"
#debo crear una función que me devuelva el string sin los espacios en blanco

def quita_espacios(texto):
    return [char for char in texto if char !=" "]
#creo una variable y le llamo a la función para luego imprimir



#2 Contar en un deccionario cuantos caracteres se repiten en un string
#sabemos que los string asi como las Listas son iterables
def cuenta_caracteres(lista):
    chars_dict = {}
    for char in lista:  #debemos preguntar si existe el caracter en el diccionario chars_dict
        if char in chars_dict:
            chars_dict[char] += 1 #vamos a acceder con char a nuestra lista
        else:
            chars_dict[char] = 1
    return chars_dict

#3 Ordenar las llave de un diccionario por el valor que tienen y devolver una lista
#que contienen tuplas
def ordena(dict):
    return sorted(
        dict.items(),
        key=lambda key: key[1],
        reverse = True,
    )

#4 De un listado de tuplas, devolver las tuplas que tengan el mayor valor
def mayores_tuplas(lista):
    maximo = lista[0][1]
    respuesta = {}
    for orden in lista:
        if maximo > orden[1]:
            break
        respuesta[orden[0]] = orden[1]
    return respuesta

#5 Crear un mensajes que diga los caracteres que mas se repitan con 4 repeticiones
def crea_mensaje(diccionario):
    mensaje = "Los que mas se repiten son: \n"
    for key, valor in diccionario.items():
        mensaje += f"- {key} con {valor} repeticiones \n"
    return mensaje

#1
sin_espacios = quita_espacios(string)
print(sin_espacios)
#2
contados = cuenta_caracteres(sin_espacios)
print(contados)
#vemos que la impresion es complicada de leer -> podemos importar pprint 
pprint(contados, width=1)
#3 
ordenados = ordena(contados)
print(ordenados)
#4
mayores = mayores_tuplas(ordenados)
print(mayores)
#5
mensaje = crea_mensaje(mayores)
print(mayores)