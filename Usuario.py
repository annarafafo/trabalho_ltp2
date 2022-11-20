from util import bd
from werkzeug.security import generate_password_hash, check_password_hash

class Usuario():
    def cadastro(self, nm, cd, cpf, email, senha, tel, dt_nasc):
        try:
            if cpf.isdecimal() and tel.isdecimal() and nm.isalpha():
                banco = bd.SQL()
                comando = '''
                        INSERT INTO tb_usuario (nm_usuario, cd_sexo, cpf_usuario, email_usuario, senha_usuario, tel_usuario, dt_nasc_usuario)
                        VALUES (%s, %s, %s, %s, %s, %s, %s)
                        '''
                inserindo = banco.executar(comando, [nm, cd, cpf, email, generate_password_hash(senha), tel, dt_nasc])

                return inserindo
            
            return False
        except:
            return False


    def cadastro_endereco(self, cep, bairro, endereco, cidade, num_endereco, des_endereco, email):
        try:
            banco = bd.SQL()
            comando = '''
                    INSERT INTO tb_endereco (cep_endereco, nm_bairro, nm_endereco, cd_cidade, num_endereco, des_endereco)
                    VALUES (%s, %s, %s, %s, %s, %s)
                    '''
            executou = banco.executar(comando, [cep, bairro, endereco, cidade, num_endereco, des_endereco])

            if executou:
                comando2 = '''
                        INSERT INTO tb_endereco__usuario (cd_endereco, cd_usuario)
                        VALUES ((SELECT max(id_endereco) FROM tb_endereco), ( SELECT id_usuario FROM tb_usuario where email_usuario = %s))
                        '''
                inserindo = banco.executar(comando2, [email])

                return inserindo
        except:
            return False
        

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

