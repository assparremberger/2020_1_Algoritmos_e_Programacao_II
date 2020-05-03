from Conexao import Conexao

import mysql.connector

nome = input("Digite o nome do produto: ")
preco = input("Preco do produto: ") 
preco = preco.replace("," , ".")
quantidade =  input("Quantidade do produto: ") 
quantidade = quantidade.replace("," , ".")

#conexao = Conexao()
conn = mysql.connector.connect( host='localhost', database='loja_ap2' , user='root', password='')
if conn.is_connected():
    print("Connectado!")

cursor = conn.cursor()

query = "INSERT INTO produtos (nome, preco , quantidade) VALUES ("
query += " '" +nome+"' , " + preco + " , " + quantidade + " )"

cursor.execute(query)

conn.commit()
