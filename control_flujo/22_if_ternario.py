"""If_Ternario"""

edad = 15

#Esta es la sintaxis mas común
# if edad > 17:
#     print("Es mayor")
# else:
#     print("Es menor")

#otra forma de escribir es utilizando un operador ternario
#que es asignar una variable a la respuesta del condicional
# if edad > 17:
#     mensaje = "Es Mayor"
# else:
#     mensaje = "Es Menor"

# print(mensaje)

mensaje = "Es mayor" if edad > 17 else "Es Menor"
#Variable------------V--Condicional--F----------
#variable = operador ternario asigna izq si es V (condición) asigna der si es F
