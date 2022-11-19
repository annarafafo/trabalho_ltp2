from Usuario import *
from werkzeug.security import generate_password_hash

user = Usuario()
user.cadastro_endereco('11111111', 'Teste boy', 'Testando', 882, 105, 'Trabalho', 'thiago@gmail.com')
