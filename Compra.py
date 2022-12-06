from util import bd
from Usuario import *
from Produto import *

class Compra:
    def gravar_dados_cartao(self, nome, numero, validade, bandeira):
        banco = bd.SQL()
        comando = 'INSERT INTO tb_cartao (nm_cartao, num_cartao, val_cartao, ban_cartao) VALUES(%s, %s, %s, %s)'
        retorno = banco.executar(comando, [nome, numero, validade, bandeira])

        return retorno