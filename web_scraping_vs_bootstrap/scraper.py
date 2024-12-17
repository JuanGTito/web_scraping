import requests
from bs4 import BeautifulSoup
import mysql.connector

def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="admin",
        database="noticias_ws_db",
    )

def execute_query(query, params=None):
    conn = get_connection()
    cursor = conn.cursor()
    if params:
        cursor.execute(query, params)
    else:
        cursor.execute(query)
    conn.commit()
    cursor.close()
    conn.close()

def dest_column_ws_data():
    url = 'https://www.tvperu.gob.pe/noticias'
    p = requests.get(url)
    soup = BeautifulSoup(p.content, 'html.parser')
    data_c_dt_p = []
    
    contenido_t_dest_column = soup.find("div", class_="title_01")
    titulo = contenido_t_dest_column.find("h3")
    imagen = contenido_t_dest_column.find("img")["src"]
    descripcion = contenido_t_dest_column.find(class_="paragraph")
    categoria = contenido_t_dest_column.find(class_="category")
    link = titulo.find("a")["href"]

    data_c_dt_p.append(
        (f"https://www.tvperu.gob.pe{link}", 
         titulo.text.strip(), 
         imagen, 
         descripcion.text.strip(), 
         categoria.text.strip())
        )
    
    query = """
    INSERT INTO noti_princ (link_prin, titulo_prin, imagen_prin ,descripcion_prin, categoria_prin)
    VALUES (%s, %s, %s, %s, %s)
    """
    values = data_c_dt_p[0]
    
    execute_query(query, values)


def dest_column_ws_data_sec():
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
            
            data_c_dt_p_sec.append([link, titulo, imagen, categoria])

    query = """
    INSERT INTO noti_sec (link_sec, titulo_sec, imagen_sec , categoria_sec)
    VALUES (%s, %s, %s, %s)
    """
    
    for i in range(len(data_c_dt_p_sec)):
        values = data_c_dt_p_sec[i]
        execute_query(query, values)


def dest_column_ws_data_sec_2():
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
        execute_query(query, values)


def row_pol_section():
    url = 'https://www.tvperu.gob.pe/noticias/seccion/politica'
    p = requests.get(url)
    soup = BeautifulSoup(p.content, 'html.parser')
    data_pol_row_section = []
    newlists = soup.find_all("div", class_="news-list")
    for news in newlists:
        titulo_elem = news.find("h3")
        imagen_elem = news.find("img")
        if titulo_elem and imagen_elem:
            titulo = titulo_elem.text.strip()
            imagen = imagen_elem["src"]
            link = titulo_elem.find("a")["href"]

            data_pol_row_section.append([f"https://www.tvperu.gob.pe{link}",titulo,imagen
            ])
    query = """
    INSERT INTO pol_sec (link_pol, titulo_pol, imagen_pol)
    VALUES (%s, %s, %s)
    """
    
    for i in range(len(data_pol_row_section)):
        values = data_pol_row_section[i]
        execute_query(query, values)

def row_mnd_section():
    url = 'https://www.bbc.com/mundo/topics/c2lej05epw5t'
    p = requests.get(url)
    soup = BeautifulSoup(p.content, 'html.parser')
    data_mnd_row_section = []
    lista_news_mnd = soup.find_all("li", class_="bbc-t44f9r", limit=10)
    for news_mnd in lista_news_mnd:
        titulo_elem = news_mnd.find("h2")
        imagen_elem = news_mnd.find("img")
        if titulo_elem and imagen_elem:
            titulo = titulo_elem.text.strip()
            imagen = imagen_elem["src"]
            link = titulo_elem.find("a")["href"]
            data_mnd_row_section.append([link, titulo, imagen])
        query = """
        INSERT INTO mnd_sec (link_mnd, titulo_mnd, imagen_mnd)
        VALUES (%s, %s, %s)
        """
    
    for i in range(len(data_mnd_row_section)):
        values = data_mnd_row_section[i]
        execute_query(query, values)

def row_eco_section():
    url = 'https://rpp.pe/economia/economia'
    p = requests.get(url)
    soup = BeautifulSoup(p.content, 'html.parser')
    data_eco_row_section = []
    lista_news_eco = soup.find("div", class_="column-fluid")
    articles = lista_news_eco.find_all("article")
    for news_eco in articles:
        titulo_elem = news_eco.find("h2", class_="news__title")
        imagen_elem = news_eco.find("img")
        if titulo_elem and imagen_elem:
            titulo = titulo_elem.text.strip()
            imagen = imagen_elem["src"]
            link = titulo_elem.find("a")["href"]
            data_eco_row_section.append([link, titulo, imagen])

        query = """
        INSERT INTO eco_sec (link_eco, titulo_eco, imagen_eco)
        VALUES (%s, %s, %s)
        """
    
    for i in range(len(data_eco_row_section)):
        values = data_eco_row_section[i]
        execute_query(query, values) 

def row_depor_section():
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
            data_depor_row_section.append([link, titulo, imagen])
        
        query = """
        INSERT INTO depor_sec (link_depor, titulo_depor, imagen_depor)
        VALUES (%s, %s, %s)
        """
    
    for i in range(len(data_depor_row_section)):
        values = data_depor_row_section[i]
        execute_query(query, values) 

def row_cult_section():
    url = 'https://www.tvperu.gob.pe/noticias/seccion/cultural'
    p = requests.get(url)
    soup = BeautifulSoup(p.content, 'html.parser')
    data_cult_row_section = []
    newlists = soup.find_all("div", class_="news-list")
    for news in newlists:
        titulo_elem = news.find("h3")
        imagen_elem = news.find("img")
        if titulo_elem and imagen_elem:
            titulo = titulo_elem.text.strip()
            imagen = imagen_elem["src"]
            link = titulo_elem.find("a")["href"]
            data_cult_row_section.append([f"https://www.tvperu.gob.pe{link}", titulo, imagen])
        
        query = """
        INSERT INTO cult_sec (link_cult, titulo_cult, imagen_cult)
        VALUES (%s, %s, %s)
        """
    
    for i in range(len(data_cult_row_section)):
        values = data_cult_row_section[i]
        execute_query(query, values)     

def row_tech_section():
    url = 'https://www.tvperu.gob.pe/noticias/seccion/tecnologia'
    p = requests.get(url)
    soup = BeautifulSoup(p.content, 'html.parser')
    data_tech_row_section = []
    newlists = soup.find_all("div", class_="news-list")
    for news in newlists:
        titulo_elem = news.find("h3")
        imagen_elem = news.find("img")
        categoria_elem = news.find("div", class_="category")
        if titulo_elem and imagen_elem:
            titulo = titulo_elem.text.strip()

            imagen = imagen_elem["src"]
            link = titulo_elem.find("a")["href"]
            data_tech_row_section.append([f"https://www.tvperu.gob.pe{link}", titulo, imagen])

        query = """
        INSERT INTO tech_sec (link_tech, titulo_tech, imagen_tech)
        VALUES (%s, %s, %s)
        """
    
    for i in range(len(data_tech_row_section)):
        values = data_tech_row_section[i]
        execute_query(query, values) 

dest_column_ws_data()
dest_column_ws_data_sec()
dest_column_ws_data_sec_2()
row_pol_section()
row_mnd_section()
row_eco_section()
row_depor_section()
row_cult_section()
row_tech_section()