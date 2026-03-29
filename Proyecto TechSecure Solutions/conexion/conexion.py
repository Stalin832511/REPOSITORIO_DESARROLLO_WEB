import mysql.connector

def get_connection():
    try:
        conexion = mysql.connector.connect(
            host="localhost",
            user="root",
            password="123456",  
            database="servicios"
        )
        return conexion
    except Exception as e:
        print("Error al conectar:", e)
        return None