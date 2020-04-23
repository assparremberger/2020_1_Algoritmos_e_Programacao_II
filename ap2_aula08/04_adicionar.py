arquivo = open("arquivo01.txt", "a")
arquivo.write( "\nAdicionando conteudo")
arquivo.close()

arquivo = open("arquivo01.txt", "r")
print( arquivo.read() )