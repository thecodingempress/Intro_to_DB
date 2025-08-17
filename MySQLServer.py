import mysql.connector
from mysql.connector import Error

try:
    alx_db = mysql.connector.connect (
    host = "localhost",
    user = "root",
    password = "01100110",
    )
    alx_cursor = alx_db.cursor()
    alx_cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
    print ("Database 'alx_book_store' created successfully!")
except Error as e:
    print (f"Error: {e}")
except mysql.connector.Error as e:
    print ("Failed to create database alx_book_store: {e}")
finally:
    alx_cursor.close()
    alx_db.close()