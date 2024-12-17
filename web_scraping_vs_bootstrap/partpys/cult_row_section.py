
import requests
from bs4 import BeautifulSoup

url = 'https://www.tvperu.gob.pe/noticias/seccion/cultural'

p = requests.get(url)
soup = BeautifulSoup(p.content, 'html.parser')

data_cult_row_section = []

newlists = soup.find_all("div", class_="news-list")

for news in newlists:
    titulo_elem = news.find("h3")
    descripcion_elem = news.find("div", class_="paragraph")
    imagen_elem = news.find("img")
    categoria_elem = news.find("div", class_="category")

    if titulo_elem and imagen_elem and categoria_elem:
        titulo = titulo_elem.text.strip()
        descripcion = descripcion_elem.text.strip()
        imagen = imagen_elem["src"]
        categoria = categoria_elem.text.strip()
        link = titulo_elem.find("a")["href"]

        data_cult_row_section.append({
            'titulo': titulo,
            'descripcion': descripcion,
            'imagen': imagen,
            'categoria': categoria,
            'link': f"https://www.tvperu.gob.pe{link}"
        })

print(data_cult_row_section)