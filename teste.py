from Usuario import *
from werkzeug.security import generate_password_hash

print(generate_password_hash('123456'))
print()
senha = check_password_hash(generate_password_hash('123456'), '123456')
print(senha)
