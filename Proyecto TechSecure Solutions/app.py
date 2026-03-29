from flask import Flask, render_template, request, redirect, session, send_file
from services.orden_service import (
    obtener_ordenes,
    crear_orden,
    eliminar_orden,
    obtener_orden,
    actualizar_orden
)
from services.usuario_service import validar_usuario

from reportlab.platypus import SimpleDocTemplate, Table, Paragraph
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet

app = Flask(__name__)
app.secret_key = "clave_secreta"

# 🔐 LOGIN
@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        usuario = validar_usuario(username, password)

        if usuario:
            session['usuario'] = username
            return redirect('/inicio')
        else:
            return "❌ Usuario incorrecto"

    return render_template('login.html')

# 🔍 LISTAR
@app.route('/inicio')
def inicio():
    if 'usuario' not in session:
        return redirect('/')

    ordenes = obtener_ordenes()
    return render_template('orden_servicio/listar.html', ordenes=ordenes)

# ➕ CREAR
@app.route('/crear', methods=['GET', 'POST'])
def crear():
    if 'usuario' not in session:
        return redirect('/')

    if request.method == 'POST':
        crear_orden(
            request.form['fecha_solicitud'],
            request.form['fecha_programada'],
            request.form['estado'],
            request.form['observaciones'],
            request.form['cedula'],
            request.form['id_servicio']
        )
        return redirect('/inicio')

    return render_template('orden_servicio/crear.html')

# ✏️ EDITAR
@app.route('/editar/<int:id>', methods=['GET', 'POST'])
def editar(id):
    if 'usuario' not in session:
        return redirect('/')

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
        return redirect('/inicio')

    return render_template('orden_servicio/editar.html', orden=orden)

# ❌ ELIMINAR
@app.route('/eliminar/<int:id>')
def eliminar(id):
    if 'usuario' not in session:
        return redirect('/')

    eliminar_orden(id)
    return redirect('/inicio')

# 📄 PDF
@app.route('/reporte')
def reporte():
    if 'usuario' not in session:
        return redirect('/')

    ordenes = obtener_ordenes()

    archivo = "reporte_ordenes.pdf"
    doc = SimpleDocTemplate(archivo)
    styles = getSampleStyleSheet()

    elementos = []
    elementos.append(Paragraph("Reporte de Órdenes de Servicio", styles['Title']))

    data = [["ID","Fecha","Programada","Estado","Cliente","Servicio"]]

    for o in ordenes:
        data.append([o[0], o[1], o[2], o[3], o[5], o[6]])

    tabla = Table(data)
    tabla.setStyle([
        ('GRID',(0,0),(-1,-1),1,colors.black)
    ])

    elementos.append(tabla)
    doc.build(elementos)

    return send_file(archivo, as_attachment=True)

# 🔓 LOGOUT
@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)