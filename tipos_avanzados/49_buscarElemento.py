"""Buscar Elementos dentro de un Arreglo"""

mascotas = ["Pelusa", "Pulga", "Felipe", "Pelusa", "Chanchito Feliz"]

#para buscar un elemento dentro de un Arreglo -> usamos el método INDEX
if "Pulga" in mascotas:
    print(mascotas.index("Pulga"))  #asi escrito solo el print me da error ->corrijo y coloco con IF
#me va a imprimir 1, que es la posición indice de la palabra Pulga

#Si quiero saber cuantas veces se encuentra algo dentro de un elemento
#utilizo el método COUNT
print(mascotas.count("Pelusa"))
if "Pelusa" in mascotas:
    print(mascotas.index("Pelusa"))

#podemos ver entonces que tenemos Pelusa dos veces pero cuando pedimos el indice solo nos imprime 0
#vamos a aprender a Agregar y Quitar Elementos
