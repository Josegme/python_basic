"""45 Listas"""

#listas de números
#creamos una variable y hacemos la lista dentro []
numeros = [1, 2, 3] #[indentificasmos la lista y el contenido, entre cada elemento una .]
#cuando armamos una lista como en la vida real estamos colocando elementos dentro de la lista 
#de diferentes tipos y como voy agregando elementos, estos van a tener un orden
letras = ["a", "b", "c"]
palabras = ["chanchito", "Feliz"]
palabrasFelices = ["Chanchito", "Feliz", "Felipe", "Alumnos"]

booleans = [True, False, True, True]
matriz =[[0, 1], [1, 0]] 

ceros = [0] * 10 #multiplica por 10 la cantidad de elementos dentro de la Lista
alfanumerico = numeros + letras  #Sumando Listas devuelve [1, 2, 3, 'a', 'b', 'c']

#rango = [1..10] #esto NO Se puede hacer
rango = list(range(10)) #crea automaticamente una lista de 10 elementos
print(rango)
#pero me va a imprimir de 0 a 9 por que son 10 elementos entonces->
rango1 = list(range(1, 11))
print(rango1) #ahora si tenemos el listado del 1 al 10

#pdemos crear listas de un string
char = list("Hola Mundo")
print(char) #me imprime cada elemento de la posición en que se encuentra dentro de la frase.
