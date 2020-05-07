import mysql.connector


conn = mysql.connector.connect( host='localhost', database='loja_ap2' , user='root', password='')

if conn.is_connected():
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM produtos ")

    result = cursor.fetchall()

    print("------------------")
    for prod in result:
        print( prod[1] )
        print( prod )
        print("------------------")

    cursor.close()
    conn.close()