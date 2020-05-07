import mysql.connector


conn = mysql.connector.connect( host='localhost', database='loja_ap2' , user='root', password='')

if conn.is_connected():
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM produtos ")

    result = cursor.fetchall()

    print("------------------")
    for prod in result:
        print( prod )
        print("------------------")

    id = input("Informe o id do produto que voce quer editar: ")
    nome = input("Digite o nome do produto: ")
    preco = input("Preco do produto: ") 
    preco = preco.replace("," , ".")
    quantidade =  input("Quantidade do produto: ") 
    quantidade = quantidade.replace("," , ".")

    query = "UPDATE produtos SET "
    query += " nome = '" + nome + "' , "
    query += " preco = " + preco + " , " 
    query += " quantidade = " + quantidade + " "
    query += " WHERE id = " + id
    cursor.execute( query )
    conn.commit()

    cursor.execute("SELECT * FROM produtos ")

    result = cursor.fetchall()

    print("\n\nProdutos\n------------------")
    for prod in result:
        print( prod )
        print("------------------")

    cursor.close()
    conn.close()