#para SMTP simple mail transfer protocol como el que utiliza gmail
#mirar SendGrid 
#gmail utiliza una opción que hay que habilitar 
"""https://myaccount.google.com/u/1/lesssecureapps"""

#enviando correos

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from pathlib import Path
import smtplib


path = Path("paquetes-nativos/nombreimagen.png")
mime_image = MIMEImage(path.read_bytes())
mensaje = MIMEMultipart()
mensaje["from"] = "Hola Mundo"
mensaje["to"] = "ultimatepython@holamundo.io"
mensaje["subject"] = "Esta es una prueba"
#se adjunta un cuerpo del msj
cuerpo = MIMEText("Cuerpo del mensaje")
mensaje.attach(cuerpo)
mensaje.attach(mime_image)

with smtplib.SMTP(host="smtp.gmail.com", port=587) as smpt:
    smtp.ehlo()
    smtp.starttls()

    smpt.login("ultimatepython@holamundo.io", "holamundo123" )
    smtp.sent_message(mensaje)
    print("Mensaje Enviado")
    #corroborar si se envió

