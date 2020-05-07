import mysql.connector
from FormCliente import FormCliente
from Cliente import Cliente

form = FormCliente()
cliente = form.show()

conn = mysql.connector.connect( host='localhost', database='loja_ap2' , user='root', password='')
if conn.is_connected():
    print("Connectado!")

cursor = conn.cursor()
query = "INSERT INTO clientes (nome, aceitaEmail, sexo, idade) VALUES ("
query += " '" +cliente.nome+"' , " +str(cliente.aceitaEmail) + " , '" + cliente.sexo + "' , " + str(cliente.idade) + " )"
cursor.execute(query)
conn.commit()
