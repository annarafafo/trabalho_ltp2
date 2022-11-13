from Usuario import *
from flask import Flask, render_template, request, session, redirect
from flask_session import Session

app = Flask(__name__)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

@app.route('/')
def index():
    if not session.get('email'):
        return redirect('/login')

    return render_template('index.html')

@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        e = request.form.get('email')
        s = request.form.get('senha')

        user = Usuario()
        valida = user.login(e, s)

        if valida:
            session['email'] = e
            return redirect('/')
        else:
            return render_template('telaLogin.html', MSG='Usuário e/ou senha inválidos')


    return render_template('telaLogin.html', MSG = '')


@app.route('/logout', methods=['POST'])
def logout():
    session['email'] = None
    return redirect('/')

@app.route('/esqueciSenha')
def esqueciSenha():
    return render_template('esqueciSenha.html')

app.run(debug=True)