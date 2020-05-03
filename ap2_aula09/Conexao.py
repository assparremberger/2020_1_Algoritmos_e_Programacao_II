import mysql.connector

class Conexao:

    def abrir(self):
        conn = mysql.connector.connect( host='localhost', database='loja_ap2' , user='root', password='')
        return conn

    def fechar(self, conn):
        conn.close()