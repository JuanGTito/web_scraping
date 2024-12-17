
import requests
from bs4 import BeautifulSoup

url = 'https://www.tvperu.gob.pe/noticias'

p = requests.get(url)
soup = BeautifulSoup(p.content, 'html.parser')
data_c_dt_p=[]

contenido_t_dest_column = soup.find("div", class_="title_01")
titulo = contenido_t_dest_column.find("h3")
imagen = contenido_t_dest_column.find("img")["src"]
descripcion = contenido_t_dest_column.find(class_="paragraph")
categoria = contenido_t_dest_column.find(class_="category")
link = titulo.find("a")["href"]

data_c_dt_p.append({
    'titulo': titulo.text.strip(),
    'imagen': imagen,
    'descripcion':descripcion.text.strip(),
    'categoria': categoria.text.strip(),
    'enlace': f"https://www.tvperu.gob.pe/{link}",
    'imagen_src': imagen
})

print(data_c_dt_p)

