"""Métodos - String"""

animal = "   chanCHito Feliz   "
print(animal.upper()) #toma el string dentro de la variable y transforma todo a Mayuscula
#método: es una función dentro de un objeto
print(animal.lower()) #toma el string y transforma todo a minusucula

print(animal.capitalize()) #Toma la primera letra pasa a mayuscula y todo el resto a minúscula
print(animal.title()) #pasa a mayuscula la primera letra de cada palabra
print(animal.strip()) #remueve espacios de izq y der del string

animal1 = "   paTIto feliz   "
print(animal1.strip().capitalize())
#estamos encadenando los métodos - tenemos lstrip y rstrip para quitar espacios de izq o der
print(animal1.find("to")) #para buscar una cadena de caracteres
print(animal1.find("ch")) #que pasa si no encuentra (devuelve -1
print(animal1.replace("TI", "ti").strip().capitalize()) #para reemplazar los caracteres 
#tiene que recibir necesariamente dos argumentos 
print("TI" in animal1) #devuelve un boolean para saber si un caracter se encuentra dentro de una variable
print("nCH" not in animal) #busca si no esta 

