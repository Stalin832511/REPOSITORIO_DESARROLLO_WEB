from conexion.conexion import get_connection

# 🔍 LEER
def obtener_ordenes():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM orden_servicio")
    datos = cursor.fetchall()
    conn.close()
    return datos

# ➕ CREAR
def crear_orden(fecha_solicitud, fecha_programada, estado, observaciones, cedula, id_servicio):
    conn = get_connection()
    cursor = conn.cursor()
    sql = """INSERT INTO orden_servicio 
             (Fecha_Solicitud, Fecha_Programada, Estado_Orden, Observaciones, Cedula_RUC, Id_Servicio)
             VALUES (%s,%s,%s,%s,%s,%s)"""
    cursor.execute(sql, (fecha_solicitud, fecha_programada, estado, observaciones, cedula, id_servicio))
    conn.commit()
    conn.close()

# ❌ ELIMINAR
def eliminar_orden(id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM orden_servicio WHERE Id_Orden_Servicio=%s", (id,))
    conn.commit()
    conn.close()

# 🔍 OBTENER UNA ORDEN POR ID
def obtener_orden(id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM orden_servicio WHERE Id_Orden_Servicio=%s", (id,))
    dato = cursor.fetchone()
    conn.close()
    return dato

# ✏️ ACTUALIZAR ORDEN
def actualizar_orden(id, fecha_solicitud, fecha_programada, estado, observaciones, cedula, id_servicio):
    conn = get_connection()
    cursor = conn.cursor()
    sql = """UPDATE orden_servicio 
             SET Fecha_Solicitud=%s, Fecha_Programada=%s, Estado_Orden=%s, 
                 Observaciones=%s, Cedula_RUC=%s, Id_Servicio=%s
             WHERE Id_Orden_Servicio=%s"""
    cursor.execute(sql, (fecha_solicitud, fecha_programada, estado, observaciones, cedula, id_servicio, id))
    conn.commit()
    conn.close()