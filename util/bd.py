import mysql.connector

class SQL:
   def __init__(self):
       self.cnx = mysql.connector.connect(user="root", password="12345678", host='127.0.0.1', database="db_loja")

   def executar(self, comando, parametros):
       cs = self.cnx.cursor()
       cs.execute(comando, parametros)
       self.cnx.commit()
       cs.close()
       return True

   def consultar(self, comando, parametros):
       cs = self.cnx.cursor()
       cs.execute(comando, parametros)
       return cs

   def __del__(self):
       self.cnx.close()
