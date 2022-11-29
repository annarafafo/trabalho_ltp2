from util import bd
from werkzeug.security import generate_password_hash, check_password_hash

class Usuario():
    def cadastro(self, nm, cd, cpf, email, senha, tel, dt_nasc, cep, bairro, endereco, cidade, num_endereco, des_endereco):
        banco = bd.SQL()
        comando = 'call sp_03(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'
        retorno = banco.executar(comando, [nm, cd, cpf, email, senha, tel, dt_nasc, cep, bairro, endereco, cidade, num_endereco, des_endereco])

        return retorno


    def cadastro_usuario(self, nm, cd, cpf, email, senha, tel, dt_nasc):
        banco = bd.SQL()
        comando = 'call sp_01(%s, %s, %s, %s, %s, %s, %s)'
        retorno = banco.executar(comando, [nm, cd, cpf, email, generate_password_hash(senha), tel, dt_nasc])

        return retorno


    def cadastro_endereco(self, cep, bairro, endereco, cidade, num_endereco, des_endereco):
        banco = bd.SQL()
        comando = 'call sp_02(%s, %s, %s, %s, %s, %s)'
        retorno = banco.executar(comando, [cep, bairro, endereco, cidade, num_endereco, des_endereco])

        return retorno
        

    def login(self, e, s):
        try:
            banco = bd.SQL()
            comando = "SELECT email_usuario, senha_usuario FROM tb_usuario where email_usuario = %s"
            cs = banco.consultar(comando, [e])
            if cs:
                [email, senha] = cs.fetchone()
                if email == e:
                    if check_password_hash(senha, s):
                        return True

            return False
        except:
            return False

