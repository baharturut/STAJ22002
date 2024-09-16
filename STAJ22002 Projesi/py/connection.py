import mysql.connector

def connection():
    return mysql.connector.connect(
        host="127.0.0.1",          
        user="bahar",      
        password="123456733",  
        database="stajproje"   
    )

# bağlantı başarılı!