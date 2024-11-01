"""Cadenas de Comparación"""

#Para ingresar a una piscina y se necesita permisos por edad.

edad = 25
#suponemos que en principio escribimos de la sig manera
# if edad >= 15 and edad <= 65:
#     print("Puede entrar a la piscina")

#entonces realizando una cadena de comparadores->se reduce el código
if 15 <= edad <= 65:
    print("Puede entrar a la piscina")

#De esta manera podemos encadenar los operadores de comparación
