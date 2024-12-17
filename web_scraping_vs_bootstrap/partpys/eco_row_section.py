
import requests
from bs4 import BeautifulSoup

url = 'https://rpp.pe/economia/economia'

p = requests.get(url)
soup = BeautifulSoup(p.content, 'html.parser')
data_mnd_row_section = []
lista_news_eco = soup.find("div", class_="column-fluid")
articles = lista_news_eco.find_all("article")
for news_eco in articles:
    titulo_elem = news_eco.find("h2", class_="news__title")
    imagen_elem = news_eco.find("img")
    if titulo_elem and imagen_elem:
        titulo = titulo_elem.text.strip()
        imagen = imagen_elem["src"]
        link = titulo_elem.find("a")["href"]
        data_mnd_row_section.append({
            'titulo': titulo,
            'imagen': imagen,
            'link': f"{link}"
        })
