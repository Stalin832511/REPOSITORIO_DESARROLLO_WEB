from conexion.conexion import get_connection

def validar_usuario(username, password):
    conn = get_connection()
    cursor = conn.cursor()

    sql = "SELECT * FROM usuarios WHERE username=%s AND password=%s"
    cursor.execute(sql, (username, password))

    usuario = cursor.fetchone()
    conn.close()

    return usuario