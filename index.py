#Importarmos flask
from flask import Flask, render_template, request, url_for, redirect


#Inicilizamos, y llamamos a la carpeta template
app = Flask(__name__, template_folder='template')

#Arreglo para almacenar las tarea

array_cliente = []
array_tienda  = []

#Controlador de la ruta pricipal
@app.route('/')
def principal():
    return render_template('admin.html',array_cliente=array_cliente,array_tienda=array_tienda)
    

@app.route('/cliente')
def cliente():
    return render_template('cliente.html', array_cliente=array_cliente)

@app.route('/tienda')
def tienda():
    return render_template('tienda.html', array_tienda=array_tienda)


#Controlador para enviar los datos
@app.route('/datos', methods=['POST'])
def datos():
    if request.method == 'POST':
        nombre = request.form['nombre']
        telefono = request.form['telefono']
        estado = request.form['estado']
        array_cliente.append({'nombre', 'telefono', 'estado' })
        return redirect(url_for('cliente'))
#Controlador subir datos
@app.route('/enviar', methods=['POST'])
def enviar():
   if request.method == 'POST':

        nombre = request.form['nombre']
        telefono = request.form['telefono']
        estado = request.form['estado']
        gerente = request.form['gerente']
        array_tienda.append({'nombre': nombre, 'telefono': telefono, 'estado': estado,'gerente': gerente })
        return redirect(url_for('tienda'))
#Método principal
if __name__ == '__main__':
    app.run(debug=True)


