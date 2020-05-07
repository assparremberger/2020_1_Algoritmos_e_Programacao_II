import mysql.connector
from FormProduto import FormProduto
from Produto import Produto


form = FormProduto()
produto = form.show()

#conexao = Conexao()
conn = mysql.connector.connect( host='localhost', database='loja_ap2' , user='root', password='')
if conn.is_connected():
    print("Connectado!")

cursor = conn.cursor()
query = "INSERT INTO produtos (nome, preco , quantidade) VALUES ("
query += " '" +produto.nome+"' , " +str(produto.preco) + " , " + str(produto.quantidade) + " )"

cursor.execute(query)
conn.commit()
