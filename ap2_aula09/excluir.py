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

    id = input("Informe o id do produto que voce quer excluir: ")

    cursor.execute("DELETE FROM produtos WHERE id = " + id)
    conn.commit()

    cursor.execute("SELECT * FROM produtos ")

    result = cursor.fetchall()

    print("\n\nProdutos\n------------------")
    for prod in result:
        print( prod )
        print("------------------")

    cursor.close()
    conn.close()