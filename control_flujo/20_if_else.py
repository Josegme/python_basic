"""If-Else: Si - Sino"""
#nos permite tomar decisiones a partir de nuestro código
#dependiendo del valor que va a tomar la variable
#Ejemplo

edad = 60 #variable
if edad > 17: #importante la identación para que tome lo que esta dentro de la Condición
    print("Puedes ver la película")
elif edad > 54:
    print("Puedes ver la pelicula con Descuento")
else:
    print("No puedes ver la película")

print("Listo")
#Siempre mantener la Identación para que este dentro del condicional
#lo que este fuera de la identación no se ejecuta con el condicional
# # #EL ORDEN EN EL CUAL COLOCAMOS DENTRO DE LAS EXPRESIONES CONDICIONALES SON IMPORTANTES
#LAS EVALUACIONES SE HACEN DE ARRIBA HACIA ABAJO
"""SI OBSERAMOS EL CASO Y EVALUA EDAD>17 VA A DAR TRUE Y DEJA DE EVALUAR
ES DECIR QUE SI COLOCO 60 VA A DAR TRUE PERO NO VA A PASAR POR EL DESCUENTO
POR ESO EL ORDEN CORRECTO SERIA 
EDAD > 54 - EDAD > 17 - ELSE"""
#el orden que colocamos dentro de las expresiones dentro de IF y ELIF 
cliente = 55
if cliente > 60:
    print("Tienes un super descuento para ver la película")
elif cliente > 54:
    print("Tienes un Descuento especial")
elif cliente > 17:
    print("Puedes ver la pelicula")
else:
    print("No pudes ver la pelicula")

print("Gracias por asistir al Cine")