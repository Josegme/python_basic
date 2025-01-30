from selenium import webdriver  # Importa el módulo de Selenium para controlar el navegador
from selenium.webdriver.common.by import By  # Importa la clase By para localizar elementos en el DOM

# tenemos que instalar selenium en la terminal -> pipenv install selenium
# Nota: El comentario tiene un error tipográfico, debería ser "pipenv install selenium"

options = webdriver.ChromeOptions()  # Crea un objeto para definir opciones personalizadas de Chrome
options.add_experimental_option("detach", True)  # Mantiene el navegador abierto después de ejecutar el script
browser = webdriver.Chrome(options=options)  # Inicia una instancia del navegador Chrome con las opciones definidas
browser.implicitly_wait(10)  # Espera implícita de 10 segundos para que los elementos aparezcan en la página

browser.get("https://github.com")  # Abre la página principal de GitHub

browser.find_element(By.LINK_TEXT, "Sign in")  # Busca el enlace de texto "Sign in" en la página
# Faltó asignar el elemento a una variable para hacer clic sobre él
link.click()  # ERROR: la variable `link` no está definida. Debería ser algo como:
# link = browser.find_element(By.LINK_TEXT, "Sign in")
# link.click()  

# Localiza el campo de usuario por su ID
user_input = browser.find_element(By.ID, "login_field")

# Localiza el campo de contraseña por su ID
pass_input = browser.find_element(By.ID, "password")

# Escribe el nombre de usuario en el campo correspondiente
user_input.send_keys("holamundo")  

# Escribe la contraseña en el campo correspondiente
pass_input.send_keys("holamundo")  

"""
Asigna el elemento del enlace de inicio de sesión a una variable antes de hacer clic:

link = browser.find_element(By.LINK_TEXT, "Sign in")
link.click()

pipenv instal selenium 
pipenv install selenium

"""
