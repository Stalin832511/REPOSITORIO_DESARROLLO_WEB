from flask import Flask, render_template, request, redirect, session, send_file
from services.orden_service import (
    obtener_ordenes,
    obtener_orden,
    crear_orden,
    actualizar_orden,
    eliminar_orden
)

from services.cliente_service import (
    obtener_clientes,
    obtener_cliente,
    crear_cliente,
    actualizar_cliente,
    eliminar_cliente
)

# ✅ PDF
from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet

app = Flask(__name__)
app.secret_key = "clave_secreta_123"


# ===============================
# 🌐 LANDING PAGE
# ===============================
@app.route('/')
def inicio():
    return render_template('index.html')


# ===============================
# 🔐 LOGIN
# ===============================
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        usuario = request.form['usuario']
        password = request.form['password']

        if usuario == 'admin' and password == '123':
            session['usuario'] = usuario
            return redirect('/dashboard')

    return render_template('login.html')


# ===============================
# 🔓 LOGOUT
# ===============================
@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')


# ===============================
# 📊 DASHBOARD
# ===============================
@app.route('/dashboard')
def dashboard():
    if 'usuario' not in session:
        return redirect('/login')

    return render_template('dashboard.html')


# ======================================================
# 👥 CLIENTES (CRUD COMPLETO)
# ======================================================

# LISTAR
@app.route('/clientes')
def clientes():
    if 'usuario' not in session:
        return redirect('/login')

    lista = obtener_clientes()
    return render_template('clientes/listar.html', clientes=lista)


# CREAR CLIENTE
@app.route('/clientes/crear', methods=['GET', 'POST'])
def crear_cliente_view():
    if 'usuario' not in session:
        return redirect('/login')

    if request.method == 'POST':
        crear_cliente(
            request.form.get('cedula'),
            request.form.get('nombre'),
            request.form.get('direccion'),
            request.form.get('telefono'),
            request.form.get('email')
        )
        return redirect('/clientes')

    return render_template('clientes/crear.html')


# EDITAR CLIENTE
@app.route('/clientes/editar/<cedula>', methods=['GET', 'POST'])
def editar_cliente_view(cedula):
    if 'usuario' not in session:
        return redirect('/login')

    cliente = obtener_cliente(cedula)

    if request.method == 'POST':
        actualizar_cliente(
            cedula,
            request.form.get('nombre'),
            request.form.get('direccion'),
            request.form.get('telefono'),
            request.form.get('email')
        )
        return redirect('/clientes')

    return render_template('clientes/editar.html', cliente=cliente)


# ELIMINAR CLIENTE
@app.route('/clientes/eliminar/<cedula>')
def eliminar_cliente_view(cedula):
    if 'usuario' not in session:
        return redirect('/login')

    eliminar_cliente(cedula)
    return redirect('/clientes')


# ======================================================
# 📄 GENERAR PDF DE CLIENTES
# ======================================================
@app.route('/clientes/pdf')
def clientes_pdf():
    if 'usuario' not in session:
        return redirect('/login')

    clientes = obtener_clientes()

    doc = SimpleDocTemplate("clientes.pdf")
    styles = getSampleStyleSheet()

    contenido = []

    for c in clientes:
        texto = f"Nombre: {c[1]} | Cédula: {c[0]} | Dirección: {c[2]}"
        contenido.append(Paragraph(texto, styles["Normal"]))

    doc.build(contenido)

    return send_file("clientes.pdf", as_attachment=True)


# ======================================================
# 📋 ORDENES (CRUD COMPLETO)
# ======================================================

# LISTAR
@app.route('/ordenes')
def listar_ordenes():
    if 'usuario' not in session:
        return redirect('/login')

    ordenes = obtener_ordenes()
    return render_template('orden_servicio/listar.html', ordenes=ordenes)


# CREAR
@app.route('/ordenes/crear', methods=['GET', 'POST'])
def crear_orden_view():
    if 'usuario' not in session:
        return redirect('/login')

    if request.method == 'POST':
        crear_orden(
            request.form['fecha_solicitud'],
            request.form['fecha_programada'],
            request.form['estado'],
            request.form['observaciones'],
            request.form['cedula'],
            request.form['id_servicio']
        )
        return redirect('/ordenes')

    return render_template('orden_servicio/crear.html')


# EDITAR
@app.route('/ordenes/editar/<int:id>', methods=['GET', 'POST'])
def editar_orden_view(id):
    if 'usuario' not in session:
        return redirect('/login')

    orden = obtener_orden(id)

    if request.method == 'POST':
        actualizar_orden(
            id,
            request.form['fecha_solicitud'],
            request.form['fecha_programada'],
            request.form['estado'],
            request.form['observaciones'],
            request.form['cedula'],
            request.form['id_servicio']
        )
        return redirect('/ordenes')

    return render_template('orden_servicio/editar.html', orden=orden)


# ELIMINAR
@app.route('/ordenes/eliminar/<int:id>')
def eliminar_orden_view(id):
    if 'usuario' not in session:
        return redirect('/login')

    eliminar_orden(id)
    return redirect('/ordenes')


# ===============================
# 🚀 EJECUTAR
# ===============================
if __name__ == '__main__':
    app.run(debug=True)