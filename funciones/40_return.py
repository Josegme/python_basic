"""Return """
#

def suma(a, b):
    resultado = a + b #definimos el resultado
    print(resultado) #muestra el valor

suma(1, 2)

#que es lo que pasa si queremos obtener un resultado fuera de la función 
#eliminamos print y asignamos return(variable)

def suma(a, b):
    resultado = a + b
    return resultado

c = suma(1 , 2) #como en la función esta RETURN para devolver el resultado de la operacion en la función
d = suma(c , 3) #c lo que va a devolver es el resultado por lo tanto c + 3 debe ser 6

