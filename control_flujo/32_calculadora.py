"""Aplicación Interactiva"""

#Calculadora en Python
#Bienvenidos a la Calculadora
#Para salir escribir Salir
#Las operaciones son Suma, Multi, Div y Resta

print("Bienvenidos a la Calculadora - Untlimited\n")
print("-Para salir escribir: Salir-\n")
print("Las operaciones son: suma, multi, div y resta")
print('')



resultado = ""
while True:
    if not resultado:
        resultado = input("Ingrese número: ")
        if resultado.lower() == "salir": #si el usuario coloca SALIR -> break
            break
        resultado = int(resultado) #si no colocó salir debe ingresar un Entero
    op = input("Ingresa Operación: ") 
    if op.lower() == "salir":
        break
    n2 = input("Ingresa el siguiente número: ")
    if n2.lower() == "salir":
        break
    n2 = int(n2)

    

    if op.lower() == "suma":
        resultado += n2
    elif op.lower() == "multi":
        resultado *= n2
    elif op.lower() == "div":
        resultado /= n2
    elif op.lower() == "resta":
        resultado -= n2
    else:
        print("Operación no válida")
        break

    print(f"El resultado es {resultado}")

    
    

    print("Loop Infinito") #esto hago para cortar el bucle
    break