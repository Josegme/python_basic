"""Alance - > SCOPE"""
saludo = 25 #Esta var esta definida en el ambito global

"
def saludar():
    global saludo
    saludo = "Hola Mundo"

def saludaChanchito():
    saludo = "Hola Chanchito" #definimos la variable
    print(saludo) #luego la llamo

#las variables que se encuentra dnetro de cada Función que definimos 
#son completamente distintas por que estan fuera del alcance y estan dentro del bloque de la función
#por lo tanto estan en un ambito local y se ejecutara desde adentro de la función 
#y no puedo acceder desde afuera -> desde el ambito global, es decir son var completamnente independientes
    

#cuando definimos una funcion con una variable podemos llamar a la variable 
#desde adentro de esa misma función y no por fuera

#saludar() #toma la variable local de la función
#print(saludo) #en esta línea toma la variable de alcance global

#utilizar varibles globales se considera una mala práctica
#para evitar errores 

#si tenemos que utilizar variables globales se recomienda de esta manera
"""
def saludar(): 
    global saludo
    saludo = "Hola Mundo"
"""
resultado1 = saludo + 3
print(resultado1)
saludar()
resultado2 = saludo + 3
print(resultado2)
#y esto va a dar un error por que como la variable esta definida en el ambito global 
#con el mismo nombre -> entonces la Función te cambio el tipo al definir saludo como "hola mundo"
#es decir creas una variable global pero luego cuando definiste la función con global 