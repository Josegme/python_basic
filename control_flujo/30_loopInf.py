"""Loop Infinito"""

#comando = "" con esta estructura no se requiere la var de comando

while True: #si tenemos un while TRUE 
    comando = input("$ ")
    print(comando)
    if comando.lower() == "salir": #siempre hay que agregar una condición de salida 
        break 
