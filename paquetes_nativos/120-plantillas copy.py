from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from pathlib import Path
from string import Template
import smtplib

plantilla = """
    <b>Hola Mundo! $usuario</b>
"""

template = Template(plantilla)
cuerpo = template.sustitute({"usuario": "Chanchito feliz"})
path = Path("paquetes-nativos/nombreimagen.png")
mime_image = MIMEImage(path.read_bytes())
mensaje = MIMEMultipart()
mensaje["from"] = "Hola Mundo"
mensaje["to"] = "ultimatepython@holamundo.io"
mensaje["subject"] = "Esta es una prueba"
#se adjunta un cuerpo del msj
cuerpo = MIMEText(cuerpo, "html")
mensaje.attach(cuerpo)
mensaje.attach(mime_image)

with smtplib.SMTP(host="smtp.gmail.com", port=587) as smpt:
    smtp.ehlo()
    smtp.starttls()

    smpt.login("ultimatepython@holamundo.io", "holamundo123" )
    smtp.sent_message(mensaje)
    print("Mensaje Enviado")
    #corroborar si se envió

#ver la clase de nuevo para ver como se importa la PLANTILLA
