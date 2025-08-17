import mysql.connector

alx_db = mysql.connector.connect (
    host = "localhost",
    user = "root",
    password = "01100110",
    database = "alx_book_store"
)
alx_cursor = alx_db.cursor()

try: 
    alx_cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
    print ("Database 'alx_book_store' created successfully!")
except:
    mysql.connector.Error
    print ("Failed to create database alx_book_store")

alx_cursor.close()
alx_db.close()