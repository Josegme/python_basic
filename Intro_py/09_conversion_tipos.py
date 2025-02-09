"""Conversion de Tipos"""

x = input("") #Input del usuario x siempre va a ser de tipo string por lo tanto hay q transformar

#int() para pasar a enteros
#str() para pasar a string
#float() para pasar a float
#bool() 
#va a tratar de transformar los datos que le pasemos a booleano
#pero en realidad lo que va a hacer es evaluar en True o False
#dentro de Python existe el concepto de datos evaluados en TRUTHTY Y FALSY
#existen datos que van a ser evaluados evaluados en True o False si le pasamos a Bool
#Falsy -> "" string vacia - cero 0 - None para que bool() devuelva False
#con todo el resto siempre evalua en True
#Ejemplos
print(bool("")) #devuelve False estring vacio
print(bool("0")) #devuelve True es un string
print(bool(None)) #False
print(bool(" ")) #True
print(bool(0)) #False

