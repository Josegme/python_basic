"""Set -> conjunto o grupo"""

#es una colección de datos que no se puede repetir y tampoco esta ordenada
primerSet = {1, 1, 2, 2, 3, 4}
#print(primerSet) #va a imprimir solo {1, 2, 3, 4} es decir que imprime solo una ocurrencia del dato en el SET
#python remueve los duplicados

primerSet.add(5)
primerSet.remove(1)
print(primerSet)

#vamos a hacer una lista y concatenar con el set
segundoSet = [3, 4, 5]
#transformamos esto a un set
segundoSet = set(segundoSet)
print(segundoSet)

#operadores dentro de SET
print(primerSet | segundoSet) #union de sets
#intersección
print(primerSet & segundoSet)
#diferencia de Sets
print(primerSet - segundoSet) 
#diferencia simetrica ^
