from Usuario import *
from werkzeug.security import generate_password_hash

user = Usuario()
user.cadastro_endereco('70070080', 'Asa Sul', 'Praça dos Tribunais Superiores', 'Brasília', 00, 'Trabalho', 'david@gmail.com')
