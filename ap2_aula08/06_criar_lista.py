arq = open("nomes.txt" , "w")
arq.write("José,Maria,Júlia,Carlos")
arq.close()

arq = open("nomes.txt")
nomes = arq.read()
lista = nomes.split(",")
lista.sort()
print()
for n in lista:
    print(n)
print()