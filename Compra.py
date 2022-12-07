from util import bd
from Usuario import *
from Produto import *

class Compra:
    def comprar(self, cartao, usuario, produto, endereco, valor):
        banco = bd.SQL()
        comando = 'call sp_07(%s, %s, %s, %s, %s, %s, %s)'
        retorno = banco.executar(comando, [endereco, usuario , cartao , valor , produto ])

        return retorno