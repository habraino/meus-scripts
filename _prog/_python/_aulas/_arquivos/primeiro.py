# file_name: primeiro.py

arq = open('arquivo.txt', 'r')

palavra = []

for i in arq:
    linha = i.strip()
    palavra.append(linha)
    print(palavra)

arq.close()