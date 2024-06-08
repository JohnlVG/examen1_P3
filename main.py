from flask import Flask, render_template

app = Flask(__name__, template_folder='productos/templates')

@app.route('/')
def index():
    return render_template('test.html')

@app.route('/agregar')
def agregar():
    return render_template('agregar.html')

@app.route('/base')
def base():
    return render_template('base.html')

@app.route('/editar')
def editar():
    return render_template('editar.html')

@app.route('/eliminar')
def eliminar():
    return render_template('eliminar.html')

@app.route('/listar')
def listar():
    return render_template('listar.html')

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
