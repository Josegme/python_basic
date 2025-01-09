"""import time

print(time.time())
#imprime un timestamp -> 1736328490.0949445 (la cantidad de segundos desde Enero de 1970)
#con respecto a UTC coordinated univesal time  -> como nosotros tenemos que trabajar las fechas

"""

from datetime import datetime

fecha = datetime(2023, 1, 1)
fecha2 = datetime(2023, 2, 1)

ahora = datetime.now()
print(ahora)

fechaStr = datetime.strptime("2023-01-03", "%Y-%m-%d")
#print(fechaStr)

#podemos buscar en crhome python 3 datetimes directivs 
print(fecha.strftime("%Y.%m.%d"))
print(fecha > fecha2) #false

print(
    fecha.year,
    fecha.month,
    fecha.day,
    fecha.hour,
    fecha.minute
)
