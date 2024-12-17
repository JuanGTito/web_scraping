
import requests
from bs4 import BeautifulSoup

url = 'https://rpp.pe/?ref=rpp'
p = requests.get(url)
soup = BeautifulSoup(p.content, 'html.parser')

data_c_dt_p_sec = []

contenido_t_dest_column = soup.find("div", class_="column-fixed")

articles = contenido_t_dest_column.find_all("article")

for article in articles:
    titulo_elem = article.find("h2", class_="news__title")
    imagen_elem = article.find("img")
    categoria_elem = article.find("h3", class_="news__tag")

    if titulo_elem and imagen_elem and categoria_elem:
        titulo = titulo_elem.text.strip()
        imagen = imagen_elem["src"]
        categoria = categoria_elem.text.strip()
        link = titulo_elem.find("a")["href"]

        data_c_dt_p_sec.append({
            'titulo': titulo,
            'imagen': imagen,
            'categoria': categoria,
            'link': link
        })

print(data_c_dt_p_sec)

