import mysql.connector

def obtener_conexion():
    try:
        conexion = mysql.connector.connect(
            host="localhost",
            user="root",
            password="123456",
            database="techsecure_bd_practica"
        )

        # ✅ Verificar conexión
        if conexion.is_connected():
            print("✅ Conexión exitosa a la base de datos")

        return conexion

    except mysql.connector.Error as e:
        print("❌ Error al conectar a la base de datos:", e)
        return None