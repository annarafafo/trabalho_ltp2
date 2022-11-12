from Usuario import *
from werkzeug.security import generate_password_hash

user = Usuario()
user.cadastro('Thiago', '1', '77777777777', 'thiago@gmail.com', '123456', '11998765432', '2003-03-09')
