from conexion.conexion import obtener_conexion

# ✅ LISTAR
def obtener_ordenes():
    conn = obtener_conexion()
    if conn is None:
        return []

    cursor = conn.cursor()
    cursor.execute("SELECT * FROM orden_servicio")
    datos = cursor.fetchall()
    conn.close()
    return datos


# ✅ OBTENER POR ID
def obtener_orden(id):
    conn = obtener_conexion()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM orden_servicio WHERE Id_Orden_Servicio=%s", (id,))
    dato = cursor.fetchone()
    conn.close()
    return dato


# ✅ CREAR
def crear_orden(fecha_solicitud, fecha_programada, estado, observaciones, cedula, id_servicio):
    conn = obtener_conexion()
    cursor = conn.cursor()

    # VALIDAR CLIENTE (evita error FK)
    cursor.execute("SELECT * FROM cliente WHERE Cedula_RUC=%s", (cedula,))
    if cursor.fetchone() is None:
        print("❌ Cliente no existe")
        conn.close()
        return

    sql = """
    INSERT INTO orden_servicio 
    (Fecha_Solicitud, Fecha_Programada, Estado, Observaciones, Cedula_RUC, Id_Servicio)
    VALUES (%s,%s,%s,%s,%s,%s)
    """

    cursor.execute(sql, (fecha_solicitud, fecha_programada, estado, observaciones, cedula, id_servicio))
    conn.commit()
    conn.close()


# ✅ ACTUALIZAR
def actualizar_orden(id, fecha_solicitud, fecha_programada, estado, observaciones, cedula, id_servicio):
    conn = obtener_conexion()
    cursor = conn.cursor()

    # VALIDAR CLIENTE
    cursor.execute("SELECT * FROM cliente WHERE Cedula_RUC=%s", (cedula,))
    if cursor.fetchone() is None:
        print("❌ Cliente no existe")
        conn.close()
        return

    sql = """
    UPDATE orden_servicio SET
    Fecha_Solicitud=%s,
    Fecha_Programada=%s,
    Estado=%s,
    Observaciones=%s,
    Cedula_RUC=%s,
    Id_Servicio=%s
    WHERE Id_Orden_Servicio=%s
    """

    cursor.execute(sql, (fecha_solicitud, fecha_programada, estado, observaciones, cedula, id_servicio, id))
    conn.commit()
    conn.close()


# ✅ ELIMINAR
def eliminar_orden(id):
    conn = obtener_conexion()
    cursor = conn.cursor()

    cursor.execute("DELETE FROM orden_servicio WHERE Id_Orden_Servicio=%s", (id,))
    conn.commit()
    conn.close()