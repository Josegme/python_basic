"""String"""
#nombre de variable = "" comillas

nombre_curso = "===Ultimate Python==="
descripcion_curso = """
Ultimate Python: Este curso contempla todos los detalles 
que necesitas aprendeer para encontrar un trabajo como programador.
"""
#Si quiero imprimir esto
print(nombre_curso, descripcion_curso)


#Función de Len para saber la longitud de un string
print(len(nombre_curso))
#quiero saber el numero de carcateres del argumnento

#si quiero acceder a la posición o indice en particular por ejemplo a U
#los string comienzan con indice 0
print(nombre_curso[0])
#si quiero obtener la palabra determinada
print(nombre_curso[3:11])
print(nombre_curso[12:]) #como no le paso nada se rellena hasta el final por dafault
print(nombre_curso[:12]) #completa hasta ese valor dado
print(nombre_curso[:]) #toma la longitud completa del string


