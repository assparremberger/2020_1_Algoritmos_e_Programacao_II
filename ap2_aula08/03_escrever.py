# Criando e escrevendo em um arquivo novo
arquivo = open("arquivo01.txt", "w")
arquivo.write("Escrevendo no Arquivo")
arquivo.close()

# Lendo o arquivo
arquivo = open("arquivo01.txt", "r")
print( arquivo.read() )