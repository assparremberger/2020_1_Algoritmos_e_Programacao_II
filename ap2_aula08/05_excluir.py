# Excluindo arquivo
import os
if os.path.exists("arquivo01.txt"):
    os.remove("arquivo01.txt")
    print("Arquivo removido!")
else:
    print("Arquivo nao encontrado")