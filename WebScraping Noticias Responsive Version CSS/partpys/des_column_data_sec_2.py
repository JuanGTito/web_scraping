import requests
from bs4 import BeautifulSoup

url = 'https://www.bbc.com/mundo'
p = requests.get(url)
soup = BeautifulSoup(p.content, 'html.parser')
data_c_dt_p_sec_2 = []
contenido_t_dest_column = soup.find("div", class_="bbc-1tzeti0")
articles = contenido_t_dest_column.find_all("li", class_="bbc-19fk8fk", limit=2)

for article in articles:
    titulo_elem = article.find("h3")
    imagen_elem = article.find("img")
    
    if titulo_elem and imagen_elem:
        titulo = titulo_elem.text.strip()
        imagen = imagen_elem["src"]
        link = titulo_elem.find("a")["href"]
        
        data_c_dt_p_sec_2.append([link, titulo, imagen, "Destacados"])
query = """
INSERT INTO noti_sec (link_sec, titulo_sec, imagen_sec , categoria_sec)
VALUES (%s, %s, %s, %s)
"""

for i in range(len(data_c_dt_p_sec_2)):
    values = data_c_dt_p_sec_2[i]

print(data_c_dt_p_sec_2)