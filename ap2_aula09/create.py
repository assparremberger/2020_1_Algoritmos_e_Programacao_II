import mysql.connector

conexao = mysql.connector.connect( host='localhost', database='loja_ap2' , user='root', password='')

if conexao.is_connected():
    info = conexao.get_server_info()
    print("Conectado ao MySQL", info)
    print("------------")
    print("Tabelas existentes:")

    cursor = conexao.cursor()
    cursor.execute( "SHOW TABLES")
    for tabela in cursor:
        print(tabela)
    print("------------")


    query = "CREATE TABLE produtos ( " 
    query += " id INT NOT NULL PRIMARY KEY AUTO_INCREMENT ,  " 
    query += " nome VARCHAR(50) ,  " 
    query += " preco DOUBLE,       " 
    query += " quantidade DOUBLE ) "
    cursor.execute( query )

    cursor.execute( "SHOW TABLES")
    print("------------")
    print("Tabelas existentes:")
    for tabela in cursor:
        print(tabela)

    cursor.close()
    conexao.close()

else:
    print("Nao foi possivel conectar ao banco")

