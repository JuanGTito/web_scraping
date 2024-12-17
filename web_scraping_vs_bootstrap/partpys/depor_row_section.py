
import requests
from bs4 import BeautifulSoup

url = 'https://elpais.com/deportes/'

p = requests.get(url)
soup = BeautifulSoup(p.content, 'html.parser')

data_depor_row_section = []
lista_news_eco = soup.find("div", class_="b-st_a")
articles = lista_news_eco.find_all("article")
for news_eco in articles:
    titulo_elem = news_eco.find("h2", class_="c_t")
    imagen_elem = news_eco.find("img")
    if titulo_elem and imagen_elem:
        titulo = titulo_elem.text.strip()
        imagen = imagen_elem["src"]
        link = titulo_elem.find("a")["href"]
        data_depor_row_section.append({
            'titulo': titulo,
            'imagen': imagen,
            'link': f"{link}"
        })


