from util import bd
from werkzeug.security import generate_password_hash, check_password_hash

class Usuario():
    def cadastro(self, nm, cd, cpf, email, senha, tel, dt_nasc):
        banco = bd.SQL()
        comando = '''
                  INSERT INTO tb_usuario (nm_usuario, cd_sexo, cpf_usuario, email_usuario, senha_usuario, tel_usuario, dt_nasc_usuario)
                  VALUES (%s, %s, %s, %s, %s, %s, %s)
                  '''
        banco.executar(comando, [nm, cd, cpf, email, generate_password_hash(senha), tel, dt_nasc])

    def login(self, e, s):
        banco = bd.SQL()
        comando = "SELECT email_usuario, senha_usuario FROM tb_usuario where email_usuario = %s"
        cs = banco.consultar(comando, [e])
        if cs:
            [email, senha] = cs.fetchone()
            if email == e:
                if check_password_hash(senha, s):
                  return True

        return False
