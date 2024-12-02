import requests
from bs4 import BeautifulSoup
from database import execute_query, get_connection
import re
# URL de la página web que quieres scrapear
urls = ['https://computactus.com.pe/web/?pagina=scc&cate=sub-cate-112&marca=0&valoracion=0&precios=0&orden=0&vista=2&b=1&stock=0',
    'https://computactus.com.pe/web/?pagina=scc&cate=sub-cate-112&marca=0&valoracion=0&precios=0&orden=0&vista=2&stock=0&b=2',
        'https://computactus.com.pe/web/?pagina=scc&cate=sub-cate-112&marca=0&valoracion=0&precios=0&orden=0&vista=2&stock=0&b=3']
# Realiza la solicitud GET a la página
productos = []
precios_ = []

for url in urls:
    pedido = requests.get(url)
    html_obtenido = pedido.text
    # Parsear el HTML
    soup = BeautifulSoup(html_obtenido, "html.parser")
    # Encontrar productos y precios
    nombres_productos = soup.find_all('span', class_='toltiptext2')
    precios_productos = soup.find_all('div', class_='precio1')
    precios_imagen = soup.find_all('a', class_='ti_h')
    nombres = []
    precios = []
    if (nombres_productos is not None) and  (precios_productos is not None):
        for nombre, precio in zip(nombres_productos, precios_productos):
            nombre_lista = nombre.text.strip()
            precio_lista = precio.text.strip().replace('S/.', '').strip()
            nombres.append(nombre_lista)
            precios.append(precio_lista)
            print(f"| {nombre_lista} | {precio_lista} |")
    else:
        print("Hay espacios vacios")
    productos.append(nombres)
    precios_.append(precios)
    
    imagenes = soup.find_all('img', class_='img_pro')
    if imagenes:
        for i, img in enumerate(imagenes):
            src = img.get('src')
            if src and ('.jpg' in src or '.png' in src or '.webp' in src):
                if src.endswith(".jpg"):
                    formato = ".jpg"
                elif src.endswith(".png"):
                    formato = ".png"
                elif src.endswith(".webp"):
                    formato = ".webp"
                #print(src)
                r = requests.get(src)
                nombre_archivo = f'{precios[i]}___{nombres[i]}{formato}'
                nombre_archivo = re.sub(r'[<>:"/\\|?*,.]', '', nombre_archivo) 
                with open(f'{nombre_archivo}{formato}', 'wb') as f:

                    f.write(r.content)
    else:
        print("No se encontró iamgenes")



consulta = "INSERT INTO Laptops VALUEs (%s, %s)"
for i in range(len(productos)):
    for j in range(len(productos[i])):
        execute_query(consulta,(productos[i][j], precios_[i][j]))
