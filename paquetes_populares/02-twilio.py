import os
from twilio.rest import Client

sid = os.environ.get("TWILIO_SID")
token = os.environ.get("TWILIO_TOKEN")
numero = os.environ.get("TWILIO_N")

cliente = Client(sid, token)
mensaje = cliente.messages.create(
    body="Hola Mundo!",
    from_=numero,
    to="+15557655310"
)
#si ejecutamos el código se va a enviar el msj a ese num.
