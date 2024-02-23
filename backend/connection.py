import mysql.connector

__cnx = None

def sql_connection():
    global __cnx
    if __cnx is None:
         cnx = mysql.connector.connect(user='root', password='Varma',
                                host='127.0.0.1',
                                database='gs')
    return __cnx