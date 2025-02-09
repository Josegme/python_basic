"""Depuración"""

def largo(texto):
    resultado = 0
    for _ in texto: #reemplazo el char por _
        resultado +=1
        return resultado
    
l = largo("Hola Mundo")
print(l)
#cuando ejecutamos el código y pedimos el lagor nos devuelve 1
#pero sabemos que Hola Mundo tiene 10 caracteres
#para encontrar el error y depurar nuestra app
    #1 Voy a Run & DebuG
    #2 Crear un archivo de LUNCH.JSON
    #3 pinchar en Lunch.Json -> nos muestra opciones -> PYTHON FILE
    #4 Ver si se creo la carpeta y el lunch
    #5 tenemos que agregar un punto -> BreakPoint -> para que el Depurador se dentenga en ese punto
    #6 F10 o avanzar en una línea
    #7 Avanzar hasta que marque un error y nos va a marcar y mostrar a la izq
    #8 F11 step ing -> ingresa en la ejecución de la función. 
    #9 Indentificar el error y volver a probar y detectar la corrección
    #10 Step out shit F11 - > si quiero iniciar la deporuacion RESTAR
    #11 para detener el depurar STOP 
    
