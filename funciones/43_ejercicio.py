"""Ejercicio 43"""
"""Este ejercicio necesita dos cosas:
1- Que alimine los Espacios en Blanco entre palabras
2- Que aplique una lectura de reversa
#print("Palabra Palindromo", miFunción("Palabra Palindromo"))
aplicar for e iterar cada uno de los caracteres.
"""

def no_space(texto):
    nuevo_texto = ""
    for char in texto: 
        if char != " ":
            nuevo_texto += char
    return nuevo_texto

def reverse(texto):
    texto_al_reves = ""
    for char in texto: 
        texto_al_reves = char + texto_al_reves
    return texto_al_reves

def es_palindromo(texto):  #palabra/frase que se lee igual del derecho y al revés
    texto = no_space(texto)
    texto_al_reves = reverse(texto)
    return texto.lower() == texto_al_reves.lower()

print(es_palindromo("Amo la paloma"))
print(es_palindromo("Hola Mundo"))


print("Abba", es_palindromo("Abba"))
print("Reconocer", es_palindromo("Reconocer"))
print("Amo la Paloma", es_palindromo("Amo la paloma"))
print("Hola Mundo", es_palindromo("Hola Mundo"))
print(es_palindromo("Somos o no somos"))

#