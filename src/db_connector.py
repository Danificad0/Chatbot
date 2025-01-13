import sqlite3

def connect_to_db(db_path):
    conn = sqlite3.connect(db_path)
    return conn

def execute_query(conn, query):
    cursor = conn.cursor()
    cursor.execute(query)
    return cursor.fetchall()
