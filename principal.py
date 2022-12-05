from Usuario import *
from Produto import *
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

    banco = bd.SQL()
    comando = "SELECT nm_produto, vlr_produto, img_produto FROM tb_produto"
    cs = banco.consultar(comando, [])
    prod = ''
    for [nm, vlr, img] in cs:
        #imagem = base64.b64decode(img)
        prod +=f'''<a class=\"produto-card\" href=\"{nm}\">
        <img src=\""data:image/jpeg; base64, {img}\">
        <p id="nome-produto">{nm}</p>
        <p>R$ {str(vlr)}</p>
        </a>'''
    cs.close()

    return render_template('index.html', produtos = prod) 


@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        e = request.form.get('email')
        s = request.form.get('senha')

        if e != '' and s != '':

            user = Usuario()
            valida = user.login(e, s)

            if valida:
                session['email'] = e
                return redirect('/')
            else:
                return render_template('telaLogin.html', MSG='Usuário e/ou senha inválidos')

    return render_template('telaLogin.html', MSG='')


@app.route('/logout', methods=['POST'])
def logout():
    session['email'] = None
    return redirect('/')


@app.route('/cadastro', methods=['POST', 'GET'])
def cadastro():
    if request.method == 'POST':
        nm = request.form.get('nome')
        sexo = int(request.form.get('sexo'))
        cpf = request.form.get('CPF')
        email = request.form.get('email')
        senha = request.form.get('senha')
        tel = request.form.get('tel')
        dt_nasc = request.form.get('dta-nasc')
        cep = request.form.get('cep')
        bairro = request.form.get('bairro')
        end = request.form.get('end')
        cid = request.form.get('cid')
        num = request.form.get('num')

        user = Usuario()
        cadastro = user.cadastro(nm, sexo, cpf, email, senha, tel, dt_nasc, cep, bairro, end, cid, num)

        if cadastro:
            return redirect('/login')
        else:
            return render_template('cadastro.html', MSG ='Cadastro Inválido!')

    return render_template('cadastro.html')
    

@app.route('/cadastroendereco', methods=['POST', 'GET'])
def cadstroendereco():
    if not session.get('email'):
        return redirect('/login') 

    if request.method == 'POST':
        cep = request.form.get('cep')
        bairro = request.form.get('bairro')
        end = request.form.get('end')
        cid = request.form.get('cid')
        num = request.form.get('num')

        user = Usuario()
        cadastro = user.cadastro_endereco(cep, bairro, end, cid, num, session.get('email'))

        if cadastro:
            return render_template('cadastroendereco.html')
        else:
            return render_template('cadastro.html', MSG ='Cadastro Inválido')

    return redirect('/cadastro')


@app.route('/cadastroproduto', methods=['POST', 'GET'])
def cadastroproduto():
    if not session.get('email'):
        return redirect('/login')
    
    if request.method == 'POST':
        nome = request.form.get('nome')
        valor = request.form.get('valor')
        categoria = request.form.get('categoria')
        img = request.files['imagem']
        descricao = request.form.get('descricao')
        estoque = request.form.get('estoque')

        imagem = base64.b64encode(img.read())
        user = Usuario()
        usuario = user.retorna_id_usuario(session.get('email'))

        produto = Produto()
        cadastro_produto = produto.cadastroprod(nome, valor, categoria, usuario, imagem, descricao, estoque)

        if cadastro_produto:
            return render_template('cadastroProduto.html', MSG = 'Produto Cadastrado')
        else:
            return render_template('cadastroProduto.html', MSG = 'Produto Não Cadastrado')
    
    return render_template('cadastroProduto.html', MSG = '')


@app.route('/esquecisenha')
def esquecisenha():
    return render_template('esqueciSenha.html')


app.run(debug=True)
