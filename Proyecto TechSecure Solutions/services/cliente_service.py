from conexion.conexion import obtener_conexion


# ✅ LISTAR CLIENTES
def obtener_clientes():
    conn = obtener_conexion()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM cliente")
    datos = cursor.fetchall()
    conn.close()
    return datos


# ✅ OBTENER CLIENTE POR ID
def obtener_cliente(cedula):
    conn = obtener_conexion()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM cliente WHERE Cedula_RUC=%s", (cedula,))
    dato = cursor.fetchone()
    conn.close()
    return dato


# ✅ CREAR CLIENTE (YA CON DIRECCION)
def crear_cliente(cedula, nombre, direccion, telefono, correo):
    conn = obtener_conexion()
    cursor = conn.cursor()

    sql = """
    INSERT INTO cliente (Cedula_RUC, Nombre, Direccion, Telefono, Correo)
    VALUES (%s, %s, %s, %s, %s)
    """

    cursor.execute(sql, (cedula, nombre, direccion, telefono, correo))
    conn.commit()
    conn.close()


# ✅ ACTUALIZAR CLIENTE (YA CON DIRECCION)
def actualizar_cliente(cedula, nombre, direccion, telefono, correo):
    conn = obtener_conexion()
    cursor = conn.cursor()

    sql = """
    UPDATE cliente SET
    Nombre=%s,
    Direccion=%s,
    Telefono=%s,
    Correo=%s
    WHERE Cedula_RUC=%s
    """

    cursor.execute(sql, (nombre, direccion, telefono, correo, cedula))
    conn.commit()
    conn.close()


# ✅ ELIMINAR CLIENTE
def eliminar_cliente(cedula):
    conn = obtener_conexion()
    cursor = conn.cursor()

    cursor.execute("DELETE FROM cliente WHERE Cedula_RUC=%s", (cedula,))
    conn.commit()
    conn.close()