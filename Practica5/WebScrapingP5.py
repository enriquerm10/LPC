import requests 
from bs4 import BeautifulSoup as bs

url = requests.get("https://es.wikipedia.org/wiki/Sergio_P%C3%A9rez")
soup = bs(url.content,"html.parser")

titulo = (soup.find("title"))
info  = open("ChecoPerez", "a")
info.write(titulo.get_text() + "\n\n")
texto = soup.find_all("p")[:5]
for p in texto:
    texto = p.get_text()
    long = len(texto)
    if long > 80:
        while long > 80:
            cadena = texto
            cadena = cadena[:80]
            texto = texto[80:]
            long = len(texto)
            info.write(cadena + "\n")
        if long <= 80:
            info.write(texto + "\n\n")
    else:
        info.write(texto)
info.close()
print("Informacion guardada en archivo txt")
