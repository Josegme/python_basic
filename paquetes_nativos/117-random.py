import random 
import string

#*
lista = [1,2,3,4,5,6,7,8]
lista2 = [1,2,3,4,5,6,7,8]
random.shuffle(lista)

print (
    random.random(),
    random.randint(1, 10),
    #random.shuffle([1,2,3,4,5,6,7,8]) #devuelve none por que debe ser una secuencia mutable
    #por eso debemos crear un lista*
    lista,
    random.choice(lista2),
    #si quiero obtener una cantidad de valores aleatorios determinado
    random.choices(lista2, k=3),
    random.choices("abcdefgh.,123", k=3) #esto nos permite generar cadenas aleatorias para contraseñas por ej.
#podemos transformar en un string-> "".join(random.chocices("abcdefghi.,123", k=3))
)

chars = string.ascii_letters
digitos = string.digits
seleccion = random.choices(chars + digitos, k=16 )
#contrasena sin ñ por si trabajo con otro desarrollador
password = "".join(seleccion)
print(password)

#y asi podemos crear num aleatorios, desordenar listas, solicitar elementos aleatorios, crear contraseñas, etc
