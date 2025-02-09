#gestionamos dependenicias utilizando herramientas de la terminal.
#vamos a usar la terminal integrada de VSC
#antes de comenzar cierro todo y abro la terminal. 
"""
La gestión de dependencias en Python se refiere al proceso de manejar las bibliotecas y paquetes externos que necesita un proyecto para funcionar correctamente. A continuación, te explico cómo gestionarlas de manera eficiente:

1. Usar un Gestor de Paquetes: pip
pip es el instalador de paquetes de Python y se utiliza para instalar, actualizar o eliminar paquetes de PyPI.

Comandos básicos:
Instalar un paquete:

bash
pip install nombre_del_paquete
Ejemplo:

bash
pip install Django
Especificar una versión:

bash

pip install nombre_del_paquete==versión
Ejemplo:

bash
pip install Django==4.1.7
Actualizar un paquete:

bash
pip install --upgrade nombre_del_paquete
Desinstalar un paquete:

bash
pip uninstall nombre_del_paquete
2. Uso de requirements.txt
Es un archivo que contiene una lista de las dependencias y sus versiones. Sirve para compartir y replicar el entorno de un proyecto en diferentes máquinas.

Crear el archivo:
Instala los paquetes necesarios para tu proyecto.
Genera el archivo con:
bash

pip freeze > requirements.txt
Esto listará todos los paquetes instalados junto con sus versiones.

Contenido típico de requirements.txt:
plaintext

Django==4.1.7
djangorestframework==3.14.0
numpy==1.23.5

Instalar dependencias desde requirements.txt:
Para instalar todas las dependencias de un proyecto:

bash

pip install -r requirements.txt

3. Usar Entornos Virtuales
Los entornos virtuales te permiten aislar las dependencias de un proyecto para evitar conflictos con otros proyectos o con las bibliotecas globales de tu sistema.

Crear un entorno virtual:
Ve al directorio de tu proyecto.
Crea un entorno virtual:
bash

python -m venv venv
Activar el entorno virtual:
Windows:
bash

venv\Scripts\activate
Linux/Mac

bash
source venv/bin/activate

Cuando el entorno esté activado, verás algo como (venv) antes del cursor en tu terminal.

Instalar dependencias en el entorno:
Una vez activado, usa pip para instalar paquetes. Esto asegura que las dependencias sean específicas para este proyecto.

Desactivar el entorno virtual:
Para salir del entorno virtual, usa:

bash
deactivate

4. Usar Herramientas Avanzadas
pipenv: Combina pip y entornos virtuales. También genera automáticamente archivos de dependencias como Pipfile y Pipfile.lock.

bash
pip install pipenv
pipenv install Django

Esto instala Django y crea un entorno virtual automáticamente.

poetry: Otra herramienta moderna para manejar dependencias y publicar paquetes.

bash

pip install poetry
poetry add Django

5. Actualizar Dependencias
Para mantener las dependencias actualizadas:

Usa el comando:

bash

pip list --outdated
Esto muestra los paquetes que tienen versiones más recientes.

Actualiza los paquetes específicos:

bash
pip install --upgrade nombre_del_paquete

6. Beneficios de una Buena Gestión
Evita conflictos: Cada proyecto tiene sus propias dependencias.
Reproducibilidad: Con un archivo como requirements.txt, otros pueden instalar exactamente las mismas versiones.
Escalabilidad: Los entornos virtuales aseguran que puedas trabajar en múltiples proyectos sin problemas.

"""