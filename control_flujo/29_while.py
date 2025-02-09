"""========WHILE========"""
#Supongamos que tenemos un número que debe ir iterendo
#incrementandose de a uno en uno hasta que llegue a 100
"""
numero = 1
while numero < 100: #mientras sea menor que 100
    print(numero)
    numero *=2 """

#devuelve -> 1 2 4 8 16 32 64
#mientras la condicion sea Verdadera se ejecuta el código
#cuando se vuelve F se detiene

comando = "" #primero comando es un STRING vacio

while comando.lower() != "salir": #comando cumple con la condición por que es distinto de la palabra SALIR
    comando = input("$ ") #este es el INPUT del Usuario -> lo que el usuario ingrese se le ASIGNA a la VARIABLE comando
    print(comando) #esto se imprime solo a fin del ejercicio

#como PYTHON es sensible a MAYUSCULAS y minusculas utilizo un método
#métdo .LOWER me permite que todo se convierta a minuscula de manera de que si
#el usuario escribe diferente (SALIR, Salir, SAliR, etc) se ejecute igualmente el programa