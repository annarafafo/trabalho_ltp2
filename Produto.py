from util import bd

class Produto():
    def cadastroprod(self, nm_produto, vlr_produto, cd_categoria, cd_usuario, img_produto, desc_produto, est_produto):
        banco = bd.SQL()
        comando = 'call sp_05(%s, %s, %s, %s, %s, %s, %s)'
        retorno = banco.executar(comando, [nm_produto, vlr_produto, cd_categoria, cd_usuario, img_produto, desc_produto, est_produto])

        return retorno
