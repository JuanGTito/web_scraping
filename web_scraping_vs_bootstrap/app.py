from flask import Flask, render_template
import requests
from bs4 import BeautifulSoup
from flask import request
import chardet
import mysql.connector

app= Flask(__name__)



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


def scrape_dcdw(url):
    l_scrape_dcdw = []
    r = requests.get(url)
    result = chardet.detect(r.content)
    r.encoding = result['encoding'] 
    soup = BeautifulSoup(r.text, 'html.parser') 
    content = soup.find("div", class_="row-white note pb-14")
    if not content:
        return []
    titulo = content.find("h1")
    descripcion = content.find("div", class_="bajada")
    imagen = content.find("img")
    contenido = content.find("div", class_="paragraph mt-20")
    if titulo and descripcion and imagen and contenido:
        descripcion_text = descripcion.prettify()
        contenido_text = contenido.prettify
        l_scrape_dcdw.append({
            'titulo': titulo.text.strip(),
            'descripcion': descripcion_text,
            'imagen': imagen["src"] if imagen else '',
            'contenido': contenido_text,
        })
    return l_scrape_dcdw
def scrape_dcwds_sec(url):
    l_scrape_dcwds_sec = []
    r = requests.get(url)
    result = chardet.detect(r.content)
    r.encoding = result['encoding'] 
    soup = BeautifulSoup(r.text, 'html.parser') 
    content = soup.find("article", class_="article")
    if not content:
        return []
    
    titulo = content.find("h1", class_="article__title")
    descripcion = content.find("div", class_="article__subtitle")
    imagen_ubicacion = content.find("figure", class_="media")
    imagen = imagen_ubicacion.find("img")
    contenido_all = content.find("div", class_="body")
    contenido = contenido_all.find_all("p")
    
    contenido_texto = ' '.join(str(p) for p in contenido)
    
    if titulo and descripcion and imagen and contenido:
        descripcion_text = descripcion.prettify()
        l_scrape_dcwds_sec.append({
            'titulo': titulo.text.strip(),
            'descripcion': descripcion_text,
            'imagen': imagen["src"] if imagen else '',
            'contenido': contenido_texto,
        })
    
    return l_scrape_dcwds_sec

def scrape_prs(url):
    l_scrape_prs = []
    r = requests.get(url)
    result = chardet.detect(r.content)
    r.encoding = result['encoding'] 
    soup = BeautifulSoup(r.text, 'html.parser') 
    content = soup.find("div", class_="row-white note pb-14")
    if not content:
        return []
    titulo = content.find("h1")
    descripcion = content.find("div", class_="bajada")
    imagen = content.find("img")
    contenido = content.find("div", class_="paragraph mt-20")
    if titulo and descripcion and imagen and contenido:
        contenido_texto = contenido.prettify
        descripcion_text = descripcion.prettify()
        l_scrape_prs.append({
            'titulo': titulo.text.strip(),
            'descripcion': descripcion_text,
            'imagen': imagen["src"] if imagen else '',
            'contenido': contenido_texto,
        })
    return l_scrape_prs

def scrape_mnd(url):
    l_scrape_mnd = []
    r = requests.get(url)
    result = chardet.detect(r.content)
    r.encoding = result['encoding'] 
    soup = BeautifulSoup(r.text, 'html.parser') 
    content = soup.find("main")
    if not content:
        return []
    titulo = content.find("h1")
    descripcion = content.find("b")
    imagen = content.find("img")
    contenido = content.find_all("p")
    
    contenido_texto = ' '.join(str(p) for p in contenido)
    if titulo and descripcion and imagen and contenido:
        descripcion_text = descripcion.prettify()
        l_scrape_mnd.append({
            'titulo': titulo.text.strip(),
            'descripcion': descripcion_text,
            'imagen': imagen["src"] if imagen else '',
            'contenido': contenido_texto,
        })
    return l_scrape_mnd

def scrape_eco(url):
    l_scrape_eco = []
    r = requests.get(url)
    result = chardet.detect(r.content)
    r.encoding = result['encoding'] 
    soup = BeautifulSoup(r.text, 'html.parser') 
    content = soup.find("article", class_="article")
    if not content:
        return []
    
    titulo = content.find("h1", class_="article__title")
    descripcion = content.find("div", class_="article__subtitle")
    imagen_ubicacion = content.find("figure", class_="media")
    imagen = imagen_ubicacion.find("img")
    contenido_all = content.find("div", class_="body")
    contenido = contenido_all.find_all("p")
    
    contenido_texto = ' '.join(str(p) for p in contenido)
    
    if titulo and descripcion and imagen and contenido:
        descripcion_text = descripcion.prettify()
        l_scrape_eco.append({
            'titulo': titulo.text.strip(),
            'descripcion': descripcion_text,
            'imagen': imagen["src"] if imagen else '',
            'contenido': contenido_texto,
        })
    
    return l_scrape_eco
def scrape_depor(url):
    l_scrape_depor = []
    r = requests.get(url)
    result = chardet.detect(r.content)
    r.encoding = result['encoding'] 
    soup = BeautifulSoup(r.text, 'html.parser') 
    content = soup.find("article", class_="a _g _g-lg _g-o")
    if not content:
        return []
    
    titulo = content.find("h1", class_="a_t")
    descripcion = content.find("h2", class_="a_st")
    imagen_ubicacion = content.find("figure")
    imagen = imagen_ubicacion.find("img")
    contenido_all = content.find("div", class_="a_c clearfix")
    contenido = contenido_all.find_all("p")
    
    contenido_texto = ' '.join(str(p) for p in contenido)
    
    if titulo and descripcion and imagen and contenido:
        descripcion_text = descripcion.prettify()
        l_scrape_depor.append({
            'titulo': titulo.text.strip(),
            'descripcion': descripcion_text,
            'imagen': imagen["src"] if imagen else '',
            'contenido': contenido_texto if contenido_texto else "blank",
        })
    
    return l_scrape_depor 

def scrape_crs(url):
    l_scrape_crs = []
    r = requests.get(url)
    result = chardet.detect(r.content)
    r.encoding = result['encoding'] 
    soup = BeautifulSoup(r.text, 'html.parser') 
    content = soup.find("div", class_="row-white note pb-14")
    if not content:
        return []
    titulo = content.find("h1")
    descripcion = content.find("div", class_="bajada")
    imagen = content.find("img")
    contenido_all = content.find("div", class_="paragraph mt-20")
    contenido = contenido_all.find_all("p")
    
    contenido_texto = ' '.join(str(p) for p in contenido)
    
    if titulo and descripcion and imagen and contenido:
        descripcion_text = descripcion.prettify()
        l_scrape_crs.append({
            'titulo': titulo.text.strip(),
            'descripcion': descripcion_text,
            'imagen': imagen["src"] if imagen else '',
            'contenido': contenido_texto,
        })
    return l_scrape_crs

def scrape_trs(url):
    l_scrape_trs = []
    r = requests.get(url)
    result = chardet.detect(r.content)
    r.encoding = result['encoding'] 
    soup = BeautifulSoup(r.text, 'html.parser') 
    content = soup.find("div", class_="row-white note pb-14")
    if not content:
        return []
    titulo = content.find("h1")
    descripcion = content.find("div", class_="bajada")
    imagen = content.find("img")
    contenido_all = content.find("div", class_="paragraph mt-20")
    contenido = contenido_all.find_all("p")
    
    contenido_texto = ' '.join(str(p) for p in contenido)
    
    if titulo and descripcion and imagen and contenido:     
        descripcion_text = descripcion.prettify()
        l_scrape_trs.append({
            'titulo': titulo.text.strip(),
            'descripcion': descripcion_text,
            'imagen': imagen["src"] if imagen else '',
            'contenido': contenido_texto,
        })
    return l_scrape_trs           

@app.route('/')
def index():
    connection = get_connection()
    cursor = connection.cursor(dictionary=True)

    cursor.execute('SELECT * FROM noti_princ')
    dest_column_ws_data_index = cursor.fetchall()

    cursor.execute('SELECT * FROM noti_sec')
    dest_column_ws_data_sec_index = cursor.fetchall()

    cursor.execute('SELECT * FROM pol_sec')
    row_pol_section_index = cursor.fetchall()

    cursor.execute('SELECT * FROM mnd_sec')
    row_mnd_section_index = cursor.fetchall()

    cursor.execute('SELECT * FROM eco_sec')
    row_eco_section_index = cursor.fetchall()

    cursor.execute('SELECT * FROM depor_sec')
    row_depor_section_index = cursor.fetchall()

    cursor.execute('SELECT * FROM cult_sec')
    row_cult_section_index = cursor.fetchall()

    cursor.execute('SELECT * FROM tech_sec')
    row_tech_section_index = cursor.fetchall()
    return render_template('index.html', 
                        dest_column_ws_data_index = dest_column_ws_data_index,
                        dest_column_ws_data_sec_index = dest_column_ws_data_sec_index,
                        row_pol_section_index = row_pol_section_index,
                        row_mnd_section_index = row_mnd_section_index,
                        row_eco_section_index = row_eco_section_index,
                        row_depor_section_index = row_depor_section_index,
                        row_cult_section_index = row_cult_section_index,
                        row_tech_section_index = row_tech_section_index
                        )

@app.route('/news_detail')

def news_detail():
    url = request.args.get('url')
    if not url:
        return "URL no proporcionada", 400
    scrape_dcdw_index = scrape_dcdw(url)
    return render_template('news_detail.html', scrape_dcdw_index=scrape_dcdw_index)

@app.route('/news_detail_sec')
def news_detail_sec():
    url = request.args.get('url')
    if not url:
        return "URL no proporcionada", 400
    scrape_dcwds_sec_index = scrape_dcwds_sec(url)
    return render_template('news_detail_sec.html', scrape_dcwds_sec_index=scrape_dcwds_sec_index)

@app.route('/news_detail_prs')
def news_detail_prs():
    url = request.args.get('url')
    if not url:
        return "URL no proporcionada", 400
    scrape_prs_index = scrape_prs(url)
    return render_template('news_detail_prs.html', scrape_prs_index=scrape_prs_index)

@app.route('/news_detail_mnd')
def news_detail_mnd():
    url = request.args.get('url')
    if not url:
        return "URL no proporcionada", 400
    scrape_mnd_index = scrape_mnd(url)
    return render_template('news_detail_mnd.html', scrape_mnd_index=scrape_mnd_index)

@app.route('/news_detail_eco')
def news_detail_eco():
    url = request.args.get('url')
    if not url:
        return "URL no proporcionada", 400
    scrape_eco_index = scrape_eco(url)
    return render_template('news_detail_eco.html', scrape_eco_index=scrape_eco_index)

@app.route('/news_detail_depor')
def news_detail_depor():
    url = request.args.get('url')
    if not url:
        return "URL no proporcionada", 400
    scrape_depor_index = scrape_depor(url)
    return render_template('news_detail_depor.html', scrape_depor_index=scrape_depor_index)

@app.route('/news_detail_crs')
def news_detail_crs():
    url = request.args.get('url')
    if not url:
        return "URL no proporcionada", 400
    scrape_crs_index = scrape_crs(url)
    return render_template('news_detail_crs.html', scrape_crs_index=scrape_crs_index)

@app.route('/news_detail_trs')
def news_detail_trs():
    url = request.args.get('url')
    if not url:
        return "URL no proporcionada", 400
    scrape_trs_index = scrape_trs(url)
    return render_template('news_detail_trs.html', scrape_trs_index=scrape_trs_index)

@app.route('/sec_pol_rows')
def sec_pol_rows():
    connection = get_connection()
    cursor = connection.cursor(dictionary=True)
    cursor.execute('SELECT * FROM pol_sec')
    sec_pol_rows_index  = cursor.fetchall()
    return render_template('sec_pol_rows.html', sec_pol_rows_index=sec_pol_rows_index)

@app.route('/sec_mnd_rows')
def sec_mnd_rows():
    connection = get_connection()
    cursor = connection.cursor(dictionary=True)
    cursor.execute('SELECT * FROM mnd_sec')
    sec_mnd_rows_index  = cursor.fetchall()
    return render_template('sec_mnd_rows.html', sec_mnd_rows_index=sec_mnd_rows_index)

@app.route('/sec_eco_rows')
def sec_eco_rows():
    connection = get_connection()
    cursor = connection.cursor(dictionary=True)
    cursor.execute('SELECT * FROM eco_sec')
    sec_eco_rows_index  = cursor.fetchall()
    return render_template('sec_eco_rows.html', sec_eco_rows_index=sec_eco_rows_index)

@app.route('/sec_depor_rows')
def sec_depor_rows():
    connection = get_connection()
    cursor = connection.cursor(dictionary=True)
    cursor.execute('SELECT * FROM depor_sec')
    sec_depor_rows_index  = cursor.fetchall()
    return render_template('sec_depor_rows.html', sec_depor_rows_index=sec_depor_rows_index)


@app.route('/sec_cult_rows')
def sec_cult_rows():
    connection = get_connection()
    cursor = connection.cursor(dictionary=True)
    cursor.execute('SELECT * FROM cult_sec')
    sec_cult_rows_index  = cursor.fetchall()
    return render_template('sec_cult_rows.html', sec_cult_rows_index=sec_cult_rows_index)

@app.route('/sec_tech_rows')
def sec_tech_rows():
    connection = get_connection()
    cursor = connection.cursor(dictionary=True)
    cursor.execute('SELECT * FROM tech_sec')
    sec_tech_rows_index  = cursor.fetchall()
    return render_template('sec_tech_rows.html', sec_tech_rows_index=sec_tech_rows_index)

if __name__ == '__main__':
    app.run(debug=True)

