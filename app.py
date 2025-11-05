"Examen Unidad II"
"Autor: Alexis Joshua Beltran Santiago"
"Fecha: 21/06/2024"

from flask import Flask, request, jsonify, render_template_string

app = Flask(__name__)

# Diccionario para guardar los dispositivos
dispositivos = {}

# Página principal
@app.route('/')
def home():
    return "Inicio de la aplicación."

# Página con formulario HTML para agregar un dispositivo
@app.route('/agregar', methods=['GET'])
def formulario_agregar():
    html = """
    <html>
    <head><title>Agregar Dispositivo</title></head>
    <body>
        <h1>Nuevo Dispositivo</h1>
        <form action="/agregar" method="post">
            ID: <input type="text" name="id"><br>
            Nombre: <input type="text" name="nombre"><br>
            IP: <input type="text" name="ip"><br>
            Protocolos (separados por coma): <input type="text" name="protocolos"><br>
            Observaciones: <input type="text" name="observaciones"><br><br>
            <input type="submit" value="Agregar">
        </form>
        <br>
        <a href="/dispositivos_html">Ver lista de dispositivos</a>
    </body>
    </html>
    """
    return render_template_string(html)

# Ruta para recibir los datos del formulario (POST)
@app.route('/agregar', methods=['POST'])
def agregar_dispositivo():
    id = request.form.get("id")
    nombre = request.form.get("nombre")
    ip = request.form.get("ip")
    protocolos = request.form.get("protocolos")
    observaciones = request.form.get("observaciones")

    if id in dispositivos:
        return f"<h3>El dispositivo con ID {id} ya existe.</h3><a href='/agregar'>Volver</a>"

    dispositivos[id] = {
        "id": id,
        "nombre": nombre,
        "ip": ip,
        "protocolos": protocolos,
        "observaciones": observaciones
    }

    return f"<h3>Dispositivo agregado correctamente.</h3><a href='/dispositivos_html'>Ver dispositivos</a>"

# Mostrar los dispositivos en HTML
@app.route('/dispositivos_html', methods=['GET'])
def mostrar_dispositivos_html():
    html = """
    <html>
    <head><title>Lista de Dispositivos</title></head>
    <body>
        <h1>Dispositivos Registrados</h1>

        {% if dispositivos %}
            {% for id, d in dispositivos.items() %}
                <h3>ID: {{ d['id'] }}</h3>
                <p><b>Nombre:</b> {{ d['nombre'] }}</p>
                <p><b>IP:</b> {{ d['ip'] }}</p>
                <p><b>Protocolos:</b> {{ d['protocolos'] }}</p>
                <p><b>Observaciones:</b> {{ d['observaciones'] }}</p>
                <hr>
            {% endfor %}
        {% else %}
            <p>No hay dispositivos registrados.</p>
        {% endif %}

        <br>
        <a href="/agregar">Agregar nuevo dispositivo</a>
    </body>
    </html>
    """
    return render_template_string(html, dispositivos=dispositivos)

if __name__ == '__main__':
    app.run(debug=True)
