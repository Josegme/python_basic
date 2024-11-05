"""Funciones"""

#por ejemplo print("Hola mundo!") -> es una función que automatiza un proceso

#para escribir una FUNCIÖN -> def nombreMiFuncion():

def hola():
    print("hola Mundo")
    print("Ultimate Python")

#debemos llamar a nuestra función para que se ejecute el bloque

hola() #llamada de función
#cada vez que llame a la función se va a ejecutar el bloque de código que esta dentro
print("")
hola()
print("")

#Argumentos y Parametros -> podemos utilizar una y otra vez pero con difereentes información
def saludar(nombre): #para utilizar una variable que pueda recibir la función y utilizarla dentro del contexto de la función
    print("Hola Mundo!")
    print(f"Bienvenido {nombre}") #De esta manera el parametro NOMBRE podra ser utilizado en nuestra función

saludar("Nicolas") #si nuestra función tiene un parámetro definido ..siempre voy a tener que darle un Valor cuando llamo a la Función
print("")
saludar("Chanchito Feliz")
print("")

#Como nombramos los valores que llamamos o recibimos a los valores de la función
#en este caso -> el Parámetro se llama nombre
#pero cuando llamamos una función le llamamos dandole un valor de ARGUMENTO
#valor que le paso al parámetro se llama argumento

#Podemos colocar mas de un parametro para que poder darle mas argumentos a la función cuando la llamemos
def saludo(name, lastname):
    print("Hola Mundo")
    print(f"Hola {name} {lastname}")

#como tiene de dos parametros cuando llame a la función 
#debemos colocar dos Argumentos como valor (si no me da una advertencia y marca un error)
saludo("José", "Martin")
print("")
saludo("Nico", "Cheto")
print("")

#para utilizar argumentos opcionales -> es decir que queremos colocar en caso de que no tengamos algú argumento
def otroSaludo(name1, lastname1="Desconocido"): #aca indicamos que valor debe tomar el argumento por defecto
    print("Esta es otra Función")
    print(f"Tu nombre es {name1} y tu apellido es {lastname1}")

otroSaludo("Julio", "Ramirez")
otroSaludo("Fulano") #en este caso como no le pasé ningú argumento a la función va a tomar el que escribi que tome por defecto en el parametro.

#37 Argumentos Nombrados -> puede ser que avance en mi código y no encuetre la función pero podemos aclarar que argumento le corresponde a cada parametro 
saludo(lastname="Schurman", name="Nicolas")
#de esta manera asigno el argumento para cada parámetro y la función tome en el lugar que le corresponde.


