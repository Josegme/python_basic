"""Introducción a las Excepciones"""

#tenemos extensiones que nos marcan o permiten que identifiquemos los errores
#print("")

#lista = [1, 2]
#lista[45] # lista[45]
          #  ~~~~~^^^^ esto nos va a marcar un error
#lo que buscamos es que detectemos los errores -> pero si que los usuarios lo "vean"

#n1 = int(input("Ingresa el primer número: "))
#esto me esta pidiendo que ingrese un entero por lo tanto si ingreso otra casa da error

try:  #try es un tipo de excepción
    n1 = int(input("Ingresa el primer número: "))
except:
    print("Ocurrio un error ") 
#la excepción va a activarse cuando ingresemos mal un dato en try
