from util import bd
from werkzeug.security import generate_password_hash, check_password_hash

class Usuario():
    def cadastro(self, nm, sexo, cpf, email, senha, tel, dt_nasc, cep, bairro, endereco, cidade, num_endereco, des_endereco):
        banco = bd.SQL()
        cd = self.retorna_id_cidade(cidade)
        comando = 'call sp_04(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'
        retorno = banco.executar(comando, [nm, sexo, cpf, email, generate_password_hash(senha), tel, dt_nasc, cep, bairro, endereco, cd, num_endereco, des_endereco])

        return retorno

    def cadastro_endereco(self, cep, bairro, endereco, cidade, num_endereco, des_endereco, email):
        banco = bd.SQL()
        cd_usuario = self.retorna_id_usuario(email)
        cd_cidade = self.retorna_id_cidade(cidade)
        comando = 'call sp_06(%s, %s, %s, %s, %s, %s, %s)'
        retorno = banco.executar(comando, [cep, bairro, endereco, cd_cidade, num_endereco, des_endereco, cd_usuario])

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


    def retorna_id_cidade(self, cidade):
        banco = bd.SQL()
        comando = "SELECT id_cidade FROM tb_cidade where nm_cidade = %s"
        cs = banco.consultar(comando, [cidade])
        [cd] = cs.fetchone()
        return cd


    def retorna_id_usuario(self, email):
        banco = bd.SQL()
        comando = "SELECT id_usuario FROM tb_usuario where email_usuario = %s"
        cs = banco.consultar(comando, [email])
        [cd] = cs.fetchone()
        return cd