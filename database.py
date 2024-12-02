import mysql.connector

def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="admin",
        password="admin",
        database="WS",
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
