from Usuario import *
from werkzeug.security import generate_password_hash

user = Usuario()
user.cadastro('Houston', 2, '12345678990', 'houston@gmail.com', '123456', '61987654321', '2003-08-12', '70070130', 'Asa sul', 'SBS Quadra 3', 882, 602, 'Minha Casa')
