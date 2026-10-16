
import mysql.connector

def get_connection():
    connection = mysql.connector.connect(
        host="127.0.0.1",
        user="yuvi",
        password="Yuvi@12345",
        database="product_db"


    )

    return connection
