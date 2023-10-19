from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


# CREACIÓN DE CLASES USUARIO Y TAREAS

class Usuario:
    def __init__(self, nombre, email):
        self.__nombre = nombre
        self.__email = email

    def get_nombre(self):
        return self.__nombre

    def get_email(self):
        return self.__email

class Tarea:
    def __init__(self, nombre, descripcion, fecha_limite, asignada_a):
        self.__nombre = nombre
        self.__descripcion = descripcion
        self.__fecha_limite = fecha_limite
        self.__asignada_a = asignada_a

    def get_nombre(self):
        return self.__nombre

    def get_descripcion(self):
        return self.__descripcion

    def get_fecha_limite(self):
        return self.__fecha_limite

    def get_asignada_a(self):
        return self.__asignada_a

usuarios = [Usuario("Juan Pérez", "juan@example.com"), Usuario("María López", "maria@example.com")]
tareas = []

@app.route('/')
def index():
    return render_template('index.html', usuarios=usuarios, tareas=tareas)


@app.route('/crear_tarea', methods=['POST'])
def crear_tarea():
    nombre_tarea = request.form['nombre_tarea']
    descripcion_tarea = request.form['descripcion_tarea']
    fecha_limite_tarea = request.form['fecha_limite_tarea']
    nombre_usuario = request.form['asignada_a']

    asignada_a = next((usuario for usuario in usuarios if usuario.get_nombre() == nombre_usuario), None)

    if asignada_a is not None:
        nueva_tarea = Tarea(nombre_tarea, descripcion_tarea, fecha_limite_tarea, asignada_a)
        tareas.append(nueva_tarea)

    return redirect(url_for('index'))

@app.route('/tareas_asignadas/<nombre_usuario>')
def tareas_asignadas(nombre_usuario):
    tareas_asignadas = [tarea for tarea in tareas if tarea.get_asignada_a().get_nombre() == nombre_usuario]
    return render_template('tareas_asignadas.html', nombre_usuario=nombre_usuario, tareas_asignadas=tareas_asignadas)

if __name__ == '__main__':
    app.run(debug=True)