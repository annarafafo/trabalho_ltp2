from flask import Flask, render_template, request, redirect, url_for
from Usuario import *

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('telaLogin.html', MSG = '')

@app.route('/inicio', methods=['POST'])
def inicio():
    e = request.form['email']
    s = request.form['senha']

    user = Usuario()
    valida = user.login(e, s)


    if valida:
        # Salvar usuário na sessão e fazer validação nas telas
        return render_template('inicio.html')
    else:
        return render_template('telaLogin.html', MSG = 'Usuário ou senha inválida')

@app.route('/esqueciSenha')
def esqueciSenha():
    return render_template('esqueciSenha.html')

app.run(debug=True)