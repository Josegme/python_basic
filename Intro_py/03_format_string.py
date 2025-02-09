"""Formatear un String"""

nombre = "Nicolas"
apellido = "Schurman"
#como concatenamos
nombre_completo = nombre +" "+ apellido
#otra forma de concatenar con mejor sintaxis
nombre_completo1 = f"{nombre} {apellido}"
print(nombre_completo)
print(nombre_completo1)

#Dentro de las {llaves} puedo escribir lo que necesite o quiera
nombre_completo2 = f"{nombre[0]} {7 + 8}"
print(nombre_completo2)

# f entonces es un operado que me permite trabajar de manera mas dinámica los string y las variables. 
