arq = open("nomes.txt" , "a")
arq.write(",Jonas,Jeremias,Lúcia,Bianca")
arq.close()

arq = open("nomes.txt")
nomes = arq.read()
lista = nomes.split(",")
lista.sort()
print()
for n in lista:
    print(n)
print()