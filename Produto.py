from util import bd
from Usuario import *
import base64

class Produto():
    def cadastroprod(self, nm_produto, vlr_produto, cd_categoria, usuario, img_produto, desc_produto, est_produto):
        banco = bd.SQL()
        comando = 'call sp_05(%s, %s, %s, %s, %s, %s, %s)'
        retorno = banco.executar(comando, [nm_produto, vlr_produto, cd_categoria, usuario, img_produto, desc_produto, est_produto])

        return retorno

    def retorna_id_produto(self, nome):
        banco = bd.SQL()
        comando = "SELECT id_produto FROM tb_produto where nm_produto = %s"
        cs = banco.consultar(comando, [nome])
        [cd] = cs.fetchone()
        return cd
