from flask import Flask, render_template, request, redirect, url_for
from Usuario import *

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('telaLogin.html')

@app.route('/inicio', methods=['POST'])
def inicio():
    e = request.form['email']
    s = request.form['senha']

    user = Usuario()
    valida = user.login(e, s)


    if valida:
            return render_template('inicio.html')

    return redirect(url_for('index'))


app.run(debug=True)