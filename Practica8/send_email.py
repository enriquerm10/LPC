#!/usr/bin/env python3
from email import encoders
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
import smtplib
import argparse
import ssl
import requests 
from bs4 import BeautifulSoup as bs

if __name__ == "__main__":
  description="Este script tiene la finalidad de mandar correos electronicos"
  parser = argparse.ArgumentParser(description="Practica 8", epilog=description, formatter_class=argparse.RawDescriptionHelpFormatter)
  parser.add_argument('-usuario', type=str , help='Correo del que se enviará el mensaje.')
  parser.add_argument('-receptor', type=str , help='Correo que recibirá el mensaje.')
  parser.add_argument('-url', type=str , help='Pagina de la que se hará web scrapping.')
  parser.add_argument('-contraseña', type=str , help='Contraseña del usuario.')
  parser.add_argument('-mensaje', type=str, help='Se debe poner un mensaje el cual se quiera enviar.',default = "Hola mundo mundial")
  parser.add_argument('-asunto', type=str, help='Se utiliza para poner el titulo que tendrá el correo.', default="Hola!")
  params = parser.parse_args()


url = (params.url)
usuario = (params.usuario)
receptor = (params.receptor)
mensaje = (params.mensaje)
asunto = (params.asunto)
contraseña = (params.contraseña)

email_msg = MIMEMultipart("alternative")
email_msg["From"] = usuario
email_msg["To"] = receptor
email_msg["Subject"] = asunto

email_msg.attach(MIMEText(mensaje, "plain"))


pagina = requests.get(url)
soup = bs(pagina.content,"html.parser")

archivo = "archivo:).txt"
arch = open(archivo, "a")
contenido = soup.find_all("p")[:3]
for p in contenido:
    contenido = p.get_text()
    arch.write(contenido)
arch.close()


filename = archivo   
with open(filename, "rb") as attachment:
    
    part = MIMEBase("application", "octet-stream")
    part.set_payload(attachment.read())
 
encoders.encode_base64(part)


part.add_header(
    "Content-Disposition",
    f"attachment; filename= {filename}",
)


email_msg.attach(part)


context = ssl.create_default_context()
with smtplib.SMTP("smtp.office365.com", 587) as server:
    server.ehlo()
    server.starttls(context=context)
    server.login(usuario, contraseña)
    server.sendmail(
        usuario, receptor, email_msg.as_string()
    )
print("successfully sent email to: %s" % (receptor))