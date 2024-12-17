
import requests
from bs4 import BeautifulSoup

url = 'https://www.bbc.com/mundo/topics/c2lej05epw5t'

p = requests.get(url)
soup = BeautifulSoup(p.content, 'html.parser')

data_mnd_row_section = []

lista_news_mnd = soup.find_all("li", class_="bbc-t44f9r")
for news_mnd in lista_news_mnd:
    titulo_elem = news_mnd.find("h2")
    imagen_elem = news_mnd.find("img")

    if titulo_elem and imagen_elem:
        titulo = titulo_elem.text.strip()
        imagen = imagen_elem["src"]
        link = titulo_elem.find("a")["href"]

        data_mnd_row_section.append({
            'titulo': titulo,
            'imagen': imagen,
            'link': f"{link}"
        })

print(data_mnd_row_section)