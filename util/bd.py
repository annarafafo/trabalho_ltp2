import mysql.connector
from dotenv import load_dotenv
import os
load_dotenv()

class SQL:
    def __init__(self):
        user = os.environ.get('user')
        password = os.environ.get('password')
        host = os.environ.get('host')
        database = os.environ.get('database')
        self.cnx = mysql.connector.connect(user=user, password=password, host=host, database=database)

    def executar(self, comando, parametros):
        try:
            cs = self.cnx.cursor()
            cs.execute(comando, parametros)
            self.cnx.commit()
            cs.close()
            self.cnx.close()
            return True
        except:
            self.cnx.rollback()
            cs.close()
            self.cnx.close()
            return False

    def consultar(self, comando, parametros):
        cs = self.cnx.cursor()
        cs.execute(comando, parametros)
        return cs

    def __del__(self):
        self.cnx.close()