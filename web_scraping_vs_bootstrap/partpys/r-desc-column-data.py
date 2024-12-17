import requests
from bs4 import BeautifulSoup

url = 'https://www.tvperu.gob.pe/noticias/nacionales/alcalde-de-lima-destaca-ley-que-impide-ordenar-prision-contra-policias-que-usen-su-arma-de-fuego'

p = requests.get(url)
soup = BeautifulSoup(p.content, 'html.parser')
l_scrape_dcdw = []

content = soup.find("div", class_="row-white note pb-14")
titulo = content.find("h1")
descripcion = content.find("div", class_="bajada")
imagen = content.find("img")
contenido = content.find("div", class_="paragraph mt-20")
if titulo and descripcion and imagen and contenido:
    contenido_texto = contenido.prettify()
    l_scrape_dcdw.append({
        'titulo': titulo.text.strip(),
        'descripcion': descripcion.text.strip(),
        'imagen': imagen["src"] if imagen else '',
        'contenido': contenido_texto,
    })

print(l_scrape_dcdw)
